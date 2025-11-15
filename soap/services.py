from spyne import ServiceBase, rpc, Integer, Unicode, Array, Boolean, Double
from modelos import Dispositivo, Usuario
import database
from mysql.connector import Error
from spyne import Fault

class ApiService(ServiceBase):
    @rpc(Integer, Unicode, Unicode, _returns=Dispositivo)
    def crear_dispositivo(ctx, id_usuario, marca, numero_serie):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Dispositivos (id_usuario, marca, numero_serie) VALUES (%s, %s, %s)",
                (id_usuario, marca, numero_serie),
            )
            conn.commit()
            nuevo_id = cur.lastrowid
            cur.execute(
                "SELECT id_dispositivo, id_usuario, marca, numero_serie FROM Dispositivos WHERE id_dispositivo=%s",
                (nuevo_id,),
            )
            row = cur.fetchone()
            if not row:
                raise Fault(faultstring="No se pudo recuperar el dispositivo creado")
            d = Dispositivo()
            d.id_dispositivo = int(row[0])
            d.id_usuario = int(row[1])
            d.marca = row[2]
            d.numero_serie = row[3]
            return d
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass

    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, Double, Double, _returns=Usuario)
    def crear_usuario(ctx, nombre, apellidos, correo_electronico, fecha_de_nacimiento, genero, peso, altura):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO usuarios (`nombre(s)`, apellidos, correo_electronico, `Fecha_de_nacimiento`, `género`, peso, altura)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (nombre, apellidos, correo_electronico, fecha_de_nacimiento, genero, peso, altura),
            )
            conn.commit()
            nuevo_id = cur.lastrowid
            cur.execute(
                """
                SELECT id_usuario, `nombre(s)`, apellidos, correo_electronico, `Fecha_de_nacimiento`, `género`, peso, altura
                FROM usuarios WHERE id_usuario=%s
                """,
                (nuevo_id,),
            )
            row = cur.fetchone()
            if not row:
                raise Fault(faultstring="No se pudo recuperar el usuario creado")
            u = Usuario()
            u.id_usuario = int(row[0])
            u.nombre = row[1]
            u.apellido = row[2]
            u.correoElectronico = row[3]
            u.fechaDeNacimiento = row[4]
            u.genero = row[5]
            u.peso = float(row[6]) if row[6] is not None else None
            u.altura = float(row[7]) if row[7] is not None else None
            return u
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass

    @rpc(Integer, _returns=Dispositivo)
    def obtener_dispositivo(ctx, id_dispositivo):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT id_dispositivo, id_usuario, marca, numero_serie FROM Dispositivos WHERE id_dispositivo=%s",
                (id_dispositivo,),
            )
            row = cur.fetchone()
            if not row:
                raise Fault(faultstring="Dispositivo no encontrado")
            d = Dispositivo()
            d.id_dispositivo = int(row[0])
            d.id_usuario = int(row[1])
            d.marca = row[2]
            d.numero_serie = row[3]
            return d
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass

    @rpc(Integer, _returns=Array(Dispositivo))
    def listar_dispositivos_por_usuario(ctx, id_usuario):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT id_dispositivo, id_usuario, marca, numero_serie FROM Dispositivos WHERE id_usuario=%s",
                (id_usuario,),
            )
            dispositivos = []
            for row in cur.fetchall():
                d = Dispositivo()
                d.id_dispositivo = int(row[0])
                d.id_usuario = int(row[1])
                d.marca = row[2]
                d.numero_serie = row[3]
                dispositivos.append(d)
            return dispositivos
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass

    @rpc(Integer, Unicode, Unicode, _returns=Dispositivo)
    def actualizar_dispositivo(ctx, id_dispositivo, marca, numero_serie):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE Dispositivos SET marca=%s, numero_serie=%s WHERE id_dispositivo=%s",
                (marca, numero_serie, id_dispositivo),
            )
            if cur.rowcount == 0:
                raise Fault(faultstring="Dispositivo no encontrado")
            conn.commit()
            cur.execute(
                "SELECT id_dispositivo, id_usuario, marca, numero_serie FROM Dispositivos WHERE id_dispositivo=%s",
                (id_dispositivo,),
            )
            row = cur.fetchone()
            if not row:
                raise Fault(faultstring="No se pudo recuperar el dispositivo actualizado")
            d = Dispositivo()
            d.id_dispositivo = int(row[0])
            d.id_usuario = int(row[1])
            d.marca = row[2]
            d.numero_serie = row[3]
            return d
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass

    @rpc(Integer, _returns=Boolean)
    def eliminar_dispositivo(ctx, id_dispositivo):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Dispositivos WHERE id_dispositivo=%s",
                (id_dispositivo,),
            )
            eliminado = cur.rowcount > 0
            conn.commit()
            if not eliminado:
                raise Fault(faultstring="Dispositivo no encontrado")
            return True
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass