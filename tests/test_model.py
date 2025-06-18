import numpy as np
from src.model import load_model, predict_sign

def test_load_model():
    model = load_model("data/keypoints/a.h5")
    assert model is not None

def test_predict_sign():
    model = load_model("data/keypoints/a.h5")
    dummy_input = np.random.rand(1, 15, 1662)
    result = predict_sign(model, dummy_input)
    assert isinstance(result, int)
