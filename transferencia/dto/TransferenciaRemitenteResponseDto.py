from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class TransferenciaRemitenteResponseDto(BaseModel):
    nombre_remitente: str
    monto: float
    fecha: datetime
    descripcion: Optional[str] = None
