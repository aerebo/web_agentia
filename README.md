# AGENTIA · sitio web

Propuesta de sitio para **agentia.com.pe**. Una sola pagina, estatica, sin build
ni dependencias: se abre, se edita y se sube tal cual.

**Vista en vivo:** https://agentia-pe.github.io/agentia-web/

La vista en vivo se actualiza sola en cada push a `main`, unos dos minutos
despues. El estado de cada publicacion esta en la pestana **Actions**.

## Arrancar en local

```
python3 servidor-local.py
```

Y abrir `http://localhost:5173`. Hace falta un servidor: abrir `index.html` con
doble clic rompe la carga de las tipografias por CORS.

## Antes de tocar nada

Tres documentos mandan sobre el codigo. Leerlos ahorra tiempo:

| Documento | Para que |
|---|---|
| [`LEEME.md`](LEEME.md) | Las trampas del codigo, lo que ya cumple y lo que falta |
| [`docs/diseno.md`](docs/diseno.md) | El sistema de diseno. Todo valor sale de los tokens de `:root` |
| [`docs/contenido-agentia.md`](docs/contenido-agentia.md) | El contenido aprobado y los `[PENDIENTE]` |

La seccion 4 de `LEEME.md` lista siete trampas que costaron encontrarse. Si se
"simplifican", algo se rompe.

## Como comentar y pedir cambios

Para el equipo, sin necesidad de saber git:

- **Un cambio, una nota.** Abrir un *issue* en la pestana **Issues**, con la
  seccion del sitio en el titulo y una captura si es visual.
- **Lo que esta en duda** no se decide por chat: esta en la seccion 8 de
  `LEEME.md`, son las decisiones abiertas que necesitan respuesta de Agentia.
- **Lo marcado `[PENDIENTE]`** en `docs/contenido-agentia.md` no se rellena a
  ojo. Se deja marcado hasta que llegue el contenido real.

## Que no se despliega

`docs/`, `servidor-local.py`, `README.md` y `LEEME.md` se quedan en el
repositorio. A la web solo suben `index.html` y `assets/`.
