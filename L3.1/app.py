import tkinter as tk
from gui import HabitTrackerApp

if __name__ == "__main__":
    # Инициализация главного окна
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()
