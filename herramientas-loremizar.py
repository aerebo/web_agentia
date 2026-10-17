#!/usr/bin/env python3
"""Deja en relleno todo el contenido, y conserva solo lo que orienta.

Regla, explicita para que se pueda discutir:

  SE CONSERVA  lo que nombra una seccion, una pagina, un destino de
               navegacion o una accion: titulares de seccion, el menu,
               la miga, los botones, las etiquetas del pacto del proceso
               y los avisos de trabajo, que son notas nuestras y no
               copia del sitio.

  PASA A RELLENO  todo lo demas: nombres y descripciones de servicio,
                  viñetas, pasos, preguntas, respuestas, clientes,
                  cifras, correos, campos del formulario y pie.

El relleno respeta el numero de palabras del original, asi que la caja
mide mas o menos lo mismo y la maqueta no miente sobre el espacio.
"""

import pathlib
import re
import sys

PALABRAS = ("lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor "
            "incididunt ut labore et dolore magna aliqua enim ad minim veniam quis nostrud "
            "exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure "
            "in reprehenderit voluptate velit esse cillum eu fugiat nulla pariatur excepteur "
            "sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim "
            "id est laborum").split()


def relleno(n, semilla):
    """n palabras de relleno, estables: la misma caja da siempre lo mismo."""
    n = max(1, min(n, 60))
    i = semilla % len(PALABRAS)
    out = [PALABRAS[(i + k) % len(PALABRAS)] for k in range(n)]
    out[0] = out[0].capitalize()
    return " ".join(out)


# Clases cuyo texto pasa a relleno
CLASES = [
    "resumen__nombre", "resumen__entrada",
    "servicio__nombre", "servicio__entrada",
    "revelado__entrada",
    "ficha__titulo", "ficha__texto",
    "publico__titulo",
    "trabajo__tipo", "trabajo__nombre",
    "marquesina__nombre", "franja__nombre", "franja__lead",
    "persona__nombre", "persona__rol",
    "llamada__texto",
    "tipo__nombre", "tipo__entrada",
    "nota",
    "pie__linea",
]

# Elementos sueltos cuyo texto tambien pasa a relleno
SUELTOS = [
    (r'(<li>)([^<]{3,})(</li>)', "li de lista"),
    (r'(<dd>)([^<]{3,})(</dd>)', "dd"),
    (r'(<div class="servicio__respuesta"><p>)(.*?)(</p>)', "respuesta"),
    (r'(<option>)([^<]+)(</option>)', "option"),
]


def contar(txt):
    return max(1, len(re.sub(r"<[^>]+>", " ", txt).split()))


def tratar(ruta):
    p = pathlib.Path(ruta)
    t = p.read_text(encoding="utf-8")
    orig = t
    cambios = 0

    for clase in CLASES:
        patron = re.compile(r'(<(\w+)[^>]*class="[^"]*\b' + clase + r'\b[^"]*"[^>]*>)(.*?)(</\2>)', re.S)

        def sust(m):
            nonlocal cambios
            dentro = m.group(3)
            if "<" in dentro and ">" in dentro:      # lleva marcado dentro, se deja
                return m.group(0)
            cambios += 1
            return m.group(1) + relleno(contar(dentro), len(dentro) + cambios) + m.group(4)

        t = patron.sub(sust, t)

    for patron, _ in SUELTOS:
        def sust2(m):
            nonlocal cambios
            cambios += 1
            return m.group(1) + relleno(contar(m.group(2)), len(m.group(2)) + cambios) + m.group(3)
        t = re.sub(patron, sust2, t, flags=re.S)

    if t != orig:
        p.write_text(t, encoding="utf-8")
    return cambios


if __name__ == "__main__":
    total = 0
    for ruta in sorted(pathlib.Path("partes").glob("*.html")):
        c = tratar(ruta)
        if c:
            print(f"  {ruta.name}: {c}")
            total += c
    print("\ncajas pasadas a relleno:", total)
