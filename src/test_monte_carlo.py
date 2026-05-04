from monte_carlo import simulate_paths, price_option
from quantum_rng import generate_classical

def test_simulate_paths():
    paths = simulate_paths(100, 1, 0.05, 0.2, 10, 100, generate_classical)
    assert paths.shape == (100, 11)

def test_price_option():
    paths = simulate_paths(100, 1, 0.05, 0.2, 10, 100, generate_classical)
    price = price_option(paths, 100, 0.05, 1)
    assert price >= 0
