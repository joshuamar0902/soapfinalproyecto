import mysql.connector
from mysql.connector import Error, errorcode
import datetime

def conectar():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            database='iotsoap'
        )
        return conn
    except Error as e:
        if getattr(e, 'errno', None) == errorcode.ER_BAD_DB_ERROR:
            tmp = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='root'
            )
            cur = tmp.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS iotsoap CHARACTER SET utf8mb4")
            tmp.commit()
            tmp.close()
            conn = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='root',
                database='iotsoap'
            )
            return conn
        print(f"Error al conectar a MySQL: {e}")
        return None

def crear_tablas():
    conn = conectar()
    if conn is None:
        return

    cur = conn.cursor()

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

    cur.execute('''CREATE TABLE IF NOT EXISTS Dispositivos (
        id_dispositivo BIGINT PRIMARY KEY AUTO_INCREMENT,
        id_usuario BIGINT NOT NULL,
        marca VARCHAR(100) NOT NULL,
        numero_serie VARCHAR(150) NOT NULL UNIQUE,
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario)
    ) ENGINE=InnoDB;''')

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

    cur.execute('''CREATE TABLE IF NOT EXISTS Datos_Sensores (
        id_dato BIGINT PRIMARY KEY AUTO_INCREMENT,
        id_actividad BIGINT NOT NULL,
        fecha_hora_registro DATETIME NOT NULL,
        frecuencia_cardiaca INTEGER,
        oxigenacion INTEGER,
        presion VARCHAR(255),
        FOREIGN KEY(id_actividad) REFERENCES Actividad_Fisica(id_actividad)
    ) ENGINE=InnoDB;''')

    print("Tablas creadas/verificadas exitosamente.")
    conn.commit()
    conn.close()