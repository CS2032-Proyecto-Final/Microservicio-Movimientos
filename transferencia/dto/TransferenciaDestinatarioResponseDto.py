from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class TransferenciaDestinatarioResponseDto(BaseModel):
    nombre_destinatario: str
    monto: float
    fecha: datetime
    descripcion: Optional[str] = None
