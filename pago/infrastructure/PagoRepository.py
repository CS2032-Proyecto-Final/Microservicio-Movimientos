from sqlalchemy.orm import Session
from models import Pago as PagoModel
from pago.domain.Pago import Pago
from typing import List
from database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager

# Manejador de contexto para gestionar la sesión
@contextmanager
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PagoRepository:
    def createPago(self, pago: Pago) -> Pago:
        try:
            with get_db() as db:
                db_pago = PagoModel(**pago.dict())
                db.add(db_pago)
                db.commit()
                db.refresh(db_pago)
                return db_pago
        except SQLAlchemyError as e:
            db.rollback()  # Revertir cambios en caso de error
            print("error al guardar en la bd")
            raise e  # Propagar la excepción

    def findAllByClienteId(self, id: int) -> List[Pago]:
        try:
            with get_db() as db:
                return db.query(PagoModel).filter(PagoModel.remitente_id == id).all()
        except SQLAlchemyError as e:
            db.rollback()  # Revertir cambios en caso de error
            raise e  # Propagar la excepción
