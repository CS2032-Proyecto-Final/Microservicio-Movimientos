from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
import enum


class Base(DeclarativeBase):
    pass


class MovimientoTipo(enum.Enum):
    transferencia = "transferencia"
    pago = "pago"


class Movimiento(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, index=True)
    remitente_id = Column(Integer, nullable=False)
    destinatario_id = Column(Integer, nullable=False)
    monto = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    tipo = Column(Enum(MovimientoTipo), nullable=False)

    # Definir relaciones inversas con Transferencia y Pago
    transferencia = relationship("Transferencia", back_populates="movimiento", uselist=False)
    pago = relationship("Pago", back_populates="movimiento", uselist=False)


class Transferencia(Movimiento):
    __tablename__ = "transferencias"

    movimiento_id = Column(Integer, ForeignKey("movimientos.id"), primary_key=True)
    descripcion = Column(String(500), nullable=True)

    # Relación con Movimiento
    movimiento = relationship("Movimiento", back_populates="transferencia")


class Pago(Movimiento):
    __tablename__ = "pagos"

    movimiento_id = Column(Integer, ForeignKey("movimientos.id"), primary_key=True)
    producto_id = Column(Integer, nullable=False)
    codigo = Column(String(50), nullable=True)

    # Relación con Movimiento
    movimiento = relationship("Movimiento", back_populates="pago")