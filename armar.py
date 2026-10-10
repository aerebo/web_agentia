"""Arma el sitio estático de Agentia a partir de las piezas de `partes/`.

Por qué existe
--------------
El sitio pasó de una página a cinco el 10 de octubre de 2026. La cabecera,
el menú y el pie son los mismos en las cinco. Sin un armador habría que
editarlos cinco veces y, el día que a alguien se le pase uno, el menú
queda distinto según la página. Eso es exactamente el tipo de error que
nadie nota hasta que lo ve un cliente.

No es un framework ni trae dependencias: lee archivos, sustituye cuatro
marcadores y escribe HTML. Solo biblioteca estándar de Python.

Qué produce
-----------
    _sitio/index.html            la portada
    _sitio/servicios/index.html  y el resto, cada una en su carpeta
    _sitio/sitemap.xml
    _sitio/robots.txt

`_sitio/` no se versiona: se genera. Lo arma el workflow al publicar y
`servidor-local.py` al servir en local.

Marcadores que entienden las piezas
-----------------------------------
    {{TITULO}}       el de la pestaña y el de og:title
    {{DESCRIPCION}}  la meta description y og:description
    {{URL}}          la canónica absoluta
    {{RAIZ}}         "" en la portada, "../" en las internas

`{{RAIZ}}` existe porque el sitio vive en un subdirectorio cuando se
publica en GitHub Pages, así que no se pueden usar rutas absolutas que
empiecen por barra: romperían fuera de la raíz del dominio.
"""

import hashlib
import pathlib
import re
import shutil

RAIZ = pathlib.Path(__file__).resolve().parent
PARTES = RAIZ / "partes"
SALIDA = RAIZ / "_sitio"

# El dominio final. Cuando agentia.com.pe apunte aquí, esto no cambia.
# Mientras tanto las canónicas apuntan al dominio real a propósito: es el
# que se va a indexar.
DOMINIO = "https://agentia.com.pe"

PAGINAS = [
    {
        "ruta": "",
        "titulo": "Agentia · Agencia de marketing con IA en Perú",
        "descripcion": "Sitios web que convierten, contenido a escala y campañas medibles. Producción creativa asistida por IA en Huaraz, Ica y Lima.",
        "piezas": ["hero", "seccion-servicios-resumen", "seccion-formulario"],
        "prioridad": "1.0",
    },
    {
        "ruta": "servicios",
        "titulo": "Servicios · Agentia",
        "descripcion": "Desarrollo web con IA, identidad y contenido, video, personajes de marca, diseño gráfico y pauta publicitaria.",
        "piezas": ["seccion-servicios"],
        "prioridad": "0.9",
    },
    {
        "ruta": "trabajos",
        "titulo": "Trabajos · Agentia",
        "descripcion": "Video, gráfica y web producidos dentro del mismo sistema de marca.",
        "piezas": ["seccion-trabajos"],
        "prioridad": "0.9",
    },
    {
        "ruta": "agentia",
        "titulo": "Agentia · Cómo trabajamos y quiénes somos",
        "descripcion": "Nuestro proceso paso a paso, qué recibes en cada uno, y quién está detrás. Operamos entre Huaraz, Ica y Lima.",
        "piezas": ["seccion-porque", "seccion-proceso", "seccion-quienes", "seccion-preguntas"],
        "prioridad": "0.8",
    },
    {
        "ruta": "contacto",
        "titulo": "Contacto · Agentia",
        "descripcion": "Cuéntanos qué necesitas resolver. Cotizaciones y propuestas en comercial@agentia.com.pe.",
        "piezas": ["seccion-correos"],
        "prioridad": "0.7",
    },
]


def sello(ruta):
    """Ocho caracteres del hash del archivo, para colgar de su URL.

    Sin esto, el navegador se queda con el CSS que ya tenia aunque el HTML
    sea nuevo: GitHub Pages sirve los assets con cache y la URL no cambia
    nunca. El sintoma es de los peores que hay, porque la pagina carga,
    no da ningun error, y simplemente no se ve el cambio. Pasa igual en
    el servidor local.

    Va por contenido y no por fecha: si el archivo no cambia, la URL
    tampoco, y el navegador se lo ahorra de verdad.
    """
    return hashlib.sha1((RAIZ / ruta).read_bytes()).hexdigest()[:8]


def pieza(nombre):
    return (PARTES / (nombre + ".html")).read_text(encoding="utf-8")


def resolver_piezas(html, vueltas=5):
    """Sustituye los {{PIEZA:nombre}} que una pieza tenga dentro.

    Existe porque el formulario aparece en dos sitios, la portada y
    /contacto/, y tenerlo copiado dos veces es pedir que alguien arregle
    un campo en uno y se olvide del otro. Es el mismo motivo por el que
    existe el armador entero.

    Con tope de vueltas: si dos piezas se incluyen entre si, para en vez
    de colgarse.
    """
    for _ in range(vueltas):
        if "{{PIEZA:" not in html:
            return html
        for nombre in set(re.findall(r"\{\{PIEZA:([a-z0-9-]+)\}\}", html)):
            html = html.replace("{{PIEZA:%s}}" % nombre, pieza(nombre))
    if "{{PIEZA:" in html:
        raise RuntimeError("piezas anidadas sin fin, revisa partes/")
    return html


