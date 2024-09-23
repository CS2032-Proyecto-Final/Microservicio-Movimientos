from sqlalchemy.orm import Session
from models import Movimiento as MovimientoModel
from movimiento.domain.Movimiento import Movimiento
from typing import List, Optional
from database import SessionLocal


class MovimientoRepository:
    def __init__(self):
        self.db: Session = SessionLocal()
