# AGENTIA · agentia.com.pe

Sitio estático de **cinco páginas**. Sin dependencias y sin framework, pero
**con un armador propio** de 150 líneas en Python puro.

Paquete preparado el 9 de octubre de 2026. Partido en cinco páginas el 10.

---

## 1. Arranque en treinta segundos

No hay `npm install`. Solo Python, que ya viene en cualquier Mac o Linux:

```
python3 servidor-local.py
```

Y abre `http://localhost:5173`.

Ese comando hace dos cosas: **arma el sitio** con `armar.py` y lo sirve sin
caché. Rearma en cada página que pides, así que editas una pieza de `partes/`,
recargas, y lo ves. No hay paso manual que olvidar.

**Ya no existe `index.html` en el repositorio: se genera.** Si lo buscas para
editarlo, lo que quieres está en `partes/`.

Si solo quieres servir lo ya armado: `python3 armar.py && python3 -m http.server 5173 --directory _sitio`.

---

## 2. Qué hay dentro

```
armar.py                        el armador. Lee partes/ y escribe _sitio/
comprobar.py                    enlaces, anclas y encabezados del sitio armado
armar-captura.py                copias autocontenidas para subir a Figma
partes/cabeza.html              head, barra y menú móvil. Los comparten las nueve
partes/pie.html                 el pie, idem
partes/hero.html                el hero de la portada
partes/seccion-*.html           una pieza por sección
_sitio/                         lo que se publica. Se genera, no se versiona
assets/css/agentia.css          todo el CSS, con los tokens en :root
assets/js/agentia.js            todo el JS, sin librerías
assets/fonts/*.woff2            tres tipografías variables autoalojadas
assets/fonts/OFL-*.txt          sus licencias. Tienen que viajar con las fuentes
assets/img/agentia-*.svg        logotipo original y sus piezas extraídas
docs/diseno.md                  el sistema de diseño. Léelo antes de tocar CSS
docs/contenido-agentia.md       el contenido aprobado y los pendientes
docs/direcciones.md             la auditoría del sitio v1 y por qué se eligió esto
docs/benchmark.md               siete sitios del sector, medidos. Qué nos falta y qué no
docs/benchmark-nosotros.md      nueve «About» de empresas de tecnología, medidas
docs/benchmark-home.md          nueve portadas de plataformas de contenido con IA
servidor-local.py               servidor de desarrollo sin caché
agentia-historial.bundle        el repositorio git completo, 13 commits
```

Peso de lo que se despliega: **328 KB**, de los cuales 222 KB son las tres tipografías.

### Las nueve páginas

| Ruta | Qué lleva |
|---|---|
| `/` | Hero · los seis servicios en resumen · formulario |
| `/servicios/` | El mando que gira y los seis en detalle |
| `/trabajos/` | Los tres tipos y la galería. Seis huecos esperando material |
| `/trabajos/video/` | Qué entra en video. Sin galería todavía |
| `/trabajos/grafica/` | Qué entra en gráfica. Sin galería todavía |
| `/trabajos/web/` | Qué entra en web. Sin galería todavía |
| `/nosotros/` | Quiénes somos · por qué · cómo trabajamos · para quién es |
| `/preguntas/` | Las cinco preguntas frecuentes. Salió de Nosotros el 10 de octubre |
| `/agentia/` | Página de salto a `/nosotros/`. La ruta cambió el 10 de octubre |
| `/contacto/` | Los tres correos. **Sin formulario**: ese vive en la portada |

Quién lleva qué lo decide la lista `PAGINAS` de `armar.py`. Añadir una página
es añadir una entrada ahí y una pieza en `partes/`. La ruta puede llevar barra:
`trabajos/video` se arma en `_sitio/trabajos/video/` y el armador le calcula
solos los `../../` que necesita para llegar a los assets.

