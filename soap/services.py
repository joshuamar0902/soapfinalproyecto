from spyne import ServiceBase, rpc, Integer, Unicode, Array, Boolean, Double
from modelos import Dispositivo, Usuario, ActividadFisica, DatosSensor, ResumenActividad
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

    @rpc(_returns=Array(Dispositivo))
    def listar_dispositivos(ctx):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT id_dispositivo, id_usuario, marca, numero_serie FROM Dispositivos"
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

    @rpc(_returns=Array(Usuario))
    def listar_usuarios(ctx):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT id_usuario, `nombre(s)`, apellidos, correo_electronico, `Fecha_de_nacimiento`, `género`, peso, altura
                FROM usuarios
                """
            )
            usuarios = []
            for row in cur.fetchall():
                u = Usuario()
                u.id_usuario = int(row[0])
                u.nombre = row[1]
                u.apellido = row[2]
                u.correoElectronico = row[3]
                u.fechaDeNacimiento = row[4]
                u.genero = row[5]
                u.peso = float(row[6]) if row[6] is not None else None
                u.altura = float(row[7]) if row[7] is not None else None
                usuarios.append(u)
            return usuarios
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass

    @rpc(Integer, Integer, Unicode, Unicode, Double, Double, Integer, Integer, _returns=ActividadFisica)
    def crear_actividad(ctx, id_usuario, id_dispositivo, fecha_hora_inicio, fecha_hora_fin, km_recorridos, calorias_quemadas, frecuencia_cardiaca, oxigenacion):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO Actividad_Fisica (id_usuario, id_dispositivo, fecha_hora_inicio, fecha_hora_fin, km_recorridos, calorias_quemadas, frecuencia_cardiaca, oxigenacion)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (id_usuario, id_dispositivo, fecha_hora_inicio, fecha_hora_fin, km_recorridos, calorias_quemadas, frecuencia_cardiaca, oxigenacion),
            )
            conn.commit()
            nuevo_id = cur.lastrowid
            cur.execute(
                """
                SELECT id_actividad, id_usuario, id_dispositivo, fecha_hora_inicio, fecha_hora_fin, km_recorridos, calorias_quemadas, frecuencia_cardiaca, oxigenacion
                FROM Actividad_Fisica WHERE id_actividad=%s
                """,
                (nuevo_id,),
            )
            row = cur.fetchone()
            a = ActividadFisica()
            a.id_actividad = int(row[0])
            a.id_usuario = int(row[1])
            a.id_dispositivo = int(row[2])
            a.fecha_hora_inicio = row[3]
            a.fecha_hora_fin = row[4]
            a.km_recorridos = float(row[5]) if row[5] is not None else None
            a.calorias_quemadas = float(row[6]) if row[6] is not None else None
            a.frecuencia_cardiaca = int(row[7]) if row[7] is not None else None
            a.oxigenacion = int(row[8]) if row[8] is not None else None
            return a
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass

    @rpc(Integer, Unicode, Unicode, _returns=Array(ActividadFisica))
    def listar_actividades_por_usuario(ctx, id_usuario, fecha_inicio, fecha_fin):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT id_actividad, id_usuario, id_dispositivo, fecha_hora_inicio, fecha_hora_fin, km_recorridos, calorias_quemadas, frecuencia_cardiaca, oxigenacion
                FROM Actividad_Fisica
                WHERE id_usuario=%s AND fecha_hora_inicio BETWEEN %s AND %s
                ORDER BY fecha_hora_inicio
                """,
                (id_usuario, fecha_inicio, fecha_fin),
            )
            actividades = []
            for row in cur.fetchall():
                a = ActividadFisica()
                a.id_actividad = int(row[0])
                a.id_usuario = int(row[1])
                a.id_dispositivo = int(row[2])
                a.fecha_hora_inicio = row[3]
                a.fecha_hora_fin = row[4]
                a.km_recorridos = float(row[5]) if row[5] is not None else None
                a.calorias_quemadas = float(row[6]) if row[6] is not None else None
                a.frecuencia_cardiaca = int(row[7]) if row[7] is not None else None
                a.oxigenacion = int(row[8]) if row[8] is not None else None
                actividades.append(a)
            return actividades
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass

    @rpc(Integer, Unicode, _returns=ResumenActividad)
    def resumen_diario_usuario(ctx, id_usuario, fecha):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT IFNULL(SUM(km_recorridos),0), IFNULL(SUM(calorias_quemadas),0),
                       IFNULL(SUM(TIMESTAMPDIFF(MINUTE, fecha_hora_inicio, fecha_hora_fin)),0)
                FROM Actividad_Fisica
                WHERE id_usuario=%s AND DATE(fecha_hora_inicio)=%s
                """,
                (id_usuario, fecha),
            )
            km, cal, mins = cur.fetchone()
            cur.execute(
                """
                SELECT IFNULL(AVG(ds.frecuencia_cardiaca),0), IFNULL(AVG(ds.oxigenacion),0)
                FROM Datos_Sensores ds
                JOIN Actividad_Fisica af ON af.id_actividad=ds.id_actividad
                WHERE af.id_usuario=%s AND DATE(ds.fecha_hora_registro)=%s
                """,
                (id_usuario, fecha),
            )
            prom_fc, prom_oxi = cur.fetchone()
            r = ResumenActividad()
            r.fecha = fecha
            r.total_km = float(km)
            r.total_calorias = float(cal)
            r.duracion_total_min = float(mins)
            r.promedio_frecuencia = int(prom_fc) if prom_fc is not None else 0
            r.promedio_oxigenacion = int(prom_oxi) if prom_oxi is not None else 0
            return r
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass

    @rpc(Integer, Integer, Unicode, Integer, Integer, Unicode, _returns=DatosSensor)
    def registrar_dato_sensor(ctx, id_actividad, id_usuario, fecha_hora_registro, frecuencia_cardiaca, oxigenacion, presion):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT 1 FROM Actividad_Fisica WHERE id_actividad=%s AND id_usuario=%s",
                (id_actividad, id_usuario),
            )
            if cur.fetchone() is None:
                raise Fault(faultstring="Actividad no pertenece al usuario")
            cur.execute(
                """
                INSERT INTO Datos_Sensores (id_actividad, fecha_hora_registro, frecuencia_cardiaca, oxigenacion, presion)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (id_actividad, fecha_hora_registro, frecuencia_cardiaca, oxigenacion, presion),
            )
            conn.commit()
            nuevo_id = cur.lastrowid
            cur.execute(
                "SELECT id_dato, id_actividad, fecha_hora_registro, frecuencia_cardiaca, oxigenacion, presion FROM Datos_Sensores WHERE id_dato=%s",
                (nuevo_id,),
            )
            row = cur.fetchone()
            d = DatosSensor()
            d.id_dato = int(row[0])
            d.id_actividad = int(row[1])
            d.fecha_hora_registro = row[2]
            d.frecuencia_cardiaca = int(row[3]) if row[3] is not None else None
            d.oxigenacion = int(row[4]) if row[4] is not None else None
            d.presion = row[5]
            return d
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass

    @rpc(Integer, Unicode, _returns=Array(DatosSensor))
    def listar_frecuencia_cardiaca_usuario(ctx, id_usuario, fecha):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión a la base de datos")
        try:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT ds.id_dato, ds.id_actividad, ds.fecha_hora_registro, ds.frecuencia_cardiaca, ds.oxigenacion, ds.presion
                FROM Datos_Sensores ds
                JOIN Actividad_Fisica af ON af.id_actividad=ds.id_actividad
                WHERE af.id_usuario=%s AND DATE(ds.fecha_hora_registro)=%s
                ORDER BY ds.fecha_hora_registro
                """,
                (id_usuario, fecha),
            )
            datos = []
            for row in cur.fetchall():
                d = DatosSensor()
                d.id_dato = int(row[0])
                d.id_actividad = int(row[1])
                d.fecha_hora_registro = row[2]
                d.frecuencia_cardiaca = int(row[3]) if row[3] is not None else None
                d.oxigenacion = int(row[4]) if row[4] is not None else None
                d.presion = row[5]
                datos.append(d)
            return datos
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            try:
                conn.close()
            except Exception:
                pass