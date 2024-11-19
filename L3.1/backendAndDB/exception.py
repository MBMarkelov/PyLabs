class HabitTrackerError(Exception):
    """Базовый класс для исключений в приложении."""
    pass

class DatabaseConnectionError(HabitTrackerError):
    def __init__(self, message="Не удалось подключиться к базе данных."):
        super().__init__(message)

class HabitNotFoundError(HabitTrackerError):
    def __init__(self, message="Привычка не найдена в базе данных."):
        super().__init__(message)

class InvalidHabitDataError(HabitTrackerError):
    def __init__(self, message="Недопустимые данные для привычки."):
        super().__init__(message)
