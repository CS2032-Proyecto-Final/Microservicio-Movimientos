from fastapi import APIRouter, status
from typing import List
from transferencia.domain.TransferenciaService import TransferenciaService
from transferencia.dto.TransferenciaRemitenteResponseDto import TransferenciaRemitenteResponseDto
from transferencia.dto.TransferenciaDestinatarioResponseDto import TransferenciaDestinatarioResponseDto
from transferencia.dto.NewTransferenciaDto import NewTransferenciaDto
from transferencia.infrastructure.TransferenciaRepository import TransferenciaRepository

router = APIRouter()

service = TransferenciaService(repo=TransferenciaRepository())

@router.post("/transferencias", status_code=status.HTTP_201_CREATED)
def postTransferencia(transferencia: NewTransferenciaDto):
    service.postTransferencia(transferencia)


@router.get("/transferencias/cliente/{id}/destinatarios", response_model=List[TransferenciaDestinatarioResponseDto])
def getDestinatarios(id: int):
    return service.getDestinatariosByRemitenteId(id)


@router.get("/transferencias/cliente/{id}/remitentes", response_model=List[TransferenciaRemitenteResponseDto])
def getRemitentes(id: int):
    return service.getRemitentesByDestinatarioId(id)
