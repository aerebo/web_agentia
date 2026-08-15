# Sistema de diseño AGENTIA

**Dirección aprobada:** B, Espécimen.
**Fecha de aprobación:** 14 de agosto de 2026.
**Regla de oro:** ningún color, tamaño, espaciado ni duración se escribe suelto en el código. Todo sale de los tokens de este documento. Si algo falta aquí, se agrega aquí primero y después se usa.

---

## 1. Tesis

El sitio no habla del sistema de marca: el sitio **es** el sistema de marca abierto y funcionando, como la lámina de muestra de una fundidora tipográfica.

La demostración es **la tuerca**: un mando que el visitante gira y que hace pasar al isotipo por sus cuatro estados. Cada estado corresponde a una línea de negocio real. En diez segundos el cliente entiende qué es un sistema de identidad y por qué Agentia cobra por definirlo, sin leer un párrafo de argumentación.

Esa es la prueba del argumento comercial que ya está en el contenido aprobado: "definimos tokens visuales, tono y plantillas reutilizables" y "consistencia visual garantizada en cualquier formato". La página no lo promete, lo ejecuta.

---

## 2. Marca

El archivo maestro es `assets/img/agentia-logo-original.svg`, exportado de Illustrator. De ahí salen `agentia-isotipo.svg` y `agentia-wordmark.svg` por corte exacto, con un script, nunca transcribiendo trazados a mano.

### 2.1 Geometría medida

| Dato | Valor en unidades del SVG original |
|---|---|
| Caja del chevron | x 438.45 a 661.94, y 315.04 a 525.59 |
| Centro del punto | 550.19, 480.64 |
| Radio del punto | 20.86 |
| Distancia del punto al vértice | 165.6 |
| Distancia del punto a las patas | 44.95 |
| Violeta del punto | `#8665F7` |

El punto está exactamente en el centro horizontal del chevron: 438.45 + 223.49 / 2 = 550.20. No es casualidad, es el eje.

### 2.2 Los cuatro estados

El isotipo es **un brazo y un punto**. Los cuatro estados son la misma pieza girando alrededor del punto. No hay redibujo, no hay traslación, no hay una segunda versión del logotipo: hay un giro.

| Grados | Forma | Estado | Significado | Servicio |
|---|---|---|---|---|
| 0 | `Λ` | `marca` | Identidad | Gestión de identidad y contenido |
| 90 | `>` | `play` | Grabación y generación | Producción de video e IA audiovisual |
| 180 | `V` | `lapiz` | Punta de lápiz hacia abajo | Diseño gráfico integral |
| 270 | `<` más su gemelo a 90: `<•>` | `code` | Código | Desarrollo web con IA |

**Por qué encaja solo.** Al girar 90 grados en sentido horario alrededor del punto, el vértice que estaba arriba queda a la derecha y el punto, que estaba dentro de la boca de la `A`, queda dentro de la boca del `>`. Es exactamente el logotipo PLAY del manual, sin haberlo dibujado aparte. Y girando en sentido contrario sale el `<`, así que `<•>` son dos copias de la misma pieza giradas en direcciones opuestas compartiendo el mismo punto. Es el logotipo CODE del manual.

**La única excepción a la rotación pura es el estado `code`.** Cada brazo se mete 44.95 unidades más allá del eje, así que dos brazos opuestos se solapan 90 unidades y forman un rombo en vez de un `<•>`. Por eso, y solo en ese estado, los brazos se separan 60 unidades y se encogen a 0.62. El escalado ocurre alrededor del punto, de modo que se alejan encogiéndose hacia el eje, que es un movimiento coherente con el resto. Medido: los brazos dejan de cruzarse, el punto queda con aire simétrico a cada lado y todo sigue dentro de la caja de 336.

**El punto nunca se mueve.** Verificado en navegador: en los cuatro estados el punto ocupa el mismo píxel. Es el eje mecánico y el eje conceptual a la vez.