**Las internas no van en el menú.** El menú tiene seis entradas —Inicio,
Servicios, Trabajos, Nosotros, Preguntas, Contacto—; a las tres de Trabajos se
llega desde su índice y se vuelve con la miga. Estando en una de ellas el menú
señala Trabajos.

Seis entradas más el botón Agendar caben hasta los 900 px, que es el ancho más
estrecho antes de que el menú pase a ser el panel móvil (860 px). Una séptima ya
no: comprobado midiendo, no a ojo.

### Comprobar antes de publicar

```bash
python3 armar.py && python3 comprobar.py
```

Revisa tres cosas sobre el sitio ya armado: que no quede ningún enlace interno
apuntando a nada, que cada ancla `#algo` exista de verdad en la página a la que
apunta, y que cada página tenga un `h1` y solo uno. Sale con código 1 si algo
falla, y el workflow lo corre antes de publicar.

Existe porque un enlace roto **no rompe el armado**: la página se publica, el
botón se ve perfecto y al pulsarlo no pasa nada. Pasó con un botón que apuntaba
a `#contacto` después de que esa sección se mudara a su propia página.

### Recuperar el historial de git

```
git clone agentia-historial.bundle agentia
```

Trae los 13 commits con sus mensajes, que explican cada decisión y cada
corrección. El primero es el sitio original sin tocar, por si hace falta
comparar.

---

## 2.b El diseño se trabaja en Figma

**Desde el 10 de octubre de 2026**, por decisión de Agentia: los cambios de
diseño se hacen primero en el lienzo, no editando el CSS.

**Archivo:** `Agentia · Mapa del sitio`
https://www.figma.com/design/mi9HmucUhbd0rcMBNntq9I

Una página, un tablero, las cinco pantallas colocadas como mapa del sitio, con
sus rutas y sus conectores. Son capas editables capturadas del sitio publicado,
no imágenes.

**El motivo fue el ciclo.** Cada retoque obligaba a publicar, esperar el
despliegue y pelear con la caché del navegador. Varias veces se reportó «sigue
igual» mirando una versión anterior. En el lienzo ese ciclo no existe.

**Lo que esto implica para quien toque este repositorio:**

- **El sitio publicado queda congelado** donde está hasta que Agentia pida bajar
  lo de Figma al código. Si lo editas por tu cuenta, los dos se separan y
  reconciliarlos después cuesta más que hacerlo bien ahora.
- **Rutas, formulario, rendimiento y accesibilidad siguen siendo del código.**
  Figma no los resuelve. Eso se pregunta antes de tocar nada.
- **Al recapturar pantallas, se recapturan las cinco.** Un cambio en la barra o
  en el pie afecta a todas, no solo a la página que tocaste. Pasó ya una vez:
  se cambió el menú y en Figma quedaron cuatro capturas con el menú viejo.

### Cómo está montado el tablero

El mapa se ha rehecho varias veces y cada vez se perdían las mismas decisiones.
Quedan escritas:

| Qué | Valor | Por qué |
|---|---|---|
| Fondo del tablero | `#12142E` | Estuvo en `#f0f0f3`, casi el mismo gris que las páginas, y las pantallas no tenían borde: se fundían con el fondo |
| Títulos y nombres | `#FAFAFC` | Sobre el fondo oscuro |
| Rutas (`/servicios/`) | `#8FA6FF` | Es el azul aprobado sobre fondo oscuro, sección 3.3 del sistema |
| Notas y conectores | `#959CBE` | |
| Ruta sobre el marco | 270 px | |
| Nombre sobre el marco | 180 px | Deja 93 px de aire. Estuvo en 130 y los rótulos quedaban pegados a la barra de cada pantalla |
| Paso entre columnas, nivel 2 | 1680 px | Marco de 1280 más 400 de aire |
| Paso entre columnas, nivel 3 | **1400 px** | Más junto a propósito: un grupo apretado se lee como subordinado |
| Dónde empieza el nivel 3 | en la x de Trabajos | **No centrado.** Centrado, las tres internas caían justo bajo Servicios, Trabajos y Nosotros, y parecía que colgaban de las tres |
| Altura del nivel 3 | bajo el pie de **toda** la fila | Medido solo desde Trabajos se encaballa con Nosotros, que es mucho más alta |

