import tkinter as tk
from tkinter import messagebox


class PomodoroApp:
    """A Pomodoro timer application built with tkinter."""

    def __init__(self, root):
        """
        Initializes the PomodoroApp.

        Args:
            root: The root tkinter window.
        """
        self.root = root
        self.root.title("Pomodoro Timer")

        # Timer display
        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        # Buttons
        controls_frame = tk.Frame(root)
        controls_frame.pack(pady=10)

        self.start_button = tk.Button(
            controls_frame, text="Start", command=self.start_timer
        )
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(
            controls_frame, text="Stop", command=self.stop_timer
        )
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(
            controls_frame, text="Reset", command=self.reset_timer
        )
        self.reset_button.pack(side="right", padx=10)

        # Settings
        settings_frame = tk.Frame(root)
        settings_frame.pack(pady=10)

        tk.Label(settings_frame, text="Work (mins):").pack(side="left")
        self.work_minutes = tk.Entry(settings_frame, width=5)
        self.work_minutes.insert(0, "25")
        self.work_minutes.pack(side="left")

        tk.Label(settings_frame, text="Break (mins):").pack(side="left")
        self.break_minutes = tk.Entry(settings_frame, width=5)
        self.break_minutes.insert(0, "5")
        self.break_minutes.pack(side="left")

        self.set_button = tk.Button(
            settings_frame, text="Set", command=self.set_durations
        )
        self.set_button.pack(side="left", padx=10)

        # Timer logic
        self.timer_running = False
        self.is_work_time = True
        self.work_duration = 25 * 60
        self.break_duration = 5 * 60
        self.remaining_time = self.work_duration
        self.timer_id = None

    def start_timer(self):
        """Starts the timer if it is not already running."""
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        """Stops the timer if it is running."""
        if self.timer_running:
            self.timer_running = False
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
                self.timer_id = None

    def reset_timer(self):
        """Resets the timer to the initial work session state."""
        self.stop_timer()
        self.is_work_time = True
        self.remaining_time = self.work_duration
        self.update_display()

    def set_durations(self):
        """Sets the work and break durations from the input fields."""
        try:
            self.work_duration = int(self.work_minutes.get()) * 60
            self.break_duration = int(self.break_minutes.get()) * 60
            self.reset_timer()
        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Please enter valid numbers for minutes."
            )

    def update_timer(self):
        """
        Updates the timer every second.

        If the time runs out, it switches between work and break sessions.
        """
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_display()
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.timer_running = False
            self.is_work_time = not self.is_work_time
            if self.is_work_time:
                self.remaining_time = self.work_duration
                messagebox.showinfo("Pomodoro Timer", "Break's over! Time to work.")
            else:
                self.remaining_time = self.break_duration
                messagebox.showinfo(
                    "Pomodoro Timer", "Work session is over! Time for a break."
                )
            self.update_display()
            # The timer will be started by the user after the message box is closed.
            # self.start_timer()

    def update_display(self):
        """Updates the timer display with the remaining time."""
        mins, secs = divmod(self.remaining_time, 60)
        self.timer_label.config(text=f"{mins:02d}:{secs:02d}")

