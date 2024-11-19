import tkinter as tk
from GUI import HabitTrackerApp

if __name__ == "__main__":
    # Инициализация главного окна
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()
