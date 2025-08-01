# CAPTCHA Solver API

API que resolve CAPTCHAs com letras minúsculas e números usando OCR (Tesseract).

## Deploy no Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

## Como usar

`POST /solve`

Envie a imagem (multipart/form-data) com chave `file`:
```bash
curl -X POST -F "file=@captcha.png" https://seu-endpoint.onrender.com/solve
```

Resposta:
```json
{ "captcha": "d7r3g5" }
```
