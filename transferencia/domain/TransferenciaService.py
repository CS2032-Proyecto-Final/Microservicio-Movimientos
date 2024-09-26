from typing import List
from transferencia.domain.Transferencia import Transferencia
from transferencia.dto.TransferenciaRemitenteResponseDto import TransferenciaRemitenteResponseDto
from transferencia.dto.TransferenciaDestinatarioResponseDto import TransferenciaDestinatarioResponseDto
from transferencia.dto.NewTransferenciaDto import NewTransferenciaDto
from transferencia.infrastructure.TransferenciaRepository import TransferenciaRepository
from datetime import datetime


class TransferenciaService:
    def __init__(self, repo: TransferenciaRepository):
        self.repo = repo

    def getDestinatariosByRemitenteId(self, id: int) -> List[TransferenciaDestinatarioResponseDto]:
        fullLista = self.repo.findAllByRemitenteId(id)
        dataLista = []

        for i in fullLista:
            transferenciaData = TransferenciaDestinatarioResponseDto(nombre_destinatario=str(i.destinatario_id),
                                                                     monto=i.monto,
                                                                     fecha=i.fecha,
                                                                     descripcion=i.descripcion)
            dataLista.append(transferenciaData)

        return dataLista

    def getRemitentesByDestinatarioId(self, id: int) -> List[TransferenciaRemitenteResponseDto]:
        fullLista = self.repo.findAllByDestinatarioId(id)
        dataLista = []

        for i in fullLista:
            transferenciaData = TransferenciaRemitenteResponseDto(nombre_remitente=str(i.remitente_id),
                                                                  monto=i.monto,
                                                                  fecha=i.fecha,
                                                                  descripcion=i.descripcion)
            dataLista.append(transferenciaData)

        return dataLista

    def postTransferencia(self, transferenciaData: NewTransferenciaDto):
        transferencia = Transferencia(destinatario_id=transferenciaData.destinatario_id,
                                      remitente_id=transferenciaData.remitente_id,
                                      monto=transferenciaData.monto,
                                      descripcion=transferenciaData.descripcion,
                                      fecha=datetime.utcnow(),
                                      tipo="transferencia")

        self.repo.createTransferencia(transferencia)
