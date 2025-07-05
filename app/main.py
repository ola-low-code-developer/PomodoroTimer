import argparse
import logging
import tkinter as tk
from app.ui import PomodoroApp


def main() -> None:
    """
    Initializes and runs the Pomodoro timer application.
    """
    parser = argparse.ArgumentParser(description="Pomodoro Timer Application")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(
        level=log_level, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Starting Pomodoro Timer Application...")
    root = tk.Tk()
    PomodoroApp(root)
    root.mainloop()
    logging.info("Pomodoro Timer Application closed.")


if __name__ == "__main__":
    main()
