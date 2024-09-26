from movimiento.domain.Movimiento import Movimiento
from typing import Optional


class Transferencia(Movimiento):
    descripcion: Optional[str] = None
