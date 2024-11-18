from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton

class Task1Tab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.text_edit = QTextEdit("Task 1 output will appear here.")
        layout.addWidget(self.text_edit)

        button = QPushButton("Generate")
        button.clicked.connect(self.generate_task1)
        layout.addWidget(button)
        self.setLayout(layout)

    def generate_task1(self):
        from tasks.task1 import generate_random_strings
        result = "\n".join(generate_random_strings(5, 10))
        self.text_edit.setPlainText(result)

class Task2Tab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.text_edit = QTextEdit("Task 2 output will appear here.")
        layout.addWidget(self.text_edit)

        button = QPushButton("Generate")
        button.clicked.connect(self.generate_task2)
        layout.addWidget(button)
        self.setLayout(layout)

    def generate_task2(self):
        from tasks.task2 import arithmetic_sequence
        seq = arithmetic_sequence(-0.5, 0.1)
        result = "\n".join(str(next(seq)) for _ in range(50))
        self.text_edit.setPlainText(result)

class Task3Tab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.text_edit = QTextEdit("Task 3 output will appear here.")
        layout.addWidget(self.text_edit)

        button = QPushButton("Generate")
        button.clicked.connect(self.generate_task3)
        layout.addWidget(button)
        self.setLayout(layout)

    def generate_task3(self):
        from tasks.task3 import map_cities
        cities = "New York Moscow Sydney London Paris"
        result = "\n".join(map_cities(cities))
        self.text_edit.setPlainText(result)
