import unittest
import tkinter as tk
from app.ui import PomodoroApp
from unittest.mock import patch


class TestPomodoroApp(unittest.TestCase):
    def setUp(self) -> None:
        self.root = tk.Tk()
        self.app = PomodoroApp(self.root)

    def tearDown(self) -> None:
        self.root.destroy()

    def test_initial_state(self) -> None:
        self.assertEqual(self.app.remaining_time, 25 * 60)
        self.assertFalse(self.app.timer_running)
        self.assertTrue(self.app.is_work_time)

    def test_start_timer(self) -> None:
        self.app.start_timer()
        self.assertTrue(self.app.timer_running)

    def test_stop_timer(self) -> None:
        self.app.start_timer()
        self.app.stop_timer()
        self.assertFalse(self.app.timer_running)

    def test_reset_timer(self) -> None:
        self.app.start_timer()
        self.app.remaining_time = 10
        self.app.reset_timer()
        self.assertFalse(self.app.timer_running)
        self.assertEqual(self.app.remaining_time, 25 * 60)

    def test_set_durations(self) -> None:
        self.app.work_minutes.delete(0, tk.END)
        self.app.work_minutes.insert(0, "30")
        self.app.break_minutes.delete(0, tk.END)
        self.app.break_minutes.insert(0, "10")
        self.app.set_durations()
        self.assertEqual(self.app.work_duration, 30 * 60)
        self.assertEqual(self.app.break_duration, 10 * 60)

    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.Tk.after")
    def test_timer_ends_work_session(
        self,
        mock_after: unittest.mock.MagicMock,
        mock_showinfo: unittest.mock.MagicMock,
    ) -> None:
        self.app.remaining_time = 0
        self.app.update_timer()
        mock_showinfo.assert_called_with(
            "Pomodoro Timer", "Work session is over! Time for a break."
        )
        self.assertFalse(self.app.is_work_time)
        self.assertEqual(self.app.remaining_time, self.app.break_duration)

    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.Tk.after")
    def test_timer_ends_break_session(
        self,
        mock_after: unittest.mock.MagicMock,
        mock_showinfo: unittest.mock.MagicMock,
    ) -> None:
        self.app.is_work_time = False
        self.app.remaining_time = 0
        self.app.update_timer()
        mock_showinfo.assert_called_with(
            "Pomodoro Timer", "Break's over! Time to work."
        )
        self.assertTrue(self.app.is_work_time)
        self.assertEqual(self.app.remaining_time, self.app.work_duration)


if __name__ == "__main__":
    unittest.main()
