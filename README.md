# Microservicio-Movimientos

### Dependencias
- FastAPI
- Uvicorn
- SQLAlchemy
- PyMySQL
- python-dotenv

```
pip3 install fastapi uvicorn sqlalchemy pymysql python-dotenv
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