### Cómo se recaptura

```
python3 armar.py                       # primero el sitio
python3 armar-captura.py               # las cinco, a _capturas/
python3 armar-captura.py nosotros      # o solo una
```

`armar-captura.py` deja una copia autocontenida de cada página: el CSS en
línea, la fuente en base64, sin JavaScript y con las piezas ya reveladas. Eso
hace falta porque **el convertidor de Figma no descarga nada ni ejecuta nada**:
lo que no esté dentro del archivo, no existe en el lienzo.

Ese archivo se sube con `html_to_figma` y el nodo que devuelve se coloca en el
tablero. `_capturas/` no se versiona: se regenera.

**Tres cosas que el convertidor no perdona**, y que ya costaron tiempo:

- **No resuelve los escapes unicode del CSS.** Un `content: '\00d7'` lo dibuja
  literal. La herramienta los sustituye por el carácter antes de subir.
- **No ejecuta JavaScript.** Sin el apaño, todo lo que el observador revela al
  bajar queda invisible.
- **Descarta las formas SVG sin relleno.** Los iconos de línea no sobreviven.
  Por eso, entre otras razones, ya no hay (sección 6.4 del documento de diseño).
- **Dibuja lo que está oculto.** El panel del menú móvil lleva `hidden` y
  `display: none`, y aun así lo pintaba encima de media página. La herramienta
  lo saca del documento.
- **No respeta `aspect-ratio`.** Los marcos del portafolio se aplastaban y la
  grilla se descuadraba. La herramienta les pone alto fijo: 276 px, que es lo
  que miden a 1280, el ancho al que renderiza el convertidor.

---

## 3. Dos documentos que mandan sobre el código

**`docs/diseno.md` es la ley del proyecto.** Ningún color, tamaño, espaciado ni
duración se escribe suelto en el CSS: todo sale de los tokens de `:root`. Si
necesitas un valor que no existe, se agrega primero al documento y después se usa.
Ahí está también la geometría medida del logotipo y por qué las rotaciones
funcionan como funcionan.

**La regla que manda sobre todas: menos es más.** La página tiene que fluir.
Un titular que resume lo que ya se entiende sin él estorba, y un rótulo pequeño
que no lleva un dato resta. Ante la duda, fuera: es más fácil volver a poner algo
que descubrir que molestaba. Está en la sección 1.0 de `docs/diseno.md` y el
armador avisa cuando se incumple.

**`docs/benchmark.md` dice contra quién nos medimos.** Siete sitios del sector
leídos uno por uno el 10 de octubre de 2026. El resumen en una línea: el oficio
de esta página está por encima de la media, y le falta lo único que todo el
mercado tiene sin excepción, que son casos con resultado. Antes de discutir
cualquier cambio de la página, léelo.

**`docs/contenido-agentia.md` es la fuente del contenido.** Titulares, servicios y
textos salen de ahí sin reescribir. Lo que está marcado `[PENDIENTE]` o
`[VERIFICAR]` no se inventa ni se rellena: se deja marcado hasta que el cliente
entregue lo real.

---

## 4. Trampas del código. Léelo antes de refactorizar

Cada una de estas costó encontrarla. Si las "simplificas", algo se rompe.

### 4.1 `--giro` está registrada con `@property` a propósito

```css
@property --giro { syntax: '<angle>'; inherits: true; initial-value: 0deg; }
```

Sin registrar, una custom property es texto sin tipo: el navegador no la puede
interpolar y **congela** cualquier propiedad que la use y tenga transición. La
aguja de la tuerca se queda clavada sin dar ningún error en consola.

