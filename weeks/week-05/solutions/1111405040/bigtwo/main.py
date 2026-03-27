"""
Big Two 執行入口。
"""

from __future__ import annotations

from ui.app import BigTwoApp


def main() -> None:
    app = BigTwoApp()
    winner = app.run()
    if winner is not None:
        print(f"遊戲結束，贏家是 {winner.name}。")


if __name__ == "__main__":
    main()
