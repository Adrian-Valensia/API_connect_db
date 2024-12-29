# API_connect_db

Para este proyecto, deberán utilizar Docker (ya sea localmente o en la nube) para ejecutar dos contenedores:<br>
1. API usando Flask o FastAPI desarrollado por el estudiante. <br>

2.Una base de datos relacional o no relaciones según preferencia (MySQL, Postgres, MongoDB,etc). Usar imagen de Docker Hub. Se deberá crear un dataset llamado my_collections, donde se tendrá una tabla my_movies con los campos “ID”, “Autor”, “Descripción”, y “Fecha de Estreno”
El API desarrollado debe implementar los métodos GET, POST, PUT y DELETE, y cada uno de ellos deberá realizar lo siguiente: <br>

• Método GET: Leer datos de la BD. Puede codificarlo para obtener solo un dato de alguna fila con un id especifico, o puede codificarlo para obtener todo el dataset. <br>
•Método POST: Escribir datos en la BD. Codificarlo para que agregar datos a la tabla my_movies y que el id se incremente secuencialmente según el último valor agregado. <br>
• Método PUT: Actualizar datos de la BD. Puede codificarlo para modificar solo uno o más campos de un elemento especifico de la tabla, o puede codificarlo para que modifique todos los campos de un elemento de la tabla. <br>
• Método DELETE: Borrar datos de la BD. Codificarlo para que borre un elemento especifico (según id) de la tabla my_movies.<br>




## Iniciar el Proyecto con Docker

### 1. Construir la Imagen de Docker

Para construir la imagen de Docker para la aplicación FastAPI, usa el siguiente comando en la raíz del proyecto donde se encuentra el `Dockerfile`:

```bash
docker build -t movie_fastapi . 
```

### 2. Crear y Ejecutar los Contenedores con Docker Compose

Si prefieres usar Docker Compose para iniciar tanto el contenedor de PostgreSQL como el de FastAPI, utiliza los siguientes comandos.

Primero, asegúrate de tener el archivo docker-compose.yml configurado correctamente. Este archivo contiene los servicios de FastAPI (API) y PostgreSQL (db).

a) Comando para Iniciar los Contenedores
Usa el siguiente comando para iniciar los servicios definidos en docker-compose.yml:

```bash
docker-compose up
```

Este comando descargará las imágenes necesarias (si no están ya en tu máquina), construirá los contenedores y los pondrá en marcha. FastAPI se ejecutará en el puerto 8000 y PostgreSQL estará disponible en el puerto 5432.

b) Comando para Iniciar los Contenedores en Segundo Plano
Si prefieres ejecutar los contenedores en segundo plano, puedes usar:

```bash
Copiar código
docker-compose up -d
```

c) Verificar los Logs
Para ver los logs de la aplicación FastAPI o PostgreSQL, usa el siguiente comando:

```bash
docker-compose logs api  # Logs del contenedor de FastAPI
docker-compose logs db   # Logs del contenedor de PostgreSQL
```

### 3. Conectar a la Base de Datos

Si necesitas conectarte al contenedor de PostgreSQL desde otro contenedor o tu máquina, usa el siguiente comando:

```bash
docker-compose exec db psql -U tu_usuario -d tu_db
```

Esto te permitirá interactuar con la base de datos dentro del contenedor de PostgreSQL.

Configuración de la Base de Datos en FastAPI

El contenedor de FastAPI se conecta a la base de datos PostgreSQL usando los siguientes parámetros de conexión:

host: db (nombre del servicio de PostgreSQL en docker-compose.yml)<br>
port: 5432 <br>
dbname: tu_db (nombre de la base de datos)<br>
user: tu_usuario (usuario de PostgreSQL)<br>
password: tu_contraseña (contraseña de PostgreSQL)<br>
Asegúrate de que estos parámetros estén correctamente configurados en tu archivo main.py.<br>

Detener los Contenedores<br>
Cuando hayas terminado de trabajar, puedes detener y eliminar los contenedores con el siguiente comando:

```bash
docker-compose down
```

Para eliminar también los volúmenes, usa:

```bash
docker-compose down -v
```
