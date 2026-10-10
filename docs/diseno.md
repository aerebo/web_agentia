# Sistema de diseño AGENTIA

**Dirección aprobada:** B, Espécimen.
**Fecha de aprobación:** 14 de agosto de 2026.
**Regla de oro:** ningún color, tamaño, espaciado ni duración se escribe suelto en el código. Todo sale de los tokens de este documento. Si algo falta aquí, se agrega aquí primero y después se usa.

---

## 1. Tesis

El sitio no habla del sistema de marca: el sitio **es** el sistema de marca abierto y funcionando, como la lámina de muestra de una fundidora tipográfica.

La demostración es **la tuerca**: un mando que el visitante gira y que hace pasar a la insignia por sus cuatro caras. Cada estado corresponde a una línea de negocio real. En diez segundos el cliente entiende qué es un sistema de identidad y por qué Agentia cobra por definirlo, sin leer un párrafo de argumentación.

Esa es la prueba del argumento comercial que ya está en el contenido aprobado: "definimos tokens visuales, tono y plantillas reutilizables" y "consistencia visual garantizada en cualquier formato". La página no lo promete, lo ejecuta.

---

### 1.1 Orden de la página

Reordenada el 10 de octubre de 2026 y **condensada el mismo día**, de doce secciones a ocho, después del benchmark de `docs/benchmark.md`.

**El orden no es estético: es el orden en que un cliente potencial hace las preguntas.** Cada sección contesta una y solo una.

| # | Sección | La pregunta que contesta |
|---|---|---|
| 1 | Hero | ¿Qué hacen? |
| 2 | Servicios | ¿Qué puedo contratar? |
| 3 | Trabajos | ¿Puedo ver algo? |
| 4 | Cómo trabajamos | ¿Cómo se trabaja y qué me van a pedir? |
| 5 | Por qué Agentia | ¿Por qué ustedes, y es para mí? |
| 6 | Quiénes somos | ¿Quién está detrás y a quién le han hecho esto? |
| 7 | Preguntas frecuentes | ¿Qué duda me queda? |
| 8 | Contacto | ¿Cómo empiezo? |

**Las dos fusiones.** Había tres secciones contestando «por qué nosotros»: posicionamiento, el diferencial y para quién es. Ningún sitio del benchmark tiene más de una. Ahora son la 5, que cierra con el «esto no es para ti si», que es el mejor final posible para ese argumento.

Y clientes se juntó con trayectoria, cifras y equipo en la 6. Esa sección ya decía «operamos entre Huaraz, Ica y Lima» y hablaba del equipo propio: **estaba hablando de nosotros, no de ellos.** Estaba mal etiquetada.

**Los id de ancla no cambian aunque cambie el rótulo.** `#diferencial` sigue siendo `#diferencial` y `#clientes` sigue siendo `#clientes`. Ver la sección 10.

**Trabajos va en la 3, no en la 2.** Lo estándar es poner la prueba arriba del todo: barrel pone los logos justo debajo del hero y thoughtbot abre con un caso. Aquí no, por una razón concreta: el material disponible son entre tres y siete piezas, y **una galería corta en lo primero que se ve expone la escasez.** Detrás de Servicios se lee como respaldo de lo que se acaba de prometer, no como catálogo. Si algún día hay ocho piezas o más, sube.

**Trabajos no es lo mismo que Casos.** Trabajos es la galería: pieza, cliente, servicio. Casos es reto, qué hicimos y resultado medible. No son dos secciones: es la misma con más profundidad, y cada pieza puede crecer a caso cuando haya números. Ver la sección 8 de `contenido-agentia.md`.

**Reglas del orden:**

- **La prueba social no se adelanta con nombres sueltos.** No hay permiso de uso de logo todavía, y una fila de nombres en texto plano no es prueba, es relleno. Cuando lleguen los permisos, se reevalúa.
- **Decir para quién NO es cierra el argumento**, no lo abre. Por eso va al final de la 5 y no en sección propia.
- **Las preguntas frecuentes van pegadas al contacto.** Son las últimas objeciones antes del formulario.
- **El oscuro sigue apareciendo una sola vez y al final.** Ver la sección 3.4.

