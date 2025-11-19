
# Plataforma IoT con Servicios SOAP y REST

# Luis Gabriel Venegas Saucedo 
# Joshua Neftali Marin Leynez

Modelos principales

- Usuario: `id_usuario`, `nombre`, `apellido`, `correoElectronico`, `fechaDeNacimiento`, `genero`, `peso`, `altura`
- Dispositivo: `id_dispositivo`, `id_usuario`, `marca`, `numero_serie`
- ActividadFisica: `id_actividad`, `id_usuario`, `id_dispositivo`, `fecha_hora_inicio`, `fecha_hora_fin`, `km_recorridos`, `calorias_quemadas`, `frecuencia_cardiaca`, `oxigenacion`
- DatosSensor: `id_dato`, `id_actividad`, `fecha_hora_registro`, `frecuencia_cardiaca`, `oxigenacion`, `presion`
- ResumenActividad: `fecha`, `total_km`, `total_calorias`, `promedio_frecuencia`, `promedio_oxigenacion`, `duracion_total_min`

## Usuarios

### crear_usuario

- Descripción: Crea un usuario.
- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:crear_usuario>
      <iot:nombre>Juan</iot:nombre>
      <iot:apellidos>Pérez</iot:apellidos>
      <iot:correo_electronico>juan@example.com</iot:correo_electronico>
      <iot:fecha_de_nacimiento>1990-01-01</iot:fecha_de_nacimiento>
      <iot:genero>Masculino</iot:genero>
      <iot:peso>70</iot:peso>
      <iot:altura>1.75</iot:altura>
    </iot:crear_usuario>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `Usuario`

### listar_usuarios

- Descripción: Devuelve todos los usuarios.
- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:listar_usuarios/>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `Array(Usuario)`

## Dispositivos

### crear_dispositivo

- Descripción: Crea un dispositivo asociado a un usuario.
- Requiere: `id_usuario` existente.
- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:crear_dispositivo>
      <iot:id_usuario>1</iot:id_usuario>
      <iot:marca>Garmin</iot:marca>
      <iot:numero_serie>ABC123</iot:numero_serie>
    </iot:crear_dispositivo>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `Dispositivo`

### obtener_dispositivo

- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:obtener_dispositivo>
      <iot:id_dispositivo>10</iot:id_dispositivo>
    </iot:obtener_dispositivo>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `Dispositivo`

### listar_dispositivos_por_usuario

- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:listar_dispositivos_por_usuario>
      <iot:id_usuario>1</iot:id_usuario>
    </iot:listar_dispositivos_por_usuario>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `Array(Dispositivo)`

### listar_dispositivos

- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:listar_dispositivos/>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `Array(Dispositivo)`

### actualizar_dispositivo

- Descripción: Actualiza `marca` y `numero_serie`.
- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:actualizar_dispositivo>
      <iot:id_dispositivo>10</iot:id_dispositivo>
      <iot:marca>Polar</iot:marca>
      <iot:numero_serie>XYZ789</iot:numero_serie>
    </iot:actualizar_dispositivo>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `Dispositivo`

### eliminar_dispositivo

- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:eliminar_dispositivo>
      <iot:id_dispositivo>10</iot:id_dispositivo>
    </iot:eliminar_dispositivo>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `Boolean`

## Actividad Física

### crear_actividad

- Descripción: Crea una sesión de actividad para un usuario y dispositivo.
- Requiere: `id_usuario` y `id_dispositivo` válidos.
- Tipos de fecha: `fecha_hora_inicio` y `fecha_hora_fin` en ISO8601.
- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:crear_actividad>
      <iot:id_usuario>1</iot:id_usuario>
      <iot:id_dispositivo>10</iot:id_dispositivo>
      <iot:fecha_hora_inicio>2025-11-18T07:00:00</iot:fecha_hora_inicio>
      <iot:fecha_hora_fin>2025-11-18T07:45:00</iot:fecha_hora_fin>
      <iot:km_recorridos>5.2</iot:km_recorridos>
      <iot:calorias_quemadas>420</iot:calorias_quemadas>
      <iot:frecuencia_cardiaca>138</iot:frecuencia_cardiaca>
      <iot:oxigenacion>97</iot:oxigenacion>
    </iot:crear_actividad>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `ActividadFisica`

### listar_actividades_por_usuario

- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:listar_actividades_por_usuario>
      <iot:id_usuario>1</iot:id_usuario>
      <iot:fecha_inicio>2025-11-18T00:00:00</iot:fecha_inicio>
      <iot:fecha_fin>2025-11-18T23:59:59</iot:fecha_fin>
    </iot:listar_actividades_por_usuario>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `Array(ActividadFisica)`

### resumen_diario_usuario

- Descripción: Devuelve totals y promedios del día para el usuario.
- Cálculos: `SUM(km/calorías)`, `SUM(duración_min)`, `AVG(frecuencia/oxigenación)`.
- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:resumen_diario_usuario>
      <iot:id_usuario>1</iot:id_usuario>
      <iot:fecha>2025-11-18</iot:fecha>
    </iot:resumen_diario_usuario>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `ResumenActividad`

## Datos de Sensores

### registrar_dato_sensor

- Descripción: Registra una muestra de sensor para una actividad del usuario.
- Valida que la actividad pertenece al usuario.
- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:registrar_dato_sensor>
      <iot:id_actividad>5</iot:id_actividad>
      <iot:id_usuario>1</iot:id_usuario>
      <iot:fecha_hora_registro>2025-11-18T07:30:00</iot:fecha_hora_registro>
      <iot:frecuencia_cardiaca>92</iot:frecuencia_cardiaca>
      <iot:oxigenacion>98</iot:oxigenacion>
      <iot:presion>120/80</iot:presion>
    </iot:registrar_dato_sensor>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `DatosSensor`

### listar_frecuencia_cardiaca_usuario

- Descripción: Lista muestras de frecuencia cardiaca del usuario para una fecha.
- Request Body (XML)

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
  <soapenv:Body>
    <iot:listar_frecuencia_cardiaca_usuario>
      <iot:id_usuario>1</iot:id_usuario>
      <iot:fecha>2025-11-18</iot:fecha>
    </iot:listar_frecuencia_cardiaca_usuario>
  </soapenv:Body>
</soapenv:Envelope>
```

- Response: `Array(DatosSensor)`

## Errores

- Los errores se devuelven como `<soap:Fault>` con `faultstring` descriptivo.
- Casos comunes:
  - FK inválida (`1452`): usuario o dispositivo inexistente.
  - Duplicado (`1062`): `numero_serie` repetido.
  - Actividad no pertenece al usuario al registrar datos.
  - Conexión fallida: revisa variables de entorno de Railway y TLS.

## Pruebas rápidas en Postman

- Importa el WSDL: `http://localhost:8000/?wsdl`.
- Configura cada request con `POST` y `Content-Type: text/xml; charset=utf-8`.
- Verifica contra Railway:
  - Crea un usuario y un dispositivo; consulta en MySQL (Railway) que se insertaron.
  - Crea una actividad y registra datos de sensores; ejecuta `SELECT COUNT(*)` en `Actividad_Fisica` y `Datos_Sensores` en Railway.

