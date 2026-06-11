import random


def make_data(n: int, seed: int = 42) -> list:
    """Return a list of n reproducible random integers."""
    raise NotImplementedError


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    """Run a benchmark for sorting methods and return a results dictionary."""
    raise NotImplementedError
