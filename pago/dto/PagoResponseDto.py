from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class PagoResponseDto(BaseModel):
    destinatario_nombre: str
    monto: float
    producto_nombre: str
    fecha: datetime
    codigo: Optional[str] = None
