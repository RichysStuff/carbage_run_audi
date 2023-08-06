# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Grid_guiRmLHtt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setMaximumSize(QSize(800, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pB_key_1_1 = QPushButton(self.centralwidget)
        self.pB_key_1_1.setObjectName(u"pB_key_1_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_key_1_1.sizePolicy().hasHeightForWidth())
        self.pB_key_1_1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.pB_key_1_1.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_key_1_1.setShortcut(u"3")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_key_1_1, 2, 1, 1, 1)

        self.pB_key_3_1 = QPushButton(self.centralwidget)
        self.pB_key_3_1.setObjectName(u"pB_key_3_1")
        sizePolicy.setHeightForWidth(self.pB_key_3_1.sizePolicy().hasHeightForWidth())
        self.pB_key_3_1.setSizePolicy(sizePolicy)
        self.pB_key_3_1.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_key_3_1.setShortcut(u"9")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_key_3_1, 2, 3, 1, 1)

        self.pTE_console = QPlainTextEdit(self.centralwidget)
        self.pTE_console.setObjectName(u"pTE_console")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pTE_console.sizePolicy().hasHeightForWidth())
        self.pTE_console.setSizePolicy(sizePolicy1)
        self.pTE_console.setMinimumSize(QSize(0, 120))
        self.pTE_console.setMaximumSize(QSize(16777215, 121))
        self.pTE_console.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.pTE_console.setReadOnly(True)

        self.gridLayout.addWidget(self.pTE_console, 0, 0, 1, 5)

        self.pB_key_4_0 = QPushButton(self.centralwidget)
        self.pB_key_4_0.setObjectName(u"pB_key_4_0")
        sizePolicy.setHeightForWidth(self.pB_key_4_0.sizePolicy().hasHeightForWidth())
        self.pB_key_4_0.setSizePolicy(sizePolicy)
        self.pB_key_4_0.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_key_4_0.setShortcut(u"/")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_key_4_0, 1, 4, 1, 1)

        self.pB_key_3_0 = QPushButton(self.centralwidget)
        self.pB_key_3_0.setObjectName(u"pB_key_3_0")
        sizePolicy.setHeightForWidth(self.pB_key_3_0.sizePolicy().hasHeightForWidth())
        self.pB_key_3_0.setSizePolicy(sizePolicy)
        self.pB_key_3_0.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_key_3_0.setShortcut(u"8")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_key_3_0, 1, 3, 1, 1)

        self.pB_key_0_0 = QPushButton(self.centralwidget)
        self.pB_key_0_0.setObjectName(u"pB_key_0_0")
        sizePolicy.setHeightForWidth(self.pB_key_0_0.sizePolicy().hasHeightForWidth())
        self.pB_key_0_0.setSizePolicy(sizePolicy)
        self.pB_key_0_0.setFont(font)

        self.gridLayout.addWidget(self.pB_key_0_0, 1, 0, 1, 1)

        self.pB_key_4_1 = QPushButton(self.centralwidget)
        self.pB_key_4_1.setObjectName(u"pB_key_4_1")
        sizePolicy.setHeightForWidth(self.pB_key_4_1.sizePolicy().hasHeightForWidth())
        self.pB_key_4_1.setSizePolicy(sizePolicy)
        self.pB_key_4_1.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_key_4_1.setShortcut(u"*")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_key_4_1, 2, 4, 1, 1)

        self.pB_all_time_1 = QPushButton(self.centralwidget)
        self.pB_all_time_1.setObjectName(u"pB_all_time_1")
        sizePolicy.setHeightForWidth(self.pB_all_time_1.sizePolicy().hasHeightForWidth())
        self.pB_all_time_1.setSizePolicy(sizePolicy)
        self.pB_all_time_1.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_all_time_1.setShortcut(u"+")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_all_time_1, 3, 2, 1, 1)

        self.pB_all_time_3 = QPushButton(self.centralwidget)
        self.pB_all_time_3.setObjectName(u"pB_all_time_3")
        sizePolicy.setHeightForWidth(self.pB_all_time_3.sizePolicy().hasHeightForWidth())
        self.pB_all_time_3.setSizePolicy(sizePolicy)
        self.pB_all_time_3.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_all_time_3.setShortcut(u"Backspace")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_all_time_3, 3, 4, 1, 1)

        self.pB_key_0_1 = QPushButton(self.centralwidget)
        self.pB_key_0_1.setObjectName(u"pB_key_0_1")
        sizePolicy.setHeightForWidth(self.pB_key_0_1.sizePolicy().hasHeightForWidth())
        self.pB_key_0_1.setSizePolicy(sizePolicy)
        self.pB_key_0_1.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_key_0_1.setShortcut(u",")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_key_0_1, 2, 0, 1, 1)

        self.pB_all_time_0 = QPushButton(self.centralwidget)
        self.pB_all_time_0.setObjectName(u"pB_all_time_0")
        sizePolicy.setHeightForWidth(self.pB_all_time_0.sizePolicy().hasHeightForWidth())
        self.pB_all_time_0.setSizePolicy(sizePolicy)
        self.pB_all_time_0.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_all_time_0.setShortcut(u"Enter")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_all_time_0, 3, 0, 1, 2)

        self.pB_key_2_0 = QPushButton(self.centralwidget)
        self.pB_key_2_0.setObjectName(u"pB_key_2_0")
        sizePolicy.setHeightForWidth(self.pB_key_2_0.sizePolicy().hasHeightForWidth())
        self.pB_key_2_0.setSizePolicy(sizePolicy)
        self.pB_key_2_0.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_key_2_0.setShortcut(u"5")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_key_2_0, 1, 2, 1, 1)

        self.pB_key_2_1 = QPushButton(self.centralwidget)
        self.pB_key_2_1.setObjectName(u"pB_key_2_1")
        sizePolicy.setHeightForWidth(self.pB_key_2_1.sizePolicy().hasHeightForWidth())
        self.pB_key_2_1.setSizePolicy(sizePolicy)
        self.pB_key_2_1.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_key_2_1.setShortcut(u"6")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_key_2_1, 2, 2, 1, 1)

        self.pB_all_time_2 = QPushButton(self.centralwidget)
        self.pB_all_time_2.setObjectName(u"pB_all_time_2")
        sizePolicy.setHeightForWidth(self.pB_all_time_2.sizePolicy().hasHeightForWidth())
        self.pB_all_time_2.setSizePolicy(sizePolicy)
        self.pB_all_time_2.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_all_time_2.setShortcut(u"-")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_all_time_2, 3, 3, 1, 1)

        self.pB_key_1_0 = QPushButton(self.centralwidget)
        self.pB_key_1_0.setObjectName(u"pB_key_1_0")
        sizePolicy.setHeightForWidth(self.pB_key_1_0.sizePolicy().hasHeightForWidth())
        self.pB_key_1_0.setSizePolicy(sizePolicy)
        self.pB_key_1_0.setFont(font)
