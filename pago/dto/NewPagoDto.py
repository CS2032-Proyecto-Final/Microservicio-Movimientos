from pydantic import BaseModel
from typing import Optional


class NewPagoDto(BaseModel):
    remitente_id: int
    destinatario_id: int
    monto: float
    producto_id: int
    codigo: Optional[str] = None