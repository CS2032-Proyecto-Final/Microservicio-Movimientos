from sqlalchemy.orm import Session
from models import Transferencia as TransferenciaModel
from transferencia.domain.Transferencia import Transferencia
from typing import List, Optional
from database import SessionLocal


class TransferenciaRepository:
    def __init__(self):
        self.db: Session = SessionLocal()
