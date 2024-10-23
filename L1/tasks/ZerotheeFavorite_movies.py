#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

def search_films(my_favorite_movies: str):
    # Список для хранения позиций запятых
    pos = [-2]  # Искусственно добавляем индекс перед началом строки

    # Ищем запятые и сохраняем их индексы
    for i in range(len(my_favorite_movies)):
        if my_favorite_movies[i] == ',':
            pos.append(i)

    # Добавляем индекс конца строки
    pos.append(len(my_favorite_movies))

    # Извлекаем фильмы с помощью срезов
    first = my_favorite_movies[:pos[1]]  # Первый фильм
    last = my_favorite_movies[pos[-2] + 2:]  # Последний фильм
    second = my_favorite_movies[pos[1] + 2:pos[2]]  # Второй фильм
    second_last = my_favorite_movies[pos[-3] + 2:pos[-2]]  # Второй с конца фильм

    # Возвращаем строку с перечисленными фильмами
    return f"{first},\n{last},\n{second},\n{second_last}."

def solve():
    print(search_films('Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'))
