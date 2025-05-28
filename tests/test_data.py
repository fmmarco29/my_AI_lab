import pytest
from my_ai_lib.data import dataset, preprocess

def test_load_data():
    # Asumamos que `load_data` devuelve un dict vacío o similar
    data = dataset.load_data()
    assert isinstance(data, dict)

def test_preprocess_data():
    # Asumamos que `preprocess_data` toma un dict y lo devuelve igual (dummy)
    raw_data = {"value": 1}
    processed = preprocess.preprocess_data(raw_data)
    assert isinstance(processed, dict)
    assert "value" in processed
