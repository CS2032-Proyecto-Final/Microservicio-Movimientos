from typing import List, Optional
from pago.domain.Pago import Pago
from pago.infrastructure.PagoRepository import PagoRepository


class PagoService:
    def __init__(self, repo: PagoRepository):
        self.repo = repo
