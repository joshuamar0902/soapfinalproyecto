from spyne import ServiceBase, rpc, Integer, Unicode, Array, Boolean, Double, Date, DateTime
# Asegúrate de importar TODOS los modelos
from modelos import Dispositivo, Usuario, ActividadFisica, DatosSensor, ResumenActividad, DispositivoIot, FrecuenciaCardiaca, SesionEntrenamiento
import database
from mysql.connector import Error
from spyne import Fault

class ApiService(ServiceBase):

    # ---------------------------------------------------------
    # GESTIÓN DE DISPOSITIVOS DE USUARIO (Tabla 'Dispositivos')
    # ---------------------------------------------------------
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
            if conn: conn.close()

    @rpc(Integer, _returns=Dispositivo)
    def obtener_dispositivo(ctx, id_dispositivo):
        conn = database.conectar()
        if conn is None:
            raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("SELECT id_dispositivo, id_usuario, marca, numero_serie FROM Dispositivos WHERE id_dispositivo=%s", (id_dispositivo,))
            row = cur.fetchone()
            if not row: raise Fault(faultstring="Dispositivo no encontrado")
            d = Dispositivo()
            d.id_dispositivo = int(row[0]); d.id_usuario = int(row[1]); d.marca = row[2]; d.numero_serie = row[3]
            return d
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    @rpc(Integer, _returns=Array(Dispositivo))
    def listar_dispositivos_por_usuario(ctx, id_usuario):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("SELECT id_dispositivo, id_usuario, marca, numero_serie FROM Dispositivos WHERE id_usuario=%s", (id_usuario,))
            lista = []
            for row in cur.fetchall():
                d = Dispositivo()
                d.id_dispositivo = int(row[0]); d.id_usuario = int(row[1]); d.marca = row[2]; d.numero_serie = row[3]
                lista.append(d)
            return lista
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    @rpc(_returns=Array(Dispositivo))
    def listar_dispositivos(ctx):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("SELECT id_dispositivo, id_usuario, marca, numero_serie FROM Dispositivos")
            lista = []
            for row in cur.fetchall():
                d = Dispositivo()
                d.id_dispositivo = int(row[0]); d.id_usuario = int(row[1]); d.marca = row[2]; d.numero_serie = row[3]
                lista.append(d)
            return lista
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    @rpc(Integer, Unicode, Unicode, _returns=Dispositivo)
    def actualizar_dispositivo(ctx, id_dispositivo, marca, numero_serie):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("UPDATE Dispositivos SET marca=%s, numero_serie=%s WHERE id_dispositivo=%s", (marca, numero_serie, id_dispositivo))
            conn.commit()
            return ApiService.obtener_dispositivo(ctx, id_dispositivo)
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    @rpc(Integer, _returns=Boolean)
    def eliminar_dispositivo(ctx, id_dispositivo):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM Dispositivos WHERE id_dispositivo=%s", (id_dispositivo,))
            eliminado = cur.rowcount > 0
            conn.commit()
            if not eliminado: raise Fault(faultstring="Dispositivo no encontrado")
            return True
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    # ---------------------------------------------------------
    # GESTIÓN DE USUARIOS (Lectura SOAP de la tabla 'usuarios')
    # ---------------------------------------------------------
    @rpc(_returns=Array(Usuario))
    def listar_usuarios(ctx):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("SELECT id_usuario, `nombre(s)`, apellidos, correo_electronico, `Fecha_de_nacimiento`, `género`, peso, altura FROM usuarios")
            lista = []
            for row in cur.fetchall():
                u = Usuario()
                u.id_usuario = int(row[0]); u.nombre = row[1]; u.apellido = row[2]; u.correoElectronico = row[3]
                u.fechaDeNacimiento = row[4]; u.genero = row[5]
                u.peso = float(row[6]) if row[6] else None; u.altura = float(row[7]) if row[7] else None
                lista.append(u)
            return lista
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    # ---------------------------------------------------------
    # GESTIÓN DE DISPOSITIVOS IOT (CATÁLOGO) (Tabla 'dispositivos_iot')
    # ---------------------------------------------------------
    @rpc(Unicode, _returns=DispositivoIot)
    def crear_dispositivo_iot(ctx, modelo):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO dispositivos_iot (modelo) VALUES (%s)", (modelo,))
            conn.commit()
            nuevo_id = cur.lastrowid
            cur.execute("SELECT id_dispositivo, modelo FROM dispositivos_iot WHERE id_dispositivo=%s", (nuevo_id,))
            row = cur.fetchone()
            d = DispositivoIot()
            d.id_dispositivo = int(row[0]); d.modelo = row[1]
            return d
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    @rpc(_returns=Array(DispositivoIot))
    def listar_dispositivos_iot(ctx):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("SELECT id_dispositivo, modelo FROM dispositivos_iot")
            lista = []
            for row in cur.fetchall():
                d = DispositivoIot()
                d.id_dispositivo = int(row[0]); d.modelo = row[1]
                lista.append(d)
            return lista
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    # ---------------------------------------------------------
    # GESTIÓN DE SESIONES DE ENTRENAMIENTO
    # ---------------------------------------------------------
    @rpc(Integer, Unicode, Unicode, Unicode, Integer, Double, Integer, Double, Double, Integer, _returns=SesionEntrenamiento)
    def crear_sesion(ctx, id_usuario, tipo_actividad, fecha_hora_inicio, fecha_hora_fin, duracion_segundos, distancia_metros, calorias_quemadas, latitud_inicio, longitud_inicio, ritmo_promedio):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO Sesiones_Entrenamiento (id_usuario, tipo_actividad, fecha_hora_inicio, fecha_hora_fin, duracion_segundos, distancia_metros, calorias_quemadas, latitud_inicio, longitud_inicio, ritmo_promedio)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (id_usuario, tipo_actividad, fecha_hora_inicio, fecha_hora_fin, duracion_segundos, distancia_metros, calorias_quemadas, latitud_inicio, longitud_inicio, ritmo_promedio))
            conn.commit()
            nid = cur.lastrowid
            # Retornamos el objeto creado (simplificado)
            s = SesionEntrenamiento()
            s.id_sesion = nid
            s.id_usuario = id_usuario
            s.tipo_actividad = tipo_actividad
            return s
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    @rpc(Integer, Unicode, Unicode, _returns=Array(SesionEntrenamiento))
    def listar_sesiones_por_usuario(ctx, id_usuario, fecha_inicio, fecha_fin):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT id_sesion, id_usuario, tipo_actividad, fecha_hora_inicio, fecha_hora_fin, duracion_segundos, distancia_metros, calorias_quemadas
                FROM Sesiones_Entrenamiento
                WHERE id_usuario=%s AND fecha_hora_inicio BETWEEN %s AND %s
                """, (id_usuario, fecha_inicio, fecha_fin))
            lista = []
            for row in cur.fetchall():
                s = SesionEntrenamiento()
                s.id_sesion = int(row[0]); s.id_usuario = int(row[1]); s.tipo_actividad = row[2]
                s.fecha_hora_inicio = row[3]; s.fecha_hora_fin = row[4]
                s.duracion_segundos = row[5]; s.distancia_metros = row[6]; s.calorias_quemadas = row[7]
                lista.append(s)
            return lista
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    # ---------------------------------------------------------
    # ACTIVIDAD FÍSICA Y SENSORES (LEGACY SOAP)
    # ---------------------------------------------------------
    @rpc(Integer, Integer, Unicode, Unicode, Double, Double, Integer, Integer, _returns=ActividadFisica)
    def crear_actividad(ctx, id_usuario, id_dispositivo, fecha_hora_inicio, fecha_hora_fin, km_recorridos, calorias_quemadas, frecuencia_cardiaca, oxigenacion):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO Actividad_Fisica (id_usuario, id_dispositivo, fecha_hora_inicio, fecha_hora_fin, km_recorridos, calorias_quemadas, frecuencia_cardiaca, oxigenacion)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (id_usuario, id_dispositivo, fecha_hora_inicio, fecha_hora_fin, km_recorridos, calorias_quemadas, frecuencia_cardiaca, oxigenacion))
            conn.commit()
            nuevo_id = cur.lastrowid
            cur.execute("SELECT id_actividad, id_usuario, id_dispositivo, fecha_hora_inicio, fecha_hora_fin FROM Actividad_Fisica WHERE id_actividad=%s", (nuevo_id,))
            row = cur.fetchone()
            a = ActividadFisica()
            a.id_actividad = int(row[0]); a.id_usuario = int(row[1]); a.id_dispositivo = int(row[2])
            a.fecha_hora_inicio = row[3]; a.fecha_hora_fin = row[4]
            return a
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    @rpc(Integer, Integer, Unicode, Integer, Integer, Unicode, _returns=DatosSensor)
    def registrar_dato_sensor(ctx, id_actividad, id_usuario, fecha_hora_registro, frecuencia_cardiaca, oxigenacion, presion):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            # Validación de propiedad
            cur.execute("SELECT 1 FROM Actividad_Fisica WHERE id_actividad=%s AND id_usuario=%s", (id_actividad, id_usuario))
            if not cur.fetchone(): raise Fault(faultstring="Actividad no pertenece al usuario")

            cur.execute("""
                INSERT INTO Datos_Sensores (id_actividad, fecha_hora_registro, frecuencia_cardiaca, oxigenacion, presion)
                VALUES (%s, %s, %s, %s, %s)
                """, (id_actividad, fecha_hora_registro, frecuencia_cardiaca, oxigenacion, presion))
            conn.commit()
            nid = cur.lastrowid
            d = DatosSensor()
            d.id_dato = nid; d.id_actividad = id_actividad; d.frecuencia_cardiaca = frecuencia_cardiaca
            return d
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()

    @rpc(Integer, Unicode, _returns=ResumenActividad)
    def resumen_diario_usuario(ctx, id_usuario, fecha):
        conn = database.conectar()
        if conn is None: raise Fault(faultstring="Error de conexión")
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT IFNULL(SUM(km_recorridos),0), IFNULL(SUM(calorias_quemadas),0),
                       IFNULL(SUM(TIMESTAMPDIFF(MINUTE, fecha_hora_inicio, fecha_hora_fin)),0)
                FROM Actividad_Fisica
                WHERE id_usuario=%s AND DATE(fecha_hora_inicio)=%s
                """, (id_usuario, fecha))
            km, cal, mins = cur.fetchone()

            # Promedios de sensores
            cur.execute("""
                SELECT IFNULL(AVG(ds.frecuencia_cardiaca),0), IFNULL(AVG(ds.oxigenacion),0)
                FROM Datos_Sensores ds
                JOIN Actividad_Fisica af ON af.id_actividad=ds.id_actividad
                WHERE af.id_usuario=%s AND DATE(ds.fecha_hora_registro)=%s
                """, (id_usuario, fecha))
            prom_fc, prom_oxi = cur.fetchone()

            r = ResumenActividad()
            r.fecha = fecha
            r.total_km = float(km); r.total_calorias = float(cal); r.duracion_total_min = float(mins)
            r.promedio_frecuencia = int(prom_fc); r.promedio_oxigenacion = int(prom_oxi)
            return r
        except Error as e:
            raise Fault(faultstring=str(e))
        finally:
            if conn: conn.close()