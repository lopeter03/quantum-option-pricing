from visualization import plot_histogram, plot_convergence

def test_plot_histogram():
    data = [1, 2, 3, 4, 5]
    plot_histogram(data, "Test Histogram")  # should run without error

def test_plot_convergence():
    prices = [10, 12, 11, 13, 12]
    plot_convergence(prices, "Test Convergence")  # should run without error
