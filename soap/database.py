import mysql.connector
from mysql.connector import Error, errorcode, ClientFlag
import os

def conectar():

    host = 'trolley.proxy.rlwy.net'
    port = 20152
    user = 'root'
    password = 'jmEAeVbihCZbTBRjfxxINhnmuDoJtHFD'
    database = 'railway'

    print(f"Conectando a: {host}:{port} con usuario {user}...")

    try:
        kwargs = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'database': database,
        }

        conn = mysql.connector.connect(**kwargs)
        print("¡Conexión EXITOSA!")
        return conn
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def crear_tablas():
    conn = conectar()
    if conn is None:
        return

    cur = conn.cursor()

    # 1. USUARIOS
    cur.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario BIGINT PRIMARY KEY AUTO_INCREMENT,
        `nombre(s)` VARCHAR(100) NOT NULL,
        apellidos VARCHAR(100) NOT NULL,
        correo_electronico VARCHAR(150) NOT NULL UNIQUE,
        `Fecha_de_nacimiento` DATE NOT NULL,
        `género` VARCHAR(50) NOT NULL,
        peso DOUBLE,
        altura DOUBLE
    ) ENGINE=InnoDB;''')

    # 2. DISPOSITIVOS
    cur.execute('''CREATE TABLE IF NOT EXISTS Dispositivos (
        id_dispositivo BIGINT PRIMARY KEY AUTO_INCREMENT,
        id_usuario BIGINT NOT NULL,
        marca VARCHAR(100) NOT NULL,
        numero_serie VARCHAR(150) NOT NULL UNIQUE,
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario)
    ) ENGINE=InnoDB;''')

    # 3. DISPOSITIVOS IOT
    cur.execute('''CREATE TABLE IF NOT EXISTS dispositivos_iot (
        id_dispositivo BIGINT PRIMARY KEY AUTO_INCREMENT,
        modelo VARCHAR(100) NOT NULL
    ) ENGINE=InnoDB;''')

    # 4. ACTIVIDAD FISICA
    cur.execute('''CREATE TABLE IF NOT EXISTS Actividad_Fisica (
        id_actividad BIGINT PRIMARY KEY AUTO_INCREMENT,
        id_usuario BIGINT NOT NULL,
        id_dispositivo BIGINT NOT NULL,
        fecha_hora_inicio DATETIME NOT NULL,
        fecha_hora_fin DATETIME NOT NULL,
        km_recorridos DOUBLE,
        calorias_quemadas DOUBLE,
        frecuencia_cardiaca INTEGER,
        oxigenacion INTEGER,
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
        FOREIGN KEY(id_dispositivo) REFERENCES Dispositivos(id_dispositivo)
    ) ENGINE=InnoDB;''')

    # 5. DATOS SENSORES
    cur.execute('''CREATE TABLE IF NOT EXISTS Datos_Sensores (
        id_dato BIGINT PRIMARY KEY AUTO_INCREMENT,
        id_actividad BIGINT NOT NULL,
        fecha_hora_registro DATETIME NOT NULL,
        frecuencia_cardiaca INTEGER,
        oxigenacion INTEGER,
        presion VARCHAR(255),
        FOREIGN KEY(id_actividad) REFERENCES Actividad_Fisica(id_actividad)
    ) ENGINE=InnoDB;''')

    # 6. SESIONES
    cur.execute('''CREATE TABLE IF NOT EXISTS Sesiones_Entrenamiento (
        id_sesion BIGINT PRIMARY KEY AUTO_INCREMENT,
        id_usuario BIGINT NOT NULL,
        tipo_actividad VARCHAR(100),
        fecha_hora_inicio DATETIME,
        fecha_hora_fin DATETIME,
        duracion_segundos INTEGER,
        distancia_metros DOUBLE,
        calorias_quemadas INTEGER,
        latitud_inicio DOUBLE,
        longitud_inicio DOUBLE,
        ritmo_promedio INTEGER,
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario)
    ) ENGINE=InnoDB;''')

    # 7. FRECUENCIA
    cur.execute('''CREATE TABLE IF NOT EXISTS frecuencia_cardiaca (
        id_frecuencia BIGINT PRIMARY KEY AUTO_INCREMENT,
        id_actividad BIGINT NOT NULL,
        fecha_hora_registro DATETIME NOT NULL,
        frecuencia_cardiaca INTEGER,
        oxigenacion INTEGER,
        presion VARCHAR(255),
        FOREIGN KEY(id_actividad) REFERENCES Sesiones_Entrenamiento(id_sesion)
    ) ENGINE=InnoDB;''')

    print("Tablas verificadas/creadas correctamente.")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_tablas()