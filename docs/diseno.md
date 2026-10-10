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

### 1.1 El sitio son cinco páginas

**Partido el 10 de octubre de 2026.** Hasta entonces era una sola página con todo dentro. El benchmark de `docs/benchmark.md` mostró que **los siete sitios del sector son multipágina**, y el sitio se alineó con eso.

| Ruta | Qué contesta |
|---|---|
| `/` | ¿Qué hacen, qué puedo contratar, y cómo los contacto? |
| `/servicios/` | ¿Qué incluye cada frente? |
| `/trabajos/` | ¿Puedo ver algo? |
| `/agentia/` | ¿Por qué ustedes, cómo trabajan, quiénes son, qué dudas quedan? |
| `/contacto/` | ¿A qué correo escribo? |

### 1.2 La portada es corta a propósito, y es una decisión suya

Los siete sitios del benchmark son multipágina **y además tienen portadas largas**: thoughtbot 10 secciones, netguru 9, barrel 11, kom.pe 8. El patrón del mercado es portada que resume todo con enlaces, no portada mínima.

**Agentia eligió la portada corta**: hero, los seis servicios en resumen, y el formulario. Se le advirtió de las dos consecuencias y decidió igual, que es su derecho:

1. **Le pide el contacto a alguien que todavía no sabe mucho.** El formulario es el final de un argumento; sin argumento delante, la conversión baja.
2. **La portada es la que posiciona en Google.** Es la que rankearía por «agencia de marketing con IA Perú». Con tres bloques tiene menos con qué hacerlo.

Queda escrito para que, si algún día los números decepcionan, se sepa dónde mirar primero y no se busque la causa en otro sitio.

### 1.3 El orden dentro de cada página

**No es estético: es el orden en que un cliente potencial hace las preguntas.**

En `/agentia/` el orden es: por qué Agentia, cómo trabajamos, quiénes somos, preguntas frecuentes. El argumento primero, la mecánica después, las credenciales al final y las objeciones pegadas a la salida.

**Reglas que sobreviven al corte:**

- **La prueba social no se adelanta con nombres sueltos.** No hay permiso de uso de logo todavía, y una fila de nombres en texto plano no es prueba, es relleno.
- **Decir para quién NO es cierra el argumento**, no lo abre. Va al final del bloque «por qué», no en sección propia.
- **Las preguntas frecuentes van las últimas** de `/agentia/`. Son las últimas objeciones antes de mandar a contacto.
- **Dos llamadas a la acción intermedias como máximo**, y solo donde el visitante acaba de recibir un argumento completo.
- **El oscuro aparece una sola vez por página y al final.** Ver la sección 3.4.

### 1.4 El sitio tiene dos llamadas a la acción, y solo dos

Fijado el 10 de octubre de 2026. Antes había **siete etiquetas distintas** en los botones, y tres de ellas —«Cotizar», «Pedir diagnóstico» y «Conversemos»— llevaban las tres al mismo sitio. El visitante no tenía forma de saber si iban a destinos diferentes.

| Etiqueta | Lleva a | Dónde |
|---|---|---|
| **Agendar** | El formulario, que vive **solo en la portada** | La principal. Barra, hero, y al cerrar «Cómo trabajamos» |
| **Contactar** | Los tres correos, que viven **solo en `/contacto/`** | La alternativa de quien prefiere escribir directo. Al cerrar «Quiénes somos» |

**Cada uno lleva a un sitio de verdad distinto**, desde el 10 de octubre de 2026. Antes `/contacto/` tenía el formulario *y* los correos, así que los dos botones acababan en la misma página y la diferencia entre ellos era nominal. Ahora el formulario es de la portada y los correos son de `/contacto/`.

Cada una de las dos páginas enlaza a la otra con una línea discreta, para quien llegó por el camino que no era.

**Agendar va en relleno y Contactar en línea.** No compiten: una es la principal y la otra es la salida de quien no quiere llenar campos.

**Van por el camino corto.** Los marcadores `{{AGENDAR}}` y `{{CONTACTAR}}` los resuelve `armar.py` según la página: si esa página ya trae el formulario o los correos, baja a ellos con un ancla; si no, va a `/contacto/`. Antes la portada mandaba a recargar otra página para llegar a un formulario que estaba justo debajo.

**«Ver servicios» no es una llamada a la acción**, es navegación, y por eso convive con las dos. Pero una sola vez por página: estaba en el hero y otra vez en el resumen de servicios, a un scroll de distancia.

### 1.5 El sitio se arma, ya no se edita a mano

