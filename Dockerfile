# Usa una imagen base oficial de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del archivo requirements.txt
RUN pip install -r requirements.txt

# Copia todo el código de tu aplicación al contenedor
COPY . .

# Establece la variable de entorno para el puerto
ENV PORT=8080

# Exponer el puerto 8080
EXPOSE 8080

# Comando para ejecutar la aplicación FastAPI con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
