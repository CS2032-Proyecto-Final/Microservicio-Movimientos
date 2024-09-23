from fastapi import APIRouter, HTTPException
from typing import List
from pago.domain.Pago import Pago
from pago.domain.PagoService import PagoService
from pago.infrastructure.PagoRepository import PagoRepository

router = APIRouter()

service = PagoService(repo=PagoRepository())
