import argparse
import matplotlib.pyplot as plt
from monte_carlo import simulate_paths, price_option
from quantum_rng import generate_classical, generate_quantum

def plot_histogram(data, title="Histogram"):
    plt.hist(data, bins=50, alpha=0.7)
    plt.title(title)
    plt.show()

def plot_convergence(prices, title="Convergence Plot"):
    plt.plot(prices)
    plt.title(title)
    plt.xlabel("Simulation")
    plt.ylabel("Option Price")
    plt.show()

def plot_compare(classical_data, quantum_data):
    plt.hist(classical_data, bins=50, alpha=0.5, label="Classical")
    plt.hist(quantum_data, bins=50, alpha=0.5, label="Quantum")
    plt.title("Classical vs Quantum Comparison")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--convergence", action="store_true")
    parser.add_argument("--compare", action="store_true")
    args = parser.parse_args()

    if args.convergence:
        # Example convergence data
        prices = [100 + (10/i) for i in range(1, 51)]
        plot_convergence(prices, "Convergence Plot")

    if args.compare:
        # Generate sample classical and quantum data
        classical_paths = simulate_paths(100, 1, 0.05, 0.2, 100, 5000, generate_classical)
        quantum_paths = simulate_paths(100, 1, 0.05, 0.2, 100, 5000, generate_quantum)
        plot_compare(classical_paths[:, -1], quantum_paths[:, -1])
