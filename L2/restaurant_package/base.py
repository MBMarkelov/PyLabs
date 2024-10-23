# restaurant_package/base.py
from abc import ABC, abstractmethod

class BaseDish(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class BaseOrder(ABC):
    @abstractmethod
    def add_dish(self, dish):
        pass

    @abstractmethod
    def calculate_total(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
