from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
# Asegúrate de que tienes el archivo services.py creado con la clase ApiService
from services import ApiService
import os
import database # Este importa tu archivo anterior con la conexión

application = Application([
    ApiService
], 'iot.soap',
   in_protocol=Soap11(), out_protocol=Soap11())

def main():
    # --- CAMBIO AQUÍ ---
    # He comentado el "if" para forzar la creación de tablas ahora mismo.
    # Así verificamos que la conexión a Railway funciona al ejecutar.
    print("Verificando conexión y tablas en Railway...")
    database.crear_tablas()
    # -------------------

    from wsgiref.simple_server import make_server
    # 0.0.0.0 permite que sea visible en tu red local si fuera necesario
    server = make_server('0.0.0.0', 8000, WsgiApplication(application))

    print("Api corriendo en http://localhost:8000")
    print("WSDL disponible en http://localhost:8000/?wsdl")
    server.serve_forever()

if __name__ == "__main__":
    main()