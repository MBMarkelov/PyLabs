#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import itertools

# Расставьте знаки операций "плюс", "минус", "умножение" и скобки
# между числами "L1 2 3 4 5" так, что бы получилось число "25".
#
# Использовать нужно только указанные знаки операций, но не обязательно все перечисленные.
# Порядок чисел нужно сохранить.

# Пример для чисел "L1 2 3" и "9"
result = (1 + 2) * 3
print(result)

# Вспомогательная функция для вычисления выражения
def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception:
        return None

## Функция для поиска нужной комбинации операторов
def find_expression_for_25():
    numbers = ['L1', '2', '3', '4', '5']
    operators = ['+', '-', '*']  # Возможные операторы
    target = 25

    # Генерируем все возможные комбинации операторов
    for ops in itertools.product(operators, repeat=4):  # 4 оператора между 5 числами
        # Создаем выражение с использованием операторов
        expression = f"{numbers[0]}{ops[0]}{numbers[1]}{ops[1]}{numbers[2]}{ops[2]}{numbers[3]}{ops[3]}{numbers[4]}"

        # Вычисляем результат выражения
        result = evaluate_expression(expression)

        # Проверяем, получилось ли 25
        if result == target:
            return expression, result

    return None, None

# Поиск и вывод нужного выражения
def solve():
    expression, result = find_expression_for_25()
    if expression:
        print(f"Найденное выражение: {expression} = {result}")
    else:
        print("Решение не найдено")