### 2.3 Implementación

- El giro se declara en la variable `--giro`, registrada con `@property` como `<angle>`. Sin registrar, el navegador no puede interpolarla.
- **Se anima la variable, no la propiedad.** `transition: --giro` sobre `.marca`, y `transform: rotate(var(--giro))` sobre el brazo, sin transición propia.
- El eje de giro se escribe en coordenadas absolutas del SVG: `transform-origin: 550.19px 480.64px`. No se usan coordenadas relativas a la esquina del `viewBox` porque los navegadores no coinciden en cómo las resuelven junto con `transform-box: view-box`.
- El `viewBox` es **cuadrado**, de 336 unidades, centrado en el punto: `382.19 312.64 336 336`. Tiene que serlo porque la unión de las cuatro rotaciones es un círculo de radio 165.6. Con una caja más baja los brazos girados se salen, y además una caja fija evita que la marca cambie de tamaño al girar, que provocaría desplazamiento de layout.
- **Curva:** `--ease-fisica`, con rebote corto, para que la tuerca se sienta mecánica. El gemelo del estado `code` aparece 60 ms después de que el brazo empieza a girar, nunca a la vez.

### 2.4 Reglas de uso

- **Una sola marca animada por pantalla.** En el hero manda la tuerca. En el resto de la página manda la sección visible, que cambia el estado del isotipo del nav. Nunca las dos a la vez en pantalla.
- **El wordmark va siempre como SVG del archivo original, nunca compuesto con una tipografía.** Su A sin travesaño y su tracking son propios del logotipo. Reconstruirlo con una fuente sería falsificarlo.
- **El wordmark no gira.** Solo el isotipo tiene estados.
- **En el bloqueo horizontal**, el chevron mide 1.6 veces la altura del wordmark, y ambos se alinean por su centro óptico. Como la caja cuadrada está centrada en el punto y no en el chevron, hay que bajar el SVG un 17.95% de su altura para que el centro óptico coincida.
- **El corte AGENT + IA no se aplica a otras palabras.** Se acabó el `Experienc<span>ia</span>`. El recurso pertenece a la marca y pierde su valor si se usa de adorno.
- **El punto es el único elemento circular del sitio**, junto con la tuerca, que es su mecanismo. Ver la sección 6.

---

## 3. Color

### 3.1 Tokens

| Token | Hex | Uso |
|---|---|---|
| `--papel` | `#F0F0F3` | Fondo de página, blanco neutro frío |
| `--lamina` | `#FAFAFC` | Superficie de lámina, un escalón por encima del papel |
| `--tinta` | `#121216` | Texto principal y bloques de contraste |
| `--lapiz` | `#63636F` | Texto secundario, cotas, metadatos |
| `--regla` | `#D8D8DE` | Líneas de grilla, cotas y separadores decorativos |
| `--borde` | `#83838F` | Bordes de elementos interactivos, campos y controles |
| `--violeta` | `#8665F7` | **El violeta del logotipo original.** El punto, rellenos y texto grande |
| `--violeta-fuerte` | `#6E48E8` | El mismo violeta profundizado hasta cumplir AA |
| `--nota` | `#EAE4FE` | Relleno suave de resaltados y estados activos |

### 3.2 Contraste verificado en navegador

Medido sobre la página real, no estimado.

| Par | Ratio | Cumple |
|---|---|---|
| `--tinta` sobre `--papel` | 16.43:1 | AAA |
| `--lapiz` sobre `--papel` | 5.21:1 | AA texto normal |
| `--lapiz` sobre `--lamina` | 5.68:1 | AA texto normal |
| `--violeta` sobre `--papel` | 3.54:1 | **Solo texto grande y componentes** |
| `--violeta-fuerte` sobre `--papel` | 4.92:1 | AA texto normal |
| `--lamina` sobre `--violeta-fuerte` | 5.36:1 | AA texto normal, botón lleno |
| `--borde` sobre `--papel` | 3.29:1 | AA componentes no textuales |
| `--regla` sobre `--papel` | 1.25:1 | Solo decorativo, nunca borde de control |

