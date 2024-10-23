# test_restaurant.py
import pytest
from restaurant_package.dish import Dish
from restaurant_package.order import Order
from restaurant_package.table import Table

# Тест для Dish
def test_create_dish():
    dish = Dish("Pizza", 10.0)
    assert dish.name == "Pizza"
    assert dish.price == 10.0

# Тест для Order
def test_order_total_without_discount():
    order = Order()
    order.add_dish(Dish("Pizza", 10.0))
    order.add_dish(Dish("Pasta", 8.0))
    assert order.calculate_total() == 18.0  # Итоговая сумма без скидки

def test_order_total_with_discount():
    order = Order()
    order.add_dish(Dish("Pizza", 10.0))
    order.add_dish(Dish("Pasta", 8.0))
    order.discount = 10  # Устанавливаем скидку 10%
    assert order.calculate_total() == 16.2  # Итог с учетом 10% скидки

# Тест на скидку (managed атрибут)
def test_order_discount():
    order = Order()
    order.discount = 20
    assert order.discount == 20

# Тест на ограничение скидки
def test_invalid_discount():
    order = Order()
    with pytest.raises(ValueError):
        order.discount = 110  # Скидка не может быть больше 100

# Тест для Table
def test_table_occupy():
    table = Table(1, 4)
    assert not table.is_occupied  # Столик изначально свободен
    table.occupy()
    assert table.is_occupied  # Столик должен быть занят
