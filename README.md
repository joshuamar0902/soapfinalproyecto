¡Claro que sí\! Aquí tienes una plantilla profesional y atractiva para el `README.md` de tu proyecto, usando la información que me diste.

Simplemente **copia y pega** este contenido en un archivo llamado `README.md` en la raíz de tu proyecto.

-----

# 🚀 Plataforma IoT con Servicios SOAP y REST

Un proyecto de: **Joshua Neftalí Marín Leynez** y **Luis Gabriel Venegas Saucedo**

## 📖 Descripción del Proyecto

Este proyecto es una plataforma integral para el **monitoreo de actividad física y sensores IoT**. La arquitectura está diseñada para ser robusta y escalable, exponiendo la lógica de negocio a través de dos tipos de servicios web:

1.  **API SOAP:** Implementada con **Python** y **Spyne**, se encarga de las operaciones CRUD (Crear, Leer, Actualizar, Borrar) de bajo nivel y la comunicación directa con los dispositivos.
2.  **API REST:** Implementada con **Java** y **Spring Boot**, consume la misma base de datos y ofrece endpoints modernos y fáciles de usar para aplicaciones web o móviles.

Ambos servicios operan sobre una base de datos **MySQL** compartida, permitiendo una verdadera arquitectura de microservicios donde los datos son consistentes sin importar cómo se acceda a ellos.

-----

## 💻 Stack Tecnológico

| Componente | Tecnología | Propósito |
| :--- | :--- | :--- |
| **API SOAP** | Python + Spyne | Exponer servicios SOAP (WSDL) para CRUDS. |
| **API REST** | Java + Spring Boot | Exponer endpoints REST (JSON) para consumo moderno. |
| **Base de Datos** | MySQL | Almacenamiento centralizado de datos. |
| **Modelos (Java)** | JPA / Hibernate | Mapeo Objeto-Relacional (ORM) para la API REST. |
| **Driver (Python)**| `mysql-connector` | Conexión de Python a MySQL. |

-----

## ✨ Características Principales

  * **Gestión de Usuarios:** CRUD completo para registrar y administrar usuarios.
  * **Gestión de Dispositivos:** CRUD para asociar dispositivos (wearables, sensores) a los usuarios.
  * **Registro de Actividad:** Almacenamiento de sesiones de actividad física (distancia, calorías, etc.).
  * **Datos de Sensores:** Almacenamiento de series temporales de datos biométricos (ritmo cardíaco, oxigenación).
  * **Doble Arquitectura:** Ofrece flexibilidad al exponer tanto SOAP como REST.

-----

## 🔧 Instalación y Puesta en Marcha

Sigue estos pasos para levantar ambos servicios.

### 1\. Base de Datos (Requisito Común)

1.  Asegúrate de tener un servidor **MySQL** corriendo.
2.  Crea una base de datos para el proyecto (ej. `iotSoap`).
    ```sql
    CREATE DATABASE iotSoap;
    ```
3.  La estructura de las tablas será creada automáticamente por los servicios.

### 2\. Servicio SOAP (Python)

1.  Clona el repositorio:
    ```bash
    git clone [URL_DE_TU_REPO]
    cd [CARPETA_DEL_PROYECTO_PYTHON]
    ```
2.  Crea un entorno virtual e instálalo:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
3.  Instala las dependencias:
    ```bash
    pip install spyne mysql-connector-python
    ```
4.  Edita `database.py` con tus credenciales de MySQL:
    ```python
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='TU_CONTRASENA_ROOT_AQUI', # <-- ¡Importante!
        database='iotSoap'
    )
    ```
5.  Inicia el servidor SOAP:
    ```bash
    python app.py
    ```
6.  ¡Listo\! El servicio SOAP estará corriendo en `http://localhost:8000`.

### 3\. Servicio REST (Java)

1.  Navega a la carpeta del proyecto Java:
    ```bash
    cd [CARPETA_DEL_PROYECTO_JAVA]
    ```
2.  Configura tu base de datos en `src/main/resources/application.properties`:
    ```properties
    spring.datasource.url=jdbc:mysql://localhost:3306/iotSoap
    spring.datasource.username=root
    spring.datasource.password=TU_CONTRASENA_ROOT_AQUI
    spring.jpa.hibernate.ddl-auto=update
    spring.jpa.show-sql=true
    ```
3.  Ejecuta el proyecto con Maven:
    ```bash
    ./mvnw spring-boot:run
    ```
4.  ¡Listo\! El servicio REST estará corriendo en `http://localhost:8080`.

-----

## ☁️ Uso de las APIs

### API SOAP (Python)

Puedes usar una herramienta como **SoapUI** o **Postman** (en modo SOAP) para interactuar con los servicios.

  * **WSDL (El "manual" de la API):**
    `http://localhost:8000/?wsdl`

**Servicios Expuestos:**

  * `UsuarioService`
  * `DispositivoService`
  * `ActividadService`
  * `DatosSensorService`

### API REST (Java)

Puedes usar **Postman**, **Insomnia** o cualquier cliente HTTP.

**Endpoints Principales (Ejemplo):**

  * `POST /api/usuarios` - Crea un nuevo usuario.
  * `GET /api/usuarios/{id}` - Obtiene un usuario por ID.
  * `GET /api/usuarios` - Obtiene todos los usuarios.
  * `POST /api/dispositivos` - Crea un nuevo dispositivo.
  * `GET /api/dispositivos/usuario/{id_usuario}` - Obtiene todos los dispositivos de un usuario.

-----

## 👨‍💻 Autores

Este proyecto fue desarrollado con dedicación por:

  * **Joshua Neftalí Marín Leynez**
  * **Luis Gabriel Venegas Saucedo**

-----

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

```
```
