"""Robot Lost pygame 互動遊戲。

操作說明：
- L / R / F: 執行一步指令
- N: 新機器人（保留 scent）
- C: 清除 scent
- P: 回放本回合歷史步驟
- ESC: 離開
"""

from __future__ import annotations

from pathlib import Path
import sys
from dataclasses import dataclass

try:
    import pygame
except ModuleNotFoundError as exc:  # pragma: no cover
    raise SystemExit(
        "找不到 pygame，請先安裝：pip install pygame"
    ) from exc

try:
    from PIL import Image
except ModuleNotFoundError:  # pragma: no cover
    Image = None

from robot_core import RobotState, simulate

# 地圖範圍是 (0,0) 到 (MAX_X, MAX_Y)，含邊界
MAX_X = 5
MAX_Y = 3
CELL_SIZE = 100
PADDING = 50
HUD_HEIGHT = 160

WINDOW_WIDTH = (MAX_X + 1) * CELL_SIZE + PADDING * 2
WINDOW_HEIGHT = (MAX_Y + 1) * CELL_SIZE + PADDING * 2 + HUD_HEIGHT
FPS = 60

BG_COLOR = (245, 247, 250)
GRID_COLOR = (150, 160, 170)
ROBOT_COLOR = (32, 98, 188)
LOST_COLOR = (200, 40, 40)
SCENT_COLOR = (30, 150, 90)
TEXT_COLOR = (30, 36, 44)
PANEL_COLOR = (230, 236, 242)


@dataclass
class GameState:
    """封裝遊戲執行狀態，便於管理與重置。"""

    robot: RobotState
    scents: set[tuple[int, int, str]]
    status_text: str
    history: list[RobotState]
    replay_index: int
    replay_mode: bool
    replay_tick: int


def grid_to_pixel(x: int, y: int) -> tuple[int, int]:
    """把格子座標轉成螢幕像素中心點。

    注意 y 軸在畫面上是向下增加，故需做翻轉。
    """
    px = PADDING + x * CELL_SIZE + CELL_SIZE // 2
    py = PADDING + (MAX_Y - y) * CELL_SIZE + CELL_SIZE // 2
    return px, py


def reset_robot() -> RobotState:
    """建立新機器人，預設放在 (0,0) 朝北。"""
    return RobotState(0, 0, "N", False)


def push_history(state: GameState, robot: RobotState) -> None:
    """記錄每一步狀態，提供回放功能使用。"""
    state.history.append(robot)


def apply_command(state: GameState, command: str) -> None:
    """對目前機器人套用單一步驟指令。"""
    command = command.upper()

    if state.robot.lost:
        state.status_text = "機器人已 LOST，請按 N 建立新機器人。"
        return

    try:
        x, y, d, lost, scents = simulate(
            max_x=MAX_X,
            max_y=MAX_Y,
            start_x=state.robot.x,
            start_y=state.robot.y,
            start_dir=state.robot.direction,
            instructions=command,
            scents=state.scents,
        )
    except ValueError:
        state.status_text = f"非法指令: {command}"
        return

    state.scents = scents
    state.robot = RobotState(x, y, d, lost)
    push_history(state, state.robot)

    if lost:
        state.status_text = f"指令 {command}：機器人在 ({x},{y}) {d} LOST。"
    else:
        state.status_text = f"指令 {command}：目前位置 ({x},{y}) {d}。"


def start_replay(state: GameState) -> None:
    """啟動回放模式，從第一步開始播。"""
    if len(state.history) <= 1:
        state.status_text = "目前沒有足夠歷史可回放。"
        return

    state.replay_mode = True
    state.replay_index = 0
    state.replay_tick = 0
    state.status_text = "開始回放。"


def update_replay(state: GameState) -> None:
    """固定節奏更新回放游標。"""
    if not state.replay_mode:
        return

    state.replay_tick += 1
    if state.replay_tick < 25:
        return

    state.replay_tick = 0
    state.replay_index += 1

    if state.replay_index >= len(state.history):
        state.replay_mode = False
        state.replay_index = len(state.history) - 1
        state.status_text = "回放結束。"


