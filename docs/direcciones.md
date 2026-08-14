# Auditoría y direcciones visuales

Documento de decisión. Fase 3 (auditoría) y Fase 4 (tres direcciones).
Cuando se apruebe una dirección, se traslada a `docs/diseno.md` como sistema de tokens.

---

## Parte 1. Lectura de las referencias

### punchteam.com

Sistema extraído del sitio en vivo:

| Elemento | Valor real |
|---|---|
| Fondo | `#000000` puro |
| Texto | `#FFFFFF` |
| Acento único | `#FF1449` (rosa rojo saturado) |
| Familia | Plus Jakarta Sans, una sola para todo |
| H1 | 63 px, **peso 200**, interlineado 1.15, sin letter-spacing |
| Scroll | Lenis (inercia desacoplada del navegador) |

**El principio que vale la pena tomar:** la jerarquía se construye con peso y escala dentro de una sola familia, y el titular grande va en peso *ligero*, no en negrita. Un H1 de 63 px en peso 200 es una decisión contraintuitiva y es exactamente lo que hace que el sitio se sienta caro. Casi todos los sitios de agencia hacen lo contrario: display en 700 u 800.

**Lo que no se toma:** el negro puro (`#000000` se lee como pantalla apagada, conviene un negro tintado), y la fila de logos "Trusted by".

### slinky.pe

| Elemento | Valor real |
|---|---|
| Fondo | `#F0F3FF` (blanco con tinte azul) |
| Texto | `#020306` |
| Acentos | `#4D61F4` azul y `#DFFF6C` lima, dos a la vez |
| Display | Unbounded, peso 600, tracking -1.6 px a 64 px |
| Cuerpo | Inter |
| Motor | GSAP + Lenis |
| Hero | Alineado a la izquierda, H1 de 1020 px de ancho arrancando a 51 px del borde |
| Ritmo | Padding vertical de 100 a 160 px por sección |

**Esta referencia es sobre todo una advertencia, no un modelo.** Slinky opera en Lima, en tu mismo mercado, y su lista de servicios se solapa casi entera con la tuya: branding, diseño web, social, performance, apps, y desde 2026 agentes de IA y WhatsApp con IA. Su hero usa un verbo rotativo, sus servicios van numerados "01 / BRANDING", y tiene una marquesina de especialidades.

Consecuencia práctica para Agentia: **Unbounded queda descartada**, la combinación azul con lima queda descartada, y la numeración tipo "01 / SERVICIO" conviene evitarla, porque tu sitio actual ya numera el proceso y la lectura sería derivativa.

**El principio que sí vale la pena tomar:** la generosidad del margen. Hero alineado a la izquierda arrancando pegado al borde, y de 100 a 160 px de aire vertical entre secciones. Eso es lo que da la sensación de estudio y no de plantilla.

---

## Parte 2. Auditoría del sitio actual

Protocolo de `redesign-existing-projects`, sección 11.B.

### Lectura de diales del sitio actual

| Dial | Actual | Objetivo |
|---|---|---|
| DESIGN_VARIANCE | 2 | 8 |
| MOTION_INTENSITY | 3 | 6 |
| VISUAL_DENSITY | 5 | 4 |

El sitio declara movimiento pero entrega casi nada, y declara diseño de agencia pero resuelve en simetría de plantilla.

### Fallas concretas

**1. El hero es la solución por defecto.** Línea 73: `min-height:88vh; display:grid; place-items:center; text-align:center`. Wordmark centrado, tagline debajo, párrafo debajo, dos botones debajo. Es la composición que trae cualquier plantilla corporativa. La skill de diseño la prohíbe explícitamente por encima de VARIANCE 4. Además `88vh` en vez de `100dvh` produce salto de layout en Safari iOS cuando aparece o se esconde la barra del navegador.

**2. Los halos azules son la huella digital más reconocible de diseño generado por IA.** Líneas 74 y 75: dos círculos de 46 rem y 34 rem con `filter: blur(90px)` y opacidad 0.5 detrás del hero, más un tercero en contacto (línea 131). La skill lo nombra por su nombre: "Purple/blue AI gradient aesthetic, the most common AI design fingerprint". Y aparte cuesta caro: tres capas de blur de 90 px obligan al navegador a rasterizar superficies enormes.

**3. Seis tarjetas iguales.** Línea 92: `repeat(auto-fit, minmax(min(100%,20rem),1fr))` con `.svc` de fondo panel, borde 1 px, radio 20 px y hover que levanta 4 px. La grilla de tarjetas equivalentes es el layout genérico número uno, y aquí está aplicado a los seis servicios sin ninguna jerarquía. El problema no es solo visual: comercialmente estás diciendo que Desarrollo Web pesa lo mismo que Pauta Publicitaria, cuando no es cierto.

**4. Eyebrows en todas partes.** El pill `.eyebrow` con mono en mayúsculas y borde aparece en las líneas 191, 200, 264, 287, 301 y 323, o sea en las seis secciones. La regla mecánica de la skill: el número de eyebrows no puede pasar de `ceil(secciones / 3)`, que aquí serían 2. Vas 6. Y encima es un badge tipo píldora, otro patrón marcado.

**5. La escala tipográfica no tiene peldaños intermedios.** H1 en `clamp(3.4rem, 13vw, 9rem)`, H2 en `clamp(2rem, 5.5vw, 3.4rem)`, cuerpo en 1 rem. Entre el H2 y el cuerpo hay un salto de 3.4x sin nada en medio: no existe un nivel de subtítulo ni un nivel de destacado. El `.lede` solo se diferencia por color, no por tamaño ni por peso. Resultado: todas las secciones se leen al mismo volumen.

**6. Los pesos cargados no se usan.** Se descargan Clash Display 600 y 700 y Satoshi 400, 500 y 700, pero los titulares usan siempre 700 y el cuerpo siempre 400. Los pesos 500 y 600 se pagan en descarga y no aparecen en pantalla. Sin peldaños de peso no hay jerarquía sutil.

**7. No hay ritmo vertical, hay repetición.** Línea 47: todas las secciones comparten `padding-block: clamp(4.5rem,10vw,8.5rem)`. Idéntico espacio entre todo. Siete secciones al mismo intervalo se leen como un deck exportado a HTML, no como una página con respiración. Nada acelera, nada se detiene.

**8. La animación de entrada es una sola para todo.** Línea 151: `.rv` hace `translateY(22px)` más fade, y el retardo se calcula como `(i % 6) * 60ms` sobre el índice del elemento en el documento (línea 365). El escalonamiento no tiene relación con el layout: elementos que están en filas distintas reciben retardos consecutivos y elementos vecinos reciben retardos lejanos. Es movimiento decorativo, no coreografía.

**9. El corte AGENT + IA se resuelve con un cambio de color y nada más.** Línea 179: `AGENT<span class="ia">IA</span>`. Es la expresión mínima de la idea. Peor: el mismo truco se aplica a palabras que no son la marca, "La <span>IA</span> no es el producto" (línea 192) y "Experienc<span>ia</span>" (línea 302). Al usarlo tres veces con tres significados distintos, el concepto deja de ser marca y se vuelve un tic.

**10. El formulario no existe.** Líneas 332 a 347: no hay elemento `<form>`, los campos tienen `id` pero no tienen `name`, y el botón de envío es un `<a href="mailto:comercial@agentia.com.pe">`. No puede enviar nada. Además la nota de desarrollo queda visible en producción (línea 348).

**11. Tres familias tipográficas desde dos CDN externos, sin autoalojar.** Líneas 12 a 14: Fontshare para Clash Display y Satoshi, Google Fonts para JetBrains Mono. Dos conexiones DNS más dos handshakes TLS antes de que se pinte texto. No hay `preload`, no hay `og:image` declarada, no hay favicon.

