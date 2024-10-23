# restaurant_package/order.py
from restaurant_package import Dish
from restaurant_package.base import BaseOrder


class Order(BaseOrder):
    def __init__(self):
        self.dishes = []
        self._discount = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if 0 <= value <= 100:
            self._discount = value
        else:
            raise ValueError("Скидка должна быть в диапазоне от 0 до 100.")

    def add_dish(self, dish: Dish):
        if isinstance(dish, Dish):
            self.dishes.append(dish)

    def calculate_total(self):
        total = sum(dish.get_price() for dish in self.dishes)
        total -= total * (self.discount / 100)
        return total

    def __str__(self):
        dishes_str = ', '.join(str(dish) for dish in self.dishes)
        return f"Order: {dishes_str}, Total: {self.calculate_total():.2f}"

    def __len__(self):
        return len(self.dishes)

    def __getitem__(self, index):
        return self.dishes[index]
