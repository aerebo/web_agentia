"""Servidor estatico de desarrollo para agentia, sin cache.

Solo para verificar en local. No forma parte del sitio ni se despliega.
"""
import functools
import http.server
import pathlib
import socketserver

# la carpeta donde vive este archivo, sirve igual en Windows, macOS y Linux
RAIZ = str(pathlib.Path(__file__).resolve().parent)
PUERTO = 5173


class SinCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, formato, *args):
        pass


socketserver.TCPServer.allow_reuse_address = True
manejador = functools.partial(SinCache, directory=RAIZ)

with socketserver.TCPServer(("127.0.0.1", PUERTO), manejador) as srv:
    print("sirviendo %s en http://localhost:%d sin cache" % (RAIZ, PUERTO))
    srv.serve_forever()
