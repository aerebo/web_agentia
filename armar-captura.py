#!/usr/bin/env python3
"""Arma una copia autocontenida de una pagina para subirla a Figma.

html_to_figma no descarga nada: ni la hoja de estilos, ni la fuente, ni las
imagenes. Todo lo que no este dentro del archivo, no existe. Esto mete el CSS
en linea, la fuente como data: URI, quita el JS (el convertidor no lo ejecuta y
las piezas con `rv` se quedarian invisibles) y deja la pagina quieta en su
estado final.

Uso:  python3 armar-captura.py nosotros  ->  _capturas/nosotros.html
"""

import base64
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).parent
SITIO = RAIZ / "_sitio"
SALIDA = RAIZ / "_capturas"


def inline_fuente(css: str) -> str:
    """Cambia cada src: url(...woff2) por el archivo en base64."""

    def pegar(m):
        nombre = pathlib.Path(m.group(1)).name
        archivo = SITIO / "assets" / "fonts" / nombre
        if not archivo.exists():
            return m.group(0)
        b64 = base64.b64encode(archivo.read_bytes()).decode("ascii")
        return f"url(data:font/woff2;base64,{b64})"

    return re.sub(r'url\(["\']?([^"\')]+\.woff2)["\']?\)', pegar, css)


ESCAPE_CSS = re.compile(r"(['\"])\\([0-9a-fA-F]{2,6})\s*\1")


def resolver_escapes(css: str) -> str:
    """Cambia los escapes unicode del CSS por el caracter que representan.

    El convertidor de Figma lee la hoja como texto plano y no resuelve
    `\\00d7`, asi que lo dibuja literal en el lienzo. Aqui se resuelven
    antes de que la vea.
    """
    return ESCAPE_CSS.sub(
        lambda m: m.group(1) + chr(int(m.group(2), 16)) + m.group(1), css
    )


def armar(ruta: str) -> pathlib.Path:
    carpeta = SITIO if ruta in ("", "/") else SITIO / ruta
    origen = carpeta / "index.html"
    if not origen.exists():
        sys.exit(f"no existe {origen}; corre primero armar.py")

    h = origen.read_text(encoding="utf-8")

    css = (SITIO / "assets/css/agentia.css").read_text(encoding="utf-8")
    css = inline_fuente(css)
    css = resolver_escapes(css)

    # La hoja de estilos entra en linea. Ojo: el reemplazo va como lambda, no
    # como cadena. Si va como cadena, re.sub le lee las barras invertidas como
    # escapes suyos y un `\\00d7` del CSS acaba convertido en un byte nulo.
    h = re.sub(
        r'<link rel="stylesheet"[^>]*>',
        lambda _: "<style>\n" + css + "\n</style>",
        h,
        count=1,
    )

    # Fuera el JS y el preload de la fuente: ya va dentro del CSS.
    h = re.sub(r'<script src="[^"]*agentia\.js[^"]*"[^>]*></script>', "", h)
    h = re.sub(r'<link rel="preload"[^>]*>', "", h)

    # El panel del menu movil esta oculto con [hidden] y display:none, pero el
    # convertidor lo dibuja igual y se come media pagina. Fuera del documento.
    h = re.sub(r'<div class="menu"[^>]*\bhidden\b[^>]*>.*?</div>\s*(?=<main|<header|<section)',
               "", h, flags=re.S)

    # El convertidor no corre JS, asi que las piezas que el observador revela
    # al bajar nunca se revelarian. Se dejan ya reveladas. Y `aspect-ratio` no
    # lo respeta: los marcos del portafolio se aplastan y la grilla se
    # descuadra, asi que se les da alto fijo. 276 px es lo que miden a 1280,
    # que es el ancho al que renderiza el convertidor.
    h = h.replace("</style>", """
/* --- solo para la captura de Figma --- */
.rv, .rv.rv--visible { opacity: 1 !important; transform: none !important; }
* { animation: none !important; transition: none !important; }
.trabajo__marco { aspect-ratio: auto; height: 276px; }
.insignia { aspect-ratio: auto; height: 176px; }
.menu { display: none !important; }
</style>""", 1)

    SALIDA.mkdir(exist_ok=True)
    destino = SALIDA / f"{ruta or 'portada'}.html"
    destino.write_text(h, encoding="utf-8")
    return destino


if __name__ == "__main__":
    for ruta in sys.argv[1:] or ["", "servicios", "trabajos", "nosotros", "contacto"]:
        d = armar(ruta)
        print(f"{d.name}  {d.stat().st_size // 1024} KB")