**Regla que se deriva de esto:** el violeta de marca `#8665F7` da 3.54:1 sobre papel. Cumple para texto grande y para componentes, pero **no** para texto pequeño ni como fondo de un botón con texto encima, donde daba 3.86:1. Para eso está `--violeta-fuerte`. No son dos acentos: es el mismo acento en dos profundidades, y la de marca manda en todo lo que sea identidad, empezando por el punto.

`--regla` nunca delimita un campo de formulario ni un control. Para eso está `--borde`.

### 3.3 Reglas de color

- **Un solo acento en toda la página.** El violeta no compite con nada. No hay un verde de éxito ni un rojo de error con otro tono: los estados se resuelven con `--tinta`, `--violeta` y peso tipográfico.
- **Los grises son todos fríos.** Ninguno se tinta en cálido. Una sola familia de gris en todo el proyecto.
- **Nada de degradados de acento.** Ni glows, ni halos, ni blur de fondo. Esa es exactamente la huella que estamos borrando del sitio anterior.
- **La textura permitida es el grano**, no el degradado: una capa fija de ruido a opacidad muy baja sobre el papel, sin eventos de puntero.

---

## 4. Tipografía

### 4.1 Familias

Las tres son SIL Open Font License 1.1, verificadas, autoalojadas en `assets/fonts/`, con `font-display: swap`.

| Rol | Familia | Ejes | Archivo | Peso |
|---|---|---|---|---|
| Display | Bricolage Grotesque | `wght` 200 a 800, `wdth` 75 a 100, `opsz` 12 a 96 | `bricolage-grotesque-var-latin.woff2` | 128.5 KB |
| Cuerpo | Instrument Sans | `wght` 400 a 700, `wdth` 75 a 100 | `instrument-sans-var-latin.woff2` | 56 KB |
| Especificación | Martian Mono | `wght` 100 a 800, `wdth` 75 a 112.5 | `martian-mono-var-latin.woff2` | 37.6 KB |

Total: 222 KB. Subconjunto latino, que cubre el español completo incluidos acentos, eñe y signos de apertura.

Las tres licencias están en `assets/fonts/OFL-*.txt` y deben viajar con los archivos.

**Por qué estas y no otras.** Bricolage es una grotesca con desajustes deliberados en las terminaciones, o sea que no se lee neutra, y sus tres ejes variables son el material mismo de la demostración: sin ejes no hay nada que enseñar. Instrument Sans es la contraparte silenciosa, con caja baja alta que sostiene texto pequeño. Martian Mono es estrecha y se lee como dato técnico, no como código de película. Unbounded queda descartada por estar ocupada por slinky.pe en el mismo mercado.

### 4.2 Escala

| Token | Valor | Uso |
|---|---|---|
| `--t-display` | `clamp(3rem, 9vw, 7.5rem)` | Titular del hero |
| `--t-h1` | `clamp(2.5rem, 6vw, 4.5rem)` | Titular de sección mayor |
| `--t-h2` | `clamp(1.875rem, 4vw, 3rem)` | Titular de sección |
| `--t-h3` | `clamp(1.25rem, 2vw, 1.5rem)` | Nombre de servicio, subtítulo |
| `--t-lede` | `clamp(1.125rem, 1.6vw, 1.375rem)` | Entrada de sección |
| `--t-cuerpo` | `clamp(1rem, 1.1vw, 1.0625rem)` | Texto corrido |
| `--t-corto` | `0.875rem` | Viñetas, pies, metadatos |
| `--t-spec` | `0.6875rem` | Mono: cotas, hex, medidas |

El nivel `--t-lede` es el peldaño que faltaba en el sitio anterior, donde el salto del H2 al cuerpo era de 3.4x sin nada en medio.

