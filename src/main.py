import argparse
from quantum_rng import generate_classical, generate_quantum
from monte_carlo import simulate_paths, price_option
from visualization import plot_histogram, plot_convergence

def run_pipeline(rng_choice):
    S0, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    steps, n_paths = 100, 10000

    if rng_choice == "classical":
        paths = simulate_paths(S0, T, r, sigma, steps, n_paths, generate_classical)
        price = price_option(paths, K, r, T)
        print("Classical RNG Price:", price)
        plot_histogram(paths[:, -1], "Classical RNG Distribution")

    elif rng_choice == "quantum":
        paths = simulate_paths(S0, T, r, sigma, steps, n_paths, generate_quantum)
        price = price_option(paths, K, r, T)
        print("Quantum RNG Price:", price)
        plot_histogram(paths[:, -1], "Quantum RNG Distribution")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rng", choices=["classical", "quantum"], required=True,
                        help="Choose RNG type: classical or quantum")
    args = parser.parse_args()
    run_pipeline(args.rng)
