# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\test\my\python_uart_tool\uart_tool_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from my_combobox import My_ComBoBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 291))
        self.groupBox.setObjectName("groupBox")
        self.timestamp_check_box = QtWidgets.QCheckBox(self.groupBox)
        self.timestamp_check_box.setGeometry(QtCore.QRect(10, 225, 61, 16))
        self.timestamp_check_box.setObjectName("timestamp_check_box")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 175, 54, 12))
        self.label_7.setObjectName("label_7")
        self.rec_hex_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.rec_hex_radio_button.setGeometry(QtCore.QRect(70, 200, 41, 16))
        self.rec_hex_radio_button.setObjectName("rec_hex_radio_button")
        self.com_combo_box = My_ComBoBox(self.groupBox)
        self.com_combo_box.setGeometry(QtCore.QRect(10, 50, 141, 22))
        self.com_combo_box.setObjectName("com_combo_box")
        self.stopbit_combo_box = QtWidgets.QComboBox(self.groupBox)
        self.stopbit_combo_box.setGeometry(QtCore.QRect(58, 110, 91, 22))
        self.stopbit_combo_box.setObjectName("stopbit_combo_box")
        self.stopbit_combo_box.addItem("")
        self.stopbit_combo_box.addItem("")
        self.stopbit_combo_box.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 145, 54, 12))
        self.label_6.setObjectName("label_6")
        self.baud_combo_box = QtWidgets.QComboBox(self.groupBox)
        self.baud_combo_box.setGeometry(QtCore.QRect(58, 80, 91, 22))
        self.baud_combo_box.setObjectName("baud_combo_box")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.baud_combo_box.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 115, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 85, 54, 12))
        self.label_4.setObjectName("label_4")
        self.checkbit_combo_box = QtWidgets.QComboBox(self.groupBox)
        self.checkbit_combo_box.setGeometry(QtCore.QRect(58, 170, 91, 22))
        self.checkbit_combo_box.setObjectName("checkbit_combo_box")
        self.checkbit_combo_box.addItem("")
        self.checkbit_combo_box.addItem("")
        self.checkbit_combo_box.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 22, 54, 20))
        self.label_3.setObjectName("label_3")
        self.databit_combo_box = QtWidgets.QComboBox(self.groupBox)
        self.databit_combo_box.setGeometry(QtCore.QRect(58, 140, 91, 22))
        self.databit_combo_box.setObjectName("databit_combo_box")
        self.databit_combo_box.addItem("")
        self.databit_combo_box.addItem("")
        self.databit_combo_box.addItem("")
        self.databit_combo_box.addItem("")
        self.uart_en_push_button = QtWidgets.QPushButton(self.groupBox)
        self.uart_en_push_button.setGeometry(QtCore.QRect(10, 250, 141, 23))
        self.uart_en_push_button.setObjectName("uart_en_push_button")
        self.rec_ascii_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.rec_ascii_radio_button.setGeometry(QtCore.QRect(10, 200, 51, 16))
        self.rec_ascii_radio_button.setObjectName("rec_ascii_radio_button")
        self.uart_rec_show = QtWidgets.QTextEdit(self.groupBox)
        self.uart_rec_show.setGeometry(QtCore.QRect(170, 10, 601, 271))
        self.uart_rec_show.setFocusPolicy(QtCore.Qt.NoFocus)
        self.uart_rec_show.setObjectName("uart_rec_show")
        self.uart_clear_rec_push_button = QtWidgets.QPushButton(self.groupBox)
        self.uart_clear_rec_push_button.setGeometry(QtCore.QRect(70, 220, 71, 23))
        self.uart_clear_rec_push_button.setObjectName("uart_clear_rec_push_button")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 300, 781, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.send_ascii_radio_button = QtWidgets.QRadioButton(self.groupBox_2)
        self.send_ascii_radio_button.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.send_ascii_radio_button.setObjectName("send_ascii_radio_button")
        self.send_hex_radio_button = QtWidgets.QRadioButton(self.groupBox_2)
        self.send_hex_radio_button.setGeometry(QtCore.QRect(70, 20, 41, 16))
        self.send_hex_radio_button.setObjectName("send_hex_radio_button")
        self.uart_timer_check_box = QtWidgets.QCheckBox(self.groupBox_2)
        self.uart_timer_check_box.setGeometry(QtCore.QRect(10, 47, 47, 16))
        self.uart_timer_check_box.setObjectName("uart_timer_check_box")
        self.uart1_ms_label = QtWidgets.QLabel(self.groupBox_2)
        self.uart1_ms_label.setGeometry(QtCore.QRect(140, 45, 20, 20))
        self.uart1_ms_label.setObjectName("uart1_ms_label")
        self.uart_timer_line_edit = QtWidgets.QLineEdit(self.groupBox_2)
        self.uart_timer_line_edit.setGeometry(QtCore.QRect(70, 45, 61, 20))
        self.uart_timer_line_edit.setObjectName("uart_timer_line_edit")
        self.uart_send_push_button = QtWidgets.QPushButton(self.groupBox_2)
        self.uart_send_push_button.setGeometry(QtCore.QRect(80, 70, 75, 23))
        self.uart_send_push_button.setObjectName("uart_send_push_button")
        self.uart_send_clear_push_button = QtWidgets.QPushButton(self.groupBox_2)
        self.uart_send_clear_push_button.setGeometry(QtCore.QRect(0, 70, 75, 23))
        self.uart_send_clear_push_button.setObjectName("uart_send_clear_push_button")
        self.uart_send_show = QtWidgets.QTextEdit(self.groupBox_2)
        self.uart_send_show.setGeometry(QtCore.QRect(170, 10, 601, 131))
        self.uart_send_show.setFocusPolicy(QtCore.Qt.NoFocus)
        self.uart_send_show.setObjectName("uart_send_show")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 100, 18, 12))
        self.label.setObjectName("label")
        self.uart_tx_data_count_label = QtWidgets.QLabel(self.groupBox_2)
        self.uart_tx_data_count_label.setGeometry(QtCore.QRect(30, 120, 100, 12))
        self.uart_tx_data_count_label.setObjectName("uart_tx_data_count_label")
        self.uart_rx_data_count_label = QtWidgets.QLabel(self.groupBox_2)
        self.uart_rx_data_count_label.setGeometry(QtCore.QRect(30, 100, 100, 12))
        self.uart_rx_data_count_label.setObjectName("uart_rx_data_count_label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 18, 12))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionguanyu = QtWidgets.QAction(MainWindow)
        self.actionguanyu.setObjectName("actionguanyu")
        self.menu.addAction(self.actionguanyu)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "串口接收设置"))
        self.timestamp_check_box.setText(_translate("MainWindow", "时间戳"))
        self.label_7.setText(_translate("MainWindow", "校验位"))
        self.rec_hex_radio_button.setText(_translate("MainWindow", "HEX"))
        self.stopbit_combo_box.setItemText(0, _translate("MainWindow", "1"))
        self.stopbit_combo_box.setItemText(1, _translate("MainWindow", "1.5"))
        self.stopbit_combo_box.setItemText(2, _translate("MainWindow", "2"))
        self.label_6.setText(_translate("MainWindow", "数据位"))
        self.baud_combo_box.setItemText(0, _translate("MainWindow", "110"))
        self.baud_combo_box.setItemText(1, _translate("MainWindow", "300"))
        self.baud_combo_box.setItemText(2, _translate("MainWindow", "600"))
        self.baud_combo_box.setItemText(3, _translate("MainWindow", "1200"))
        self.baud_combo_box.setItemText(4, _translate("MainWindow", "2400"))
        self.baud_combo_box.setItemText(5, _translate("MainWindow", "4800"))
        self.baud_combo_box.setItemText(6, _translate("MainWindow", "9600"))
        self.baud_combo_box.setItemText(7, _translate("MainWindow", "14400"))
        self.baud_combo_box.setItemText(8, _translate("MainWindow", "19200"))
        self.baud_combo_box.setItemText(9, _translate("MainWindow", "38400"))
        self.baud_combo_box.setItemText(10, _translate("MainWindow", "43000"))
        self.baud_combo_box.setItemText(11, _translate("MainWindow", "57600"))
        self.baud_combo_box.setItemText(12, _translate("MainWindow", "76800"))
        self.baud_combo_box.setItemText(13, _translate("MainWindow", "115200"))
        self.baud_combo_box.setItemText(14, _translate("MainWindow", "128000"))
        self.baud_combo_box.setItemText(15, _translate("MainWindow", "230400"))
        self.baud_combo_box.setItemText(16, _translate("MainWindow", "256000"))
        self.baud_combo_box.setItemText(17, _translate("MainWindow", "460800"))
        self.baud_combo_box.setItemText(18, _translate("MainWindow", "921600"))
        self.baud_combo_box.setItemText(19, _translate("MainWindow", "1000000"))
        self.baud_combo_box.setItemText(20, _translate("MainWindow", "2000000"))
        self.baud_combo_box.setItemText(21, _translate("MainWindow", "3000000"))
        self.label_5.setText(_translate("MainWindow", "停止位"))
        self.label_4.setText(_translate("MainWindow", "波特率"))
        self.checkbit_combo_box.setItemText(0, _translate("MainWindow", "None"))
        self.checkbit_combo_box.setItemText(1, _translate("MainWindow", "Odd"))
        self.checkbit_combo_box.setItemText(2, _translate("MainWindow", "Even"))
        self.label_3.setText(_translate("MainWindow", "串口选择"))
        self.databit_combo_box.setItemText(0, _translate("MainWindow", "8"))
        self.databit_combo_box.setItemText(1, _translate("MainWindow", "7"))
        self.databit_combo_box.setItemText(2, _translate("MainWindow", "6"))
        self.databit_combo_box.setItemText(3, _translate("MainWindow", "5"))
        self.uart_en_push_button.setText(_translate("MainWindow", "打开串口"))
        self.rec_ascii_radio_button.setText(_translate("MainWindow", "ASCII"))
        self.uart_clear_rec_push_button.setText(_translate("MainWindow", "清除接收"))
        self.groupBox_2.setTitle(_translate("MainWindow", "串口发送设置"))
        self.send_ascii_radio_button.setText(_translate("MainWindow", "ASCII"))
        self.send_hex_radio_button.setText(_translate("MainWindow", "HEX"))
        self.uart_timer_check_box.setText(_translate("MainWindow", "定时"))
        self.uart1_ms_label.setText(_translate("MainWindow", "ms"))
        self.uart_send_push_button.setText(_translate("MainWindow", "发送数据"))
        self.uart_send_clear_push_button.setText(_translate("MainWindow", "清除发送"))
        self.label.setText(_translate("MainWindow", "R："))
        self.uart_tx_data_count_label.setText(_translate("MainWindow", "0"))
        self.uart_rx_data_count_label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "T："))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.actionguanyu.setText(_translate("MainWindow", "关于"))