Por eso además **se anima la variable, no la propiedad**. La transición va sobre
`--giro` en `.tuerca`, y el `transform: rotate(var(--giro))` del agarre no lleva
transición propia.

Soporte: Chrome 85+, Safari 16.4+, Firefox 128+.

> Aquí vivían también `--gemelo`, `--sep` y `--escala`, que abrían el estado de
> código del isotipo anterior. Con la insignia no hay brazos que separar y se
> quitaron. Si aparecen en algún sitio, es código muerto.

### 4.2 La insignia no gira, y eso no es un olvido

**Un cuadrado girado 90 grados es el mismo cuadrado.** El isotipo anterior tenía
cuatro estados que eran cuatro rotaciones de 90 grados; con el cuadro IA esa
rotación no se leería y el mando parecería roto.

Por eso la insignia cambia de **glifo**, no de ángulo: `IA`, triángulo de
reproducción, lápiz, `< >`. Los cuatro se apilan en la misma celda de grilla y
se turnan con opacidad y escala.

La aguja de la tuerca **sí** gira, porque una aguja es la forma a la que la
rotación le sienta. Si alguien "arregla" esto haciendo girar la insignia, el
mando deja de comunicar nada.

### 4.3 En el campo del hero la rotación sí se lee

Las 29 piezas son el mismo cuadro y **sí** giran, hacia el puntero. La diferencia
con la insignia es que aquí los ángulos son libres: un cuadro inclinado 30 grados
se distingue perfectamente de uno recto.

La regla no es "los cuadrados no giran". Es **los cuadrados no giran en múltiplos
de 90**.

### 4.4 El contenido es visible por defecto

Las entradas al hacer scroll funcionan al revés de lo habitual: el contenido se ve,
y el script **añade** la clase `js-rv` al `<html>` para autorizar que se esconda y
se revele. Además hay una red de seguridad a los 2.5 segundos.

Motivo: el patrón normal, esconder con `opacity: 0` y que el JS lo revele, deja la
página **en blanco** si el `IntersectionObserver` no dispara. Pasa de verdad, por
ejemplo con la pestaña en segundo plano. No lo inviertas.

### 4.5 El bucle de físicas del hero lleva control explícito de fotograma

El campo de 29 piezas guarda el id del `requestAnimationFrame` y escucha
`visibilitychange`. Si la pestaña se va al fondo con un fotograma pendiente, el
navegador lo congela y sin ese control el campo se queda muerto para siempre.

Las piezas además **nacen alineadas a cero**, no desordenadas, por el mismo motivo
que 4.4: si el bucle nunca corre, el campo se ve igual de correcto.

El campo se oculta por debajo de 900 px: se activa con el puntero y en táctil no
hay puntero.

### 4.6 Cuidado con el nombre de clase `.campo`

`.campo` son los campos del formulario. El SVG de las piezas del hero es
`.campo-piezas`. Compartieron nombre por error y el formulario heredaba ancho y
alto al 100%, lo que convertía el input de Nombre en una caja gigante. No vuelvas
a juntarlos.

### 4.7 El logotipo depende de que la fuente cargue

Se compone con **Instrument Sans 700 al 92% de ancho**, no con trazados. Eso lo
hace escalar a cualquier tamaño sin exportar versiones, pero si la tipografía no
carga, el logotipo se dibuja con la fuente del sistema y deja de ser el logotipo.

La fuente va autoalojada y precargada, que es el escenario en el que esto falla
menos. Si hace falta blindarlo del todo, se piden los trazados a quien firmó la
propuesta y se cambia la regla `.logo` por un SVG.

El 92% no se toca con `letter-spacing`: apretar junta las letras sin adelgazarlas
y el bloque se ensucia. Es el eje de ancho variable de la familia.

### 4.8 Nada de rutas que empiecen por barra

En `partes/` las rutas se escriben con `{{RAIZ}}` delante:

