# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sysinfoSaMBOG.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form_General(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(416, 541)
        Form.setMinimumSize(QSize(350, 280))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.proclabel = QLabel(Form)
        self.proclabel.setObjectName(u"proclabel")
        self.proclabel.setMinimumSize(QSize(154, 0))

        self.horizontalLayout.addWidget(self.proclabel)

        self.proclineEdit = QLineEdit(Form)
        self.proclineEdit.setObjectName(u"proclineEdit")
        self.proclineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.proclineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.yadrlabel = QLabel(Form)
        self.yadrlabel.setObjectName(u"yadrlabel")
        self.yadrlabel.setMinimumSize(QSize(154, 0))

        self.horizontalLayout_2.addWidget(self.yadrlabel)

        self.yadrlineEdit = QLineEdit(Form)
        self.yadrlineEdit.setObjectName(u"yadrlineEdit")
        self.yadrlineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.yadrlineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_cpu = QLabel(Form)
        self.label_cpu.setObjectName(u"label_cpu")
        self.label_cpu.setMinimumSize(QSize(154, 0))

        self.horizontalLayout_3.addWidget(self.label_cpu)

        self.lineEdit_cpu = QLineEdit(Form)
        self.lineEdit_cpu.setObjectName(u"lineEdit_cpu")
        self.lineEdit_cpu.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_cpu)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_ram = QLabel(Form)
        self.label_ram.setObjectName(u"label_ram")
        self.label_ram.setMinimumSize(QSize(154, 0))

        self.horizontalLayout_4.addWidget(self.label_ram)

        self.lineEdit_ram = QLineEdit(Form)
        self.lineEdit_ram.setObjectName(u"lineEdit_ram")
        self.lineEdit_ram.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_ram)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_ramvalue = QLabel(Form)
        self.label_ramvalue.setObjectName(u"label_ramvalue")
        self.label_ramvalue.setMinimumSize(QSize(154, 0))

        self.horizontalLayout_5.addWidget(self.label_ramvalue)

        self.lineEdit_ramvalue = QLineEdit(Form)
        self.lineEdit_ramvalue.setObjectName(u"lineEdit_ramvalue")
        self.lineEdit_ramvalue.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_ramvalue)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_hdd = QLabel(Form)
        self.label_hdd.setObjectName(u"label_hdd")

        self.horizontalLayout_6.addWidget(self.label_hdd)

        self.lineEdit_hdd = QLineEdit(Form)
        self.lineEdit_hdd.setObjectName(u"lineEdit_hdd")
        self.lineEdit_hdd.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_hdd)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.label_hdd_about = QLabel(Form)
        self.label_hdd_about.setObjectName(u"label_hdd_about")

        self.verticalLayout.addWidget(self.label_hdd_about)

        self.plainTextEdit_hdd_about = QPlainTextEdit(Form)
        self.plainTextEdit_hdd_about.setObjectName(u"plainTextEdit_hdd_about")

        self.verticalLayout.addWidget(self.plainTextEdit_hdd_about)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_interval = QLabel(Form)
        self.label_interval.setObjectName(u"label_interval")

        self.horizontalLayout_7.addWidget(self.label_interval)

        self.comboBox_interval = QComboBox(Form)
        self.comboBox_interval.addItem("")
        self.comboBox_interval.addItem("")
        self.comboBox_interval.addItem("")
        self.comboBox_interval.addItem("")
        self.comboBox_interval.setObjectName(u"comboBox_interval")

        self.horizontalLayout_7.addWidget(self.comboBox_interval)

        self.label_interval_2 = QLabel(Form)
        self.label_interval_2.setObjectName(u"label_interval_2")

        self.horizontalLayout_7.addWidget(self.label_interval_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"general", None))
        self.proclabel.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430:", None))
        self.yadrlabel.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044f\u0434\u0435\u0440", None))
        self.label_cpu.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU", None))
        self.label_ram.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044a\u0435\u043c \u043f\u0430\u043c\u044f\u0442\u0438", None))
        self.label_ramvalue.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 RAM", None))
        self.label_hdd.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0436\u0435\u0441\u0442\u043a\u0438\u0445 \u0434\u0438\u0441\u043a\u043e\u0432", None))
        self.label_hdd_about.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u043e \u0434\u0438\u0441\u043a\u0430\u043c:", None))
        self.label_interval.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u0447\u0435\u0440\u0435\u0437:", None))
        self.comboBox_interval.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.comboBox_interval.setItemText(1, QCoreApplication.translate("Form", u"5", None))
        self.comboBox_interval.setItemText(2, QCoreApplication.translate("Form", u"15", None))
        self.comboBox_interval.setItemText(3, QCoreApplication.translate("Form", u"30", None))

        self.label_interval_2.setText(QCoreApplication.translate("Form", u"\u0441\u0435\u043a.", None))
    # retranslateUi

