# U02. GCD 閃燈觀察器（課堂互動遊戲）
# tkinter 視覺化：藉由不同閃燈間隔，觀察最大公因數 (GCD) 與最小公倍數 (LCM)
#
# 玩法：
#   1. 按「▶ 開始」讓燈開始閃爍。
#   2. 觀察哪幾盞燈同時亮起 → 那個節拍就是它們的最小公倍數 (LCM)。
#   3. 調整間隔，找出讓所有燈同時亮起需要最久的組合。
#   4. 按「⏭ 一拍」逐拍推進，仔細觀察每一拍的狀態。

import tkinter as tk
from math import gcd
from functools import reduce


def multi_gcd(nums):
    """計算一組數字的最大公因數"""
    return reduce(gcd, nums)


def multi_lcm(nums):
    """計算一組數字的最小公倍數"""
    result = nums[0]
    for n in nums[1:]:
        # 公式：LCM(a, b) = (a * b) // GCD(a, b)
        result = result * n // gcd(result, n)
    return result


# ── 每個燈的外觀與初始設定 ──────────────────────────────────────
CONFIGS = [
    {"name": "A", "default": 2, "on": "#FF5252", "off": "#2D0A0A", "ring": "#FF8A80"},
    {"name": "B", "default": 3, "on": "#69F0AE", "off": "#0A2D1A", "ring": "#A5D6A7"},
    {"name": "C", "default": 4, "on": "#448AFF", "off": "#0A1A2D", "ring": "#82B1FF"},
    {"name": "D", "default": 6, "on": "#FFD740", "off": "#2D220A", "ring": "#FFE57F"},
]

BG    = "#0D0D1A"   # 視窗背景顏色
PANEL = "#16213E"   # 儀表板背景顏色