---

## 2. Marca

**La marca cambió el 9 de octubre de 2026.** Antes era el chevron violeta heredado del archivo de Illustrator, girando sobre su punto. Ahora es un logotipo tipográfico: **AGENT** en tinta más **IA** en blanco dentro de un cuadro azul. El cambio lo pidió el cliente sobre una propuesta entregada como imagen.

Lo que sigue describe la marca nueva. La anterior está en el historial de git, hasta el commit `3afe24e`, por si hiciera falta compararlas.

### 2.1 El juego de palabras es el logotipo

AGENTIA se parte en **AGENT** + **IA**. No es un adorno tipográfico: es el argumento entero de la empresa metido en el nombre, y el cuadro azul existe para que no pase desapercibido.

De ahí sale la regla más dura de esta sección: **el corte no se aplica a ninguna otra palabra.** Nada de `Experienc<span>ia</span>`. El recurso pertenece al logotipo y se gasta si se usa de adorno.

### 2.2 Proporciones medidas

Medidas sobre la imagen entregada, con los extremos tomados por umbral de columna para que un píxel suelto de compresión no corrompa el borde. Todo se expresa en **múltiplos de la altura de mayúscula de AGENT**, que es la unidad de la marca:

| Dato | Valor |
|---|---|
| Alto del cuadro | 1.853 |
| Ancho del cuadro | 1.765 |
| Hueco entre AGENT y el cuadro | 0.441 |
| El cuadro sube sobre la mayúscula | 0.382 |
| El cuadro baja bajo la línea base | 0.471 |
| Radio de esquina | 0.19 |
| Azul del cuadro | `#1540F5` |

**El cuadro sale casi cuadrado**, 1.765 de ancho por 1.853 de alto, y **no está centrado en la mayúscula**: cuelga más por debajo de la línea base (0.471) que lo que sube por encima (0.382). Si se centra, el logotipo se desequilibra hacia arriba. Es asimétrico a propósito.

El azul se midió del original: los píxeles limpios caen en `#1540FF` y la media del bloque, con los artefactos de compresión incluidos, en `#1D48F4`. Se adoptó `#1540F5`.

### 2.3 Implementación

**El logotipo se compone con tipografía viva, no con trazados.** Esto invierte la regla que tenía el logotipo anterior, y el motivo es que la marca cambió de naturaleza: el chevron era un dibujo y había que respetarlo como dibujo; AGENT es texto y el original también es texto.

- Familia: **Instrument Sans**, peso 700, la misma que ya va autoalojada para el cuerpo.
- **Ancho 92%.** Instrument Sans dibuja AGENT un 9% más ancho que el original. Se corrige con su eje de ancho variable, **no apretando el `letter-spacing`**: apretar junta las letras sin adelgazarlas y el bloque se ensucia.
- `letter-spacing: -0.03em`, que es el del original, y es aparte del ancho.
- Todo se expresa en múltiplos de `--cap`, que vale `0.72em`: la altura de mayúscula medida de Instrument Sans. Cambiar el cuerpo del logotipo reescala el cuadro solo.

**Ventaja:** un solo logotipo sirve a 17 px en la barra y a 52 px en el hero, sin exportar una versión por tamaño y sin pixelarse.

**Precio, y hay que saberlo:** depende de que la fuente cargue. Si algún día hace falta blindarlo, se piden los trazados a quien firmó la propuesta y se cambia la regla por un SVG. Mientras tanto, la fuente va autoalojada y precargada, que es el caso en el que esto falla menos.

### 2.4 La insignia, y por qué ya no gira

El cuadro azul, en grande y solo, hace de símbolo de la marca. Es lo que mueve la tuerca del banco.

**El isotipo anterior tenía cuatro estados que eran cuatro rotaciones de 90 grados.** Eso con un cuadrado no funciona: **un cuadrado girado 90 grados es el mismo cuadrado.** La rotación dejaría de leerse y el mando parecería roto.

Así que lo que cambia es el contenido del cuadro, no su ángulo:

