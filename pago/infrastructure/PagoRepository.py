from sqlalchemy.orm import Session
from models import Pago as PagoModel
from pago.domain.Pago import Pago
from typing import List, Optional
from database import SessionLocal


class PagoRepository:
    def __init__(self):
        self.db: Session = SessionLocal()
