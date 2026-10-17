#!/usr/bin/env python3
"""Arma una copia autocontenida de una pagina para subirla a Figma.

html_to_figma no descarga nada: ni la hoja de estilos, ni la fuente, ni las
imagenes. Todo lo que no este dentro del archivo, no existe. Esto mete el CSS
en linea, la fuente como data: URI, quita el JS (el convertidor no lo ejecuta y
las piezas con `rv` se quedarian invisibles) y deja la pagina quieta en su
estado final.

Uso:  python3 armar-captura.py nosotros        -> _capturas/nosotros.html
      python3 armar-captura.py trabajos/video -> _capturas/trabajos-video.html
      python3 armar-captura.py                -> las ocho
"""

import base64
import pathlib
import re
import sys

import armar as armador

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


ANCHO_MOVIL = 375


def fijar_escala_fluida(css: str) -> str:
    """Resuelve los clamp() con vw al valor que tendrian en 375 px.

    Este es el que de verdad inflaba la captura movil, y costo encontrarlo.
    El convertidor renderiza la pagina en una ventana de 1280 px aunque el
    cuerpo mida 375, asi que una unidad vw sigue valiendo 12,8 px. El
    titular del hero, que es clamp(3rem, 9vw, 7.5rem), salia a 115 px en vez
    de a 48: toda la escala tipografica del sitio es fluida, asi que la
    pagina entera salia entre un 20 y un 77 por ciento mas alta.

    Aqui cada clamp se sustituye por el numero que daria en un telefono.
    """

    def a_px(valor, unidad):
        return float(valor) * (16.0 if unidad == "rem" else 1.0)

    def resolver(m):
        minimo = a_px(m.group(1), m.group(2))
        medio = float(m.group(3)) * ANCHO_MOVIL / 100.0
        maximo = a_px(m.group(4), m.group(5))
        return "%.4gpx" % max(minimo, min(medio, maximo))

    css = re.sub(
        r"clamp\(\s*([\d.]+)(rem|px)\s*,\s*([\d.]+)vw\s*,\s*([\d.]+)(rem|px)\s*\)",
        resolver, css)

    # Y cualquier vw que quede suelto. El primer arreglo solo miraba dentro
    # de clamp(), y la tarjeta del carrusel usa min(78vw, 22rem): salia a
    # 352 px en vez de 293 y se comia el borde de la tarjeta siguiente, que
    # es justo lo que avisa de que el carrusel se desliza.
    return re.sub(r"([\d.]+)vw",
                  lambda m: "%.4gpx" % (float(m.group(1)) * ANCHO_MOVIL / 100.0),
                  css)


def forzar_movil(css: str) -> str:
    """Deja el CSS como si la ventana midiera 375 px.

    El convertidor de Figma renderiza siempre a 1280, asi que las consultas
    de medios nunca se activan y la captura sale en escritorio pase lo que
    pase. Aqui se sacan las reglas de los bloques `@media (max-width: N)`
    con N >= 375 y se vuelven a pegar al final, sin envolver: al ir las
    ultimas, ganan por orden de cascada.

    Las de `prefers-reduced-motion` y las de ancho minimo se quedan dentro,
    que no tienen nada que ver con el ancho del telefono.
    """
    fuera = []
    salida = []
    i = 0
    while True:
        j = css.find("@media", i)
        if j == -1:
            salida.append(css[i:])
            break

        fin_cabecera = css.find("{", j)
        cabecera = css[j:fin_cabecera]

        # Cerrar el bloque contando llaves
        prof = 0
        k = fin_cabecera
        while k < len(css):
            if css[k] == "{":
                prof += 1
            elif css[k] == "}":
                prof -= 1
                if prof == 0:
                    break
            k += 1

        cuerpo = css[fin_cabecera + 1:k]
        m = re.search(r"max-width:\s*(\d+)px", cabecera)
        if m and int(m.group(1)) >= ANCHO_MOVIL and "min-width" not in cabecera:
            fuera.append(cuerpo)
            salida.append(css[i:j])          # el bloque entero se omite aqui
        else:
            salida.append(css[i:k + 1])      # se queda tal cual

        i = k + 1

    ancho = (
        "\n/* --- captura de movil: la ventana se simula en %d px --- */\n"
        "html, body { width: %dpx; max-width: %dpx; overflow-x: hidden; }\n"
        % (ANCHO_MOVIL, ANCHO_MOVIL, ANCHO_MOVIL)
    )
    return "".join(salida) + ancho + "\n".join(fuera)


# Lo que el movil oculta con display:none y el convertidor dibuja igual.
# Mismo problema que el panel del menu: hay que sacarlo del documento, no
# basta con ocultarlo. Si no, la captura trae el contenido de escritorio
# apretado en 375 px y sale un sesenta por ciento mas alta de lo que mide
# la pagina de verdad.
OCULTOS_EN_MOVIL = [
    r'<p class="hero__marca">.*?</p>',
    r'<div class="hero__campo".*?</div>\s*',
    r'<ul class="nav__enlaces">.*?</ul>\s*',
]


def quitar_lo_que_el_movil_oculta(h: str) -> str:
    for patron in OCULTOS_EN_MOVIL:
        h = re.sub(patron, "", h, flags=re.S)
    # El boton Agendar de la barra: el primero dentro de nav__acciones.
    h = re.sub(r'(<div class="nav__acciones">)\s*<a class="boton[^"]*"[^>]*>.*?</a>',
               r"\1", h, count=1, flags=re.S)
    return h


def armar_captura(ruta: str, movil: bool = False) -> pathlib.Path:
    carpeta = SITIO if ruta in ("", "/") else SITIO / ruta
    origen = carpeta / "index.html"
    if not origen.exists():
        sys.exit(f"no existe {origen}; corre primero armar.py")

    h = origen.read_text(encoding="utf-8")

    css = (SITIO / "assets/css/agentia.css").read_text(encoding="utf-8")
    css = inline_fuente(css)
    css = resolver_escapes(css)
    if movil:
        css = fijar_escala_fluida(css)
        css = forzar_movil(css)

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

    if movil:
        h = quitar_lo_que_el_movil_oculta(h)

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
    # Una ruta puede tener barra, como trabajos/video. El archivo se llama
    # trabajos-video.html y queda todo plano: son capturas para subir una a
    # una, no un sitio, y asi se ven juntas al listar la carpeta.
    base = ruta.replace("/", "-") if ruta else "portada"
    destino = SALIDA / (base + ("-movil" if movil else "") + ".html")
    destino.write_text(h, encoding="utf-8")
    return destino


if __name__ == "__main__":
    # Sin argumentos, las que diga el armador: asi no hay dos listas de
    # paginas que puedan quedar desparejas.
    argumentos = sys.argv[1:]
    movil = "--movil" in argumentos
    argumentos = [a for a in argumentos if a != "--movil"]

    todas = [p["ruta"] for p in armador.PAGINAS]
    for ruta in argumentos or todas:
        d = armar_captura(ruta, movil=movil)
        print(f"{d.name}  {d.stat().st_size // 1024} KB")
