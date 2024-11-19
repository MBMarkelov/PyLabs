import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from backendAndDB.db import create_tables, add_habit, get_habits, get_habit_history, add_habit_history

class HabitTrackerApp:
    def __init__(self, root):
        create_tables()
        self.root = root
        self.root.title("Habit Tracker")
        self.root.geometry("600x400")
        self.create_widgets()



    def create_widgets(self):
        # Название привычки
        self.name_label = tk.Label(self.root, text="Habit Name:")
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        # Описание привычки
        self.desc_label = tk.Label(self.root, text="Habit Description:")
        self.desc_label.pack(pady=5)

        self.desc_entry = tk.Entry(self.root)
        self.desc_entry.pack(pady=5)

        # Кнопка добавления привычки
        self.add_button = tk.Button(self.root, text="Add Habit", command=self.add_habit)
        self.add_button.pack(pady=5)

        # Список привычек
        self.habits_listbox = tk.Listbox(self.root, width=50, height=10)
        self.habits_listbox.pack(pady=10)

        # Кнопка для отображения графика
        self.plot_button = tk.Button(self.root, text="Plot Habit Activity", command=self.plot_activity)
        self.plot_button.pack(pady=5)

        # Кнопка для добавления записи в историю
        self.mark_button = tk.Button(self.root, text="Mark Habit Completed", command=self.mark_completed)
        self.mark_button.pack(pady=5)

        # Загрузка привычек
        self.load_habits()

    def load_habits(self):
        self.habits_listbox.delete(0, tk.END)
        habits = get_habits()
        for habit in habits:
            self.habits_listbox.insert(tk.END, f"{habit[1]} - {habit[2]}")

    def add_habit(self):
        name = self.name_entry.get()
        description = self.desc_entry.get()
        if name and description:
            add_habit(name, description)
            self.load_habits()
        else:
            messagebox.showwarning("Input Error", "Please provide both name and description.")

    def mark_completed(self):
        selected_habit_index = self.habits_listbox.curselection()
        if selected_habit_index:
            habit_id = get_habits()[selected_habit_index[0]][0]
            add_habit_history(habit_id)
            messagebox.showinfo("Success", "Habit marked as completed!")
        else:
            messagebox.showwarning("Selection Error", "Please select a habit.")

    def plot_activity(self):
        selected_habit_index = self.habits_listbox.curselection()
        if selected_habit_index:
            habit_id = get_habits()[selected_habit_index[0]][0]
            history = get_habit_history(habit_id)
            dates = [str(date) for date in history]

            if dates:
                plt.plot(dates, range(len(dates)))
                plt.xlabel('Date')
                plt.ylabel('Occurrences')
                plt.title('Habit Activity')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            else:
                messagebox.showinfo("No History", "No activity recorded for this habit.")
        else:
            messagebox.showwarning("Selection Error", "Please select a habit.")
