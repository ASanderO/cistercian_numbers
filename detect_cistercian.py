import cv2
import numpy as np
from keras.models import model_from_json
from tensorflow.keras.models import load_model
import os


# Função para carregar o modelo treinado
def load_trained_model(model_json_path, model_weights_path):
    # Carregar a arquitetura do modelo
    with open(model_json_path, 'r') as json_file:
        loaded_model_json = json_file.read()
    model = model_from_json(loaded_model_json)

    # Carregar os pesos do modelo
    model.load_weights(model_weights_path)
    return model


# Função para pré-processar a imagem
def preprocess_image(image_path, target_size=(48, 48)):
    # Verificar se o caminho da imagem é válido
    if not os.path.exists(image_path):
        raise ValueError(f"O caminho da imagem {image_path} não existe.")

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Erro ao carregar a imagem de {image_path}.")

    # Redimensionar a imagem
    image = cv2.resize(image, target_size)
    # Normalizar a imagem
    image = image.astype('float32') / 255.0
    # Expandir dimensões para corresponder ao formato do modelo
    image = np.expand_dims(image, axis=-1)  # Adicionar canal
    image = np.expand_dims(image, axis=0)  # Adicionar batch
    return image


# Função para fazer a predição
def predict_number(model, image_path, class_labels):
    # Pré-processar a imagem
    image = preprocess_image(image_path)

    # Fazer predição
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)[0]

    return class_labels[predicted_class]


# Caminhos para o modelo treinado
model_json_path = "models_number/number_model.json"
model_weights_path = "models_number/number_model.weights.h5"

# Carregar o modelo treinado
model = load_trained_model(model_json_path, model_weights_path)

# Dicionário de classes (ajuste conforme suas classes)
class_labels = {
    0: "Zero",
    1: "Um",
    2: "Dois",
    3: "Três",
    4: "Quatro",
    5: "Cinco",
    6: "Seis",
    7: "Sete",
    8: "Oito",
    9: "Nove",
    10: "Dez",
    # Adicione os outros números conforme necessário
}

# Caminho para a imagem a ser predita
image_path = '5_validation.png'  # Ajuste este caminho conforme necessário

# Fazer a predição
predicted_label = predict_number(model, image_path, class_labels)

# Exibir o resultado
print(f"Predicted Class: {predicted_label}")
