# Microservicio-Movimientos

## Para probar localmente

### Dependencias
- FastAPI
- Uvicorn
- SQLAlchemy
- PyMySQL
- python-dotenv
- cryptography

```
pip3 install fastapi uvicorn sqlalchemy pymysql python-dotenv cryptography
```

### .env
Se tiene que crear un archivo .env con la información de acceso a la base de datos.

Ejemplo:
```
DB_USER=root
DB_PASSWORD=123
DB_HOST=0.0.0.0
DB_PORT=8000
DB_NAME=bd
```

### Correr api
```
uvicorn main:app
```

## Para construir y correr la api en un contenedor

### Construir la imagen
```
docker build -t api-movimientos .
```

### Correr la imagen
```
docker run -d -p 8000:8000 \
  -e DB_USER=<usuario> \
  -e DB_PASSWORD=<contraseña> \
  -e DB_HOST=<host> \
  -e DB_PORT=<puerto> \
  -e DB_NAME=<nombre de la base de datos> \
  api-movimientos
```