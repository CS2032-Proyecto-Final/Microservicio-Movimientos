from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,      # Verificar si la conexión está activa
    pool_size=10,            # Número de conexiones abiertas simultáneamente
    max_overflow=20,         # Conexiones adicionales permitidas
    pool_timeout=30          # Tiempo máximo para esperar una conexión libre
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base
