from movimiento.domain.Movimiento import Movimiento


class Pago(Movimiento):
    movimiento_id: int
    producto_id: int
    codigo: str