| Paso | Glifo dentro del cuadro | Estado | Servicio |
|---|---|---|---|
| 0 | `IA` | `marca` | Gestión de identidad y contenido |
| 1 | Triángulo de reproducción | `play` | Producción de video e IA audiovisual |
| 2 | Lápiz | `lapiz` | Diseño gráfico integral |
| 3 | `< >` | `code` | Desarrollo web con IA |

Los glifos se apilan en la misma celda de grilla y se turnan con opacidad y una escala de 0.82 a 1. El cambio es un relevo, no un giro.

**La aguja de la tuerca sí sigue girando**, porque una aguja es justamente la forma a la que la rotación sí le sienta. El mando se arrastra igual que antes, la insignia cambia de cara al cruzar cada detención, y el control real sigue siendo un `input range` para teclado y lectores de pantalla.

**Esto además dice algo más claro que antes.** La silueta rotada había que aprendérsela; `< >` se entiende sin manual.

### 2.5 Dónde sí se lee una rotación

En el campo del hero. Ahí las piezas son el mismo cuadro, giran a **ángulos libres** hacia el puntero, y un cuadro inclinado 30 grados se distingue perfectamente de uno recto. Lo que no se leería son los múltiplos de 90, que es justo lo que hacía la tuerca. La regla no es "los cuadrados no giran": es **los cuadrados no giran en múltiplos de 90**.

### 2.6 Reglas de uso

- **El logotipo no se transforma nunca.** No gira, no cambia de estado al hacer scroll, no se anima. El isotipo anterior sí cambiaba de estado en la barra según la sección visible; eso se quitó. Lo que cambia es la insignia del banco, y la mueve el usuario.
- **Sobre la banda oscura se invierte**, no se recolorea a capricho: AGENT pasa a `--lamina`, el cuadro a `--azul-claro` y las letras de dentro a `--azul-tinta`. El azul de marca contra el azul tinta da 2.72:1 y el cuadro se disolvería en el fondo.
- **El cuadro no se separa del logotipo para usarlo de icono suelto**, salvo en la insignia del banco y en las piezas del hero, que son los dos usos documentados.
- **AGENT y el cuadro no se separan en dos líneas.** El logotipo lleva `white-space: nowrap`.
- **El archivo maestro antiguo** `assets/img/agentia-logo-original.svg` se conserva en el repositorio. Ya no se usa en la página, pero es la única copia del logotipo anterior fuera del historial.

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
| `--azul-humo` | `#EFF2FE` | Fondo de sección, lavado casi imperceptible |
| `--azul-nota` | `#DCE3FD` | Relleno de resaltado y estado activo |
| `--azul-claro` | `#8FA6FF` | Acento sobre fondo oscuro |
| `--azul` | `#1540F5` | **El azul del cuadro IA.** Rellenos, acentos y texto |
| `--azul-fuerte` | `#1434C8` | El mismo azul profundizado, para énfasis y foco |
| `--azul-tinta` | `#0D1030` | Azul llevado a negro. Banda de cierre |
| `--humo-claro` | `#959CBE` | Texto secundario sobre la banda oscura |

Una sola familia de azul en seis profundidades. No son seis acentos: es el mismo color con distinto peso.

### 3.2 Contraste

Calculado con la fórmula de luminancia relativa de WCAG sobre los tokens, que es exactamente lo que mide un comprobador de contraste.

| Par | Ratio | Cumple |
|---|---|---|
| `--tinta` sobre `--papel` | 16.43:1 | AAA |
| `--lapiz` sobre `--papel` | 5.21:1 | AA texto normal |
| `--azul` sobre `--papel` | 5.99:1 | AA texto normal |
| `--azul` sobre `--lamina` | 6.53:1 | AA texto normal |
| `--azul-fuerte` sobre `--papel` | 7.84:1 | AAA texto grande, AA normal |
| `--lamina` sobre `--azul` | 6.81:1 | AA texto normal. **Es el par del cuadro IA** |
| `--lamina` sobre `--azul-fuerte` | 8.92:1 | AAA texto normal |
| `--tinta` sobre `--azul-nota` | 14.64:1 | AAA |
| `--azul-fuerte` sobre `--azul-nota` | 6.98:1 | AA texto normal |
| `--borde` sobre `--papel` | 3.29:1 | AA componentes no textuales |
| `--regla` sobre `--papel` | 1.25:1 | Solo decorativo, nunca borde de control |