**12. Accesibilidad y semántica.** Los nombres de clientes son `<div class="logo">` sin semántica. No hay enlace de salto al contenido. El anillo de foco existe solo en `.btn` (línea 66), los enlaces de navegación no tienen ninguno. El color `.note` `#4E566B` sobre `#04060B` da alrededor de 4.0:1, por debajo del mínimo AA para texto pequeño.

**13. La arquitectura de información y las etiquetas no coinciden.** El nav apunta a `#clientes`, pero esa sección (líneas 299 a 316) mezcla el eyebrow "Trayectoria", un titular de experiencia, un párrafo de cobertura geográfica y la grilla de logos. Tres cosas distintas bajo una etiqueta.

### Qué se conserva

- **El corte conceptual AGENT + IA.** La idea es buena, la ejecución no. Se conserva la idea y se le construye una expresión tipográfica real, y se deja de aplicar a palabras que no son la marca.
- **Los IDs de ancla y las etiquetas del nav.** `#servicios`, `#diferencial`, `#proceso`, `#clientes`, `#contacto` se mantienen tal cual. La skill lo pide y el SEO lo agradece.
- **El tratamiento del tagline.** `letter-spacing: .42em` en mono mayúsculas sobre "OPTIMIZAMOS TUS PROCESOS" (línea 79) es la mejor decisión tipográfica de la página. Se conserva el principio.
- **La disciplina con los placeholders.** Los recuadros punteados marcados como ficticios y la nota que recuerda reemplazarlos. Ese comportamiento se mantiene, incluida la regla de no publicar cifras sin contarlas.
- **El bloque `prefers-reduced-motion`** (líneas 153 a 157), que está bien implementado.
- **El JSON-LD de Organization y la meta description**, que se amplían pero no se rehacen.
- **Los huesos de la sección Proceso.** La estructura de riel numerado con columna de 4.5 rem (línea 113) es lo más cercano a una idea de layout que hay en la página.

---

## Parte 3. Tres direcciones

Cada una pasó el filtro: ¿llegaría a esto mismo para cualquier otra agencia? Si la respuesta era sí, se descartó.

---

### Dirección A. Punto de Fuga

**Tesis:** el punto del isotipo se despega de la A y recorre la página como cabezal de reproducción, de modo que navegar el sitio es literalmente reproducir una línea de tiempo.

**Por qué es de Agentia y no de cualquiera:** el punto dentro de la A ya es un play, un prompt y una punta de lápiz. Y Agentia hace producción audiovisual: la línea de tiempo es la herramienta con la que trabajan todos los días. Ninguna agencia sin ese isotipo y sin esa práctica llegaría a esto.

**Paleta**

| Token | Hex | Uso |
|---|---|---|
| `--tinta` | `#0B0B0F` | Fondo base, negro tintado en frío, nunca `#000` |
| `--grafito` | `#16161C` | Superficies elevadas y el riel del timeline |
| `--linea` | `#26262F` | Reglas de 1 px y marcas de sección |
| `--punto` | `#8B7BF5` | Acento único, tomado del isotipo |
| `--papel` | `#EDEDF2` | Texto principal |
| `--humo` | `#8A8A99` | Texto secundario |

**Tipografía**

- **Display: Archivo Expanded** (SIL OFL, Omnibus-Type). Variable en peso 100 a 900 y en ancho 62 a 125. Se elige por dos razones concretas: primero, permite montar el wordmark AGENTIA en ancho expandido y peso 200, que es el movimiento de Punch traducido a otra familia y no copiado; segundo, su A tiene el vértice alto y el ápice plano, que es exactamente la geometría del chevrón de tu isotipo, así que el logotipo y el titular pertenecen al mismo alfabeto.
- **Cuerpo: Archivo** (misma superfamilia, ancho normal). Una sola descarga variable cubre display y cuerpo. La jerarquía sale de peso y ancho, no de mezclar familias.
- **Datos: Geist Mono** (SIL OFL) solo para los timecodes del riel. Numerales tabulares reales.

**Layout**

