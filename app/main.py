# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# from utils import process_image
# import shutil
# import os

# app = FastAPI()

# # CORS para permitir requisições APENAS do sistec
# origins = ["https://sistec.mec.gov.br"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,           # Não pode ser ["*"] se allow_credentials=True
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/solve")
# async def solve(file: UploadFile = File(...)):
#     with open("temp.png", "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     text = process_image("temp.png")
#     os.remove("temp.png")
#     return {"captcha": text}

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.utils import process_image  # ✅ certo
import tempfile
import os

app = FastAPI()

# CORS para permitir requisições APENAS do sistec
origins = ["https://sistec.mec.gov.br"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/solve")
async def solve(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_path = temp_file.name
            temp_file.write(await file.read())

        text = process_image(temp_path)
        return {"captcha": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar imagem: {str(e)}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
