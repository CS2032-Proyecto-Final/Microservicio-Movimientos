from typing import List

from fastapi import HTTPException

from transferencia.domain.Transferencia import Transferencia
from transferencia.dto.TransferenciaRemitenteResponseDto import TransferenciaRemitenteResponseDto
from transferencia.dto.TransferenciaDestinatarioResponseDto import TransferenciaDestinatarioResponseDto
from transferencia.dto.NewTransferenciaDto import NewTransferenciaDto
from transferencia.infrastructure.TransferenciaRepository import TransferenciaRepository
from datetime import datetime
from url import *
import requests


class TransferenciaService:
    def __init__(self, repo: TransferenciaRepository):
        self.repo = repo

    def getDestinatariosByRemitenteId(self, id: int) -> List[TransferenciaDestinatarioResponseDto]:
        fullLista = self.repo.findAllByRemitenteId(id)

        if not fullLista:
            return []

        destinatario_ids = [{"id": i.destinatario_id} for i in fullLista]

        response = requests.patch(
            URL_MC+"/personas/nombre",
            json=destinatario_ids
        )

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error al comunicarse con el microservicio de clientes")

        nombres_destinatarios = {item["id"]: item["nombre_destinatario"] for item in response.json()}

        dataLista = []

        for i in fullLista:

            nombre_destinatario = nombres_destinatarios.get(i.destinatario_id, "")

            transferenciaData = TransferenciaDestinatarioResponseDto(nombre_destinatario=nombre_destinatario,
                                                                     monto=i.monto,
                                                                     fecha=i.fecha,
                                                                     descripcion=i.descripcion)
            dataLista.append(transferenciaData)

        return dataLista

    def getRemitentesByDestinatarioId(self, id: int) -> List[TransferenciaRemitenteResponseDto]:
        fullLista = self.repo.findAllByDestinatarioId(id)

        if not fullLista:
            return []

        remitente_ids = [{"id": i.remitente_id} for i in fullLista]

        print(remitente_ids)
        response = requests.patch(
            URL_MC+"/personas/nombre",
            json=remitente_ids
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error al comunicarse con el microservicio de clientes")
        
        nombres_remitentes = {item["id"]: item["nombre_destinatario"] for item in response.json()}

        dataLista = []

        for i in fullLista:
            nombre_remitente = nombres_remitentes.get(i.remitente_id, "")

            transferenciaData = TransferenciaRemitenteResponseDto(nombre_remitente=nombre_remitente,
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
