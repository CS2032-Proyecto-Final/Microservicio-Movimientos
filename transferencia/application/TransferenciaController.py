from fastapi import APIRouter, HTTPException
from typing import List
from transferencia.domain.Transferencia import Transferencia
from transferencia.domain.TransferenciaService import TransferenciaService
from transferencia.infrastructure.TransferenciaRepository import TransferenciaRepository

router = APIRouter()

service = TransferenciaService(repo=TransferenciaRepository())