**El azul levantó la restricción que tenía el violeta.** `#8665F7` daba 3.54:1 sobre papel y estaba prohibido en texto pequeño; `#1540F5` da 5.99:1 y sirve para todo. Por eso `--azul-fuerte` **ya no es una obligación de contraste**: queda para énfasis, hover y anillos de foco, donde se quiere más peso, no más legibilidad.

### 3.3 Contraste sobre la banda oscura

| Par | Ratio |
|---|---|
| `--lamina` sobre `--azul-tinta` | 18.52:1 |
| `--humo-claro` sobre `--azul-tinta` | 6.86:1 |
| `--azul-claro` sobre `--azul-tinta` | 8.00:1 |
| `--azul` sobre `--azul-tinta` | **2.72:1** |

Sobre oscuro **no se usa `--azul`**: 2.72:1 no alcanza ni para un componente no textual, que pide 3:1. Para eso está `--azul-claro`. Esta es la razón de que el logotipo se invierta en el pie.

### 3.4 Ritmo tonal de la página

El azul atraviesa el sitio en tres profundidades de fondo. No es decoración: marca el recorrido.

| Sección | Fondo | Por qué |
|---|---|---|
| Hero | `--papel` | Punto de partida neutro |
| Banco de marca | `--papel` | La lámina de espécimen ya aporta su propio escalón |
| Posicionamiento | `--papel` | Una sola frase, mucho aire |
| Servicios | `--papel` | Lista larga: el fondo no debe competir |
| Diferencial | `--azul-humo` | Primer cambio de tono, marca el argumento |
| Proceso | `--papel` | Vuelve a neutro, la secuencia manda |
| Clientes | `--azul-humo` | Segundo lavado, cierra el bloque de prueba |
| Contacto y pie | `--azul-tinta` | Cierre. **Único bloque oscuro de todo el sitio** |

**Regla dura:** el oscuro aparece una sola vez y al final. Un bloque oscuro suelto en medio de una página clara se lee como un error de copiar y pegar, no como una decisión.

### 3.5 Reglas de color

- **Un solo acento en toda la página.** El azul no compite con nada. No hay un verde de éxito ni un rojo de error con otro tono: los estados se resuelven con `--tinta`, `--azul` y peso tipográfico.
- **Los grises son todos fríos.** Ninguno se tinta en cálido. Una sola familia de gris en todo el proyecto.
- **Nada de degradados de acento.** Ni glows, ni halos, ni blur de fondo. Esa es exactamente la huella que estamos borrando del sitio anterior.
- **La textura permitida es el grano**, no el degradado: una capa fija de ruido a opacidad muy baja sobre el papel, sin eventos de puntero.
- `--regla` nunca delimita un campo de formulario ni un control. Para eso está `--borde`.

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

**La esquina redondeada pertenece a la marca, y a nada más.** El cuadro IA lleva radio 0.19 de la altura de mayúscula, y la insignia y las piezas del hero lo heredan en proporción. Ese es el motivo de que el resto del sitio sea de esquina viva: si nada más se redondea, el cuadro se lee como lo que es. Redondear una tarjeta o un botón le quita al logotipo su única seña de forma.

**La única forma circular del sitio es la tuerca**, con su eje y su aguja. Se permite porque no compite con el cuadro: es un mecanismo, no una pieza de identidad. Antes esa excepción se justificaba por el punto del isotipo, que ya no existe.

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
| `--dur-media` | `420ms` | Entradas de elemento, relevo de glifo de la insignia |
| `--dur-larga` | `720ms` | Entradas de sección |
| `--ease-salida` | `cubic-bezier(0.16, 1, 0.3, 1)` | Todo lo que entra |
| `--ease-fisica` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Solo la aguja de la tuerca y el campo del hero, con rebote |

### 7.1 El campo del hero

29 cuadros del logotipo, cada uno girando sobre su centro. Muelle amortiguado con rigidez 0.07 y amortiguación 0.78, alcance del puntero 190 unidades del `viewBox`. Las piezas despiertas se tiñen de `--azul`.

