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

# Rutas que cambiaron de nombre. Siguen existiendo como pagina de salto
# porque ya se habian compartido: quien tenga el enlace viejo guardado
# llega al nuevo en vez de encontrarse un 404.
#
# Pages no sabe hacer redirecciones de servidor, asi que se hace con la
# pagina: meta refresh para el navegador, canonical para los buscadores y
# noindex para que la vieja no compita con la nueva en Google.
REDIRECCIONES = {
    "agentia": "nosotros",
}

PAGINAS = [
    # Portada. Replica la estructura de mindcircus.agency medida el 17 de
    # octubre de 2026: hero, intro con una sola llamada, rejilla de
    # servicios, franja de clientes, banner de frase, equipo, carrusel de
    # casos, herramientas, cifras, formulario y cierre.
    {
        "ruta": "",
        "titulo": "Agentia · Agencia de marketing con IA en Perú",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        # Servicios y Trabajos no son secciones de la portada: son dos
        # botones. La portada presenta y reparte; el contenido vive en su
        # pagina. Antes llevaba el mando entero y el selector entero, que
        # son las dos paginas metidas aqui dentro.
        "piezas": ["hero", "seccion-intro", "seccion-puertas",
                   "seccion-formulario", "seccion-cta-contactar"],
        "prioridad": "1.0",
    },

    # Indice de servicios: hero, rejilla de seis, cierre.
    {
        "ruta": "servicios",
        "titulo": "Servicios · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        "piezas": ["seccion-servicios-selector", "seccion-cta-final"],
        "prioridad": "0.9",
    },
    {
        "ruta": "servicios/uno",
        "titulo": "Servicio · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        "piezas": ["seccion-servicio-interna", "seccion-cta-final"],
        "prioridad": "0.7",
    },
    {
        "ruta": "servicios/dos",
        "titulo": "Servicio · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        "piezas": ["seccion-servicio-interna", "seccion-cta-final"],
        "prioridad": "0.7",
    },
    {
        "ruta": "servicios/tres",
        "titulo": "Servicio · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        "piezas": ["seccion-servicio-interna", "seccion-cta-final"],
        "prioridad": "0.7",
    },
    {
        "ruta": "servicios/cuatro",
        "titulo": "Servicio · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        "piezas": ["seccion-servicio-interna", "seccion-cta-final"],
        "prioridad": "0.7",
    },
    {
        "ruta": "servicios/cinco",
        "titulo": "Servicio · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        "piezas": ["seccion-servicio-interna", "seccion-cta-final"],
        "prioridad": "0.7",
    },
    {
        "ruta": "servicios/seis",
        "titulo": "Servicio · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        "piezas": ["seccion-servicio-interna", "seccion-cta-final"],
        "prioridad": "0.7",
    },

    # Indice de trabajos: hero, filtros, rejilla de fichas, cierre.
    {
        "ruta": "trabajos",
        "titulo": "Trabajos · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        "piezas": ["seccion-trabajos-selector", "seccion-cta-final"],
        "prioridad": "0.9",
    },


    {
        "ruta": "nosotros",
        "titulo": "Nosotros · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        "piezas": ["seccion-equipo", "seccion-cifras", "seccion-nosotros-historia",
                   "seccion-puertas", "seccion-cta-final"],
        "prioridad": "0.8",
    },

    {
        "ruta": "preguntas",
        "titulo": "Preguntas frecuentes · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
        "piezas": ["seccion-preguntas", "seccion-cta-final"],
        "prioridad": "0.7",
    },

    {
        "ruta": "contacto",
        "titulo": "Contacto · Agentia",
        "descripcion": "Estructura en pruebas. Contenido pendiente.",
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

    Va por `data-nav` y no por href. Buscar el href fallaba en cuanto una
    pagina enlazaba a su propia seccion desde el cuerpo: /trabajos/video/
    tiene una miga que vuelve a /trabajos/, con el mismo href que el menu,
    y el replace marcaba tambien esa miga como pagina actual. El atributo
    solo esta en los diez enlaces del menu, asi que no hay confusion.

    Una interna marca su seccion madre: estando en /trabajos/video/ el
    menu senala Trabajos, que es donde el visitante cree que esta.
    """
    seccion = ruta.split("/")[0] if ruta else "inicio"
    marca = 'data-nav="%s"' % seccion
    return html.replace(marca, marca + ' aria-current="page"')


def promover_a_h1(html):
    """Sube a h1 el primer titular de la pagina, si no hay uno ya.

    Cuatro de las cinco paginas se quedaron sin h1 cuando el sitio se
    partio: todas las secciones traen su titular como h2 porque nacieron
    siendo secciones de una sola pagina larga, donde el h1 era el del
    hero. Repartidas en cinco paginas, cuatro quedaron empezando por h2.

    Para un buscador y para un lector de pantalla eso es una pagina sin
    titulo: el h1 es lo que anuncia de que va y es el primer salto de
    navegacion por encabezados.

    Se arregla aqui y no editando las piezas porque una misma pieza es la
    primera en una pagina y la tercera en otra. El resumen de servicios
    abre la portada por debajo del hero, que ya tiene su h1, y entonces
    tiene que seguir siendo h2. La posicion la sabe el armador, no la
    pieza.
    """
    if "<h1" in html:
        return html
    return re.sub(r'<h2(\s+class="seccion__titular[^"]*"[^>]*)>(.*?)</h2>',
                  r'<h1\1>\2</h1>', html, count=1, flags=re.S)


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
        # Una pagina puede colgar de otra: /trabajos/video/ esta a dos
        # niveles, asi que necesita dos "../" para llegar a los assets. Se
        # cuenta por segmentos y no por if, que es lo que habia cuando todas
        # las paginas estaban al mismo nivel.
        raiz = "../" * len([s for s in ruta.split("/") if s])
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
        html = promover_a_h1(html)

        sospechosos = avisar_de_eyebrows(html)
        if sospechosos:
            avisos.append((ruta or "(portada)", sospechosos))

        destino = SALIDA / ruta if ruta else SALIDA
        destino.mkdir(parents=True, exist_ok=True)
        (destino / "index.html").write_text(html, encoding="utf-8")

    for vieja, nueva in REDIRECCIONES.items():
        destino = SALIDA / vieja
        destino.mkdir(parents=True, exist_ok=True)
        (destino / "index.html").write_text(
            '<!DOCTYPE html>\n<html lang="es-PE">\n<head>\n'
            '<meta charset="UTF-8">\n'
            '<meta http-equiv="refresh" content="0; url=../%s/">\n'
            '<meta name="robots" content="noindex">\n'
            '<link rel="canonical" href="%s/%s/">\n'
            '<title>Esta página se mudó · Agentia</title>\n'
            '</head>\n<body>\n'
            '<p>Esta página ahora está en <a href="../%s/">/%s/</a>.</p>\n'
            '</body>\n</html>\n' % (nueva, DOMINIO, nueva, nueva, nueva),
            encoding="utf-8")

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
