FROM python:3-slim

WORKDIR /app/api-movimientos

RUN pip3 install fastapi
RUN pip3 install uvicorn
RUN pip3 install sqlalchemy
RUN pip3 install pymysql
RUN pip3 install python-dotenv
RUN pip3 install requests
RUN pip3 install cryptography

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]