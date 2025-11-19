from spyne import ComplexModel, Unicode, Integer, Double, DateTime, Date, Array, Enum

class Usuario(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_usuario = Integer
    nombre = Unicode(100)
    apellido = Unicode(100)
    correoElectronico = Unicode(150)
    fechaDeNacimiento = Date
    genero = Unicode(50)
    peso = Double
    altura = Double

class Dispositivo(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_dispositivo = Integer
    id_usuario = Integer
    marca = Unicode(100)
    numero_serie = Unicode(150)

class ActividadFisica(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_actividad = Integer
    id_usuario = Integer
    id_dispositivo = Integer
    fecha_hora_inicio = DateTime
    fecha_hora_fin = DateTime
    km_recorridos = Double
    calorias_quemadas = Double
    frecuencia_cardiaca = Integer
    oxigenacion = Integer

class DatosSensor(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_dato = Integer
    id_actividad = Integer
    fecha_hora_registro = DateTime
    frecuencia_cardiaca = Integer
    oxigenacion = Integer
    presion = Unicode(255)

class ResumenActividad(ComplexModel):
    __namespace__ = 'iot.soap.model'
    fecha = Date
    total_km = Double
    total_calorias = Double
    promedio_frecuencia = Integer
    promedio_oxigenacion = Integer
    duracion_total_min = Double

class DispositivoIot(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_dispositivo = Integer
    modelo = Unicode(100)

class FrecuenciaCardiaca(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_frecuencia = Integer
    id_actividad = Integer
    fecha_hora_registro = DateTime
    frecuencia_cardiaca = Integer
    oxigenacion = Integer
    presion = Unicode(255)

class SesionEntrenamiento(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_sesion = Integer
    id_usuario = Integer
    TipoActividad = Enum('Correr','Caminar','Nadar','Ciclismo','Levantamiento_de_pesas','Yoga','Otro', type_name='TipoActividad')
    tipo_actividad = TipoActividad
    fecha_hora_inicio = DateTime
    fecha_hora_fin = DateTime
    duracion_segundos = Integer
    distancia_metros = Double
    calorias_quemadas = Integer
    latitud_inicio = Double
    longitud_inicio = Double
    ritmo_promedio = Integer