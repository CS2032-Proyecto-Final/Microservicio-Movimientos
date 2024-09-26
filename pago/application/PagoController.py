from fastapi import APIRouter, HTTPException, status
from typing import List
from pago.domain.PagoService import PagoService
from pago.dto.NewPagoDto import NewPagoDto
from pago.dto.PagoResponseDto import PagoResponseDto
from pago.infrastructure.PagoRepository import PagoRepository

router = APIRouter()

service = PagoService(repo=PagoRepository())


@router.post("/pagos", status_code=status.HTTP_201_CREATED)
def postPago(pago: NewPagoDto):
    service.postPago(pago)


@router.get("/pagos/cliente/{id}", response_model=List[PagoResponseDto])
def getPagos(id: int):
    return service.getPagosByClienteId(id)