Un riel vertical fijo pegado al borde izquierdo recorre toda la página. El contenido cuelga a su derecha, nunca centrado. Cada sección es una marca en el riel con su timecode. El punto viaja por el riel según el avance del scroll y al pasar por cada marca la enciende. Los servicios abandonan la grilla de tarjetas y se convierten en filas de ancho completo separadas por reglas de 1 px: al pasar el cursor, la fila se abre y muestra sus tres viñetas. Eso resuelve de paso el problema comercial, porque una lista tiene orden y una grilla no.

```
┌──────────────────────────────────────────────────────┐
│ ▲ AGENTIA                       servicios   contacto │
├───┬──────────────────────────────────────────────────┤
│   │                                                  │
│ ● │   A G E N T                                      │
│ │ │   I A                                            │
│ │ │        O P T I M I Z A M O S   T U S             │
│ │ │        P R O C E S O S                           │
│ │ │                                                  │
│ │ │   Convertimos tecnologias de vanguardia          │
│ │ │   en metricas de negocio.                        │
│ │ │                                                  │
│ │ │   conversemos tu proyecto  →                     │
│ ├─┼──────────────────────────────────────────────────┤
│ │ │ 00:01  La IA no es el producto. El resultado si. │
│ ├─┼──────────────────────────────────────────────────┤
│ │ │ 00:02  Desarrollo web con IA              +      │
│ │ │        ──────────────────────────────────────    │
│ │ │        Gestion de identidad y contenido   +      │
│ │ │        ──────────────────────────────────────    │
│ ▼ │        Produccion de video e IA           +      │
└───┴──────────────────────────────────────────────────┘
  riel fijo            contenido colgado a la derecha
```

En menos de 768 px el riel se convierte en una barra de progreso de 2 px pegada al borde superior y el contenido pasa a columna única.

**Elemento firma:** el punto viajero. Sale del isotipo en el hero, baja por el riel durante todo el scroll, y al llegar a contacto se detiene dentro del botón de envío del formulario, que es la única superficie violeta sólida de la página. El recorrido del punto es el recorrido comercial.

**Riesgo:** un elemento ligado al scroll que atraviesa la página entera se nota mucho cuando funciona y se nota más cuando se traba. Se construye con `IntersectionObserver` y animación por scroll de CSS, nunca con un listener de scroll, y colapsa a estático bajo `prefers-reduced-motion`. La apuesta vale porque es la única de las tres en que el movimiento no es decoración: es el argumento de venta ejecutado en pantalla.

---

### Dirección B. Espécimen

**Tesis:** el sitio no habla del sistema de marca, el sitio *es* el sistema de marca abierto y en funcionamiento, como la lámina de muestra de una fundidora tipográfica.

**Por qué es de Agentia y no de cualquiera:** tu paso 2 del proceso dice literalmente "definimos tokens visuales, tono y plantillas reutilizables", y tu servicio 2 promete "manual de marca vivo". Esta dirección convierte esa promesa en la interfaz. Una agencia que no venda sistemas no puede usar este sitio, porque no tendría qué mostrar.

**Paleta**

| Token | Hex | Uso |
|---|---|---|
| `--papel` | `#F0F0F3` | Fondo, blanco neutro frío |
| `--tinta` | `#121216` | Texto principal |
| `--lapiz` | `#6E6E7A` | Texto secundario y cotas |
| `--regla` | `#D8D8DE` | Líneas de grilla y marcas de medida |
| `--violeta` | `#6D4AFF` | Acento único, el violeta del isotipo oscurecido para cumplir AA sobre papel |
| `--nota` | `#E9E4FF` | Relleno suave de resaltados y estados activos |

**Tipografía**

