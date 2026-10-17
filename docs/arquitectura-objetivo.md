# Arquitectura objetivo · a partir de mindcircus.agency

**17 de octubre de 2026.** A pedido de Agentia: *«haz un scraping y mapa de sitio de esta web https://mindcircus.agency/, necesito que apliquemos lo mismo para Agentia»*.

## Lo que se hizo

Se leyó su `sitemap.xml` y su `robots.txt` el 17 de octubre de 2026. **154 URLs.** El XML queda guardado en `docs/mindcircus-sitemap.xml` para que cualquiera compruebe estas cuentas.

## Su arquitectura, contada

| Rama | Páginas | Patrón |
|---|---|---|
| Portada | 1 | |
| `/servicios` | 1 índice + **11 internas** | Una página por servicio: `/servicios/inteligencia-artificial`, `/servicios/produccion-audiovisual`, `/servicios/influencer-marketing`… |
| `/casos` | 1 índice + **23 internas** | Una página por caso: `/caso/merck-stand-360-impe`, `/caso/hells-pizza`… Fíjate en el singular: el índice es `/casos`, la ficha es `/caso/` |
| `/blog` | 1 índice + **112 artículos** | El grueso del sitio |
| `/nosotros` | 1 | |
| **Ciudades** | **4** | `/agencia-marketing-digital-buenos-aires`, `-rosario`, `-cordoba`, `-mendoza` |

**Tres decisiones de arquitectura que valen más que el diseño:**

1. **Cada servicio tiene su propia URL.** No un acordeón dentro de una página: once páginas que posicionan por separado.
2. **Cada trabajo tiene su propia URL.** Veintitrés fichas de caso, no una galería de miniaturas.
3. **Una página por ciudad.** Cuatro ciudades, cuatro URLs, cada una compitiendo por «agencia de marketing digital en {ciudad}». Es la jugada de SEO local más directa que existe, y Agentia opera en tres ciudades sin una sola página que lo diga.

Y el `robots.txt` bloquea `/team/`, `/config.php` e `/includes/`, lo que dice que el sitio corre sobre PHP a medida.

## La arquitectura que se propone para Agentia

```
/                                        portada
│
├── /servicios/                          índice, los seis
│   ├── /servicios/desarrollo-web/
│   ├── /servicios/identidad-contenido/
│   ├── /servicios/produccion-video/
│   ├── /servicios/personajes-marca/
│   ├── /servicios/diseno-grafico/
│   └── /servicios/pauta-publicitaria/
│
├── /trabajos/                           índice
│   ├── /trabajos/video/                 ya existen
│   ├── /trabajos/grafica/
│   ├── /trabajos/web/
│   └── /trabajo/<cliente-pieza>/        una ficha por trabajo ← nuevo
│
├── /nosotros/
├── /preguntas/
├── /contacto/
│
├── /agencia-marketing-ia-huaraz/        ciudad ← nuevo
├── /agencia-marketing-ia-ica/           ciudad ← nuevo
└── /agencia-marketing-ia-lima/          ciudad ← nuevo
```

**De 9 páginas a 21**, sin contar las fichas de trabajo ni blog.

### Qué se puede montar hoy y qué no

| Rama | ¿Se puede? | Por qué |
|---|---|---|
| 6 páginas de servicio | **Sí** | El contenido ya existe: cada servicio tiene su entrada y tres viñetas aprobadas en `docs/contenido-agentia.md`. Hoy viven apretadas en un acordeón |
| 3 páginas de ciudad | **Sí, la estructura** | Huaraz, Ica y Lima están confirmadas. El texto de cada una hay que escribirlo |
| Fichas de trabajo | **No** | Depende del mismo material que tiene vacíos los seis marcos de Trabajos |
| Blog | **No** | No hay ni un artículo, y un blog vacío resta |

### Lo que NO conviene copiar

**El blog de 112 artículos.** Es el 73% de su sitio y es su motor de captación, construido durante años. Abrir un `/blog/` hoy significa publicar con constancia o tener una sección muerta con fecha a la vista, que es peor que no tenerla.

**Las 23 fichas de caso.** El patrón es correcto; el problema es que Agentia tiene cero piezas publicables. La ficha por trabajo se monta el día que haya material, no antes.

## Lo que esto cambia respecto de lo que había

El benchmark de `docs/benchmark-home.md` miraba portadas de plataformas de producto y concluyó cosas de portada. Este documento mira la **arquitectura de una agencia de servicios**, que es lo que Agentia es, y la conclusión es distinta y más accionable: **el problema no era cuántos bloques tiene la portada, sino cuántas URLs tiene el sitio.**

Seis servicios metidos en un acordeón son un servicio a ojos de un buscador. Tres ciudades sin página son cero ciudades.

---

**Fuente:** [mindcircus.agency/sitemap.xml](https://mindcircus.agency/sitemap.xml), leído el 17 de octubre de 2026 y guardado en `docs/mindcircus-sitemap.xml`.
