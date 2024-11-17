class HabitTrackerError(Exception):
    """Базовый класс для исключений в приложении."""
    pass

class DatabaseConnectionError(HabitTrackerError):
    """Ошибка подключения к базе данных."""
    def __init__(self, message="Не удалось подключиться к базе данных."):
        super().__init__(message)

class HabitNotFoundError(HabitTrackerError):
    """Ошибка: привычка не найдена."""
    def __init__(self, message="Привычка не найдена в базе данных."):
        super().__init__(message)

class InvalidHabitDataError(HabitTrackerError):
    """Ошибка: недопустимые данные привычки."""
    def __init__(self, message="Недопустимые данные для привычки."):
        super().__init__(message)
