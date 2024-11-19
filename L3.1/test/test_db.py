import pytest
import psycopg2
from backendAndDB.db import get_connection, add_habit, get_habits


def test_get_connection():
    conn = get_connection()
    assert conn is not None, "Ошибка подключения к базе данных"
    conn.close()


def test_create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT to_regclass('public.habits')")
    result = cursor.fetchone()
    assert result[0] is not None, "Таблица 'habits' не создана"

    cursor.execute("SELECT to_regclass('public.habit_history')")
    result = cursor.fetchone()
    assert result[0] is not None, "Таблица 'habit_history' не создана"

    cursor.close()
    conn.close()


def test_add_habit():
    habit_data = {'name': 'Test Habit', 'description': 'Test description'}
    add_habit(habit_data)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habits WHERE name = %s", (habit_data['name'],))
    result = cursor.fetchone()
    assert result is not None, "Привычка не была добавлена в базу данных"
    cursor.close()
    conn.close()


def test_get_habits():
    habits = get_habits()
    assert len(habits) >= 1, "Не удалось получить привычки из базы данных"