def draw_grid(screen: pygame.Surface) -> None:
    """繪製地圖格線。"""
    for x in range(MAX_X + 2):
        sx = PADDING + x * CELL_SIZE
        pygame.draw.line(screen, GRID_COLOR, (sx, PADDING), (sx, PADDING + (MAX_Y + 1) * CELL_SIZE), 2)

    for y in range(MAX_Y + 2):
        sy = PADDING + y * CELL_SIZE
        pygame.draw.line(screen, GRID_COLOR, (PADDING, sy), (PADDING + (MAX_X + 1) * CELL_SIZE, sy), 2)


def draw_scents(screen: pygame.Surface, scents: set[tuple[int, int, str]]) -> None:
    """在留下 scent 的格子畫小圓點。"""
    for x, y, _ in scents:
        px, py = grid_to_pixel(x, y)
        pygame.draw.circle(screen, SCENT_COLOR, (px, py), 8)


def robot_triangle_points(robot: RobotState) -> list[tuple[int, int]]:
    """依機器人朝向回傳三角形頂點。"""
    cx, cy = grid_to_pixel(robot.x, robot.y)
    size = CELL_SIZE // 3

    if robot.direction == "N":
        return [(cx, cy - size), (cx - size // 2, cy + size // 2), (cx + size // 2, cy + size // 2)]
    if robot.direction == "E":
        return [(cx + size, cy), (cx - size // 2, cy - size // 2), (cx - size // 2, cy + size // 2)]
    if robot.direction == "S":
        return [(cx, cy + size), (cx - size // 2, cy - size // 2), (cx + size // 2, cy - size // 2)]
    return [(cx - size, cy), (cx + size // 2, cy - size // 2), (cx + size // 2, cy + size // 2)]


def draw_robot(screen: pygame.Surface, robot: RobotState) -> None:
    """繪製機器人本體與 LOST 狀態框。"""
    color = LOST_COLOR if robot.lost else ROBOT_COLOR
    pygame.draw.polygon(screen, color, robot_triangle_points(robot))

    if robot.lost:
        px, py = grid_to_pixel(robot.x, robot.y)
        pygame.draw.circle(screen, LOST_COLOR, (px, py), CELL_SIZE // 3, 4)


def draw_hud(screen: pygame.Surface, font: pygame.font.Font, state: GameState) -> None:
    """繪製下方說明與狀態資訊。"""
    panel_top = PADDING + (MAX_Y + 1) * CELL_SIZE + 16
    panel_rect = pygame.Rect(PADDING, panel_top, (MAX_X + 1) * CELL_SIZE, HUD_HEIGHT - 20)
    pygame.draw.rect(screen, PANEL_COLOR, panel_rect, border_radius=8)

    commands = "L/R/F: 一步指令   N: 新機器人   C: 清除 scent   P: 回放   G: 存GIF   S: 存截圖   ESC: 離開"
    status = f"位置=({state.robot.x},{state.robot.y}) 方向={state.robot.direction} LOST={state.robot.lost} scent數={len(state.scents)}"

    screen.blit(font.render(commands, True, TEXT_COLOR), (PADDING + 12, panel_top + 12))
    screen.blit(font.render(status, True, TEXT_COLOR), (PADDING + 12, panel_top + 48))
    screen.blit(font.render(state.status_text, True, TEXT_COLOR), (PADDING + 12, panel_top + 84))


def current_robot_for_render(state: GameState) -> RobotState:
    """若在回放模式，取回放游標的狀態；否則取即時狀態。"""
    if state.replay_mode:
        return state.history[state.replay_index]
    return state.robot


def draw_scene(screen: pygame.Surface, font: pygame.font.Font, state: GameState, robot: RobotState, status_text: str | None = None) -> None:
    """繪製完整畫面，供即時渲染與 GIF 輸出共用。"""
    original_robot = state.robot
    original_status = state.status_text
    state.robot = robot
    if status_text is not None:
        state.status_text = status_text

    screen.fill(BG_COLOR)
    draw_grid(screen)
    draw_scents(screen, state.scents)
    draw_robot(screen, robot)
    draw_hud(screen, font, state)

    state.robot = original_robot
    state.status_text = original_status


def save_gameplay_screenshot(screen: pygame.Surface) -> Path:
    """把目前畫面存到 assets/gameplay.png。"""
    output_path = Path(__file__).resolve().parent / "assets" / "gameplay.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pygame.image.save(screen, str(output_path))
    return output_path


def save_replay_gif(font: pygame.font.Font, state: GameState) -> Path:
    """把歷史狀態輸出成 assets/replay.gif。"""
    if Image is None:
        raise RuntimeError("找不到 Pillow，請先安裝：pip install pillow")

    if len(state.history) <= 1:
        raise RuntimeError("歷史步驟不足，至少先操作 2 步再輸出 GIF")

    output_path = Path(__file__).resolve().parent / "assets" / "replay.gif"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    frames: list[Image.Image] = []
    total = len(state.history)
    for idx, robot in enumerate(state.history, start=1):
        frame_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        draw_scene(frame_surface, font, state, robot, status_text=f"GIF 回放 {idx}/{total}")
        raw = pygame.image.tobytes(frame_surface, "RGB")
        frame = Image.frombytes("RGB", (WINDOW_WIDTH, WINDOW_HEIGHT), raw)
        frames.append(frame)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=280,
        loop=0,
    )
    return output_path


def run() -> None:
    """啟動遊戲主迴圈。"""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Week 03 - Robot Lost")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("microsoftjhenghei", 24)

    initial = reset_robot()
    state = GameState(
        robot=initial,
        scents=set(),
        status_text="遊戲開始：請按 L / R / F 操作機器人。",
        history=[initial],
        replay_index=0,
        replay_mode=False,
        replay_tick=0,
    )

    key_to_command = {
        # 非文字按鍵只用 KEYDOWN；文字按鍵統一走 TEXTINPUT，避免單次按鍵重複觸發。
        pygame.K_LEFT: "L",
        pygame.K_RIGHT: "R",
        pygame.K_UP: "F",
    }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.WINDOWFOCUSLOST:
                state.status_text = "視窗失去焦點，請先點一下遊戲視窗再按鍵。"

            if event.type == pygame.WINDOWFOCUSGAINED:
                state.status_text = "已取得焦點：可使用 L/R/F，或左/右/上方向鍵。"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in key_to_command:
                    state.replay_mode = False
                    apply_command(state, key_to_command[event.key])
                elif event.key == pygame.K_n:
                    state.replay_mode = False
                    state.robot = reset_robot()
                    push_history(state, state.robot)
                    state.status_text = "已建立新機器人（保留 scent）。"
                elif event.key == pygame.K_c:
                    state.replay_mode = False
                    state.scents.clear()
                    state.status_text = "已清除所有 scent。"
                elif event.key == pygame.K_p:
                    start_replay(state)
                elif event.key == pygame.K_g:
                    try:
                        path = save_replay_gif(font, state)
                        state.status_text = f"已儲存 GIF：{path.name}"
                    except RuntimeError as err:
                        state.status_text = str(err)
                elif event.key == pygame.K_s:
                    path = save_gameplay_screenshot(screen)
                    state.status_text = f"已儲存截圖：{path.name}"

            # 文字按鍵統一在 TEXTINPUT 處理，避免與 KEYDOWN 重複執行。
            if event.type == pygame.TEXTINPUT and event.text:
                text = event.text.lower()
                if text in {"l", "r", "f"}:
                    state.replay_mode = False
                    apply_command(state, text.upper())
                elif text in {"a", "d"}:
                    state.replay_mode = False
                    mapping = {"a": "L", "d": "R"}
                    apply_command(state, mapping[text])
                elif text == "n":
                    state.replay_mode = False
                    state.robot = reset_robot()
                    push_history(state, state.robot)
                    state.status_text = "已建立新機器人（保留 scent）。"
                elif text == "c":
                    state.replay_mode = False
                    state.scents.clear()
                    state.status_text = "已清除所有 scent。"
                elif text == "p":
                    start_replay(state)
                elif text == "g":
                    try:
                        path = save_replay_gif(font, state)
                        state.status_text = f"已儲存 GIF：{path.name}"
                    except RuntimeError as err:
                        state.status_text = str(err)
                elif text == "s":
                    path = save_gameplay_screenshot(screen)
                    state.status_text = f"已儲存截圖：{path.name}"

        update_replay(state)

        draw_scene(screen, font, state, current_robot_for_render(state))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    run()
