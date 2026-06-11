import os


def generate_plot(input_path: str, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    open(output_path, "w").close()
