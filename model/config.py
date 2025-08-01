# Estrutura de arquivos de um projeto simples para treinar e usar um modelo CNN com TensorFlow

# ===== config.py =====
# Define configurações globais
characters = list("abcdefghijklmnopqrstuvwxyz0123456789")
num_classes = len(characters)
image_width = 160
image_height = 60
captcha_length = 6