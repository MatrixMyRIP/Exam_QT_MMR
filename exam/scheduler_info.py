from PySide6 import QtWidgets

from exam.threads import SystemInfo
from exam.ui.scheduler import Ui_Form_Scheduler


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
