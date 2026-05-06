import math
import struct
import zlib
from pathlib import Path


SOLUTION_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_PATH = SOLUTION_DIR / "output" / "timing_comparison.png"
TIMING_SECONDS = {
    "read_csv": 0.002250,
    "write_json": 0.001564,
    "read_json": 0.000500,
    "write_xml": 0.001542,
}


FONT = {
    " ": ["000", "000", "000", "000", "000", "000", "000"],
    ".": ["0", "0", "0", "0", "0", "0", "1"],
    "/": ["00001", "00010", "00010", "00100", "01000", "01000", "10000"],
    "(": ["001", "010", "100", "100", "100", "010", "001"],
    ")": ["100", "010", "001", "001", "001", "010", "100"],
    "_": ["00000", "00000", "00000", "00000", "00000", "00000", "11111"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    ":": ["0", "1", "0", "0", "0", "1", "0"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    "6": ["00110", "01000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00010", "11100"],
}


LETTER_PATTERNS = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01111", "10000", "10000", "10011", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["111", "010", "010", "010", "010", "010", "111"],
    "J": ["00111", "00010", "00010", "00010", "10010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
}

FONT.update(LETTER_PATTERNS)


def draw_chart(timings: dict[str, float], output_path: str | Path = DEFAULT_OUTPUT_PATH) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if try_matplotlib(timings, output_path):
        print(f"圖表已儲存：{output_path.relative_to(SOLUTION_DIR)}")
        return
    draw_png_fallback(timings, output_path)
    print(f"圖表已儲存：{output_path.relative_to(SOLUTION_DIR)}")


def try_matplotlib(timings: dict[str, float], output_path: Path) -> bool:
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        return False

    names = list(timings)
    values = [timings[name] for name in names]
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(names, values, color=["#2563eb", "#059669", "#d97706", "#7c3aed"])
    ax.set_title("Task 1/2 Function Runtime Comparison")
    ax.set_xlabel("Function")
    ax.set_ylabel("Runtime (seconds)")
    ax.set_ylim(0, max(values) * 1.25 if values else 1)
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{value:.6f}s",
            ha="center",
            va="bottom",
            fontsize=9,
        )
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    return True


def draw_png_fallback(timings: dict[str, float], output_path: Path) -> None:
    width, height = 900, 540
    pixels = [[(255, 255, 255) for _ in range(width)] for _ in range(height)]
    colors = [(37, 99, 235), (5, 150, 105), (217, 119, 6), (124, 58, 237)]
    left, top, right, bottom = 100, 80, 830, 420
    max_value = max(timings.values()) if timings else 1.0
    max_value = max(max_value, 0.000001)

    draw_text(pixels, 215, 25, "TASK 1/2 FUNCTION RUNTIME COMPARISON", (17, 24, 39), 2)
    draw_text(pixels, 375, 500, "FUNCTION", (17, 24, 39), 2)
    draw_text(pixels, 15, 45, "RUNTIME (SECONDS)", (17, 24, 39), 1)
    draw_line(pixels, left, bottom, right, bottom, (31, 41, 55))
    draw_line(pixels, left, top, left, bottom, (31, 41, 55))

    for i in range(5):
        y = bottom - int((bottom - top) * i / 4)
        draw_line(pixels, left - 5, y, right, y, (226, 232, 240))
        label = f"{max_value * i / 4:.4f}"
        draw_text(pixels, 35, y - 4, label, (71, 85, 105), 1)

    names = list(timings)
    values = [timings[name] for name in names]
    gap = 45
    bar_width = math.floor((right - left - gap * (len(names) + 1)) / len(names))
    for index, (name, value) in enumerate(zip(names, values)):
        x1 = left + gap + index * (bar_width + gap)
        x2 = x1 + bar_width
        bar_height = int((bottom - top) * value / max_value)
        y1 = bottom - bar_height
        fill_rect(pixels, x1, y1, x2, bottom - 1, colors[index % len(colors)])
        draw_text(pixels, x1 + 6, y1 - 18, f"{value:.6f}S", (17, 24, 39), 1)
        draw_text(pixels, x1, bottom + 15, name.upper(), (17, 24, 39), 1)

    write_png(output_path, pixels)


def fill_rect(pixels, x1, y1, x2, y2, color):
    height = len(pixels)
    width = len(pixels[0])
    for y in range(max(0, y1), min(height, y2 + 1)):
        for x in range(max(0, x1), min(width, x2 + 1)):
            pixels[y][x] = color


def draw_line(pixels, x1, y1, x2, y2, color):
    if y1 == y2:
        fill_rect(pixels, min(x1, x2), y1, max(x1, x2), y1, color)
    elif x1 == x2:
        fill_rect(pixels, x1, min(y1, y2), x1, max(y1, y2), color)


def draw_text(pixels, x, y, text, color, scale=1):
    cursor = x
    for char in text.upper():
        pattern = FONT.get(char, FONT[" "])
        for row_index, row in enumerate(pattern):
            for col_index, bit in enumerate(row):
                if bit == "1":
                    fill_rect(
                        pixels,
                        cursor + col_index * scale,
                        y + row_index * scale,
                        cursor + (col_index + 1) * scale - 1,
                        y + (row_index + 1) * scale - 1,
                        color,
                    )
        cursor += (len(pattern[0]) + 1) * scale


def write_png(output_path: Path, pixels: list[list[tuple[int, int, int]]]) -> None:
    height = len(pixels)
    width = len(pixels[0])
    raw = b"".join(b"\x00" + b"".join(bytes(pixel) for pixel in row) for row in pixels)

    def chunk(chunk_type: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data))
            + chunk_type
            + data
            + struct.pack(">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
        )

    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(raw, level=9))
    png += chunk(b"IEND", b"")
    output_path.write_bytes(png)


def main() -> None:
    draw_chart(TIMING_SECONDS)


if __name__ == "__main__":
    main()