`armar.py` lee `partes/` y escribe `_sitio/`. La cabecera, el menú y el pie son los mismos en las cinco páginas: sin armador habría que editarlos cinco veces y el día que a alguien se le pase uno, el menú queda distinto según la página.

No es un framework y no trae dependencias: lee archivos, sustituye cuatro marcadores y escribe HTML, con biblioteca estándar de Python. La regla de **cero dependencias en tiempo de ejecución** sigue intacta: lo que llega al navegador es HTML, CSS y JavaScript propio.

**`{{RAIZ}}` y por qué no hay rutas absolutas:** ver la sección 4.8 del LEEME.

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
| Contacto | `--papel` | **Cambiado el 10 de octubre de 2026.** Era la banda oscura; ahora comparte fondo con el hero |
| Pie | `--azul-tinta` | Cierre. **Único bloque oscuro de todo el sitio** |

**Regla dura:** el oscuro aparece una sola vez y al final. Un bloque oscuro suelto en medio de una página clara se lee como un error de copiar y pegar, no como una decisión.

**El formulario dejó de vivir sobre oscuro el 10 de octubre de 2026**, a petición de Agentia: comparte fondo con el hero. El bloque oscuro se reduce al pie.

Al moverlo salió a la luz un fallo que llevaba ahí desde el principio y que nadie habría visto en el diseño anterior: **los tres correos estaban pintados en `--papel`**, que sobre la banda oscura era blanco legible y sobre papel es exactamente el color del fondo. Quedaron invisibles. Lo mismo las líneas de la lista, que eran blancos translúcidos, y el texto del desplegable.

Lección para la próxima: cuando un bloque cambia de fondo, **no basta con mirarlo**. Hay que recorrer sus textos comparando color contra fondo, porque un texto invisible no se nota en una captura: se nota cuando falta.

### 3.5 Reglas de color

- **Un solo acento en toda la página.** El azul no compite con nada. No hay un verde de éxito ni un rojo de error con otro tono: los estados se resuelven con `--tinta`, `--azul` y peso tipográfico.
- **Los grises son todos fríos.** Ninguno se tinta en cálido. Una sola familia de gris en todo el proyecto.
- **Nada de degradados de acento.** Ni glows, ni halos, ni blur de fondo. Esa es exactamente la huella que estamos borrando del sitio anterior.
- **La textura permitida es el grano**, no el degradado: una capa fija de ruido a opacidad muy baja sobre el papel, sin eventos de puntero.
- `--regla` nunca delimita un campo de formulario ni un control. Para eso está `--borde`.
- **Los campos de formulario llevan línea gruesa y relleno blanco**, no la línea fina del resto del sitio. Cuando el formulario se mudó al fondo claro el 10 de octubre de 2026, quedó con relleno `--lamina` sobre `--papel`: **1.09:1 contra la página, o sea invisible**, y todo el peso del campo recaía en un pelo de 1px a 3.29:1. Pasaba el mínimo de 3:1 sobre el papel y aun así no se veía. El campo es donde el visitante hace lo único que queremos que haga: se gana la línea gruesa, igual que la tuerca se gana ser lo único redondo.

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
| `--t-indice` | `clamp(1.5rem, 2.2vw, 2rem)` | Mono: los números de las listas numeradas |

**`--t-indice`** es el cuerpo de los números de las listas numeradas, añadido el 10 de octubre de 2026. Antes salían del cuerpo de cota, 11 px, y a ese tamaño no pesaban nada: la columna de la izquierda quedaba vacía y la lista se leía como párrafos sueltos en vez de como una serie.

**El número no es una cota más**: es lo que ordena la lista y lo primero que el ojo usa para contar. Va alineado con la primera línea del nombre y no centrado en la fila, porque centrado flota cuando la entrada ocupa dos líneas.

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

**La cota de ancho del hero se quitó el 10 de octubre de 2026.** Era la línea con topes que anunciaba «809 PX» y se actualizaba al redimensionar. Venía de la dirección visual elegida en `docs/direcciones.md`, que proponía presentar cada sección como una lámina de manual de marca, con su cota y su ficha técnica al margen.

**El recurso se cayó con el resto del lenguaje de lámina.** La página ya no se lee como un espécimen: tiene fichas con icono, tarjetas redondeadas y un logotipo tipográfico. Una cota suelta en el hero dejó de ser una señal de oficio y pasó a ser un resto de otra versión.

Se quitaron con ella su JavaScript, que observaba el redimensionado, y sus cuatro reglas de CSS. **No se deja código muerto de una decisión revertida.**


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

