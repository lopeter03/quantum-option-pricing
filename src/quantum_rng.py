import requests
import numpy as np

def generate_classical(size: int) -> np.ndarray:
    """Generate classical random numbers using NumPy."""
    return np.random.rand(size)

def generate_quantum(size: int) -> np.ndarray:
    """Fetch quantum random numbers from ANU Quantum RNG API with fallback."""
    try:
        url = f"https://qrng.anu.edu.au/API/jsonI.php?length={size}&type=uint8"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return np.array(data['data']) / 255.0
    except Exception:
        # Fallback to classical RNG if API fails
        return np.random.rand(size)