- **Display: Bricolage Grotesque** (SIL OFL, Mathieu Triay). Variable en peso, ancho y tamaño óptico. Se elige porque es una grotesca con desajustes deliberados en las terminaciones, o sea que tiene la rareza justa para no leerse neutra, y porque sus tres ejes variables son el material mismo de la demostración: sin ejes variables esta dirección no tiene qué mostrar.
- **Cuerpo: Instrument Sans** (SIL OFL). Neutra pero no anónima, con una caja baja alta que sostiene textos largos en tamaño pequeño. Es la contraparte silenciosa que deja que el display haga el ruido.
- **Especificaciones: Martian Mono** (SIL OFL) para hex, medidas y cotas. Es una mono de ancho estrecho, se lee como dato técnico y no como código de película.

**Layout**

Grilla modular visible. No decorativa: las cotas y los rieles de medida son parte del contenido, como en una lámina de manual de marca. Márgenes muy amplios, columnas desiguales (`2fr 1fr 1fr`). Cada sección se presenta como una lámina con su cota de ancho y su ficha técnica al margen. La sección de servicios se organiza en dos columnas asimétricas donde el servicio activo ocupa el ancho grande y los demás quedan como índice a la izquierda.

```
┌──────────────────────────────────────────────────────┐
│  ├──────────────── 1440 ────────────────┤            │
│                                                      │
│   ▲ AGENTIA          peso ▁▂▃▄▅▆▇█                   │
│                      ancho ◄────●────►               │
│                      [ arrastra y mira que pasa ]    │
│                                                      │
│   OPTIMIZAMOS TUS PROCESOS                           │
│   ────────────────────────                           │
│   12 pt / 0.42 em / mayusculas                       │
│                                                      │
├─────────────────┬────────────────────────────────────┤
│  #6D4AFF        │  Convertimos tecnologias de        │
│  violeta        │  vanguardia en metricas de         │
│  acento unico   │  negocio.                          │
│  ▓▓▓▓▓▓▓▓       │  ├───────── 62 ch ─────────┤       │
├─────────────────┴────────────────────────────────────┤
│  indice           │  Desarrollo web con IA           │
│  · web            │                                  │
│  · identidad      │  Landing pages y sitios de alto  │
│  · video          │  impacto visual.                 │
│  · personajes     │  ├─ tracking desde el dia uno    │
└──────────────────────────────────────────────────────┘
```

**Elemento firma:** la tira de control del hero. Dos deslizadores, peso y ancho, que el visitante arrastra. El wordmark AGENTIA responde en tiempo real y **todos los titulares de la página responden con él**, porque están conectados a la misma variable CSS. En quince segundos el cliente entendió qué es un sistema de marca y por qué Agentia cobra por definirlo, sin leer una sola línea de argumentación.

**Riesgo:** es la dirección más fría de las tres, y una lámina técnica puede leerse como corporativa si el aire no está bien calibrado. Además el control interactivo tiene que estar impecable en táctil o se vuelve una promesa incumplida en el 60% de las visitas. La apuesta vale porque es la única que convierte el argumento comercial en algo que el visitante *hace* en lugar de leer, y porque en fondo claro te aleja del mar de sitios oscuros de agencias de IA.

---

### Dirección C. Título de Crédito

**Tesis:** una agencia cuyo diferencial declarado es "dirección de arte humana sobre producción asistida" debería verse dirigida por una persona, no ensamblada por una máquina, y eso se argumenta con tipografía de alto contraste sobre papel, que es justo lo que ninguna herramienta de IA propone por defecto.

**Por qué es de Agentia y no de cualquiera:** sale de una frase que está en tu propio contenido, en el servicio de video, y del hecho de que producen cortometrajes. La didona sobre fondo claro es el lenguaje de la placa de título de cine y de la portada de moda. Es la dirección que más lejos queda del deck azul actual y de las dos referencias que me diste.

**Paleta**

| Token | Hex | Uso |
|---|---|---|
| `--lino` | `#EDE9E2` | Fondo papel, cálido |
| `--tinta` | `#15121B` | Texto y bloques oscuros de contraste |
| `--violeta` | `#5B3CE0` | Acento único, el violeta del isotipo saturado para papel cálido |
| `--sombra` | `#6B6459` | Texto secundario sobre lino |
| `--arena` | `#C9C1B4` | Reglas de 1 px y bordes de fotograma, nunca texto |

