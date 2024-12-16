from PySide6 import QtWidgets

from exam.threads import SystemInfo
from exam.ui.process import Ui_Form_Process


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