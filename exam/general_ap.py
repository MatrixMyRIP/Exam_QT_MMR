import time
from sys import platform
import cpuinfo
import os

import psutil
import win32com.client
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout

from exam.ui.process import Ui_Form_Process
from exam.ui.scheduler import Ui_Form_Scheduler
from exam.ui.services import Ui_Form_Services
from ui.general import Ui_Form_General


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while True:
            cpu_name = cpuinfo.get_cpu_info()
            cpu_cores = psutil.cpu_count()
            cpu_value = psutil.cpu_percent()
            ram_total = psutil.virtual_memory().total / (1024.0 ** 3)
            ram_used = psutil.virtual_memory().used / (1024.0 ** 3)
            processes = [item.name() for item in psutil.process_iter()]
            services = [service.name() for service in psutil.win_service_iter()]
            scheduler = self.scheduler_list()
            self.systemInfoReceived.emit([cpu_name['brand_raw'], cpu_cores, cpu_value, round(ram_total, 2),
                                          round(ram_used, 2), processes, services, scheduler])
            time.sleep(self.delay)

    def setDelay(self, delay):
        self.delay = delay

    def scheduler_list(self):
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        tasks = scheduler.GetFolder('\\').GetTasks(0)
        tasks_list = ""
        for task in tasks:
            tsk = task.Name
            pr = str(task.Path)
            state = task.State
            if state == 1:
                state = "Выполняется"
            if state == 2:
                state = "Готова"
            if state == 3:
                state = "Приостановлена"
            last_run = task.LastRunTime
            next_run = task.NextRunTime
            enb = task.Enabled
            if enb:
                enb = "Включена"
            if not enb:
                enb = "Выключена"
            tasks_list += (f"Название задачи:{tsk}\nМестоположение задачи:{pr}\nСостояние задачи:{state}\n"
                          f"Последнее время выполнения:{last_run}\nСледующее время выполнения:{next_run}\n"
                          f"Статус задачи:{enb}\n---\n")
        return tasks_list


class SystemWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form_General()
        self.ui.setupUi(self)
        self.initSignals()
        self.initThreads()

    def initThreads(self) -> None:
        self.thread = SystemInfo()
        self.thread.systemInfoReceived.connect(self.checkUP)
        self.thread.start()

    def checkUP(self, value) -> None:
        self.ui.proclineEdit.setText(f"{value[0]}")
        self.ui.yadrlineEdit.setText(f"{value[1]}")
        self.ui.lineEdit_cpu.setText(f"{value[2]} %")
        self.ui.lineEdit_ram.setText(f"{value[3]} Gb")
        self.ui.lineEdit_ramvalue.setText(f"{value[4]} Gb")
        self.ui.lineEdit_hdd.setText(self.disc_count())
        self.ui.plainTextEdit_hdd_about.setPlainText(self.disc_info_full())

    def disc_count(self):
        disc_info_full = psutil.disk_partitions()
        disc_num = len(disc_info_full)
        return f"{disc_num}"

    def disc_info_full(self):
        disc_info_full = psutil.disk_partitions()
        disks_info = ""
        for i, disc in enumerate(disc_info_full):
            if os.name == 'nt':
                if 'cdrom' in disc.opts or disc.fstype == '':
                    continue
            info = psutil.disk_usage(disc.mountpoint)
            total = info.total // (1024 ** 3)
            used = info.used // (1024 ** 3)
            free = info.free // (1024 ** 3)
            disks_info += f"Диск {i + 1}: {disc.device}: Объем: {total} Gb, Занято: {used} Gb, Свободно: {free} Gb \n"
        return disks_info

    def initSignals(self) -> None:
        self.ui.comboBox_interval.currentIndexChanged.connect(self.update_interval)
        # self.ui.lineEditdelay.textChanged.connect(self.onDelayLineEditTextChanged)

    def update_interval(self, index):
        try:
            if index == 0:
                delay = 1
            if index == 1:
                delay = 5
            if index == 2:
                delay = 15
            if index == 3:
                delay = 30
            self.thread.setDelay(delay)
        except Exception:
            pass

    # def onDelayLineEditTextChanged(self, data):
    #     try:
    #         delay = int(data)
    #         self.thread.setDelay(delay)
    #     except Exception:
    #         pass


class ProcessWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form_Process()
        self.ui.setupUi(self)
        self.initThreads()

    def initThreads(self) -> None:
        self.thread = SystemInfo()
        self.thread.systemInfoReceived.connect(self.processes_info)
        self.thread.start()

    def processes_info(self, value):
        self.ui.label_process.setText(f"Работающие процессы: {len(value[5])}")
        self.ui.plainTextEdit.setPlainText('\n'.join(value[5]))


class ServicesWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form_Services()
        self.ui.setupUi(self)
        self.initThreads()

    def initThreads(self) -> None:
        self.thread = SystemInfo()
        self.thread.systemInfoReceived.connect(self.services_info)
        self.thread.start()

    def services_info(self, value):
        self.ui.label_services.setText(f"Работающие службы:: {len(value[6])}")
        self.ui.plainTextEdit_2.setPlainText('\n'.join(value[6]))


class SchedulerWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form_Scheduler()
        self.ui.setupUi(self)
        self.initThreads()

    def initThreads(self) -> None:
        self.thread = SystemInfo()
        self.thread.systemInfoReceived.connect(self.scheduler_info)
        self.thread.start()

    def scheduler_info(self, value):
        self.ui.plainTextEdit.setPlainText(f"{value[7]}")


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#         content_widget = QWidget()
#         self.setCentralWidget(content_widget)
#         layout_main = QVBoxLayout()
#         layout_main.addWidget(SystemWindow())
#         layout_main.addWidget(ProcessWindow())
#         layout_main.addWidget(ServicesWindow())
#         layout_main.addWidget(SchedulerWindow())
#         content_widget.setLayout(layout_main)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUIMainWindow()

    def initUIMainWindow(self):
        self.setWindowTitle('Диспетчер задач')
        self.setGeometry(500, 400, 500, 400)

        tab_widget = QTabWidget()
        self.system_info_tab = SystemWindow()
        self.process_tab = ProcessWindow()
        self.service_tab = ServicesWindow()
        self.scheduler_tab = SchedulerWindow()

        tab_widget.addTab(self.system_info_tab, "System Info")
        tab_widget.addTab(self.process_tab, "Process Info")
        tab_widget.addTab(self.service_tab, "Services Info")
        tab_widget.addTab(self.scheduler_tab, "Scheduler Info")

        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(tab_widget)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    # app = QtWidgets.QApplication()
    #
    # window = ServicesWindow()
    # window.show()
    #
    # app.exec()
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    app.exec()
