import pytest
from my_ai_lib.models import model_factory

def test_create_model():
    # Asumamos que `create_model` devuelve un string o dict según el tipo
    model = model_factory.create_model("linear")
    assert model is not None
