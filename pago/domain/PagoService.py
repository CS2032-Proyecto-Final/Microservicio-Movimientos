from typing import List
from pago.domain.Pago import Pago
from pago.dto.NewPagoDto import NewPagoDto
from pago.dto.PagoResponseDto import PagoResponseDto
from pago.infrastructure.PagoRepository import PagoRepository
from datetime import datetime


class PagoService:
    def __init__(self, repo: PagoRepository):
        self.repo = repo

    def postPago(self, pagoData: NewPagoDto):
        pago = Pago(destinatario_id=pagoData.destinatario_id,
                    remitente_id=pagoData.remitente_id,
                    monto=pagoData.monto,
                    producto_id=pagoData.producto_id,
                    codigo=pagoData.codigo,
                    fecha=datetime.utcnow(),
                    tipo="pago")

        self.repo.createPago(pago)

    def getPagosByClienteId(self, id: int) -> List[PagoResponseDto]:
        fullLista = self.repo.findAllByClienteId(id)
        dataLista = []

        for i in fullLista:
            pagoData = PagoResponseDto(destinatario_nombre=str(i.destinatario_id),
                                       monto=i.monto,
                                       producto_nombre=str(i.producto_id),
                                       fecha=i.fecha,
                                       codigo=i.codigo)
            dataLista.append(pagoData)

        return dataLista