### 4.3 Peso y ancho

| Token | Valor | Uso |
|---|---|---|
| `--w-fino` | `200` | Display de gran tamaño |
| `--w-libro` | `400` | Texto corrido |
| `--w-medio` | `500` | Titulares de sección, énfasis |
| `--w-fuerte` | `600` | Etiquetas activas, botón |
| `--wd-estrecho` | `75` | Cotas y mono |
| `--wd-normal` | `100` | Todo lo demás |

Los seis niveles se usan de verdad. El sitio anterior descargaba pesos 500 y 600 y no los pintaba nunca.

### 4.4 Peso de titulares

`--w-titular: 340`. Un solo valor para todos los titulares, aplicado con `font-weight`, no con `font-variation-settings`.

**Nota de historia del proyecto.** La primera versión de esta dirección exponía los ejes variables de Bricolage al visitante con dos deslizadores. Se descartó: era una demostración de fundidora tipográfica, no de Agentia. La demostración correcta es la tuerca de la sección 2, porque lo que Agentia vende no es tipografía variable, es una identidad que se adapta al contexto sin dejar de ser la misma.

Los ejes variables se siguen usando internamente, para la escalera de pesos y para el ancho estrecho de las etiquetas mono. Lo que se quitó fue el control expuesto.

### 4.5 Detalles

- Medida de línea máxima 62 caracteres en texto corrido.
- Interlineado: 1.05 en display, 1.15 en titulares, 1.6 en cuerpo.
- Tracking: negativo en display (`-0.03em`), cero en cuerpo, `0.42em` en las etiquetas mono en mayúsculas. Ese `0.42em` viene del sitio anterior y es lo mejor que tenía.
- `text-wrap: balance` en titulares, `pretty` en párrafos, para que ninguna línea quede con una palabra huérfana.
- Numerales tabulares obligatorios en cualquier cifra.

---

## 5. Espacio y grilla

| Token | Valor |
|---|---|
| `--e-1` | `0.5rem` |
| `--e-2` | `1rem` |
| `--e-3` | `1.5rem` |
| `--e-4` | `2.5rem` |
| `--e-5` | `4rem` |
| `--e-6` | `6rem` |
| `--e-7` | `9rem` |

| Token | Valor | Uso |
|---|---|---|
| `--ancho-max` | `1440px` | Ancho máximo del lienzo |
| `--margen` | `clamp(1.25rem, 5vw, 6rem)` | Margen lateral |
| `--columnas` | `12` | Grilla base |

### Ritmo vertical

El error del sitio anterior era que todas las secciones tenían el mismo espaciado. Aquí hay tres, y se alternan a propósito:

| Token | Valor | Cuándo |
|---|---|---|
| `--sec-amplia` | `var(--e-7)` | Después del hero y antes de contacto: los respiros largos |
| `--sec-normal` | `var(--e-6)` | Secciones de contenido |
| `--sec-corta` | `var(--e-5)` | Cuando dos secciones son continuación una de otra |

Secuencia definida para la página: hero, amplia, normal, corta, normal, amplia, normal.

---

## 6. Forma

**Bloqueo de forma:** todo el sitio es de esquina viva, radio 0. Sin excepciones en tarjetas, campos, botones ni imágenes.

**Las únicas formas circulares del sitio son el punto del isotipo y la tuerca.** Esa es justamente la razón de la regla: si nada más es redondo, el punto no compite con nada y se lee como el elemento de marca que es. La tuerca es la única excepción documentada, y se permite porque no es otra forma: es el punto agrandado hasta volverse mecanismo. Comparten el mismo eje.

| Token | Valor |
|---|---|
| `--r-0` | `0` |
| `--linea-fina` | `1px` |
| `--linea-gruesa` | `2px` |

Sin sombras. La elevación se comunica con `--lamina` sobre `--papel` y con líneas, nunca con `box-shadow`. Una lámina de espécimen no tiene sombra.

