from sqlalchemy.orm import Session
from database import SessionLocal


class MovimientoRepository:
    def __init__(self):
        self.db: Session = SessionLocal()
