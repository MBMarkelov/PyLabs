# restaurant_package/dish.py
from restaurant_package.base import BaseDish


class Dish(BaseDish):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.name}: {self.price:.2f}"

    def __repr__(self):
        return f"Dish({self.name}, {self.price})"

    def __eq__(self, other):
        if isinstance(other, Dish):
            return self.name == other.name and self.price == other.price
        return False

    def __lt__(self, other):
        if isinstance(other, Dish):
            return self.price < other.price
        return NotImplemented