```html
<link rel="stylesheet" href="{{RAIZ}}assets/css/agentia.css">
<a href="{{RAIZ}}servicios/">Servicios</a>
```

`{{RAIZ}}` vale `""` en la portada y `"../"` en las internas. **No se puede usar
`/assets/...`**: el sitio vive en `aerebo.github.io/web_agentia/`, o sea en un
subdirectorio, y una ruta absoluta se iría a la raíz del dominio y daría 404.

Funcionaría en el dominio propio y fallaría en la vista previa, que es la peor
combinación posible: se rompe justo donde lo revisa el equipo.

### 4.9 El CSS y el JS van con sello de contenido en la URL

`armar.py` les cuelga `?v=` y ocho caracteres del hash del archivo:

```html
<link rel="stylesheet" href="assets/css/agentia.css?v=5bf0d3ec">
```

**Sin eso el navegador se queda con el CSS que ya tenia aunque el HTML sea
nuevo.** GitHub Pages sirve los assets con cache y la URL no cambiaba nunca.
El sintoma es de los peores que hay: la pagina carga, no da ningun error, y
simplemente no se ve el cambio. Paso de verdad durante el desarrollo.

Va por contenido y no por fecha: si el archivo no cambia, la URL tampoco, y
el navegador se lo ahorra de verdad.

**El HTML sigue sin sello**, porque no puede tenerlo: es la puerta de
entrada. Para eso esta el sello de version del pie, que dice de un vistazo
si lo que ves es lo ultimo.

### 4.10 El radio del cuadro IA ya no es el medido

El original entregado tenía radio 0.19 de la altura de mayúscula. En el código
dice 0.24, y no es un error de transcripción.

Desde que la página tiene tarjetas redondeadas (10 de octubre de 2026), 0.19
convertía al cuadro de marca en una tarjeta pequeña más. Se subió a 0.24 para
que siga siendo lo más redondeado de la página.

**Si algún día se quitan las tarjetas, vuelve a 0.19.** Ver la sección 6 de
`docs/diseno.md`.

### 4.11 La página activa se marca al armar, no con JavaScript

`armar.py` le pone `aria-current="page"` al enlace de la página en la que estás.
Se hace al armar a propósito: si dependiera del script, un fallo de JS dejaría el
menú sin indicar dónde está el visitante, y eso es orientación, no adorno.

Va por el atributo `data-nav` de los diez enlaces del menú, no por su `href`.
Buscar el href fallaba en cuanto una página enlazaba a su propia sección desde el
cuerpo: `/trabajos/video/` tiene una miga que vuelve a `/trabajos/` con el mismo
href que el menú, y la miga acababa marcada también como página actual.

### 4.12 El h1 lo pone el armador

Cuatro de las cinco páginas se quedaron sin `h1` al partir el sitio: todas las
secciones traen su titular como `h2` porque nacieron siendo secciones de una sola
página larga, donde el `h1` era el del hero.

El armador sube a `h1` el primer titular de cada página, si no hay uno ya. Se hace
ahí y no editando las piezas porque **una misma pieza es la primera en una página
y la tercera en otra**: el resumen de servicios abre la portada por debajo del
hero, que ya tiene su `h1`, así que ahí tiene que seguir siendo `h2`. La posición
la sabe el armador, no la pieza. `comprobar.py` vigila que siga cumpliéndose.

---

## 5. Lo que ya cumple. No lo rompas

Todo esto está medido en navegador, no estimado.

**Contraste.** Mínimo 5.21:1 sobre fondos claros y 6.86:1 sobre la banda oscura.
Todo AA. El azul de marca `#1540F5` da 5.99:1 sobre papel, así que **sí sirve para
texto pequeño**, al revés que el violeta anterior, que daba 3.54:1 y estaba
prohibido. Sobre la banda oscura el azul de marca **no** se usa: da 2.72:1. Ahí va
`--azul-claro` `#8FA6FF`, y por eso el logotipo del pie se invierte.