#if QT_CONFIG(shortcut)
        self.pB_key_1_0.setShortcut(u"2")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.pB_key_1_0, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pB_key_1_1.setText(QCoreApplication.translate("MainWindow", u"Key_1_1", None))
        self.pB_key_3_1.setText(QCoreApplication.translate("MainWindow", u"Key_3_1", None))
        self.pTE_console.setPlaceholderText("")
        self.pB_key_4_0.setText(QCoreApplication.translate("MainWindow", u"Key_4_0", None))
        self.pB_key_3_0.setText(QCoreApplication.translate("MainWindow", u"Key_3_0", None))
        self.pB_key_0_0.setText(QCoreApplication.translate("MainWindow", u"Nicht Belegt", None))
        self.pB_key_4_1.setText(QCoreApplication.translate("MainWindow", u"Key_4_1", None))
        self.pB_all_time_1.setText(QCoreApplication.translate("MainWindow", u"ALA_1", None))
        self.pB_all_time_3.setText(QCoreApplication.translate("MainWindow", u"ALA_3", None))
        self.pB_key_0_1.setText(QCoreApplication.translate("MainWindow", u"Key_0_1", None))
        self.pB_all_time_0.setText(QCoreApplication.translate("MainWindow", u"ALA_0", None))
        self.pB_key_2_0.setText(QCoreApplication.translate("MainWindow", u"Key_2_0", None))
        self.pB_key_2_1.setText(QCoreApplication.translate("MainWindow", u"Key_2_1", None))
        self.pB_all_time_2.setText(QCoreApplication.translate("MainWindow", u"ALA_2", None))
        self.pB_key_1_0.setText(QCoreApplication.translate("MainWindow", u"Key_1_0", None))
    # retranslateUi

