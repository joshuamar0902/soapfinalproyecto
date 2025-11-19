from spyne import ComplexModel, Unicode, Integer, Double, DateTime, Date, Array, Enum

class Usuario(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_usuario = Integer(min=1)
    nombre = Unicode(100, min_len=1)
    apellido = Unicode(100, min_len=1)
    correoElectronico = Unicode(150, min_len=1)
    fechaDeNacimiento = Date
    genero = Unicode(50, min_len=1)
    peso = Double(min=0)
    altura = Double(min=0)

class Dispositivo(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_dispositivo = Integer(min=1)
    id_usuario = Integer(min=1)
    marca = Unicode(100, min_len=1)
    numero_serie = Unicode(150, min_len=1)

class ActividadFisica(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_actividad = Integer(min=1)
    id_usuario = Integer(min=1)
    id_dispositivo = Integer(min=1)
    fecha_hora_inicio = DateTime
    fecha_hora_fin = DateTime
    km_recorridos = Double(min=0)
    calorias_quemadas = Double(min=0)
    frecuencia_cardiaca = Integer(min=0, max=300)
    oxigenacion = Integer(min=0, max=100)

class DatosSensor(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_dato = Integer(min=1)
    id_actividad = Integer(min=1)
    fecha_hora_registro = DateTime
    frecuencia_cardiaca = Integer(min=0, max=300)
    oxigenacion = Integer(min=0, max=100)
    presion = Unicode(255, min_len=1)

class ResumenActividad(ComplexModel):
    __namespace__ = 'iot.soap.model'
    fecha = Date
    total_km = Double(min=0)
    total_calorias = Double(min=0)
    promedio_frecuencia = Integer(min=0)
    promedio_oxigenacion = Integer(min=0)
    duracion_total_min = Double(min=0)

class DispositivoIot(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_dispositivo = Integer(min=1)
    modelo = Unicode(100, min_len=1)

class FrecuenciaCardiaca(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_frecuencia = Integer(min=1)
    id_actividad = Integer(min=1)
    fecha_hora_registro = DateTime
    frecuencia_cardiaca = Integer(min=0, max=300)
    oxigenacion = Integer(min=0, max=100)
    presion = Unicode(255, min_len=1)

class SesionEntrenamiento(ComplexModel):
    __namespace__ = 'iot.soap.model'
    id_sesion = Integer(min=1)
    id_usuario = Integer(min=1)
    TipoActividad = Enum('Correr','Caminar','Nadar','Ciclismo','Levantamiento_de_pesas','Yoga','Otro', type_name='TipoActividad')
    tipo_actividad = TipoActividad
    fecha_hora_inicio = DateTime
    fecha_hora_fin = DateTime
    duracion_segundos = Integer(min=0)
    distancia_metros = Double(min=0)
    calorias_quemadas = Integer(min=0)
    latitud_inicio = Double(min=-90, max=90)
    longitud_inicio = Double(min=-180, max=180)
    ritmo_promedio = Integer(min=0)