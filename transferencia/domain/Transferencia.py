from movimiento.domain.Movimiento import Movimiento
from typing import Optional


class Transferencia(Movimiento):
    movimiento_id: int
    descripcion: Optional[str] = None
