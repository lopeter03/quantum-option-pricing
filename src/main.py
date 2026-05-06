import argparse
from quantum_rng import generate_classical, generate_quantum
from monte_carlo import simulate_paths, price_option
from visualization import plot_histogram

def run_pipeline(rng_choice="both", show_plots=True):

    S0, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    steps, n_paths = 100, 10000

    if rng_choice == "classical":
        paths = simulate_paths(S0, T, r, sigma, steps, n_paths, generate_classical)
        price = price_option(paths, K, r, T)
        print("Classical RNG Price:", price)
        if show_plots:   # ✅ ensures pytest also opens the plot
            plot_histogram(paths[:, -1], "Classical RNG Distribution")

    elif rng_choice == "quantum":
        paths = simulate_paths(S0, T, r, sigma, steps, n_paths, generate_quantum)
        price = price_option(paths, K, r, T)
        print("Quantum RNG Price:", price)
        if show_plots:   # ✅ ensures pytest also opens the plot
            plot_histogram(paths[:, -1], "Quantum RNG Distribution")

    elif rng_choice == "both":
        classical_paths = simulate_paths(S0, T, r, sigma, steps, n_paths, generate_classical)
        quantum_paths = simulate_paths(S0, T, r, sigma, steps, n_paths, generate_quantum)

        classical_price = price_option(classical_paths, K, r, T)
        quantum_price = price_option(quantum_paths, K, r, T)

        print("Classical RNG Price:", classical_price)
        print("Quantum RNG Price:", quantum_price)

        if show_plots:   # ✅ both plots shown
            plot_histogram(classical_paths[:, -1], "Classical RNG Distribution")
            plot_histogram(quantum_paths[:, -1], "Quantum RNG Distribution")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rng", choices=["classical", "quantum", "both"], default="both",
                        help="Choose RNG type: classical, quantum, or both")
    args = parser.parse_args()
    run_pipeline(args.rng, show_plots=True)
