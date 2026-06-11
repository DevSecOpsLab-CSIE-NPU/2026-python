import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    """Load benchmark results from a JSON file."""
    raise NotImplementedError


def plot_results(results: dict, out_path: str) -> None:
    """Plot benchmark results and save them to out_path."""
    raise NotImplementedError
