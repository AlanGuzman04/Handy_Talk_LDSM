import pytest
from src.utils import normalize_keypoints, convert_to_text

def test_normalize_keypoints():
    input_data = [0.5, 0.6, 0.7]
    expected = [0.0, 0.1, 0.2]
    result = normalize_keypoints(input_data)
    assert result == pytest.approx(expected, abs=0.01)

def test_convert_to_text():
    prediction = 2
    label_map = {0: "a", 1: "b", 2: "c"}
    assert convert_to_text(prediction, label_map) == "c"
