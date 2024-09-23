from fastapi import FastAPI
from transferencia.application.TransferenciaController import router as transferencia_router
from pago.application.PagoController import router as pago_router
from database import engine
from models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI

app.include_router(transferencia_router)
app.include_router(pago_router)
