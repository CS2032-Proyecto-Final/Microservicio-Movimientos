from movimiento.domain.Movimiento import Movimiento
from typing import Optional


class Pago(Movimiento):
    producto_id: int
    codigo: Optional[str] = None
