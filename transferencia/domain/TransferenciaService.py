from typing import List, Optional
from transferencia.domain.Transferencia import Transferencia
from transferencia.infrastructure.TransferenciaRepository import TransferenciaRepository


class TransferenciaService:
    def __init__(self, repo: TransferenciaRepository):
        self.repo = repo
