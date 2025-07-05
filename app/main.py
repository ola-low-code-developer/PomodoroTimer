import logging
import tkinter as tk
from app.ui import PomodoroApp


def main() -> None:
    """
    Initializes and runs the Pomodoro timer application.
    """
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Starting Pomodoro Timer Application...")
    root = tk.Tk()
    PomodoroApp(root)
    root.mainloop()
    logging.info("Pomodoro Timer Application closed.")


if __name__ == "__main__":
    main()
