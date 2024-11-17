import pytest
from unittest.mock import MagicMock

from db import get_connection
from gui import HabitTrackerApp
import tkinter as tk

def test_add_habit_via_gui():
    root = tk.Tk()
    app = HabitTrackerApp(root)

    app.name_entry = MagicMock()
    app.name_entry.get.return_value = 'Test Habit'


    app.desc_entry = MagicMock()
    app.desc_entry.get.return_value = 'Test description'

    app.add_habit_button = MagicMock()
    app.add_habit_button.invoke()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habits WHERE name = %s", ('Test Habit',))
    result = cursor.fetchone()
    assert result is not None, "Привычка не была добавлена через интерфейс"
    cursor.close()
    conn.close()
