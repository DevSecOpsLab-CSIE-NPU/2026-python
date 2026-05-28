from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_solution(filename: str):
    path = BASE_DIR / filename
    module_name = path.stem.replace("-", "_")
    spec = spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load solution module: {path}")

    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
