from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from services import ApiService
import database

application = Application([
    ApiService
], 'iot.soap',
   in_protocol=Soap11(), out_protocol=Soap11())

def main():
    database.crear_tablas()
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, WsgiApplication(application))
    print("Api corriendo http://localhost:8000")
    server.serve_forever()

if __name__ == "__main__":
    main()
