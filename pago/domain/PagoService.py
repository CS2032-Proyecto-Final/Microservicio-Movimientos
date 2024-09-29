import random
import string
from typing import List

from fastapi import HTTPException

from pago.domain.Pago import Pago
from pago.dto.NewPagoDto import NewPagoDto
from pago.dto.PagoResponseDto import PagoResponseDto
from pago.infrastructure.PagoRepository import PagoRepository
from datetime import datetime
from url import *
import requests


class PagoService:
    def __init__(self, repo: PagoRepository):
        self.repo = repo

    def postPago(self, pagoData: NewPagoDto):

        codigo_aleatorio = ''.join(random.choices(string.ascii_letters, k=3)) + '-' + ''.join(random.choices(string.digits, k=3))

        pago = Pago(destinatario_id=pagoData.destinatario_id,
                    remitente_id=pagoData.remitente_id,
                    monto=pagoData.monto,
                    producto_id=pagoData.producto_id,
                    codigo=codigo_aleatorio,
                    fecha=datetime.utcnow(),
                    tipo="pago")

        self.repo.createPago(pago)

    def getPagosByClienteId(self, id: int) -> List[PagoResponseDto]:
        fullLista = self.repo.findAllByClienteId(id)

        tienda_ids = [i.destinatario_id for i in fullLista]
        producto_ids = [i.producto_id for i in fullLista]

        tienda_response = requests.post(
            URL_MC+"/tiendas/nombre",
            json={tienda_ids}
        )

        producto_response = requests.post(
            URL_MP+"/productos/nombre",
            json={producto_ids}
        )

        if tienda_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error al comunicarse con el microservicio de clientes")

        if producto_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error al comunicarse con el microservicio de promociones")

        nombre_tiendas = {item["tienda_id"]: item["nombre_tienda"] for item in tienda_response.json()}
        nombre_productos = {item["producto_id"]: item["nombre_producto"] for item in producto_response.json()}

        dataLista = []

        for i in fullLista:

            nombre_tienda = nombre_tiendas.get(i.remitente_id, "")
            nombre_producto = nombre_productos.get(i.producto_id, "")

            pagoData = PagoResponseDto(destinatario_nombre=nombre_tienda,
                                       monto=i.monto,
                                       producto_nombre=nombre_producto,
                                       fecha=i.fecha,
                                       codigo=i.codigo)
            dataLista.append(pagoData)

        return dataLista
