import importlib.util
from pathlib import Path
import sys


def _load_chibi_battle_class():
    engine_path = Path(__file__).resolve().parent / "核心戰鬥引擎.py"
    spec = importlib.util.spec_from_file_location("core_battle_engine", engine_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"無法載入核心戰鬥引擎模組: {engine_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.ChibiBattle


ChibiBattle = _load_chibi_battle_class()


def main() -> None:
    """簡化版入口，保留同樣規則但程式更短。"""
    root = Path(__file__).resolve().parent.parent
    game = ChibiBattle()
    game.load_generals(root / "generals.txt")
    game.run_full_battle(waves=3)


if __name__ == "__main__":
    main()
