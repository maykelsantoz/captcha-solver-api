# ===== predict.py =====
# Faz a predição com uma imagem nova
def predict_captcha(image_path):
    model = tf.keras.models.load_model('captcha_model.h5')
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (image_width, image_height))
    img = img / 255.0
    img = img.reshape((1, image_height, image_width, 1))

    prediction = model.predict(img)
    result = ''.join(characters[np.argmax(p)] for p in prediction)
    return result

# Exemplo de uso
if __name__ == '__main__':
    print(predict_captcha('data/train/57h79y.png'))
