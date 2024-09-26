from sqlalchemy.orm import Session
from models import Transferencia as TransferenciaModel
from transferencia.domain.Transferencia import Transferencia
from typing import List
from database import SessionLocal


class TransferenciaRepository:
    def __init__(self):
        self.db: Session = SessionLocal()

    def findAllByRemitenteId(self, id: int) -> List[Transferencia]:
        return self.db.query(TransferenciaModel).filter(TransferenciaModel.remitente_id == id)

    def findAllByDestinatarioId(self, id: int) -> List[Transferencia]:
        return self.db.query(TransferenciaModel).filter(TransferenciaModel.destinatario_id == id)

    def createTransferencia(self, transferencia: Transferencia) -> Transferencia:
        db_transferencia = TransferenciaModel(**transferencia.dict())
        self.db.add(db_transferencia)
        self.db.commit()
        self.db.refresh(db_transferencia)
        return db_transferencia
