import tkinter as tk
from tkinter import messagebox
import psycopg2

import matplotlib
from datetime import datetime

# Подключение к базе данных
DB_CONFIG = {
    "dbname": "habit_tracker",
    "user": "habit_user",
    "password": "0000",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.OperationalError as e:
        messagebox.showerror("Ошибка подключения", f"Ошибка подключения к базе данных: {e}")
        return None

def create_tables():
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS habits (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS habit_history (
                    id SERIAL PRIMARY KEY,
                    habit_id INTEGER REFERENCES habits(id),
                    date_completed DATE
                );
            """)
            conn.commit()
        conn.close()



def add_habit(name, description):
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO habits (name, description) VALUES (%s, %s) RETURNING id;
            """, (name, description))
            habit_id = cursor.fetchone()[0]
            conn.commit()
        conn.close()

def get_habits():
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, description FROM habits;")
            habits = cursor.fetchall()
        conn.close()
        return habits
    return []

def delete_habit(habit_id):
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM habits WHERE id = %s;", (habit_id,))
            conn.commit()
        conn.close()

def add_habit_history(habit_id):
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO habit_history (habit_id, date_completed)
                VALUES (%s, %s);
            """, (habit_id, datetime.now().date()))
            conn.commit()
        conn.close()

def get_habit_history(habit_id):
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT date_completed FROM habit_history
                WHERE habit_id = %s;
            """, (habit_id,))
            history = cursor.fetchall()
        conn.close()
        return [h[0] for h in history]
    return []







