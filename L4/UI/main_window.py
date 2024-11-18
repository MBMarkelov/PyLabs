from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from UI import Task3Tab,Task2Tab,Task1Tab


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Lab Tasks")

        layout = QVBoxLayout()
        tabs = QTabWidget()

        tabs.addTab(Task1Tab(), "Task 1")
        tabs.addTab(Task2Tab(), "Task 2")
        tabs.addTab(Task3Tab(), "Task 3")

        layout.addWidget(tabs)
        self.setLayout(layout)
