
# Plataforma IoT con Servicios SOAP y REST

# Luis Gabriel Venegas Saucedo 
# Joshua Neftali Marin Leynez



## 🚀 API REST (Spring Boot) - Endpoints

La API utiliza JSON para el intercambio de datos.

### 1\. Gestión de Usuarios (`/api/usuarios`)

Control total sobre los perfiles de los atletas.

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `GET` | `/` | Lista todos los usuarios registrados. |
| `GET` | `/{id}` | Obtiene el detalle de un usuario por su ID. |
| `POST` | `/` | Registra un nuevo usuario. |
| `PUT` | `/{id}` | Actualiza la información de un usuario existente. |
| `DELETE` | `/{id}` | Elimina un usuario del sistema. |

**Ejemplo de Payload (POST/PUT):**

```json
{
    "nombre": "Luis",
    "apellido": "Venegas",
    "correoElectronico": "luis.venegas@email.com",
    "fechaDeNacimiento": "2000-01-01",
    "genero": "Masculino",
    "peso": 75.5,
    "altura": 1.78
}
```

### 2\. Sesiones de Entrenamiento (`/api/sesion_entrenamiento`)

Registro de actividades deportivas (Correr, Nadar, Ciclismo, etc.).

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `GET` | `/` | Historial completo de sesiones. |
| `GET` | `/{id}` | Detalle de una sesión específica. |
| `POST` | `/` | Crea una nueva sesión de entrenamiento. |
| `PUT` | `/{id}` | Modifica una sesión existente. |
| `DELETE` | `/{id}` | Elimina una sesión. |

**Ejemplo de Payload (POST):**

```json
{
    "usuario": {
        "id_usuario": 1
    },
    "tipoActividad": "Correr",
    "fechaHoraInicio": "2024-05-20T08:00:00",
    "fechaHoraFin": "2024-05-20T09:00:00",
    "duracionSegundos": 3600,
    "distanciaMetros": 10000.0,
    "caloriasQuemadas": 750,
    "latitudInicio": 19.432608,
    "longitudInicio": -99.133209,
    "ritmoPromedio": 5
}
```

*Tipos de Actividad Soportados:* `Correr`, `Caminar`, `Nadar`, `Ciclismo`, `Levantamiento_de_pesas`, `Yoga`, `Otro`.

### 3\. Frecuencia Cardíaca (`/api/frecuencia_cardiaca`)

Registro detallado de métricas biométricas vinculadas a una sesión.

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `GET` | `/` | Lista todas las mediciones. |
| `GET` | `/{id}` | Obtiene una medición específica. |
| `POST` | `/` | Registra una medición puntual. |
| `PUT` | `/{id}` | Actualiza una medición. |
| `DELETE` | `/{id}` | Elimina una medición. |

**Ejemplo de Payload (POST):**

```json
{
    "sesionEntrenamiento": {
        "id_sesion": 1
    },
    "fechaHoraRegistro": "2024-05-20T08:15:00",
    "frecuenciaCardiaca": 145,
    "oxigenacion": 98,
    "presion": "120/80"
}
```

-----

## 📦 API SOAP (Python) - Operaciones

Todas las peticiones deben ser `POST` con `Content-Type: text/xml`.
Namespace: `xmlns:iot="iot.soap"`

### 1\. Inventario de Dispositivos (Usuarios)

Gestión de la asignación de dispositivos a usuarios (Tabla `Dispositivos`).

  * **`crear_dispositivo`**: Asigna un dispositivo a un usuario.
  * **`obtener_dispositivo`**: Busca un dispositivo por su ID único.
  * **`listar_dispositivos_por_usuario`**: Muestra todos los dispositivos de un usuario.
  * **`listar_dispositivos`**: Inventario global de dispositivos asignados.
  * **`actualizar_dispositivo`**: Modifica marca o número de serie.
  * **`eliminar_dispositivo`**: Desvincula/Borra un dispositivo.

