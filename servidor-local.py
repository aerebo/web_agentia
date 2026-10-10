"""Servidor estatico de desarrollo para agentia, sin cache.

Arma el sitio con armar.py en cada peticion y sirve _sitio/. Rearmar es
barato (son cinco archivos de texto) y a cambio editas una pieza de
partes/, recargas, y lo ves: no hay paso manual que olvidar.

Solo para verificar en local. No forma parte del sitio ni se despliega.
"""
import functools
import http.server
import importlib
import pathlib
import socketserver

import armar

RAIZ = pathlib.Path(__file__).resolve().parent
SALIDA = RAIZ / "_sitio"
PUERTO = 5173


class SinCache(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # se rearma antes de servir el documento, no antes de cada imagen
        if "." not in self.path.rsplit("/", 1)[-1]:
            try:
                # Se recarga el modulo, no solo se le llama. Sin esto el
                # servidor se queda con el armar.py que leyo al arrancar:
                # editas la lista de paginas, recargas, y no pasa nada.
                # Las piezas de partes/ si se releen solas porque se abren
                # en cada pasada; el codigo del armador no.
                importlib.reload(armar)
                armar.armar()
            except Exception as error:
                self.send_error(500, "fallo al armar: %s" % error)
                return
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, formato, *args):
        pass


armar.armar()
socketserver.TCPServer.allow_reuse_address = True
manejador = functools.partial(SinCache, directory=str(SALIDA))

with socketserver.TCPServer(("127.0.0.1", PUERTO), manejador) as srv:
    print("sirviendo http://localhost:%d sin cache, rearmando en cada pagina" % PUERTO)
    srv.serve_forever()
