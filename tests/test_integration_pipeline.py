import numpy as np
from src.model import load_model, predict_sign
from src.utils import convert_to_text
from src.database import save_translation, get_last_translation

def test_full_prediction_pipeline():
    # Simular entrada
    input_data = np.random.rand(1, 15, 1662)

    # Cargar modelo
    model = load_model("data/keypoints/a.h5")

    # Predecir
    prediction = predict_sign(model, input_data)

    # Convertir
    label_map = {0: "a", 1: "b", 2: "c"}
    text = convert_to_text(prediction, label_map)

    # Guardar en la base de datos
    save_translation(text)

    # Verificar
    assert get_last_translation() == text