Nota deliberada: la skill prohíbe la paleta beige más latón más espresso como recurso automático de "producto premium". Aquí el cálido no viene de ahí sino del papel de guion, y el violeta saturado lo saca por completo de la familia artesanal.

**Tipografía**

- **Display: Bodoni Moda** (SIL OFL, Indestructible Type). Didona variable con eje de tamaño óptico de 6 a 96 pt. Se elige por una razón que solo aplica a este cliente: las placas de título de cine usan didonas desde hace un siglo, y Agentia vende cortometrajes. Además su eje óptico permite que el titular de 120 px tenga astas finísimas y el mismo tipo a 20 px se mantenga legible, que es la diferencia entre usar bien una didona y arruinarla.
- **Cuerpo: Familjen Grotesk** (SIL OFL, Stefan Ellmer). Grotesca sueca con detalles ligeramente extraños en la a y la g. Se elige porque una didona necesita una compañera con carácter propio o el conjunto se cae en el cliché de moda de los años noventa. Familjen aporta lo suficiente para sostener el contraste sin pelear.

**Layout**

Editorial cinematográfico. El hero es una placa de título: enorme, alineada de forma escalonada, con muchísimo aire alrededor y créditos abajo en letra pequeña. Los servicios se presentan como una hoja de contactos, o sea la lámina de fotogramas que el fotógrafo marca para elegir cuál imprimir: seis fotogramas en grilla irregular, cada uno con su borde de perforación y su número de toma. Al pasar el cursor, el fotograma se expande y se lleva el espacio de sus vecinos.

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│                                                      │
│      Optimizamos                                     │
│            tus procesos                              │
│                              ▲                       │
│                              ●                       │
│                                                      │
│   ────────────────────────────────────────────────   │
│   AGENTIA   Huaraz · Ica · Lima      agentia.com.pe  │
├──────────────────────────────────────────────────────┤
│ ┌─────────┐ ┌─────────┐ ┌─────────┐                  │
│ │  ·   ·  │ │  ·   ·  │ │  ·   ·  │   La IA no es    │
│ │  web    │ │identidad│ │  video  │   el producto.   │
│ │  ·   ·  │ │  ·   ·  │ │  ·   ·  │   El resultado   │
│ └─────────┘ └─────────┘ └─────────┘   si.            │
│  toma 01     toma 02     toma 03                     │
└──────────────────────────────────────────────────────┘
```

**Elemento firma:** la apertura de iris. Cada sección entra a través de una máscara circular que se abre desde el punto del isotipo, igual que el iris de una cámara antigua o el cierre de una escena. El punto no viaja como en la dirección A: aquí es el obturador por el que entra cada plano. Se construye con `clip-path: circle()` animado, que es barato y no toca el layout.

**Riesgo:** es la apuesta más alta y también la más fácil de arruinar. Una didona mal espaciada se lee amateur de inmediato, y "agencia de IA con tipografía de moda" puede leerse como incoherente si el resto no acompaña. También es la que más depende de tener material audiovisual real, y tu propio documento dice que la sección de casos no se publica sin material. Vale la pena porque es la única de las tres que un competidor peruano no va a poder imitar el mes siguiente, y porque contradice de frente la expectativa de cómo se ve una agencia de IA, que es exactamente el efecto que buscas cuando el sitio es la pieza de portafolio.

---

## Comparación rápida

| | A. Punto de Fuga | B. Espécimen | C. Título de Crédito |
|---|---|---|---|
| Fondo | Oscuro tintado | Papel frío | Papel cálido |
| Argumento | El proceso en movimiento | El sistema en funcionamiento | La dirección de arte humana |
| Riesgo técnico | Alto (scroll) | Medio (táctil) | Bajo |
| Riesgo de gusto | Bajo | Medio | Alto |
| Distancia del deck actual | Media | Alta | Máxima |
| Se puede imitar en | 6 meses | 3 meses | No fácilmente |