**Teclado.** Enlace de salto al contenido, anillo de foco visible en todo elemento
interactivo, la tuerca operable con flechas, el acordeón con botones reales, y el
menú móvil cierra con Escape devolviendo el foco al botón que lo abrió.

**Lectores de pantalla.** Las tres fichas de servicio ocultas quedan fuera del
orden de tabulación y del árbol de accesibilidad. La tuerca anuncia el nombre del
modo en español, no un número. Los SVG decorativos van con `aria-hidden`.

**Responsive.** Verificado sin desborde horizontal en 360, 768 y 1440.

**`prefers-reduced-motion`.** Respetado en todo: las físicas pasan a estático y las
entradas se desactivan.

---

## 6. Lo que falta. Nada de esto está hecho

| Pendiente | Bloqueado por |
|---|---|
| Conectar el formulario | Decidir entre `contact.php` propio o servicio externo |
| `favicon` | Nada. Se puede hacer ya, a partir del cuadro IA |
| Imagen OG 1200×630 | Nada. Se puede hacer ya |
| `sitemap.xml` y `robots.txt` | Nada. Se puede hacer ya |
| `.cpanel.yml` | Falta el usuario real de cPanel |
| Trace de rendimiento | No se ha corrido todavía |

### El formulario no envía, y es a propósito

El `<form>` está completo: campos con `name`, etiquetas reales asociadas, campo
trampa contra spam (`.trampa`, el input `web`), y `novalidate` puesto para que la
validación sea de servidor y no del navegador.

**El botón se deshabilita hasta que los campos obligatorios estén completos y
el correo sea válido**, que es el comportamiento normal de cualquier formulario.
El aviso en pantalla de que el envío no está conectado se quitó el 10 de octubre
de 2026 por decisión de Agentia.

**Consecuencia que hay que tener presente:** con todo completo el botón se
habilita, y al pulsarlo el script frena el envío para no recargar la página y
perder lo escrito. O sea que **no pasa nada visible**. Esto se arregla solo
conectando el backend, no retocando el formulario.

**El botón viaja habilitado en el HTML** y es el script el que lo deshabilita,
al revés que lo habitual. Mismo motivo que la sección 4.4: si el script no
corre, un botón muerto para siempre es peor que uno que se pueda pulsar. Se hizo así para
que no finja funcionar, que es lo que hacía la versión anterior del sitio con un
`mailto:` disfrazado de botón de envío.

Cuando se decida el backend: destino `comercial@agentia.com.pe`, validación del
lado del servidor, sanitización de entradas, rechazar el envío si el campo trampa
viene lleno, y confirmación en la misma página.

### Presupuesto de rendimiento acordado

LCP por debajo de 2.5 s en 4G simulado, CLS por debajo de 0.1, primera vista por
debajo de 800 KB. Hoy el sitio pesa 328 KB y hace 5 peticiones, así que hay margen,
pero **el trace no se ha corrido**. No des por hecho que cumple hasta medirlo.

---

## 7. Despliegue en Verpex

Es un sitio estático, pero **hay que armarlo antes de subirlo**:

```
python3 armar.py
```

Y se sube el contenido de `_sitio/` a `public_html`. `partes/`, `docs/`,
`armar.py`, `servidor-local.py` y el bundle de git **no se suben**: son el
código fuente, no el sitio.

Si se hace por git desde cPanel, la regla importante: **el repositorio nunca se
clona dentro de `public_html`**. Va fuera de la raíz web, por ejemplo en
`/home/USUARIO/repos/agentia`, y un `.cpanel.yml` copia a `public_html` solo lo
público. Exponer `.git` en la raíz web deja el historial completo descargable por
cualquiera.

Antes de publicar, la checklist que está en `docs/contenido-agentia.md`: SSL activo
con redirección a HTTPS, buzones de correo creados, DNS apuntando, compresión y
caché activadas, y formulario probado con un envío real.

---

