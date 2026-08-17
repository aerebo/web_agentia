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
     1.b Campo de piezas del hero

     Cada pieza es el isotipo girando sobre su punto. En reposo miran todas
     a cero: un sistema. Al pasar el puntero, las cercanas se orientan hacia
     el, con muelle amortiguado, y vuelven solas.

     El bucle solo corre cuando queda movimiento pendiente y la seccion esta
     a la vista. No hay animacion infinita de fondo.
     ------------------------------------------------------------------------ */

  var campo = document.querySelector('.campo-piezas');

  if (campo) {
    var COLUMNAS = 5;
    var FILAS = 7;
    var RADIO = 190;          /* alcance del puntero, en unidades del viewBox */
    var RIGIDEZ = 0.07;       /* muelle */
    var AMORTIGUA = 0.78;
    var HUECOS = [3, 9, 16, 22, 27, 31];  /* posiciones vacias, para dar aire */

    var VB = { w: 600, h: 760 };
    var piezas = [];
    var punteroActivo = false;
    var puntero = { x: 0, y: 0 };
    var idFrame = 0;
    var enPantalla = true;

    /* Ruido reproducible: el campo se ve igual en cada carga, no aleatorio */
    function pseudo(i, semilla) {
      var v = Math.sin(i * 12.9898 + semilla * 78.233) * 43758.5453;
      return v - Math.floor(v);
    }

    (function sembrar() {
      var pasoX = VB.w / (COLUMNAS + 1);
      var pasoY = VB.h / (FILAS + 1);
      var indice = 0;

      for (var f = 0; f < FILAS; f++) {
        for (var c = 0; c < COLUMNAS; c++) {
          indice++;
          if (HUECOS.indexOf(indice) > -1) continue;

          var jitterX = (pseudo(indice, 1) - 0.5) * pasoX * 0.5;
          var jitterY = (pseudo(indice, 2) - 0.5) * pasoY * 0.4;
          var x = pasoX * (c + 1) + jitterX;
          var y = pasoY * (f + 1) + jitterY;
          var escala = 0.09 + pseudo(indice, 3) * 0.055;

          var g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
          g.setAttribute('class', 'campo__pieza');
          var uso = document.createElementNS('http://www.w3.org/2000/svg', 'use');
          uso.setAttribute('href', '#pieza');
          g.appendChild(uso);
          campo.appendChild(g);

          piezas.push({
            el: g,
            x: x,
            y: y,
            escala: escala,
            /* Nacen alineadas, no desordenadas. Si el bucle nunca corre
               (pestana en segundo plano, rAF pausado, JS lento), el campo
               se ve igual de correcto: todas mirando al mismo sitio, que
               es justamente lo que la seccion afirma. */
            angulo: 0,
            objetivo: 0,
            velocidad: 0,
            despierta: false
          });
        }
      }
    })();

    function pintarPieza(p) {
      p.el.setAttribute(
        'transform',
        'translate(' + p.x.toFixed(2) + ',' + p.y.toFixed(2) + ') ' +
        'rotate(' + p.angulo.toFixed(2) + ') ' +
        'scale(' + p.escala.toFixed(4) + ')'
      );
    }

    function paso() {
      idFrame = 0;
      var quedaMovimiento = false;

      for (var i = 0; i < piezas.length; i++) {
        var p = piezas[i];
        var cerca = false;

        if (punteroActivo) {
          var dx = puntero.x - p.x;
          var dy = puntero.y - p.y;
          var dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < RADIO) {
            cerca = true;
            /* mismo criterio que la tuerca: cero grados apuntando arriba */
            p.objetivo = Math.atan2(dx, -dy) * 180 / Math.PI;
          }
        }

        if (!cerca) p.objetivo = 0;

        if (cerca !== p.despierta) {
          p.despierta = cerca;
          if (cerca) {
            p.el.setAttribute('data-despierta', 'true');
          } else {
            p.el.removeAttribute('data-despierta');
          }
        }

        /* por el camino corto, nunca dando la vuelta larga */
        var delta = (((p.objetivo - p.angulo) % 360) + 540) % 360 - 180;
        p.velocidad = (p.velocidad + delta * RIGIDEZ) * AMORTIGUA;
        p.angulo += p.velocidad;

        if (Math.abs(p.velocidad) > 0.05 || Math.abs(delta) > 0.3) {
          quedaMovimiento = true;
        }

        pintarPieza(p);
      }

      if ((quedaMovimiento || punteroActivo) && enPantalla) {
        idFrame = window.requestAnimationFrame(paso);
      }
    }

    function despertarBucle() {
      if (idFrame || !enPantalla) return;
      /* si el campo esta oculto por CSS, no hay nada que animar */
      if (!campo.getClientRects().length) return;
      idFrame = window.requestAnimationFrame(paso);
    }

    /* Si la pestana se va al fondo, el navegador congela el fotograma
       pendiente y el campo se queda a medias. Al volver se cancela el
       fotograma zombi y se reanuda. */
    document.addEventListener('visibilitychange', function () {
      if (document.visibilityState !== 'visible') return;
      if (idFrame) {
        window.cancelAnimationFrame(idFrame);
        idFrame = 0;
      }
      despertarBucle();
    });

    if (movimientoReducido.matches) {
      piezas.forEach(function (p) { p.angulo = 0; pintarPieza(p); });
    } else {
      var zona = campo.closest('.hero__campo');

      zona.style.pointerEvents = 'none';
      var hero = campo.closest('.hero');

      hero.addEventListener('pointermove', function (evento) {
        var caja = campo.getBoundingClientRect();
        if (!caja.width || !caja.height) return;
        puntero.x = ((evento.clientX - caja.left) / caja.width) * VB.w;
        puntero.y = ((evento.clientY - caja.top) / caja.height) * VB.h;
        punteroActivo = true;
        despertarBucle();
      });

      hero.addEventListener('pointerleave', function () {
        punteroActivo = false;
        despertarBucle();
      });

      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (entradas) {
          enPantalla = entradas[0].isIntersecting;
          if (enPantalla) despertarBucle();
        }, { threshold: 0 }).observe(campo);
      }

      piezas.forEach(pintarPieza);
      despertarBucle();
    }
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
     3.b Servicios: filas que se abren
     Uno abierto a la vez. El primero arranca abierto para que la seccion
     nunca se lea como una lista muerta de titulos.
     ------------------------------------------------------------------------ */

  var servicios = document.querySelectorAll('.servicio');

  if (servicios.length) {
    Array.prototype.forEach.call(servicios, function (servicio) {
      var boton = servicio.querySelector('.servicio__cabecera');

      boton.addEventListener('click', function () {
        var abierto = servicio.getAttribute('data-abierto') === 'true';

        Array.prototype.forEach.call(servicios, function (otro) {
          otro.removeAttribute('data-abierto');
          otro.querySelector('.servicio__cabecera').setAttribute('aria-expanded', 'false');
        });

        if (!abierto) {
          servicio.setAttribute('data-abierto', 'true');
          boton.setAttribute('aria-expanded', 'true');
        }
      });
    });
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
