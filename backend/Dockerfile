FROM python:3.12.3-slim

WORKDIR /app

#instala dependencias do sistema críticas
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

#copia requirements primeiro
COPY requirements.txt .

#instalar setuptools primeiro, depois dependências
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

#copia codigo
COPY . .

#configura variaveis de ambiente
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]