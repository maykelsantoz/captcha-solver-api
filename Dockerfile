FROM python:3.9-slim

# Instala o Tesseract, libs de imagem e o libGL para OpenCV funcionar
RUN apt-get update && \
    apt-get install -y tesseract-ocr libglib2.0-0 libsm6 libxrender1 libxext6 libgl1-mesa-glx && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /app

# Copia o código
COPY . /app

# Instala dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta
EXPOSE 10000

# Inicia o FastAPI com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
