from fastapi import FastAPI
from pago.application.PagoController import router as movimiento_router
from transferencia.application.TransferenciaController import router as transferencia_router
from database import engine
from models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI

app.include_router(movimiento_router)
app.include_router(transferencia_router)
