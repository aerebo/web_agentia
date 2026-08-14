# Sistema de diseño AGENTIA

**Dirección aprobada:** B, Espécimen.
**Fecha de aprobación:** 14 de agosto de 2026.
**Regla de oro:** ningún color, tamaño, espaciado ni duración se escribe suelto en el código. Todo sale de los tokens de este documento. Si algo falta aquí, se agrega aquí primero y después se usa.

---

## 1. Tesis

El sitio no habla del sistema de marca: el sitio **es** el sistema de marca abierto y funcionando, como la lámina de muestra de una fundidora tipográfica. Dos demostraciones en vivo lo sostienen:

1. **Los ejes tipográficos.** El visitante mueve peso y ancho y todos los titulares de la página responden.
2. **Las físicas del isotipo.** La marca cambia de estado según el contexto, sin dejar de ser la misma marca.

Ambas cosas son la prueba del argumento comercial: "definimos tokens visuales, tono y plantillas reutilizables" y "manual de marca vivo, aplicado en cada entrega". La página no lo promete, lo ejecuta.

---

## 2. Marca

### 2.1 Los tres estados

El isotipo es **dos brazos y un punto**. Los tres estados son la misma geometría en distinta posición.

| Estado | Forma | Significado | Dónde se usa |
|---|---|---|---|
| `marca` | `Λ` con el punto bajo el vértice | Identidad base | Hero, nav en reposo, footer, favicon |
| `play` | `>` con el punto a la izquierda del vértice | Grabación y generación con IA | Producción de video e IA audiovisual, creación de personajes |
| `code` | `<•>` con el punto centrado | Código | Desarrollo web con IA |

### 2.2 Las físicas

La transformación no es un cambio de imagen, es un movimiento continuo de las mismas piezas. Esto es lo que hace que la marca se lea viva y no como tres logos distintos.

- **`marca` a `play`:** rotación de 90 grados en sentido horario del grupo completo. La `Λ` con el vértice arriba se convierte en `>` con el vértice a la derecha, y el punto, que estaba debajo del vértice, queda a su izquierda. Es una sola rotación, no un redibujo. Esa es la razón por la que los dos logotipos del manual son coherentes entre sí.
- **`play` a `code`:** el `>` se desplaza a la izquierda, entra su copia espejada `<` desde la derecha, y el punto viaja al centro entre los dos vértices.
- **Vuelta a `marca`:** rotación inversa, el `<` sale por donde entró.

**Curva:** `--ease-fisica`, con rebote corto. El punto siempre llega un instante después que los brazos, nunca al mismo tiempo. Ese retardo de 60 ms es lo que da la sensación de masa.

### 2.3 Reglas de uso

- **Una sola marca animada por pantalla.** La del nav es la que se transforma. Las que aparecen dentro de las secciones son estados fijos que funcionan como señal de sección, no se animan solas.
- **El wordmark AGENTIA va como SVG, nunca como texto vivo.** Su A sin travesaño y su tracking amplio son propios del logotipo y no coinciden con ninguna tipografía del sistema. Trazarlo con una fuente sería falsificarlo.
- **El corte AGENT + IA no se aplica a otras palabras.** Se acabó el `Experienc<span>ia</span>`. El recurso pertenece a la marca y pierde todo su valor si se usa como adorno.
- **El punto es el único elemento circular de todo el sitio.** Ver la regla de forma en la sección 6.

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
| `--borde` | `#8A8A96` | Bordes de elementos interactivos, campos y controles |
| `--violeta` | `#6D4AFF` | Acento único: rellenos, estados activos, el punto |
| `--violeta-texto` | `#5B36E8` | El mismo acento, solo para texto pequeño sobre papel |
| `--nota` | `#E9E4FF` | Relleno suave de resaltados y estados activos |

### 3.2 Contraste verificado

| Par | Ratio | Cumple |
|---|---|---|
| `--tinta` sobre `--papel` | 16.0:1 | AAA |
| `--lapiz` sobre `--papel` | 5.2:1 | AA texto normal |
| `--violeta` sobre `--papel` | 4.5:1 | AA texto normal, al límite |
| `--violeta-texto` sobre `--papel` | 5.9:1 | AA texto normal, con margen |
| `--borde` sobre `--papel` | 3.0:1 | AA componentes no textuales |
| `--regla` sobre `--papel` | 1.25:1 | Solo decorativo, nunca borde de control |

Por eso existen dos tokens de violeta y dos de gris de línea. `--violeta` se usa en rellenos, superficies y texto grande. Para un enlace en tamaño de cuerpo va `--violeta-texto`. `--regla` nunca delimita un campo de formulario: para eso está `--borde`.

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

### 4.4 Ejes en vivo

```
--eje-peso:  340   /* lo mueve el deslizador de peso  */
--eje-ancho: 100   /* lo mueve el deslizador de ancho */
```

Todos los titulares de la página se declaran con `font-variation-settings: 'wght' var(--eje-peso), 'wdth' var(--eje-ancho)`. Los deslizadores escriben sobre estas dos variables en `:root` y nada más. Un solo punto de control, toda la página responde.

**Valores de reposo:** peso 340, ancho 100. **Rango expuesto al visitante:** peso 200 a 800, ancho 75 a 100.
**Persistencia:** ninguna. Al recargar vuelve al reposo. No se guarda nada en el navegador del visitante.

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

**La única forma circular del sitio es el punto del isotipo.** Esa es justamente la razón de la regla: si nada más es redondo, el punto no compite con nada y se lee como el elemento de marca que es.

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

- Contraste AA verificado, tabla en 3.2.
- Anillo de foco visible en **todos** los elementos interactivos, no solo en botones: `outline: 2px solid var(--violeta); outline-offset: 3px`.
- Enlace de salto al contenido como primer elemento del documento.
- Los deslizadores de ejes son `<input type="range">` reales, operables con teclado, con `aria-label` y `aria-valuetext` en español.
- La demostración tipográfica es un adorno funcional: si el visitante no la toca, la página se lee igual. Nunca es requisito para acceder a información.
- `aria-current="true"` en el enlace de navegación de la sección visible.
- Los estados del isotipo son decorativos: el SVG lleva `aria-hidden="true"` y el nombre accesible lo da el texto.

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
