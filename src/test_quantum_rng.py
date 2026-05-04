import numpy as np
from quantum_rng import generate_classical, generate_quantum

def test_generate_classical():
    data = generate_classical(1000)
    assert len(data) == 1000
    assert np.all((data >= 0) & (data <= 1))

def test_generate_quantum():
    data = generate_quantum(1000)
    assert len(data) == 1000
    assert np.all((data >= 0) & (data <= 1))