## 8. Decisiones abiertas con el cliente

No son tareas técnicas: necesitan respuesta de Agentia antes de tocarse.

1. **Backend del formulario.** PHP propio o servicio externo.
2. **Alto del hero.** Mide 1108 px y en una ventana de 900 los botones quedan bajo
   el pliegue. Hay tres salidas posibles y ninguna es obviamente mejor.
3. ~~**Dos servicios fuera del mando.**~~ **Resuelto el 10 de octubre de 2026.** El
   banco de marca se fusiono con Servicios: la tuerca muestra cuatro en detalle y
   el acordeon de abajo enumera los seis. Ya no se contradicen.
4. **Permisos de logo de clientes**, y decidir si se atribuyen a Agentia o a otra
   marca del grupo. Hoy aparecen como texto, con el aviso puesto.
5. **Material real de casos.** Sin piezas reales, la sección de casos no se publica.
6. **Teléfono, WhatsApp y handles de redes.**
7. **Cifras de trayectoria.** No se publican hasta contarlas. En la pagina solo
   van las tres confirmadas: ciudades, sectores y produccion propia.
8. **Material para Trabajos.** Seis huecos esperando pieza real. Por cada una
   hace falta imagen o video, tipo, cliente con permiso y titulo. Ver la
   seccion 8.a de `docs/contenido-agentia.md`.
9. **Testimonios.** Aparcados por Agentia el 10 de octubre de 2026. Se suben
   despues. No volver a proponerlos.
10. **Entregables del proceso.** Las lineas de «recibes» y «te pedimos» de cada
   paso son redaccion propuesta, derivada de lo que ya decia cada paso, pero
   comprometen entregables. Confirmar antes de publicar.
11. **Las tres puertas que cierra «para quien no es».** Pieza suelta, precio mas
   bajo, e IA sin revision humana. Son tres clientes que Agentia rechaza por
   escrito. Confirmar las tres.
12. **Cinco preguntas frecuentes sin respuesta.** Contratar un solo servicio,
   que pasa si ya hay agencia, permanencia minima, de quien son los archivos al
   terminar, y si se publican rangos de precio. Estan listadas en la seccion 8.c
   de `docs/contenido-agentia.md` y no se publican hasta tener respuesta. La de
   los archivos es la que mas incomoda y la que mas confianza da contestarla.

---

## 9. Tipografía y licencia

**Una sola familia desde el 10 de octubre de 2026: Instrument Sans.**

Antes eran tres: Bricolage Grotesque para titulares, Instrument Sans para el
cuerpo y Martian Mono para cotas y números. Agentia pidió una sola.

**Se conservó Instrument Sans por un motivo que no admite discusión: el
logotipo está construido con ella.** Cambiar de familia sería cambiar la marca.

| Rol | Ejes variables |
|---|---|
| Todo | peso 400-700, ancho 75-100 |

Solo se incluye el subconjunto latino, que cubre el español completo con
acentos, eñe y signos de apertura.

Es **SIL Open Font License 1.1**, que permite el autoalojamiento sin pagar y
sin pedir permiso. La licencia está en `assets/fonts/` y **tiene que viajar con
el archivo** si el sitio se copia a otro lado.

Las dos familias que se fueron se borraron con sus licencias. La OFL obliga a
que la licencia viaje con la fuente, no a guardarla cuando la fuente ya no está.
Se recuperan del historial de git si alguna vez vuelven.

**Qué se ganó y qué se perdió.** Se ganaron 166 KB: el sitio pasó de 352 a 186.
Se perdió el contraste tipográfico entre titular, cuerpo y cota, que ahora se
distinguen solo por tamaño, peso, caja y tracking. Son cuatro señales y bastan,
pero es menos de lo que había.

El logotipo **sí es tipografía**, al revés que el original de Illustrator:
Instrument Sans 700 al 92% de ancho. Ver la sección 2 de `docs/diseno.md`.