**Ejemplo XML (Crear Dispositivo):**

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
   <soapenv:Body>
      <iot:crear_dispositivo>
         <iot:id_usuario>1</iot:id_usuario>
         <iot:marca>Garmin</iot:marca>
         <iot:numero_serie>SN-123456789</iot:numero_serie>
      </iot:crear_dispositivo>
   </soapenv:Body>
</soapenv:Envelope>
```

### 2\. Catálogo IoT

Gestión de modelos de dispositivos soportados (Tabla `dispositivos_iot`).

  * **`crear_dispositivo_iot`**: Registra un nuevo modelo en el catálogo.
  * **`listar_dispositivos_iot`**: Lista todos los modelos disponibles.

**Ejemplo XML (Crear Modelo):**

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
   <soapenv:Body>
      <iot:crear_dispositivo_iot>
         <iot:modelo>Apple Watch Series 9</iot:modelo>
      </iot:crear_dispositivo_iot>
   </soapenv:Body>
</soapenv:Envelope>
```

### 3\. Usuarios (Solo Lectura)

Espejo de la tabla de usuarios para sistemas SOAP.

  * **`listar_usuarios`**: Devuelve la lista de usuarios (creados en REST) para consulta desde SOAP.

### 4\. Gestión de Sesiones (SOAP)

Funcionalidad espejo para registrar entrenamientos desde clientes SOAP.

  * **`crear_sesion`**: Permite registrar una sesión de entrenamiento.
  * **`listar_sesiones_por_usuario`**: Consulta sesiones en un rango de fechas.

**Ejemplo XML (Crear Sesión):**

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
   <soapenv:Body>
      <iot:crear_sesion>
         <iot:id_usuario>1</iot:id_usuario>
         <iot:tipo_actividad>Ciclismo</iot:tipo_actividad>
         <iot:fecha_hora_inicio>2024-06-01T10:00:00</iot:fecha_hora_inicio>
         <iot:fecha_hora_fin>2024-06-01T12:00:00</iot:fecha_hora_fin>
         <iot:duracion_segundos>7200</iot:duracion_segundos>
         <iot:distancia_metros>45000.5</iot:distancia_metros>
         <iot:calorias_quemadas>1200</iot:calorias_quemadas>
         <iot:latitud_inicio>19.43</iot:latitud_inicio>
         <iot:longitud_inicio>-99.13</iot:longitud_inicio>
         <iot:ritmo_promedio>25</iot:ritmo_promedio>
      </iot:crear_sesion>
   </soapenv:Body>
</soapenv:Envelope>
```

### 5\. Actividad Física y Sensores (Datos Crudos)

Módulo para la ingesta de datos raw desde los dispositivos.

  * **`crear_actividad`**: Registra un bloque de actividad física general.
  * **`registrar_dato_sensor`**: Inserta un dato puntual de sensores (FC, Oxigenación, Presión) vinculado a una actividad.

**Ejemplo XML (Registrar Dato Sensor):**

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
   <soapenv:Body>
      <iot:registrar_dato_sensor>
         <iot:id_actividad>1</iot:id_actividad>
         <iot:id_usuario>1</iot:id_usuario>
         <iot:fecha_hora_registro>2024-06-01T10:05:00</iot:fecha_hora_registro>
         <iot:frecuencia_cardiaca>135</iot:frecuencia_cardiaca>
         <iot:oxigenacion>97</iot:oxigenacion>
         <iot:presion>120/80</iot:presion>
      </iot:registrar_dato_sensor>
   </soapenv:Body>
</soapenv:Envelope>
```

### 6\. Reportes

Generación de resúmenes y analíticas.

  * **`resumen_diario_usuario`**: Calcula el total de kilómetros, calorías y promedios biométricos de un usuario en una fecha específica.

**Ejemplo XML:**

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iot="iot.soap">
   <soapenv:Body>
      <iot:resumen_diario_usuario>
         <iot:id_usuario>1</iot:id_usuario>
         <iot:fecha>2024-06-01</iot:fecha>
      </iot:resumen_diario_usuario>
   </soapenv:Body>
</soapenv:Envelope>
```
