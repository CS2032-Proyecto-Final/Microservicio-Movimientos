from sqlalchemy.orm import Session
from models import Transferencia as TransferenciaModel
from transferencia.domain.Transferencia import Transferencia
from typing import List
from database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager

@contextmanager
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TransferenciaRepository:
    def findAllByRemitenteId(self, id: int) -> List[Transferencia]:
        try:
            with get_db() as db:
                return db.query(TransferenciaModel).filter(TransferenciaModel.remitente_id == id).all()
        except SQLAlchemyError as e:
            raise e  # Propagar la excepción

    def findAllByDestinatarioId(self, id: int) -> List[Transferencia]:
        try:
            with get_db() as db:
                return db.query(TransferenciaModel).filter(TransferenciaModel.destinatario_id == id).all()
        except SQLAlchemyError as e:
            raise e  # Propagar la excepción

    def createTransferencia(self, transferencia: Transferencia) -> Transferencia:
        try:
            with get_db() as db:
                db_transferencia = TransferenciaModel(**transferencia.dict())
                db.add(db_transferencia)
                db.commit()
                db.refresh(db_transferencia)
                return db_transferencia
        except SQLAlchemyError as e:
            db.rollback()  # Revertir los cambios en caso de error
            print("error al guardar en la bd")
            raise e  # Propagar la excepción
