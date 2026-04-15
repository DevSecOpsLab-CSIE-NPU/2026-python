from __future__ import annotations

import importlib.util
import pathlib
import subprocess
import sys
from types import ModuleType


BASE_DIR = pathlib.Path(__file__).resolve().parent


def load_module(file_name: str) -> ModuleType:
    file_path = BASE_DIR / file_name
    module_name = file_name.replace("-", "_").replace(".", "_")
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module: {file_name}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_script(file_name: str, input_data: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(BASE_DIR / file_name)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout
