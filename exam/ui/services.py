# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'servicesZlFToo.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form_Services(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(438, 425)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_services = QLabel(Form)
        self.label_services.setObjectName(u"label_services")
        self.label_services.setMinimumSize(QSize(171, 20))

        self.verticalLayout.addWidget(self.label_services)

        self.plainTextEdit_2 = QPlainTextEdit(Form)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"services", None))
        self.label_services.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0435 \u0441\u043b\u0443\u0436\u0431\u044b:", None))
    # retranslateUi

