"""Game entry point."""

from ui.app import BigTwoApp


if __name__ == "__main__":
    try:
        app = BigTwoApp()
        app.run()
    except ImportError as e:
        print(f"Error: {e}")
        print("Please install pygame: pip install pygame")
    except Exception as e:
        print(f"Unexpected error: {e}")
