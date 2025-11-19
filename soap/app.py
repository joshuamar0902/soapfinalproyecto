from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from services import ApiService
import os
import database

application = Application([
    ApiService
], 'iot.soap',
   in_protocol=Soap11(), out_protocol=Soap11())

def main():

    print("Verificando conexión y tablas en Railway...")
    database.crear_tablas()
    # -------------------

    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, WsgiApplication(application))

    print("Api corriendo en http://localhost:8000")
    print("WSDL disponible en http://localhost:8000/?wsdl")
    server.serve_forever()

if __name__ == "__main__":
    main()