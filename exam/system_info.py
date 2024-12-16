import os

import psutil
from PySide6 import QtWidgets

from exam.threads import SystemInfo
from exam.ui.general import Ui_Form_General


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