import pytest
from my_ai_lib import main

def test_main_runs():
    # Asumimos que `main.run_pipeline()` existe
    result = main.run_pipeline()
    assert result is not None
