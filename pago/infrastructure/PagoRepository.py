from sqlalchemy.orm import Session
from models import Pago as PagoModel
from pago.domain.Pago import Pago
from typing import List
from database import SessionLocal


class PagoRepository:
    def __init__(self):
        self.db: Session = SessionLocal()

    def createPago(self, pago: Pago) -> Pago:
        db_pago = PagoModel(**pago.dict())
        self.db.add(db_pago)
        self.db.commit()
        self.db.refresh(db_pago)
        return db_pago

    def findAllByClienteId(self, id: int) -> List[Pago]:
        return self.db.query(PagoModel).filter(PagoModel.remitente_id == id)
