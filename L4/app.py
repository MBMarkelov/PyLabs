import sys

from itertools import islice
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QTabWidget

from UI.main_window import MainWindow
from tasks import  generate_random_strings, map_cities, arithmetic_sequence

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Python Lab Tasks')

        layout = QVBoxLayout()

        tabs = QTabWidget()
        tabs.addTab(self.create_task1_tab(), "Task 1")
        tabs.addTab(self.create_task2_tab(), "Task 2")
        tabs.addTab(self.create_task3_tab(), "Task 3")

        layout.addWidget(tabs)
        self.setLayout(layout)

    def create_task1_tab(self):
        task1_widget = QWidget()
        task1_layout = QVBoxLayout()

        self.text_edit_task1 = QTextEdit()
        self.text_edit_task1.setPlainText("Task 1 results will appear here.")
        task1_layout.addWidget(self.text_edit_task1)

        generate_button = QPushButton('Generate Strings')
        generate_button.clicked.connect(self.generate_strings)
        task1_layout.addWidget(generate_button)

        task1_widget.setLayout(task1_layout)
        return task1_widget

    def create_task2_tab(self):
        task2_widget = QWidget()
        task2_layout = QVBoxLayout()

        self.text_edit_task2 = QTextEdit()
        self.text_edit_task2.setPlainText("Task 2 results will appear here.")
        task2_layout.addWidget(self.text_edit_task2)

        generate_button = QPushButton('Generate Sequence')
        generate_button.clicked.connect(self.generate_sequence)
        task2_layout.addWidget(generate_button)

        task2_widget.setLayout(task2_layout)
        return task2_widget

    def create_task3_tab(self):
        task3_widget = QWidget()
        task3_layout = QVBoxLayout()

        self.text_edit_task3 = QTextEdit()
        self.text_edit_task3.setPlainText("Task 3 results will appear here.")
        task3_layout.addWidget(self.text_edit_task3)

        generate_button = QPushButton('Filter Cities')
        generate_button.clicked.connect(self.filter_cities)
        task3_layout.addWidget(generate_button)

        task3_widget.setLayout(task3_layout)
        return task3_widget

    def generate_strings(self):
        result = "\n".join(generate_random_strings(5, 10))  # Генерируем только 5 строк для UI
        self.text_edit_task1.setPlainText(result)

    def generate_sequence(self):
        result = "\n".join(str(value) for value in islice(arithmetic_sequence(-0.5, 0.1), 50))
        self.text_edit_task2.setPlainText(result)

    def filter_cities(self):
        city_names = "New York Moscow Sydney London Paris"
        result = "\n".join(map_cities(city_names))
        self.text_edit_task3.setPlainText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = MainWindow()
    app_window.show()
    sys.exit(app.exec())
