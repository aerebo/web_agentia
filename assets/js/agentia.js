/* ==========================================================================
   AGENTIA
   Sin dependencias. Solo IntersectionObserver y eventos de entrada.
   Prohibido escuchar el evento scroll: ver docs/diseno.md seccion 7.
   ========================================================================== */

(function () {
  'use strict';

  var raiz = document.documentElement;
  var movimientoReducido = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* ------------------------------------------------------------------------
     1. La tuerca
     Cuatro detenciones, una cada 90 grados. Cada una es la misma pieza del
     isotipo girada sobre el punto violeta, que es el eje y nunca se mueve.
     ------------------------------------------------------------------------ */

  var ESTADOS = ['marca', 'play', 'lapiz', 'code'];
  var NOMBRES = ['Identidad', 'Video', 'Diseño', 'Código'];

  /* separacion y escala del estado code, en las mismas unidades que el CSS */
  var SEP_CODE = 60;
  var ESCALA_CODE = 0.62;

  var control = document.getElementById('tuerca');

  if (control) {
    var tuerca = control.closest('.tuerca');
    var mando = control.closest('.tuerca__mando');
    var marcaPanel = document.querySelector('[data-marca-panel]');
    var salidaModo = document.getElementById('modo-activo');
    var revelados = document.querySelectorAll('.revelado');

    /* angulo continuo: no se reinicia al pasar de 360, para que la aguja
       nunca se desenrolle hacia atras sin motivo */
    var anguloContinuo = 0;
    var arrastrando = false;

    function pasoDesdeAngulo(a) {
      return ((Math.round(a / 90) % 4) + 4) % 4;
    }

    /* Durante el arrastre libre, el estado code se abre de forma gradual:
       cuanto mas cerca de los 270 grados, mas separados y mas pequenos los
       brazos. Asi no hay salto al soltar. */
    function proximidadACode(a) {
      var d = Math.abs((((a - 270) % 360) + 540) % 360 - 180);
      return Math.max(0, Math.min(1, 1 - d / 45));
    }

    function pintarModo(paso) {
      if (salidaModo) salidaModo.textContent = NOMBRES[paso];
      control.setAttribute('aria-valuetext', NOMBRES[paso]);

      Array.prototype.forEach.call(revelados, function (ficha) {
        if (Number(ficha.dataset.modo) === paso) {
          ficha.setAttribute('data-activo', 'true');
        } else {
          ficha.removeAttribute('data-activo');
        }
      });
    }

    /* estado libre: se escribe angulo crudo, sin pasar por data-estado */
    function pintarAnguloLibre(a) {
      var t = proximidadACode(a);
      [tuerca, marcaPanel].forEach(function (el) {
        if (!el) return;
        el.style.setProperty('--giro', a + 'deg');
        el.style.setProperty('--gemelo', t);
        el.style.setProperty('--sep', SEP_CODE * t + 'px');
        el.style.setProperty('--escala', 1 - (1 - ESCALA_CODE) * t);
      });
    }

    /* estado en reposo: manda el data-estado y el CSS pone los valores */
    function asentar(paso) {
      [tuerca, marcaPanel].forEach(function (el) {
        if (!el) return;
        el.style.removeProperty('--gemelo');
        el.style.removeProperty('--sep');
        el.style.removeProperty('--escala');
      });
      if (marcaPanel) marcaPanel.dataset.estado = ESTADOS[paso];
      /* la tuerca no tiene data-estado, asi que conserva el angulo continuo */
      if (tuerca) tuerca.style.setProperty('--giro', anguloContinuo + 'deg');
      if (marcaPanel) marcaPanel.style.setProperty('--giro', anguloContinuo + 'deg');
      pintarModo(paso);
    }

    /* mueve el angulo continuo al equivalente mas cercano del paso pedido,
       para que ir de Codigo a Identidad avance 90 grados y no retroceda 270 */
    function irAPaso(paso) {
      var objetivo = paso * 90;
      var delta = (((objetivo - anguloContinuo) % 360) + 540) % 360 - 180;
      anguloContinuo += delta;
      control.value = paso;
      asentar(paso);
    }

    control.addEventListener('input', function () {
      irAPaso(Number(control.value));
    });

    /* ---- arrastre giratorio ---- */

    function anguloDelPuntero(evento) {
      var caja = mando.getBoundingClientRect();
      var cx = caja.left + caja.width / 2;
      var cy = caja.top + caja.height / 2;
      /* 0 grados arriba, positivo en sentido horario */
      return Math.atan2(evento.clientX - cx, cy - evento.clientY) * 180 / Math.PI;
    }

    function alMover(evento) {
      if (!arrastrando) return;
      var crudo = anguloDelPuntero(evento);
      var delta = (((crudo - anguloContinuo) % 360) + 540) % 360 - 180;
      anguloContinuo += delta;
      pintarAnguloLibre(anguloContinuo);
      pintarModo(pasoDesdeAngulo(anguloContinuo));
    }

    function alSoltar(evento) {
      if (!arrastrando) return;
      arrastrando = false;
      tuerca.classList.remove('tuerca--arrastrando');
      if (marcaPanel) marcaPanel.classList.remove('marca--siguiendo');
      if (evento.pointerId !== undefined && mando.releasePointerCapture) {
        try { mando.releasePointerCapture(evento.pointerId); } catch (e) {}
      }
      irAPaso(pasoDesdeAngulo(anguloContinuo));
    }

    Array.prototype.forEach.call(mando.querySelectorAll('[data-agarre]'), function (tirador) {
      tirador.addEventListener('pointerdown', function (evento) {
        evento.preventDefault();
        arrastrando = true;
        tuerca.classList.add('tuerca--arrastrando');
        if (marcaPanel) marcaPanel.classList.add('marca--siguiendo');
        control.focus({ preventScroll: true });
        if (mando.setPointerCapture) {
          try { mando.setPointerCapture(evento.pointerId); } catch (e) {}
        }
        alMover(evento);
      });
    });

    mando.addEventListener('pointermove', alMover);
    mando.addEventListener('pointerup', alSoltar);
    mando.addEventListener('pointercancel', alSoltar);
    window.addEventListener('blur', alSoltar);

    irAPaso(0);
  }

  /* ------------------------------------------------------------------------
     2. Cota de ancho del lienzo
     La lamina declara su propia medida, y se actualiza al redimensionar.
     ------------------------------------------------------------------------ */

  var cotas = document.querySelectorAll('[data-cota-ancho]');

  function actualizarCotas() {
    Array.prototype.forEach.call(cotas, function (cota) {
      var referencia = document.querySelector(cota.dataset.cotaAncho);
      if (!referencia) return;
      cota.textContent = Math.round(referencia.getBoundingClientRect().width) + ' PX';
    });
  }

  if (cotas.length) {
    actualizarCotas();
    if ('ResizeObserver' in window) {
      new ResizeObserver(actualizarCotas).observe(document.body);
    }
  }

  /* ------------------------------------------------------------------------
     3. Entradas escalonadas
     El retardo se calcula por posicion real en la fila, nunca por indice
     en el documento. Ese fue el error de la version anterior del sitio.
     ------------------------------------------------------------------------ */

  var revelables = document.querySelectorAll('.rv');

  function asignarRetardos() {
    var filas = new Map();

    Array.prototype.forEach.call(revelables, function (el) {
      var caja = el.getBoundingClientRect();
      var fila = Math.round((caja.top + window.scrollY) / 32);
      if (!filas.has(fila)) filas.set(fila, []);
      filas.get(fila).push(el);
    });

    filas.forEach(function (elementos) {
      elementos
        .sort(function (a, b) {
          return a.getBoundingClientRect().left - b.getBoundingClientRect().left;
        })
        .forEach(function (el, i) {
          el.style.setProperty('--rv-retardo', i * 70 + 'ms');
        });
    });
  }

  function revelarTodo() {
    Array.prototype.forEach.call(revelables, function (el) {
      el.classList.add('rv--visible');
    });
  }

  if (revelables.length && 'IntersectionObserver' in window && !movimientoReducido.matches) {
    /* Recien aqui se autoriza a esconder el contenido: si el script no
       llega hasta esta linea, la pagina se ve entera igual. */
    raiz.classList.add('js-rv');
    asignarRetardos();

    var observador = new IntersectionObserver(
      function (entradas) {
        entradas.forEach(function (entrada) {
          if (!entrada.isIntersecting) return;
          entrada.target.classList.add('rv--visible');
          observador.unobserve(entrada.target);
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -8% 0px' }
    );

    Array.prototype.forEach.call(revelables, function (el) {
      observador.observe(el);
    });

    /* Red de seguridad: si el observador no dispara (pestana en segundo
       plano, prerender, navegador que lo limita), el contenido aparece
       igual pasados dos segundos y medio. Nunca una pagina en blanco. */
    window.setTimeout(revelarTodo, 2500);

    if ('ResizeObserver' in window) {
      new ResizeObserver(asignarRetardos).observe(document.body);
    }
  }

  /* ------------------------------------------------------------------------
     4. Menu movil
     Panel completo, cierre con Escape, foco devuelto al boton que lo abrio.
     ------------------------------------------------------------------------ */

  var menu = document.getElementById('menu');
  var abrir = document.querySelector('.nav__toggle');

  if (menu && abrir) {
    var cerrar = menu.querySelector('[data-cerrar-menu]');

    function abrirMenu() {
      menu.hidden = false;
      abrir.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      cerrar.focus();
    }

    function cerrarMenu(devolverFoco) {
      menu.hidden = true;
      abrir.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      if (devolverFoco) abrir.focus();
    }

    abrir.addEventListener('click', abrirMenu);
    cerrar.addEventListener('click', function () { cerrarMenu(true); });

    Array.prototype.forEach.call(menu.querySelectorAll('a'), function (enlace) {
      enlace.addEventListener('click', function () { cerrarMenu(false); });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !menu.hidden) cerrarMenu(true);
    });

    window.addEventListener('resize', function () {
      if (!menu.hidden && window.innerWidth > 860) cerrarMenu(false);
    });
  }

  /* ------------------------------------------------------------------------
     5. Seccion visible: marca el enlace del nav y cambia el estado del isotipo
     Cada seccion declara que estado de marca le corresponde con data-marca.
     ------------------------------------------------------------------------ */

  var marcaNav = document.querySelector('[data-marca-viva]');
  var secciones = document.querySelectorAll('[data-marca]');
  var enlaces = document.querySelectorAll('.nav__enlaces a[href^="#"]');

  function activarEnlace(id) {
    Array.prototype.forEach.call(enlaces, function (enlace) {
      if (enlace.getAttribute('href') === '#' + id) {
        enlace.setAttribute('aria-current', 'true');
      } else {
        enlace.removeAttribute('aria-current');
      }
    });
  }

  if (secciones.length) {
    var visibles = new Map();

    var vigia = new IntersectionObserver(
      function (entradas) {
        entradas.forEach(function (entrada) {
          visibles.set(entrada.target, entrada.intersectionRatio);
        });

        var mejor = null;
        var mayor = 0;

        visibles.forEach(function (ratio, seccion) {
          if (ratio > mayor) {
            mayor = ratio;
            mejor = seccion;
          }
        });

        if (!mejor) return;

        if (marcaNav) {
          marcaNav.dataset.estado = mejor.dataset.marca;
        }
        if (mejor.id) {
          activarEnlace(mejor.id);
        }
      },
      { threshold: [0, 0.25, 0.5, 0.75, 1] }
    );

    Array.prototype.forEach.call(secciones, function (seccion) {
      vigia.observe(seccion);
    });
  }
})();
