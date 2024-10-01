from sqlalchemy.orm import Session
from models import Transferencia as TransferenciaModel
from transferencia.domain.Transferencia import Transferencia
from typing import List
from database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError

class TransferenciaRepository:
    def __init__(self):
        self.db: Session = SessionLocal()

    def findAllByRemitenteId(self, id: int) -> List[Transferencia]:
        try:
            return self.db.query(TransferenciaModel).filter(TransferenciaModel.remitente_id == id).all()
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def findAllByDestinatarioId(self, id: int) -> List[Transferencia]:
        try:
            return self.db.query(TransferenciaModel).filter(TransferenciaModel.destinatario_id == id).all()
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def createTransferencia(self, transferencia: Transferencia) -> Transferencia:
        try:
            db_transferencia = TransferenciaModel(**transferencia.dict())
            self.db.add(db_transferencia)
            self.db.commit()
            self.db.refresh(db_transferencia)
            return db_transferencia
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e
        finally:
            self.db.close()
