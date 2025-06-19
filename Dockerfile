FROM python:3.10-slim

# Crea un directorio dentro del contenedor
WORKDIR /app

# Copia solo el script (no el output.txt)
COPY generator/ ./generator/

# Ejecutar el script al iniciar el contenedor
CMD ["python", "generator/generateData.py"]
