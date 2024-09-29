import string

import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()

# Configuraciones
num_records = 1000  # Número de registros a generar
monto_min = 10.0  # Monto mínimo
monto_max = 1000.0  # Monto máximo
producto_id_limit = 100  # Límite para el producto_id
destinatario_limit = 1999  # Límite para el destinatario_id
fecha_inicio = datetime(2020, 1, 1)  # Fecha de inicio
fecha_fin = datetime(2023, 12, 31)  # Fecha de fin

# Generar datos para la tabla 'movimientos'
movimiento_data = []
transferencia_ids = set()
pago_ids = set()

for i in range(num_records):
    remitente_id = random.randint(1, 999)
    destinatario_id = random.randint(1, destinatario_limit)

    while destinatario_id == remitente_id:
        destinatario_id = random.randint(1, destinatario_limit)

    monto = round(random.uniform(monto_min, monto_max), 2)
    fecha = fake.date_time_between(start_date=fecha_inicio, end_date=fecha_fin)

    if destinatario_id <= 999:
        tipo = 'transferencia'
        movimiento_id = i
        transferencia_ids.add(movimiento_id)
        pago_ids.discard(movimiento_id)
    else:
        tipo = 'pago'
        movimiento_id = i
        pago_ids.add(movimiento_id)
        transferencia_ids.discard(movimiento_id)

    movimiento_data.append({
        "id": movimiento_id,
        "remitente_id": remitente_id,
        "destinatario_id": destinatario_id,
        "monto": monto,
        "fecha": fecha.strftime('%Y-%m-%d %H:%M:%S'),
        "tipo": tipo
    })

movimiento_df = pd.DataFrame(movimiento_data)
movimiento_df.to_csv('movimientos.csv', index=False)

# Generar datos para la tabla 'transferencias'
transferencia_data = []
for t_id in transferencia_ids:
    descripcion = fake.sentence(nb_words=8)
    transferencia_data.append({
        "movimiento_id": t_id,
        "descripcion": descripcion
    })

transferencia_df = pd.DataFrame(transferencia_data)
transferencia_df.to_csv('transferencias.csv', index=False)

# Generar datos para la tabla 'pagos'
pago_data = []
for p_id in pago_ids:
    producto_id = random.randint(1, producto_id_limit)
    codigo = fake.bothify(text='???-###', letters=string.ascii_letters)
    pago_data.append({
        "movimiento_id": p_id,
        "producto_id": producto_id,
        "codigo": codigo
    })

pago_df = pd.DataFrame(pago_data)
pago_df.to_csv('pagos.csv', index=False)

print("Se generaron los CSVs.")