**Cambiado el 10 de octubre de 2026**, a petición de Agentia sobre una referencia visual. Hasta entonces el sitio era de esquina viva sin una sola excepción.

### 6.1 La regla nueva

| Token | Valor | Dónde |
|---|---|---|
| `--r-0` | `0` | Botones, campos de formulario, láminas, el acordeón |
| `--r-tarjeta` | `0.875rem` | Fichas, marcos de trabajos, columnas de «para quién es» |
| `--r-circulo` | `50%` | El número de cada ficha, el eje de la tuerca |
| El cuadro IA | `0.24` de la mayúscula | Solo el logotipo y la insignia |

**El cuadro de marca sube su radio de 0.19 a 0.24.** Esa es la compensación, y conviene entender por qué:

0.19 era el radio **medido del original entregado**. Mientras el sitio era de esquina viva, ese radio bastaba para que el cuadro fuera lo único redondeado y se leyera como marca. Con tarjetas redondeadas por todas partes, 0.19 lo convertía en una tarjeta pequeña más. Se sube a 0.24 para que siga siendo, con diferencia, **lo más redondeado de la página**.

Es decir: el valor ya no sale de la medición, sale de mantener una jerarquía. Si algún día se quitan las tarjetas, vuelve a 0.19.

### 6.2 Lo que esto costó, dicho claro

La regla anterior decía: *«la esquina redondeada pertenece a la marca, y a nada más. Redondear una tarjeta o un botón le quita al logotipo su única seña de forma.»*

**Eso sigue siendo verdad.** El logotipo perdió exclusividad sobre el redondeo y ahora solo conserva ventaja de grado, no de tipo. Se aceptó a cambio de lo que ganan las fichas: cada punto se lee como una unidad cerrada, y el número pasa de ser una cota a ser una etiqueta.

Queda escrito para que nadie lo redescubra dentro de seis meses y lo trate como un descuido.

### 6.3 Lo que no cambió

- **Los botones y los campos siguen en radio 0.** Si todo se redondea, no queda contraste de forma en ninguna parte.
- **Sigue sin haber sombras.** La elevación se comunica con `--lamina` sobre `--papel` y con líneas, nunca con `box-shadow`. Una ficha es una lámina con borde, no una tarjeta flotante.
- **La tuerca sigue siendo el único mecanismo circular**, y ahora comparte lo redondo con los números de ficha, que son etiquetas y no mecanismos.

| Token | Valor |
|---|---|
| `--linea-fina` | `1px` |
| `--linea-gruesa` | `2px` |
| `--alto-control` | `3.5rem` |

**`--alto-control` es el alto de todo lo pulsable**, añadido el 10 de octubre de 2026. Botones, botón de menú y botón de envío miden lo mismo aunque lleven tipografías de distinto cuerpo.

Sin él, el botón de menú salía a 31 px contra los 56 del botón de al lado: mismo relleno declarado, distinto cuerpo de letra, distinta altura resultante. **Dos botones pegados con alturas distintas no se leen como un par, se leen como un error de maquetación.**

Los 56 px además superan los 44 que piden las pautas de accesibilidad para una diana táctil.

### 6.4 Iconos

Ocho iconos de línea, dibujados a mano como SVG en línea dentro de las piezas: cuatro para el proceso y cuatro para los pilares. Mismo trazo que los glifos de la insignia: sin relleno, `stroke-width: 7` sobre un `viewBox` de 100, puntas y uniones redondeadas.

**No hay librería de iconos ni CDN**, y no la va a haber: es la regla de cero dependencias de la sección 10. Si hace falta un icono nuevo, se dibuja con esos mismos parámetros o desentona.

Van en `--azul` y con `aria-hidden="true"`: son refuerzo visual del título, no información.

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
- La insignia y sus cuatro glifos son decorativos: llevan `aria-hidden="true"` y quien anuncia el modo es el `output` de la tuerca, con el nombre en español, no un número.
- **Ese `output` dejó de verse el 10 de octubre de 2026, pero sigue ahí.** El rótulo «Modo de marca / Identidad» se quitó de la vista porque repetía lo que ya dice la ficha de al lado y se comía una pantalla de alto. El elemento se conserva con `.oculto-visual`: es a quien apunta el `aria-describedby` del mando y es lo que anuncia el cambio a un lector de pantalla. **Borrarlo dejaría el mando sin voz**, que es el tipo de regresión que no se nota mirando la página. El logotipo del hero lleva `role="img"` y `aria-label="Agentia"`; el de la barra y el del pie van ocultos del árbol y el nombre lo da su texto alternativo.
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
