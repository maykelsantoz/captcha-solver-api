FROM python:3.9-slim

# Instala o Tesseract e outras dependências básicas
RUN apt-get update && \
    apt-get install -y tesseract-ocr libglib2.0-0 libsm6 libxrender1 libxext6 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia os arquivos da aplicação
WORKDIR /app
COPY . /app

# Instala dependências do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta da aplicação
EXPOSE 10000

# Inicia a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
