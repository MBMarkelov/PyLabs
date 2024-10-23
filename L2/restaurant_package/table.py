# restaurant_package/table.py

class Table:
    def __init__(self, table_number, seats):
        self.table_number = table_number
        self.seats = seats
        self.is_occupied = False

    def occupy(self):
        self.is_occupied = True

    def release(self):
        self.is_occupied = False

    def __str__(self):
        status = "Occupied" if self.is_occupied else "Available"
        return f"Table {self.table_number} ({self.seats} seats): {status}"
