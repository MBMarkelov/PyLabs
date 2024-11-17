class Habit:
    def __init__(self, name, frequency, last_updated=None):
        self.name = name
        self.frequency = frequency
        self.last_updated = last_updated

    def __repr__(self):
        return f"Habit(name={self.name}, frequency={self.frequency})"

class HabitException(Exception):
    """Кастомное исключение для ошибок работы с привычками."""
