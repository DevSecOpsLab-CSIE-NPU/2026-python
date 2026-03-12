"""
Robot Lost pygame 互動程式（MVP）。

操作鍵：
- L / R / F：執行一步指令
- N：建立新機器人（保留 scent）
- C：清除 scent
- P：播放 / 停止回放
- G：嘗試輸出 replay.gif（選配）
- ESC：離開
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys
import time

from robot_core import MOVE_STEP, RobotState, RobotWorld


try:
    import pygame
except ImportError:
    print("尚未安裝 pygame。請先執行：pip install pygame")
    sys.exit(1)


ASSETS_DIR = Path(__file__).resolve().parent / "assets"


@dataclass
class Snapshot:
    """回放快照。"""

    x: int
    y: int
    direction: str
    lost: bool
    scents: set[tuple[int, int, str]]
    command: str


class RobotGameApp:
    """Robot Lost 遊戲主程式。"""

    def __init__(self, width: int = 5, height: int = 3, cell_size: int = 90):
        self.world = RobotWorld(width=width, height=height)
        self.cell_size = cell_size
        self.margin = 20
        self.sidebar_width = 350
        self.grid_width_px = (width + 1) * cell_size
        self.grid_height_px = (height + 1) * cell_size
        self.screen_width = self.grid_width_px + self.sidebar_width + self.margin * 2
        self.screen_height = self.grid_height_px + self.margin * 2

        self.robot = RobotState(x=0, y=0, direction="N", lost=False)
        self.robot_id = 1
        self.command_history: list[str] = []
        self.snapshots: list[Snapshot] = []
        self.add_snapshot(command="START")

        self.replay_mode = False
        self.replay_index = 0
        self.last_replay_tick = 0
        self.replay_interval_ms = 320
        self.message = "準備完成"

        ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    def world_to_screen(self, x: int, y: int) -> tuple[int, int]:
        """將世界座標轉為畫面座標（左下為原點）。"""
        px = self.margin + x * self.cell_size + self.cell_size // 2
        py = self.margin + (self.world.height - y) * self.cell_size + self.cell_size // 2
        return px, py

    def add_snapshot(self, command: str) -> None:
        self.snapshots.append(
            Snapshot(
                x=self.robot.x,
                y=self.robot.y,
                direction=self.robot.direction,
                lost=self.robot.lost,
                scents=set(self.world.scents),
                command=command,
            )
        )

    def current_snapshot(self) -> Snapshot:
        if self.replay_mode and self.snapshots:
            return self.snapshots[self.replay_index]
        return self.snapshots[-1]

    def execute_step(self, cmd: str) -> None:
        """執行一步 L / R / F。"""
        if self.robot.lost:
            self.message = "機器人已 LOST，請按 N 建立新機器人。"
            return

        self.world.execute_instruction(self.robot, cmd)
        self.command_history.append(cmd)
        self.add_snapshot(command=cmd)

        if self.robot.lost:
            self.message = f"機器人 #{self.robot_id} LOST（位置 {self.robot.x}, {self.robot.y}, {self.robot.direction}）"
        else:
            self.message = f"已執行：{cmd}"

    def new_robot(self) -> None:
        """建立新機器人（保留 scent）。"""
        self.robot_id += 1
        self.robot = RobotState(x=0, y=0, direction="N", lost=False)
        self.command_history.append("|N|")
        self.add_snapshot(command="N")
        self.message = f"建立機器人 #{self.robot_id}"

    def clear_scents(self) -> None:
        """清除所有 scent。"""
        self.world.scents.clear()
        self.command_history.append("|C|")
        self.add_snapshot(command="C")
        self.message = "已清除 scent"

    def toggle_replay(self) -> None:
        if not self.snapshots:
            self.message = "沒有可回放資料"
            return
        self.replay_mode = not self.replay_mode
        if self.replay_mode:
            self.replay_index = 0
            self.last_replay_tick = pygame.time.get_ticks()
            self.message = "開始回放（按 P 可停止）"
        else:
            self.message = "停止回放"

    def update_replay(self) -> None:
        if not self.replay_mode or not self.snapshots:
            return
        now = pygame.time.get_ticks()
        if now - self.last_replay_tick < self.replay_interval_ms:
            return
        self.last_replay_tick = now
        if self.replay_index + 1 < len(self.snapshots):
            self.replay_index += 1
        else:
            self.replay_mode = False
            self.message = "回放結束"

    def try_export_replay_gif(self, surface: pygame.Surface) -> None:
        """
        嘗試輸出 replay.gif（選配）。

        若缺少 imageio / numpy，僅提示，不中斷遊戲。
        """
        try:
            import imageio.v2 as imageio  # type: ignore
            import numpy as np  # type: ignore
        except Exception:
            self.message = "未安裝 imageio 或 numpy，無法輸出 GIF。"
            return

        frames = []
        original_mode = self.replay_mode
        original_index = self.replay_index

        self.replay_mode = True
        for index in range(len(self.snapshots)):
            self.replay_index = index
            self.draw(surface)
            rgb = pygame.surfarray.array3d(surface)
            frame = np.transpose(rgb, (1, 0, 2))
            frames.append(frame)

        output = ASSETS_DIR / "replay.gif"
        imageio.mimsave(output, frames, duration=0.25)
        self.replay_mode = original_mode
        self.replay_index = original_index
        self.message = f"已輸出：{output.name}"

    def draw_grid(self, surface: pygame.Surface) -> None:
        grid_color = (70, 70, 70)
        for x in range(self.world.width + 2):
            px = self.margin + x * self.cell_size
            pygame.draw.line(
                surface,
                grid_color,
                (px, self.margin),
                (px, self.margin + self.grid_height_px),
                1,
            )
        for y in range(self.world.height + 2):
            py = self.margin + y * self.cell_size
            pygame.draw.line(
                surface,
                grid_color,
                (self.margin, py),
                (self.margin + self.grid_width_px, py),
                1,
            )

    def draw_scents(self, surface: pygame.Surface, snapshot: Snapshot, font: pygame.font.Font) -> None:
        for x, y, direction in snapshot.scents:
            cx, cy = self.world_to_screen(x, y)
            pygame.draw.circle(surface, (255, 180, 0), (cx, cy), 8)
            label = font.render(direction, True, (40, 40, 40))
            surface.blit(label, (cx - 5, cy - 10))

    def draw_robot(self, surface: pygame.Surface, snapshot: Snapshot) -> None:
        cx, cy = self.world_to_screen(snapshot.x, snapshot.y)
        color = (220, 60, 60) if snapshot.lost else (40, 180, 255)
        pygame.draw.circle(surface, color, (cx, cy), self.cell_size // 4)

        dx, dy = MOVE_STEP[snapshot.direction]
        tip_x = cx + dx * (self.cell_size // 3)
        tip_y = cy - dy * (self.cell_size // 3)
        pygame.draw.line(surface, (20, 20, 20), (cx, cy), (tip_x, tip_y), 4)

        if snapshot.lost:
            size = self.cell_size // 3
            pygame.draw.line(surface, (0, 0, 0), (cx - size, cy - size), (cx + size, cy + size), 3)
            pygame.draw.line(surface, (0, 0, 0), (cx - size, cy + size), (cx + size, cy - size), 3)

    def draw_hud(self, surface: pygame.Surface, snapshot: Snapshot, title_font, text_font) -> None:
        base_x = self.margin + self.grid_width_px + 20
        y = self.margin

        def draw_line(text: str, color=(230, 230, 230), gap=28):
            nonlocal y
            label = text_font.render(text, True, color)
            surface.blit(label, (base_x, y))
            y += gap

        title = title_font.render("Robot Lost MVP", True, (255, 255, 255))
        surface.blit(title, (base_x, y))
        y += 40

        draw_line(f"Robot #{self.robot_id}")
        draw_line(f"位置: ({snapshot.x}, {snapshot.y})")
        draw_line(f"方向: {snapshot.direction}")
        draw_line(f"狀態: {'LOST' if snapshot.lost else 'ALIVE'}")
        draw_line(f"scent 數量: {len(snapshot.scents)}")
        draw_line(f"最近指令: {snapshot.command}")
        y += 10

        draw_line("操作鍵：", color=(255, 220, 150))
        draw_line("L/R/F: 單步操作")
        draw_line("N: 新機器人（保留 scent）")
        draw_line("C: 清除 scent")
        draw_line("P: 回放")
        draw_line("G: 匯出 replay.gif（選配）")
        draw_line("ESC: 離開")
        y += 10

        commands = "".join(self.command_history[-28:])
        draw_line(f"History: {commands if commands else '(空)'}", color=(200, 255, 200))
        draw_line(self.message, color=(180, 220, 255))

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((25, 28, 35))
        self.draw_grid(surface)
        snapshot = self.current_snapshot()

        font = pygame.font.SysFont("consolas", 18)
        title_font = pygame.font.SysFont("consolas", 28, bold=True)
        text_font = pygame.font.SysFont("consolas", 20)

        self.draw_scents(surface, snapshot, font)
        self.draw_robot(surface, snapshot)
        self.draw_hud(surface, snapshot, title_font, text_font)

    def run(self) -> None:
        pygame.init()
        pygame.display.set_caption("Robot Lost - Week 03 Homework")
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        clock = pygame.time.Clock()

        key_to_cmd = {
            pygame.K_l: "L",
            pygame.K_r: "R",
            pygame.K_f: "F",
        }

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_n:
                        self.new_robot()
                    elif event.key == pygame.K_c:
                        self.clear_scents()
                    elif event.key == pygame.K_p:
                        self.toggle_replay()
                    elif event.key == pygame.K_g:
                        self.try_export_replay_gif(screen)
                    elif event.key in key_to_cmd:
                        self.execute_step(key_to_cmd[event.key])

            self.update_replay()
            self.draw(screen)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


def main() -> None:
    app = RobotGameApp(width=5, height=3, cell_size=90)
    app.run()


if __name__ == "__main__":
    main()