---

## 7. Movimiento

`MOTION_INTENSITY: 6`. La página se mueve de verdad, y todo se construye en CSS. Sin librerías.

| Token | Valor | Uso |
|---|---|---|
| `--dur-rapida` | `180ms` | Estados de hover y foco |
| `--dur-media` | `420ms` | Entradas de elemento, cambio de estado del isotipo |
| `--dur-larga` | `720ms` | Entradas de sección |
| `--ease-salida` | `cubic-bezier(0.16, 1, 0.3, 1)` | Todo lo que entra |
| `--ease-fisica` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Solo las físicas del isotipo, con rebote |
| `--retardo-punto` | `60ms` | El punto siempre llega después que los brazos |

**Reglas duras:**

- Solo se animan `transform` y `opacity`. Nunca `top`, `left`, `width` ni `height`.
- Prohibido `window.addEventListener('scroll')`. Se usa `IntersectionObserver` o animaciones de scroll de CSS.
- El escalonamiento de entrada se calcula por posición real en la fila, no por índice en el documento. Ese fue el error del sitio anterior.
- Todo lo anterior colapsa a estático bajo `prefers-reduced-motion: reduce`. Las físicas del isotipo pasan a cambio instantáneo de estado, sin rotación.

---

## 8. Capas

| Token | Valor | Capa |
|---|---|---|
| `--z-base` | `0` | Contenido |
| `--z-grano` | `1` | Textura de ruido |
| `--z-lamina` | `10` | Láminas y elementos pegajosos internos |
| `--z-nav` | `100` | Navegación |
| `--z-overlay` | `200` | Menú móvil |

Nada de `z-index: 9999`.

---

## 9. Accesibilidad

- Contraste AA verificado en navegador, tabla en 3.2.
- Anillo de foco visible en **todos** los elementos interactivos, no solo en botones: `outline: 2px solid var(--violeta); outline-offset: 3px`.
- Enlace de salto al contenido como primer elemento del documento.
- **La tuerca es un `<input type="range">` real**, invisible por encima del mando. Funciona con flechas del teclado, tiene `aria-label` y actualiza `aria-valuetext` al nombre del modo en español, no al número. El dibujo del mando lleva `aria-hidden`.
- La tuerca es un adorno funcional: si el visitante no la toca, la página se lee igual. Nunca es requisito para acceder a información.
- `aria-current="true"` en el enlace de navegación de la sección visible.
- Los estados del isotipo son decorativos: el SVG lleva `aria-hidden="true"` y el nombre accesible lo da el texto. El wordmark sí lleva `role="img"` y `aria-label="Agentia"`.
- **El contenido es visible por defecto.** Solo se esconde para revelarlo cuando el script confirma que puede, con red de seguridad a los 2.5 segundos. Un fallo de JavaScript nunca deja la página en blanco.

---

## 10. Lo que no se toca

- **El contenido sale de `docs/contenido-agentia.md` y no se reescribe.**
- **Los IDs de ancla se conservan:** `#servicios`, `#diferencial`, `#proceso`, `#clientes`, `#contacto`.
- **Nada de contenido de negocio inventado.** Ni clientes, ni cifras, ni testimonios, ni años de experiencia. Los marcadores provisionales se quedan marcados como provisionales.
- **Sin dependencias de terceros en tiempo de ejecución.** Ni GSAP, ni Lenis, ni iconos por CDN. Todo es CSS y JavaScript propio.

---

## 11. Presupuesto

| Métrica | Objetivo |
|---|---|
| LCP en 4G simulado | menos de 2.5 s |
| CLS | menos de 0.1 |
| Peso de la primera vista | menos de 800 KB |

Consumido hasta ahora: 222 KB de tipografías. Queda margen suficiente, siempre que las imágenes vayan en formato moderno y con `width` y `height` declarados para no generar desplazamiento.
