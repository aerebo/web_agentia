# AGENTIA · agentia.com.pe

Sitio estático de una sola página. **Sin build, sin dependencias, sin framework.**
Se abre, se edita y se sube tal cual.

Paquete preparado el 9 de octubre de 2026.

---

## 1. Arranque en treinta segundos

No hay `npm install`. No hay nada que compilar. Solo hace falta un servidor estático,
porque abrir `index.html` con doble clic rompe la carga de tipografías por CORS.

Con Python:

```
python -m http.server 5173 --directory .
```

O usa `servidor-local.py`, incluido en este paquete, que además manda cabeceras
anti caché para que los cambios se vean al instante:

```
python servidor-local.py
```

Luego abre `http://localhost:5173`.

Con Node, si lo prefieres: `npx serve .` o `npx http-server -p 5173`.

---

## 2. Qué hay dentro

```
index.html                      la página entera
assets/css/agentia.css          todo el CSS, con los tokens en :root
assets/js/agentia.js            todo el JS, sin librerías
assets/fonts/*.woff2            tres tipografías variables autoalojadas
assets/fonts/OFL-*.txt          sus licencias. Tienen que viajar con las fuentes
assets/img/agentia-*.svg        logotipo original y sus piezas extraídas
docs/diseno.md                  el sistema de diseño. Léelo antes de tocar CSS
docs/contenido-agentia.md       el contenido aprobado y los pendientes
docs/direcciones.md             la auditoría del sitio v1 y por qué se eligió esto
servidor-local.py               servidor de desarrollo sin caché
agentia-historial.bundle        el repositorio git completo, 13 commits
```

Peso de lo que se despliega: **328 KB**, de los cuales 222 KB son las tres tipografías.

### Recuperar el historial de git

```
git clone agentia-historial.bundle agentia
```

Trae los 13 commits con sus mensajes, que explican cada decisión y cada
corrección. El primero es el sitio original sin tocar, por si hace falta
comparar.

---

## 3. Dos documentos que mandan sobre el código

**`docs/diseno.md` es la ley del proyecto.** Ningún color, tamaño, espaciado ni
duración se escribe suelto en el CSS: todo sale de los tokens de `:root`. Si
necesitas un valor que no existe, se agrega primero al documento y después se usa.
Ahí está también la geometría medida del logotipo y por qué las rotaciones
funcionan como funcionan.

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

**El botón está deshabilitado y la página lo dice en pantalla.** Se hizo así para
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

Es un sitio estático: basta con subir `index.html` y `assets/` a `public_html`.
`docs/`, `servidor-local.py` y el bundle de git **no se suben**.

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
7. **Cifras de trayectoria.** No se publican hasta contarlas.
8. **Entregables del proceso.** Las lineas de «recibes» y «te pedimos» de cada
   paso son redaccion propuesta, derivada de lo que ya decia cada paso, pero
   comprometen entregables. Confirmar antes de publicar.
9. **Las tres puertas que cierra «para quien no es».** Pieza suelta, precio mas
   bajo, e IA sin revision humana. Son tres clientes que Agentia rechaza por
   escrito. Confirmar las tres.
10. **Cinco preguntas frecuentes sin respuesta.** Contratar un solo servicio,
   que pasa si ya hay agencia, permanencia minima, de quien son los archivos al
   terminar, y si se publican rangos de precio. Estan listadas en la seccion 8.c
   de `docs/contenido-agentia.md` y no se publican hasta tener respuesta. La de
   los archivos es la que mas incomoda y la que mas confianza da contestarla.

---

## 9. Tipografías y licencias

Las tres son **SIL Open Font License 1.1**, que permite el autoalojamiento sin
pagar y sin pedir permiso. Las licencias están en `assets/fonts/` y **tienen que
viajar con los archivos** si el sitio se copia a otro lado.

| Rol | Familia | Ejes variables |
|---|---|---|
| Display | Bricolage Grotesque | peso 200-800, ancho 75-100, óptico 12-96 |
| Cuerpo | Instrument Sans | peso 400-700, ancho 75-100 |
| Datos | Martian Mono | peso 100-800, ancho 75-112.5 |

Solo se incluye el subconjunto latino, que cubre el español completo con acentos,
eñe y signos de apertura.

El logotipo **sí es tipografía**, desde el cambio de marca del 9 de octubre de
2026: Instrument Sans 700 al 92% de ancho. Esto invierte la regla anterior, que
exigía trazados, y el motivo es que la marca cambió de naturaleza. Los SVG del
logotipo viejo siguen en `assets/img/` pero ya no se usan en la página. Ver la
sección 2 de `docs/diseno.md`.
