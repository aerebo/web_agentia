#!/usr/bin/env python3
"""Comprueba el sitio ya armado: enlaces, anclas y encabezados.

Por que existe
--------------
El sitio son ocho paginas que se arman a trozos, y los enlaces entre
ellas se escriben a mano con {{RAIZ}} delante. Un enlace roto no da
error al armar: la pagina se publica, el boton se ve bien y al pulsarlo
no pasa nada. Ya ocurrio una vez, con un boton que apuntaba a #contacto
despues de que esa seccion se mudara a su propia pagina.

Tambien vigila que cada pagina tenga un h1 y solo uno, que es lo que
anuncia de que va a un buscador y a un lector de pantalla.

Uso:  python3 armar.py && python3 comprobar.py
Sale con codigo 1 si encuentra algo, para que el workflow lo note.
"""

import pathlib
import posixpath
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent
SITIO = RAIZ / "_sitio"

EXTERNOS = ("http://", "https://", "mailto:", "tel:")


def paginas():
    for f in sorted(SITIO.rglob("index.html")):
        carpeta = f.parent.relative_to(SITIO).as_posix()
        yield ("" if carpeta == "." else carpeta), f


def anclas(html):
    return set(re.findall(r'\bid="([^"]+)"', html))


def comprobar():
    fallos = []
    textos = {ruta: f.read_text(encoding="utf-8") for ruta, f in paginas()}

    for ruta, html in textos.items():
        nombre = ruta or "(portada)"

        # Las paginas de salto de REDIRECCIONES son tres lineas con un
        # meta refresh. No tienen encabezados ni los necesitan: nadie las
        # lee, solo las atraviesa.
        if 'http-equiv="refresh"' in html:
            continue

        # --- un h1, ni cero ni dos ---
        cuantos = len(re.findall(r"<h1\b", html))
        if cuantos != 1:
            fallos.append("%s: tiene %d <h1>, debe tener exactamente 1"
                          % (nombre, cuantos))

        # --- marcadores sin sustituir ---
        for marcador in set(re.findall(r"\{\{[A-Z:a-z0-9-]+\}\}", html)):
            fallos.append("%s: quedo un marcador sin sustituir -> %s"
                          % (nombre, marcador))

        # --- enlaces y recursos ---
        refs = re.findall(r'(?:href|src)="([^"]+)"', html)
        for ref in refs:
            if ref.startswith(EXTERNOS) or ref.startswith("data:"):
                continue

            camino, _, ancla = ref.partition("#")
            camino = camino.split("?")[0]

            if not camino:
                # ancla dentro de la propia pagina
                if ancla and ancla not in anclas(html):
                    fallos.append("%s: ancla #%s que no existe en la pagina"
                                  % (nombre, ancla))
                continue

            destino = posixpath.normpath(posixpath.join(ruta, camino))
            archivo = SITIO / destino
            if archivo.is_dir():
                archivo = archivo / "index.html"

            if not archivo.exists():
                fallos.append("%s: enlace a %s, que no existe" % (nombre, ref))
                continue

            if ancla:
                destino_ruta = destino[:-len("/index.html")] if destino.endswith("index.html") else destino
                destino_ruta = destino_ruta.rstrip("/")
                destino_ruta = "" if destino_ruta in (".", "") else destino_ruta
                otra = textos.get(destino_ruta)
                if otra is None:
                    otra = archivo.read_text(encoding="utf-8")
                if ancla not in anclas(otra):
                    fallos.append("%s: enlace a %s, pero esa pagina no tiene #%s"
                                  % (nombre, ref, ancla))

    return fallos


if __name__ == "__main__":
    if not SITIO.exists():
        sys.exit("no hay _sitio/; corre primero armar.py")
    fallos = comprobar()
    if fallos:
        print("COMPROBACION FALLIDA, %d problema(s):" % len(fallos))
        for f in fallos:
            print("  -", f)
        sys.exit(1)
    print("comprobadas %d paginas: enlaces, anclas y encabezados en orden"
          % len(list(paginas())))
