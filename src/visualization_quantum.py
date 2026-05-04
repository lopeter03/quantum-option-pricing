import numpy as np
import matplotlib.pyplot as plt
from monte_carlo import simulate_paths, price_option
from quantum_rng import generate_quantum

def plot_convergence(prices, title="Convergence Plot"):
    plt.plot(prices)
    plt.title(title)
    plt.xlabel("Simulation")
    plt.ylabel("Option Price")
    plt.show()

if __name__ == "__main__":
    # Parameters
    S0, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    steps, n_paths = 100, 5000

    # Generate quantum paths
    paths = simulate_paths(S0, T, r, sigma, steps, n_paths, generate_quantum)

    # Build convergence evidence
    prices = []
    for i in range(100, n_paths, 100):
        partial_paths = paths[:i]
        prices.append(price_option(partial_paths, K, r, T))

    plot_convergence(prices, "Quantum Convergence Plot")
