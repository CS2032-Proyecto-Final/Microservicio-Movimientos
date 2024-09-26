from typing import Optional
from pydantic import BaseModel

class NewTransferenciaDto(BaseModel):
    remitente_id: int
    destinatario_id: int
    monto: float
    descripcion: Optional[str] = None