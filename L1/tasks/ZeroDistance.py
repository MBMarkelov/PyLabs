#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from itertools import combinations

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Функция для вычисления расстояния между двумя точками
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


# Составим словарь расстояний между городами
def get_distances(sites):
    distances = {}
    # Используем combinations для создания пар городов
    for city1, city2 in combinations(sites, 2):
        dist = calculate_distance(sites[city1], sites[city2])

        # Заполняем словарь для обоих направлений (город1 -> город2 и город2 -> город1)
        if city1 not in distances:
            distances[city1] = {}
        if city2 not in distances:
            distances[city2] = {}

        distances[city1][city2] = dist
        distances[city2][city1] = dist

    return distances


# Выводим словарь расстояний
def solve():
    print(get_distances(sites))

