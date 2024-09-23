from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Movimiento(BaseModel):
    id: Optional[int] = None
    remitente_id: int
    destinatario_id: int
    monto: float
    fecha: datetime
