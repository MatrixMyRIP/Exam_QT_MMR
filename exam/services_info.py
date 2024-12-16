from PySide6 import QtWidgets

from exam.threads import SystemInfo
from exam.ui.services import Ui_Form_Services


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