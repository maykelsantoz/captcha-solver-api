import os
import requests

captchas = {
    "57h79y": "https://sistec.mec.gov.br/captcha/91f1ee84b5c842018cc6db00f3c5016e.png",
    "v966u4": "https://sistec.mec.gov.br/captcha/2a72cc578ad745f97c2a38b2123c5471.png",
    "ze4ot3": "https://sistec.mec.gov.br/captcha/ac1a78c970e38308400f9742431103c2.png",
    "c39ihy": "https://sistec.mec.gov.br/captcha/143b8d745676e8b3a2d0eeaf13f9029b.png",
    "da68m2": "https://sistec.mec.gov.br/captcha/2062e288bc60abc3aa2d8931a41c979d.png",
    "64s84e": "https://sistec.mec.gov.br/captcha/5a03b41a4669c4ea49135cd9812e5afd.png",
    "p89ozu": "https://sistec.mec.gov.br/captcha/3edb080926a253150db43751ca1fde76.png",
    "66sak6": "https://sistec.mec.gov.br/captcha/e9a4cc7f5a7b08f79f6abeefae33c5fa.png",
    "h9g4ne": "https://sistec.mec.gov.br/captcha/d2eee1b77f77e50904035774295e1e87.png",
    "s27u73": "https://sistec.mec.gov.br/captcha/b395df334c069b8f4860cdcf51e8c3f6.png",
}

os.makedirs("data/train", exist_ok=True)

for name, url in captchas.items():
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(f"data/train/{name}.png", "wb") as f:
                f.write(response.content)
            print(f"[OK] Baixou {name}")
        else:
            print(f"[ERRO] {name} -> status {response.status_code}")
    except Exception as e:
        print(f"[ERRO] {name} -> {e}")