class GCDBlinkGame:
    LIGHT_R  = 52   # 燈光圓形半徑（像素）
    COL_W    = 160  # 每個燈佔用的水平寬度
    CANVAS_H = 260  # 畫布高度

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GCD 閃燈觀察器")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.tick    = 0      # 當前節拍
        self.running = False  # 是否正在運行
        self._job    = None   # 用於儲存 root.after 的任務 ID
        self.tick_ms = 700    # 預設每拍的時間間隔 (毫秒)

        self.n     = len(CONFIGS)
        # 使用 IntVar 來動態儲存與更新每盞燈的閃爍間隔
        self.ivars = [tk.IntVar(value=c["default"]) for c in CONFIGS]

        self._build_ui()   # 建構使用者介面
        self._refresh()    # 初始刷新數據
        self.root.mainloop()

    # ── UI 建構邏輯 ───────────────────────────────────────────

    def _build_ui(self):
        """建構主視窗的所有元件"""
        # 標題區
        tk.Label(self.root, text="GCD 閃燈觀察器", bg=BG, fg="#E94560",
                 font=("Segoe UI", 18, "bold")).pack(pady=(12, 0))
        tk.Label(self.root,
                 text="哪幾盞燈同時亮起？那個節拍 = LCM！  GCD 是各週期的最大公因子",
                 bg=BG, fg="#445566", font=("Segoe UI", 9)).pack(pady=(2, 8))

        # 燈光畫布區
        cw = self.COL_W * self.n + 40
        self.cv = tk.Canvas(self.root, width=cw, height=self.CANVAS_H,
                            bg=PANEL, highlightthickness=0)
        self.cv.pack(padx=20)
        self._build_lights()

        # 資訊顯示列（節拍 / GCD / LCM / 同步提示）
        info = tk.Frame(self.root, bg=PANEL)
        info.pack(fill="x", padx=20, pady=(6, 0))

        self.lbl_tick = tk.Label(info, text="節拍：0", bg=PANEL, fg="#CCC",
                                 font=("Segoe UI", 14, "bold"), width=11, anchor="w")
        self.lbl_tick.pack(side="left", padx=14, pady=6)

        self.lbl_gcd = tk.Label(info, text="GCD = ?", bg=PANEL, fg="#69F0AE",
                                font=("Segoe UI", 14, "bold"), width=10)
        self.lbl_gcd.pack(side="left")

        self.lbl_lcm = tk.Label(info, text="LCM = ?", bg=PANEL, fg="#82B1FF",
                                font=("Segoe UI", 14, "bold"), width=10)
        self.lbl_lcm.pack(side="left")

        self.lbl_sync = tk.Label(info, text="", bg=PANEL, fg="#FFD740",
                                 font=("Segoe UI", 11, "bold"))
        self.lbl_sync.pack(side="right", padx=14)

        # 間隔調整控制項 (Spinbox)
        row = tk.Frame(self.root, bg=BG)
        row.pack(pady=(10, 0))
        for i, (cfg, iv) in enumerate(zip(CONFIGS, self.ivars)):
            tk.Label(row, text=f"燈 {cfg['name']}", bg=BG, fg=cfg["ring"],
                     font=("Segoe UI", 10, "bold")).grid(row=0, column=i*2, padx=(12, 2))
            # 設定 Spinbox，當數值改變時調用 _refresh
            tk.Spinbox(row, from_=1, to=20, textvariable=iv, width=3,
                       font=("Segoe UI", 12), bg=PANEL, fg="#EEE",
                       buttonbackground="#1F3060", justify="center",
                       state="readonly", command=self._refresh).grid(
                           row=0, column=i*2+1, padx=(2, 12))

        # 速度控制滑桿 (Scale)
        sp = tk.Frame(self.root, bg=BG)
        sp.pack(pady=(8, 0))
        tk.Label(sp, text="速度 (ms/拍):", bg=BG, fg="#888",
                 font=("Segoe UI", 10)).pack(side="left")
        self.speed_scale = tk.Scale(
            sp, from_=150, to=2000, orient="horizontal", length=220,
            bg=BG, fg="#CCC", troughcolor=PANEL, highlightthickness=0,
            resolution=50, command=lambda v: setattr(self, "tick_ms", int(v)))
        self.speed_scale.set(self.tick_ms)
        self.speed_scale.pack(side="left", padx=6)

        # 底部控制按鈕
        btns = tk.Frame(self.root, bg=BG)
        btns.pack(pady=12)

        def mk_btn(text, fg, cmd):
            return tk.Button(btns, text=text, font=("Segoe UI", 12, "bold"),
                             bg="#0F3460", fg=fg, activebackground="#E94560",
                             width=7, relief="flat", cursor="hand2", command=cmd)

        self.b_start = mk_btn("▶ 開始", "#69F0AE", self.start)
        self.b_start.pack(side="left", padx=6)

        self.b_step = mk_btn("⏭ 一拍", "#82B1FF", self.step)
        self.b_step.pack(side="left", padx=6)

        self.b_pause = mk_btn("⏸ 暫停", "#FFD740", self.pause)
        self.b_pause.pack(side="left", padx=6)
        self.b_pause.config(state="disabled")

        mk_btn("↺ 重置", "#FF8A80", self.reset).pack(side="left", padx=6)

    def _build_lights(self):
        """在畫布上繪製燈光圓圈、字母、進度環等"""
        R = self.LIGHT_R
        self.ovals      = []  # 存儲圓形燈 ID
        self.oval_names = []  # 存儲文字名稱 ID
        self.rings      = []  # 存儲進度環 ID
        self.cnt_texts  = []  # 存儲倒數數字 ID
        self.iv_texts   = []  # 存儲間隔說明文字 ID

        for i, cfg in enumerate(CONFIGS):
            cx = self.COL_W * i + self.COL_W // 2 + 20
            cy = self.CANVAS_H // 2

            # 倒數進度環：顯示距離下次亮燈的進度
            ring = self.cv.create_arc(
                cx-R-10, cy-R-10, cx+R+10, cy+R+10,
                start=90, extent=0,
                outline=cfg["ring"], width=4, style="arc"
            )
            self.rings.append(ring)

            # 主燈圓形：平常為暗色
            oval = self.cv.create_oval(
                cx-R, cy-R, cx+R, cy+R,
                fill=cfg["off"], outline="", width=0
            )
            self.ovals.append(oval)

            # 燈號字母 (A, B, C, D)
            name = self.cv.create_text(
                cx, cy - 8,
                text=cfg["name"], font=("Segoe UI", 22, "bold"), fill="#444"
            )
            self.oval_names.append(name)

            # 倒數數字（例如：還有 3 拍亮燈）
            cnt = self.cv.create_text(
                cx, cy + 14,
                text=str(cfg["default"]), font=("Segoe UI", 11), fill="#555"
            )
            self.cnt_texts.append(cnt)

            # 底部間隔說明文字
            iv_txt = self.cv.create_text(
                cx, cy + R + 22,
                text=f"每 {cfg['default']} 拍",
                font=("Segoe UI", 10), fill=cfg["ring"]
            )
            self.iv_texts.append(iv_txt)

    # ── 遊戲邏輯與更新 ──────────────────────────────────────────

    def _intervals(self):
        """取得目前四盞燈設定的閃爍間隔清單"""
        return [max(1, v.get()) for v in self.ivars]

    def _refresh(self):
        """當玩家手動調整間隔後，重新計算 GCD/LCM 並更新畫布文字"""
        ivs = self._intervals()
        self.lbl_gcd.config(text=f"GCD = {multi_gcd(ivs)}")
        self.lbl_lcm.config(text=f"LCM = {multi_lcm(ivs)}")
        for i, iv in enumerate(ivs):
            self.cv.itemconfig(self.iv_texts[i], text=f"每 {iv} 拍")
        self._update_rings()

    def _update_rings(self):
        """根據當前節拍與各燈間隔，更新畫布上的進度環與倒數文字"""
        for i, iv in enumerate(self._intervals()):
            # 剩餘拍數 = 間隔 - (目前節拍 % 間隔)
            # 如果餘數為 0，代表剛好到達亮燈點
            remaining = iv - (self.tick % iv)
            extent = -(360 * remaining / iv)    # 圓弧程度 (負值為順時針)
            self.cv.itemconfig(self.rings[i], extent=extent)
            self.cv.itemconfig(self.cnt_texts[i], text=str(remaining))

    def _advance(self):
        """核心邏輯：推進一個節拍，判斷哪些燈需要亮起"""
        self.tick += 1
        self.lbl_tick.config(text=f"節拍：{self.tick}")
        self._update_rings()

        ivs    = self._intervals()
        # 找出哪些燈在此拍亮起 (節拍可被間隔整除)
        synced = [i for i, iv in enumerate(ivs) if self.tick % iv == 0]

        for i in synced:
            self._blink_on(i)

        if len(synced) == self.n:
            # 全部燈同時亮起 → 節拍必然是 LCM 的倍數
            self.lbl_sync.config(text="✨ 全部同步！= LCM", fg="#FFD740")
            self.cv.config(bg="#1A1A0A")  # 背景閃一下黃光
            self.root.after(350, lambda: self.cv.config(bg=PANEL))
        elif len(synced) > 1:
            # 部分同步：顯示哪些燈同時亮起
            names = " + ".join(CONFIGS[i]["name"] for i in synced)
            self.lbl_sync.config(text=f"⚡ {names} 同步", fg="#82B1FF")
        else:
            self.lbl_sync.config(text="")

    def _blink_on(self, i):
        """點亮第 i 盞燈，並設定稍後自動熄滅"""
        self.cv.itemconfig(self.ovals[i], fill=CONFIGS[i]["on"])
        self.cv.itemconfig(self.oval_names[i], fill="#111")
        # 亮燈持續時間根據當前速度動態調整
        dur = max(120, min(self.tick_ms // 3, 500))
        self.root.after(dur, lambda idx=i: self._blink_off(idx))

    def _blink_off(self, i):
        """熄滅第 i 盞燈"""
        self.cv.itemconfig(self.ovals[i], fill=CONFIGS[i]["off"])
        self.cv.itemconfig(self.oval_names[i], fill="#444")

    def _loop(self):
        """自動運行的循環"""
        if not self.running:
            return
        self._advance()
        # 遞迴呼叫實現循環，間隔時間由使用者透過 Scale 調整
        self._job = self.root.after(self.tick_ms, self._loop)

    # ── 按鈕動作控制 ──────────────────────────────────────────

    def start(self):
        """開始自動閃爍"""
        if self.running:
            return
        self.running = True
        self.b_start.config(state="disabled")
        self.b_step.config(state="disabled")
        self.b_pause.config(state="normal")
        self._loop()

    def step(self):
        """逐拍推進（方便玩家仔細觀察特定節拍）"""
        if not self.running:
            self._advance()

    def pause(self):
        """暫停閃爍"""
        self.running = False
        if self._job:
            self.root.after_cancel(self._job)
        self.b_start.config(state="normal", text="▶ 繼續")
        self.b_step.config(state="normal")
        self.b_pause.config(state="disabled")

    def reset(self):
        """重置所有狀態至初始節拍"""
        self.running = False
        if self._job:
            self.root.after_cancel(self._job)
        self.tick = 0
        self.lbl_tick.config(text="節拍：0")
        self.lbl_sync.config(text="")
        self.b_start.config(state="normal", text="▶ 開始")
        self.b_step.config(state="normal")
        self.b_pause.config(state="disabled")
        for i in range(self.n):
            self.cv.itemconfig(self.ovals[i], fill=CONFIGS[i]["off"])
            self.cv.itemconfig(self.oval_names[i], fill="#444")
        self._update_rings()


if __name__ == "__main__":
    GCDBlinkGame()
