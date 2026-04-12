from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass
from pathlib import Path
from tkinter import messagebox
from typing import Dict, List, Optional


@dataclass
class Unit:
    faction: str
    name: str
    hp: int
    atk: int
    def_: int
    spd: int
    is_leader: bool
    current_hp: int

    @property
    def alive(self) -> bool:
        return self.current_hp > 0


class ChibiBattleVisualGame:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("赤壁之戰")
        self.root.geometry("1180x760")
        self.root.configure(bg="#101820")
        self._set_app_icon()

        self.units: Dict[str, Unit] = {}
        self.turn_order: List[str] = []
        self.turn_index = 0
        self.current_attacker: Optional[str] = None
        self.auto_mode = False

        self.target_var = tk.StringVar(value="請先開始回合")

        self._build_ui()
        self.start_new_game()
        self._bring_to_front()

    def _bring_to_front(self) -> None:
        self.root.update_idletasks()
        self.root.deiconify()
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.focus_force()
        self.root.after(500, lambda: self.root.attributes("-topmost", False))

    def _set_app_icon(self) -> None:
        icon_dir = Path(__file__).resolve().parent / "遊戲圖片"
        for icon_path in [icon_dir / "app圖示.gif", icon_dir / "app圖示.png"]:
            if not icon_path.exists() or not icon_path.is_file():
                continue
            try:
                self._app_icon = tk.PhotoImage(file=str(icon_path))
                self.root.iconphoto(True, self._app_icon)
                return
            except tk.TclError:
                continue
        self._app_icon = None

    def _build_ui(self) -> None:
        top = tk.Frame(self.root, bg="#1e2a36", padx=12, pady=8)
        top.pack(fill=tk.X)

        tk.Label(
            top,
            text="赤壁之戰",
            bg="#1e2a36",
            fg="#ffd966",
            font=("PingFang TC", 18, "bold"),
        ).pack(side=tk.LEFT)

        controls = tk.Frame(top, bg="#1e2a36")
        controls.pack(side=tk.RIGHT)
        tk.Button(controls, text="重新開始", width=10, command=self.start_new_game).pack(side=tk.LEFT, padx=4)
        tk.Button(controls, text="下一回合", width=10, command=self.next_turn).pack(side=tk.LEFT, padx=4)
        self.btn_auto = tk.Button(controls, text="開始自動戰鬥", width=12, command=self.toggle_auto)
        self.btn_auto.pack(side=tk.LEFT, padx=4)

        body = tk.Frame(self.root, bg="#101820")
        body.pack(fill=tk.BOTH, expand=True)

        left = tk.Frame(body, bg="#0f1419", bd=1, relief=tk.SOLID)
        left.place(relx=0.01, rely=0.02, relwidth=0.64, relheight=0.96)

        tk.Label(
            left,
            text="LEFT PANEL OK - 戰場總覽",
            bg="#0f1419",
            fg="#ff6b6b",
            font=("Menlo", 14, "bold"),
            anchor="w",
            padx=10,
            pady=6,
        ).pack(fill=tk.X)

        self.left_text = tk.Text(
            left,
            bg="#0f1419",
            fg="#e8eef5",
            insertbackground="#e8eef5",
            font=("Menlo", 13),
            relief=tk.FLAT,
            wrap=tk.WORD,
        )
        self.left_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        right = tk.Frame(body, bg="#ffffff", bd=1, relief=tk.SOLID)
        right.place(relx=0.67, rely=0.02, relwidth=0.32, relheight=0.96)

        op = tk.LabelFrame(right, text="你的操作", bg="#ffffff", fg="#111111", font=("PingFang TC", 12, "bold"), padx=10, pady=10)
        op.pack(fill=tk.X, padx=10, pady=10)

        self.turn_info = tk.Label(op, text="回合資訊：", bg="#ffffff", fg="#111111", font=("PingFang TC", 12, "bold"), anchor="w")
        self.turn_info.pack(fill=tk.X, pady=(0, 8))

        tk.Label(op, text="選擇攻擊目標（魏軍）", bg="#ffffff", fg="#111111", anchor="w").pack(fill=tk.X)
        self.target_menu = tk.OptionMenu(op, self.target_var, "請先開始回合")
        self.target_menu.configure(width=24, bg="#f8f8f8", fg="#111111")
        self.target_menu.pack(fill=tk.X, pady=(6, 8))

        self.attack_btn = tk.Button(op, text="發動攻擊", command=self.player_attack, state=tk.DISABLED)
        self.attack_btn.pack(fill=tk.X)

        self.log_text = tk.Text(
            right,
            bg="#ffffff",
            fg="#111111",
            insertbackground="#111111",
            font=("Menlo", 11),
            wrap=tk.WORD,
            relief=tk.SUNKEN,
            bd=1,
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        self.log_text.configure(state=tk.DISABLED)

    def load_generals(self, filename: Path) -> Dict[str, Unit]:
        units: Dict[str, Unit] = {}
        with filename.open("r", encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line:
                    continue
                if line == "EOF":
                    break
                faction, name, hp, atk, def_, spd, is_leader = line.split()
                hp_i = int(hp)
                units[name] = Unit(
                    faction=faction,
                    name=name,
                    hp=hp_i,
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == "True"),
                    current_hp=hp_i,
                )
        return units

    def start_new_game(self) -> None:
        base = Path(__file__).resolve().parent.parent
        self.units = self.load_generals(self._resolve_generals_file(base))
        self.turn_order = self._alive_sorted_names()
        self.turn_index = 0
        self.current_attacker = None
        self.auto_mode = False
        self.btn_auto.config(text="開始自動戰鬥")

        self._refresh_left_panel()
        self._set_controls(False)
        self._set_turn_info("新遊戲已開始，按『下一回合』")
        self._log("=== 赤壁之戰開始 ===")

    def _resolve_generals_file(self, base: Path) -> Path:
        candidates = ["generals.txt", "角色資料主檔.txt"]
        for name in candidates:
            path = base / name
            if path.exists() and path.is_file():
                return path
        return base / candidates[0]

    def _alive_sorted_names(self) -> List[str]:
        alive = [u for u in self.units.values() if u.alive]
        alive.sort(key=lambda u: (-u.spd, u.name))
        return [u.name for u in alive]

    def _alive_faction(self, factions: List[str]) -> List[str]:
        return [u.name for u in self.units.values() if u.faction in factions and u.alive]

    def _pick_ai_target(self, names: List[str]) -> str:
        return min(names, key=lambda n: (self.units[n].current_hp, n))

    def _calc_damage(self, a: Unit, d: Unit) -> int:
        base = max(1, a.atk - d.def_)
        return base + 2 if a.is_leader else base

    def _refresh_left_panel(self) -> None:
        lines: List[str] = []
        lines.append("[系統] 左側面板正常渲染")
        lines.append("=" * 42)
        for faction in ["蜀", "吳", "魏"]:
            lines.append(f"\n【{faction}軍】")
            members = [u for u in self.units.values() if u.faction == faction]
            members.sort(key=lambda u: (-u.spd, u.name))
            for u in members:
                role = "軍師" if u.is_leader else "武將"
                bar_len = int((u.current_hp / u.hp) * 20) if u.hp else 0
                bar = "█" * bar_len + "░" * (20 - bar_len)
                state = "陣亡" if not u.alive else "存活"
                lines.append(f"{u.name:4} {bar} {u.current_hp:>3}/{u.hp:<3} {state} {role} 攻{u.atk} 防{u.def_} 速{u.spd}")

        self.left_text.configure(state=tk.NORMAL)
        self.left_text.delete("1.0", tk.END)
        self.left_text.insert(tk.END, "\n".join(lines))
        self.left_text.configure(state=tk.DISABLED)

    def _log(self, msg: str) -> None:
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.insert(tk.END, msg + "\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state=tk.DISABLED)

    def _set_turn_info(self, text: str) -> None:
        self.turn_info.config(text=f"回合資訊：{text}")

    def _set_target_options(self, targets: List[str]) -> None:
        menu = self.target_menu["menu"]
        menu.delete(0, "end")
        for n in targets:
            menu.add_command(label=n, command=lambda x=n: self.target_var.set(x))
        self.target_var.set(targets[0] if targets else "無可選目標")

    def _set_controls(self, enabled: bool, targets: Optional[List[str]] = None) -> None:
        if enabled and targets:
            self._set_target_options(targets)
            self.attack_btn.config(state=tk.NORMAL)
        else:
            self._set_target_options([])
            self.attack_btn.config(state=tk.DISABLED)

    def _next_attacker(self) -> Optional[str]:
        if not self._alive_faction(["蜀", "吳"]) or not self._alive_faction(["魏"]):
            return None
        while True:
            if not self.turn_order or self.turn_index >= len(self.turn_order):
                self.turn_order = self._alive_sorted_names()
                self.turn_index = 0
                if not self.turn_order:
                    return None
            name = self.turn_order[self.turn_index]
            self.turn_index += 1
            if self.units[name].alive:
                return name

    def _apply_attack(self, attacker_name: str, defender_name: str) -> None:
        a = self.units[attacker_name]
        d = self.units[defender_name]
        damage = self._calc_damage(a, d)
        d.current_hp = max(0, d.current_hp - damage)
        self._log(f"{a.name} 攻擊 {d.name}，造成 {damage} 傷害")
        if not d.alive:
            self._log(f"{d.name} 已被擊敗")
        self._refresh_left_panel()

    def _game_over(self) -> bool:
        allied = self._alive_faction(["蜀", "吳"])
        wei = self._alive_faction(["魏"])
        if allied and wei:
            return False

        self._set_controls(False)
        self.auto_mode = False
        self.btn_auto.config(text="開始自動戰鬥")

        if allied:
            msg = "蜀吳聯軍獲勝！"
        elif wei:
            msg = "魏軍獲勝！"
        else:
            msg = "雙方同歸於盡！"
        self._set_turn_info(msg)
        self._log("=== 戰鬥結束 ===")
        self._log(msg)
        messagebox.showinfo("戰鬥結束", msg)
        return True

    def next_turn(self) -> None:
        if self._game_over():
            return
        attacker_name = self._next_attacker()
        if attacker_name is None:
            return

        self.current_attacker = attacker_name
        attacker = self.units[attacker_name]

        if attacker.faction in ["蜀", "吳"]:
            targets = self._alive_faction(["魏"])
            if not targets:
                self._game_over()
                return
            self._set_turn_info(f"輪到 {attacker.name}，請選擇目標")
            self._set_controls(True, targets)
            if self.auto_mode:
                self.root.after(120, self.player_attack)
        else:
            targets = self._alive_faction(["蜀", "吳"])
            if not targets:
                self._game_over()
                return
            t = self._pick_ai_target(targets)
            self._set_turn_info(f"輪到 {attacker.name}（魏軍）")
            self._apply_attack(attacker.name, t)
            self._set_controls(False)
            if self.auto_mode and not self._game_over():
                self.root.after(350, self.next_turn)

    def player_attack(self) -> None:
        if self.current_attacker is None:
            return
        attacker = self.units[self.current_attacker]
        if attacker.faction not in ["蜀", "吳"]:
            return

        target = self.target_var.get().strip()
        if not target or target in ["無可選目標", "請先開始回合"]:
            return
        if target not in self.units or not self.units[target].alive:
            messagebox.showwarning("無效目標", "請重新選擇存活的目標")
            return

        self._apply_attack(attacker.name, target)
        self._set_controls(False)
        if self.auto_mode and not self._game_over():
            self.root.after(350, self.next_turn)

    def toggle_auto(self) -> None:
        self.auto_mode = not self.auto_mode
        if self.auto_mode:
            self.btn_auto.config(text="停止自動戰鬥")
            self._log("[系統] 自動戰鬥已啟用")
            self.next_turn()
        else:
            self.btn_auto.config(text="開始自動戰鬥")
            self._log("[系統] 自動戰鬥已停止")


def main() -> None:
    root = tk.Tk()
    try:
        app = ChibiBattleVisualGame(root)
    except FileNotFoundError:
        messagebox.showerror("檔案錯誤", "找不到 generals.txt 或 角色資料主檔.txt，請確認 week-07 資料完整")
        root.destroy()
        return

    app._log("[系統] 視窗已啟動")
    app._log("提示：按『下一回合』開始")
    root.mainloop()


if __name__ == "__main__":
    main()
