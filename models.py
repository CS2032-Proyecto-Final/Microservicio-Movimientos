from sqlalchemy import Column, Integer, String, Double, DateTime
from database import Base
from datetime import datetime


class Movimiento(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, index=True)
    remitente_id = Column(Integer, nullable=False)
    destinatario_id = Column(Integer, nullable=False)
    monto = Column(Double, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow())


class Transferencia(Movimiento):
    __tablename__ = "transferencias"

    movimiento_id = Column(Integer, nullable=False)
    descripcion = Column(String(500), nullable=True)


class Pago(Movimiento):
    __tablename__ = "pagos"

    movimiento_id = Column(Integer, nullable=False)
    producto_id = Column(Integer, nullable=False)
    codigo = Column(String(20), nullable=False)
