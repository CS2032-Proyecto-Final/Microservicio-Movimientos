from movimiento.domain.Movimiento import Movimiento


class Pago(Movimiento):
    producto_id: int
    codigo: str
