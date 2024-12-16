
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout

from exam.process_info import ProcessWindow
from exam.scheduler_info import SchedulerWindow
from exam.services_info import ServicesWindow
from exam.system_info import SystemWindow







class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUIMainWindow()

    def initUIMainWindow(self):
        self.setWindowTitle('Диспетчер задач')
        self.setGeometry(600, 400, 600, 400)
        self.setMinimumSize(QSize(600, 400))
        tab_widget = QTabWidget()
        self.system_info_tab = SystemWindow()
        self.process_tab = ProcessWindow()
        self.service_tab = ServicesWindow()
        self.scheduler_tab = SchedulerWindow()

        tab_widget.addTab(self.system_info_tab, "Сведения о системе")
        tab_widget.addTab(self.process_tab, "Работающие процессы")
        tab_widget.addTab(self.service_tab, "Работающие службы")
        tab_widget.addTab(self.scheduler_tab, "Планировщик заданий")

        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(tab_widget)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    app.exec()