# Un rotulo de cota seguido de un titular es el patron del «eyebrow»: una
# etiqueta pequena en caja alta que nombra la categoria de lo que el
# titular dice justo debajo. Agentia los fue quitando uno por uno el 10 de
# octubre de 2026 y pidio que no volvieran.
#
# La diferencia entre un eyebrow y una cota legitima no la da la posicion,
# la da el contenido:
#
#   eyebrow   «Servicios», «Hablemos», «Por que Agentia»  -> sobra
#   cota      «Video · Cliente por confirmar», «01»        -> es un dato
#
# Asi que se marca solo lo que ademas de ir encima de un titular no lleva
# ningun dato dentro: sin cifras, sin separador de campos y de cuatro
# palabras o menos. Las piezas de Trabajos pasan la prueba porque llevan
# el punto medio y el tipo de pieza.
#
# Avisa, no bloquea: es una regla de estilo, no un error. Pero sale en el
# registro del workflow, asi que nadie puede decir que no se vio.
EYEBROW = re.compile(
    r'<(p|span)[^>]*class="[^"]*\bspec\b[^"]*"[^>]*>([^<]{1,48})</\1>\s*<h[1-3]')


def avisar_de_eyebrows(html):
    """Rotulos pequenos que nombran la categoria del titular que va debajo."""
    sospechosos = []
    for m in EYEBROW.finditer(html):
        texto = m.group(2).strip()
        if any(c.isdigit() for c in texto):
            continue
        if "·" in texto or "|" in texto:
            continue
        if len(texto.split()) > 4:
            continue
        sospechosos.append(texto)
    return sospechosos


def marcar_activo(html, ruta):
    """Senala en el menu la pagina en la que estamos.

    Se hace al armar y no con JavaScript: si dependiera del script, un
    fallo de JS dejaria el menu sin indicar donde esta el visitante, y
    esa es informacion de orientacion, no un adorno.
    """
    destino = 'href="./"' if not ruta else 'href="../%s/"' % ruta
    return html.replace(destino, destino + ' aria-current="page"')


def armar():
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    SALIDA.mkdir()

    avisos = []
    cabeza = pieza("cabeza")
    pie = pieza("pie")
    version_css = sello("assets/css/agentia.css")
    version_js = sello("assets/js/agentia.js")

    for pagina in PAGINAS:
        ruta = pagina["ruta"]
        raiz = "" if not ruta else "../"
        url = DOMINIO + "/" + (ruta + "/" if ruta else "")

        # Los dos CTA llevan a sitios de verdad distintos: Agendar al
        # formulario, que vive solo en la portada, y Contactar a los
        # correos, que viven solo en /contacto/. Si la pagina actual ya
        # trae uno de los dos, se baja a el con un ancla en vez de
        # recargar otra pagina para ver lo que estaba debajo.
        piezas = pagina["piezas"]
        tiene_formulario = "seccion-formulario" in piezas
        tiene_correos = "seccion-correos" in piezas
        # el formulario vive solo en la portada, asi que desde fuera se va
        # a la raiz del sitio, no a /contacto/
        agendar = "#formulario" if tiene_formulario else raiz + "#formulario"
        # En la portada el enlace a Inicio es "./" y no "": vacio apunta a
        # la URL actual con sus parametros, y ademas no se puede marcar
        # como pagina actual sin pisar otros href vacios que aparezcan.
        inicio = "./" if not ruta else raiz
        contactar = "#correos" if tiene_correos else raiz + "contacto/#correos"

        cuerpo = resolver_piezas("\n\n".join(pieza(p) for p in pagina["piezas"]))
        html = cabeza + "\n\n" + cuerpo + "\n\n" + pie
        html = (html
                .replace("{{TITULO}}", pagina["titulo"])
                .replace("{{DESCRIPCION}}", pagina["descripcion"])
                .replace("{{URL}}", url)
                .replace("{{INICIO}}", inicio)
                .replace("{{AGENDAR}}", agendar)
                .replace("{{CONTACTAR}}", contactar)
                .replace("{{RAIZ}}", raiz))
        html = html.replace("assets/css/agentia.css",
                            "assets/css/agentia.css?v=" + version_css)
        html = html.replace("assets/js/agentia.js",
                            "assets/js/agentia.js?v=" + version_js)
        html = marcar_activo(html, ruta)

        sospechosos = avisar_de_eyebrows(html)
        if sospechosos:
            avisos.append((ruta or "(portada)", sospechosos))

        destino = SALIDA / ruta if ruta else SALIDA
        destino.mkdir(parents=True, exist_ok=True)
        (destino / "index.html").write_text(html, encoding="utf-8")

    shutil.copytree(RAIZ / "assets", SALIDA / "assets")
    (SALIDA / ".nojekyll").write_text("", encoding="utf-8")

    if (RAIZ / "CNAME").exists():
        shutil.copy(RAIZ / "CNAME", SALIDA / "CNAME")

    urls = "\n".join(
        "  <url><loc>%s</loc><priority>%s</priority></url>"
        % (DOMINIO + "/" + (p["ruta"] + "/" if p["ruta"] else ""), p["prioridad"])
        for p in PAGINAS)
    (SALIDA / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls + "\n</urlset>\n", encoding="utf-8")

    (SALIDA / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % DOMINIO,
        encoding="utf-8")

    for ruta, rotulos in avisos:
        print("AVISO  %s: rotulo pequeno encima de un titular -> %s"
              % (ruta, ", ".join(rotulos)))
        print("       Si el titular ya dice de que va, el rotulo sobra.")

    return [p["ruta"] or "(portada)" for p in PAGINAS]


if __name__ == "__main__":
    hechas = armar()
    print("armadas %d paginas: %s" % (len(hechas), ", ".join(hechas)))