**Aquí la rotación sí se lee**, al revés que en la insignia: los ángulos son libres y un cuadro inclinado se distingue de uno recto. Ver la sección 2.5.

- **En reposo miran todas a cero.** Ese es el argumento: un sistema, no un enjambre suelto.
- **Nacen ya alineadas, no desordenadas.** Si `requestAnimationFrame` nunca corre, el campo se ve igual de correcto. Mismo principio que las entradas de sección.
- **El bucle lleva control explícito de fotograma.** Si la pestaña se va al fondo con un fotograma pendiente, el navegador lo congela y sin este control el campo se quedaría muerto para siempre. Al volver al primer plano se cancela el fotograma zombi y se reanuda.
- **El bucle solo corre cuando hay movimiento pendiente y la sección está a la vista.** No hay animación infinita de fondo.
- **Se oculta por debajo de 900 px.** Se activa con el puntero, y en táctil no hay puntero: sería decoración muerta ocupando media pantalla y gastando batería en el dispositivo con menos potencia.

### 7.2 Reglas duras

- Solo se animan `transform` y `opacity`. Nunca `top`, `left`, `width` ni `height`.
- Prohibido `window.addEventListener('scroll')`. Se usa `IntersectionObserver` o animaciones de scroll de CSS.
- El escalonamiento de entrada se calcula por posición real en la fila, no por índice en el documento. Ese fue el error del sitio anterior.
- Todo lo anterior colapsa a estático bajo `prefers-reduced-motion: reduce`. Las físicas del campo pasan a estático y la insignia cambia de glifo sin transición.

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
- Anillo de foco visible en **todos** los elementos interactivos, no solo en botones: `outline: 2px solid var(--azul); outline-offset: 3px`.
- Enlace de salto al contenido como primer elemento del documento.
- **La tuerca es un `<input type="range">` real**, invisible por encima del mando. Funciona con flechas del teclado, tiene `aria-label` y actualiza `aria-valuetext` al nombre del modo en español, no al número. El dibujo del mando lleva `aria-hidden`.
- La tuerca es un adorno funcional: si el visitante no la toca, la página se lee igual. Nunca es requisito para acceder a información.
- `aria-current="true"` en el enlace de navegación de la sección visible.
- La insignia y sus cuatro glifos son decorativos: llevan `aria-hidden="true"` y quien anuncia el modo es el `output` de la tuerca, con el nombre en español, no un número. El logotipo del hero lleva `role="img"` y `aria-label="Agentia"`; el de la barra y el del pie van ocultos del árbol y el nombre lo da su texto alternativo.
- **El contenido es visible por defecto.** Solo se esconde para revelarlo cuando el script confirma que puede, con red de seguridad a los 2.5 segundos. Un fallo de JavaScript nunca deja la página en blanco.

---

## 10. Lo que no se toca

- **El contenido sale de `docs/contenido-agentia.md` y no se reescribe.**
- **Los IDs de ancla se conservan:** `#servicios`, `#diferencial`, `#proceso`, `#clientes`, `#contacto`.
- **Nada de contenido de negocio inventado.** Ni clientes, ni cifras, ni testimonios, ni años de experiencia. Los marcadores provisionales se quedan marcados como provisionales.
- **Sin dependencias de terceros en tiempo de ejecución.** Ni GSAP, ni Lenis, ni iconos por CDN. Todo es CSS y JavaScript propio.
- **El corte AGENT + IA no se aplica a ninguna otra palabra.** Ver la sección 2.1.
- **La esquina redondeada es solo del cuadro de marca.** El resto del sitio es radio 0. Ver la sección 6.

---

## 11. Presupuesto

| Métrica | Objetivo |
|---|---|
| LCP en 4G simulado | menos de 2.5 s |
| CLS | menos de 0.1 |
| Peso de la primera vista | menos de 800 KB |

Consumido hasta ahora: 222 KB de tipografías. Queda margen suficiente, siempre que las imágenes vayan en formato moderno y con `width` y `height` declarados para no generar desplazamiento.
