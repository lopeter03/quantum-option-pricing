import numpy as np

def simulate_paths(S0, T, r, sigma, steps, n_paths, rng_func):
    """Simulate asset price paths using RNG function."""
    dt = T / steps
    paths = np.zeros((n_paths, steps + 1))
    paths[:, 0] = S0
    for t in range(1, steps + 1):
        z = rng_func(n_paths)
        paths[:, t] = paths[:, t-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
    return paths

def price_option(paths, K, r, T):
    """Price European call option using simulated paths."""
    payoffs = np.maximum(paths[:, -1] - K, 0)
    return np.exp(-r * T) * np.mean(payoffs)
