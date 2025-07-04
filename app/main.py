import tkinter as tk
from app.ui import PomodoroApp


def main() -> None:
    """
    Initializes and runs the Pomodoro timer application.
    """
    root = tk.Tk()
    PomodoroApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
