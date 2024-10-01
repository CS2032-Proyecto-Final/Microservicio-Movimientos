from sqlalchemy.orm import Session
from models import Pago as PagoModel
from pago.domain.Pago import Pago
from typing import List
from database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError

class PagoRepository:
    def __init__(self):
        self.db: Session = SessionLocal()

    def createPago(self, pago: Pago) -> Pago:
        try:
            db_pago = PagoModel(**pago.dict())
            self.db.add(db_pago)
            self.db.commit()
            self.db.refresh(db_pago)
            return db_pago
        except SQLAlchemyError as e:
            self.db.rollback()  # Revertir cambios en caso de error
            raise e  # Propagar la excepción
        finally:
            self.db.close()  # Asegurarse de que la sesión se cierre

    def findAllByClienteId(self, id: int) -> List[Pago]:
        try:
            return self.db.query(PagoModel).filter(PagoModel.remitente_id == id).all()
        except SQLAlchemyError as e:
            self.db.rollback()  # Revertir cambios en caso de error
            raise e  # Propagar la excepción
        finally:
            self.db.close()  # Asegurarse de que la sesión se cierre
