from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transferencia.application.TransferenciaController import router as transferencia_router
from pago.application.PagoController import router as pago_router
from database import engine
from models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Enable Cors"}
app.include_router(transferencia_router)
app.include_router(pago_router)
