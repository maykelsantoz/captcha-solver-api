from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils import process_image
import shutil
import os

app = FastAPI()

# CORS para permitir requisições da extensão
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/solve")
async def solve(file: UploadFile = File(...)):
    with open("temp.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = process_image("temp.png")
    os.remove("temp.png")
    return {"captcha": text}
