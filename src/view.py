# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created: Sun Jun 26 23:22:07 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Faunus(object):
    def setupUi(self, Faunus):
        Faunus.setObjectName("Faunus")
        Faunus.resize(682, 400)
        self.centralWidget = QtWidgets.QWidget(Faunus)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_home = QtWidgets.QWidget()
        self.tab_home.setObjectName("tab_home")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_home)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.groupBox_home_status = QtWidgets.QGroupBox(self.tab_home)
        self.groupBox_home_status.setObjectName("groupBox_home_status")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_home_status)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_home_status)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_14.addWidget(self.label_15, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_home_status)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_14.addWidget(self.label, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_home_status)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_14.addWidget(self.label_14, 1, 0, 1, 1)
        self.lbl_main_unseen = QtWidgets.QLabel(self.groupBox_home_status)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_main_unseen.setFont(font)
        self.lbl_main_unseen.setObjectName("lbl_main_unseen")
        self.gridLayout_14.addWidget(self.lbl_main_unseen, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem, 3, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem1, 0, 2, 2, 1)
        self.gridLayout_13.addWidget(self.groupBox_home_status, 0, 1, 1, 1)
        self.groupBox_home_settings = QtWidgets.QGroupBox(self.tab_home)
        self.groupBox_home_settings.setObjectName("groupBox_home_settings")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_home_settings)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.chb_startup_faunus = QtWidgets.QCheckBox(self.groupBox_home_settings)
        self.chb_startup_faunus.setChecked(True)
        self.chb_startup_faunus.setObjectName("chb_startup_faunus")
        self.gridLayout_12.addWidget(self.chb_startup_faunus, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem2, 5, 1, 1, 1)
        self.btn_home_settings_save = QtWidgets.QPushButton(self.groupBox_home_settings)
        self.btn_home_settings_save.setObjectName("btn_home_settings_save")
        self.gridLayout_12.addWidget(self.btn_home_settings_save, 4, 1, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox_home_settings, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_home, "")
        self.tab_mail = QtWidgets.QWidget()
        self.tab_mail.setObjectName("tab_mail")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_mail)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_settings = QtWidgets.QGroupBox(self.tab_mail)
        self.groupBox_settings.setObjectName("groupBox_settings")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_settings)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.chb_automail = QtWidgets.QCheckBox(self.groupBox_settings)
        self.chb_automail.setObjectName("chb_automail")
        self.gridLayout_3.addWidget(self.chb_automail, 0, 0, 1, 1)
        self.chb_startup_automail = QtWidgets.QCheckBox(self.groupBox_settings)
        self.chb_startup_automail.setObjectName("chb_startup_automail")
        self.gridLayout_3.addWidget(self.chb_startup_automail, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_settings, 1, 0, 1, 1)
        self.groupBox_smtp = QtWidgets.QGroupBox(self.tab_mail)
        self.groupBox_smtp.setObjectName("groupBox_smtp")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_smtp)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_smtp)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.lne_smtp_server = QtWidgets.QLineEdit(self.groupBox_smtp)
        self.lne_smtp_server.setFrame(True)
        self.lne_smtp_server.setObjectName("lne_smtp_server")
        self.gridLayout_6.addWidget(self.lne_smtp_server, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_smtp)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 1, 0, 1, 1)
        self.lne_smtp_port = QtWidgets.QLineEdit(self.groupBox_smtp)
        self.lne_smtp_port.setObjectName("lne_smtp_port")
        self.gridLayout_6.addWidget(self.lne_smtp_port, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_smtp, 1, 1, 1, 1)
        self.groupBox_imap = QtWidgets.QGroupBox(self.tab_mail)
        self.groupBox_imap.setObjectName("groupBox_imap")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_imap)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lne_imap_server = QtWidgets.QLineEdit(self.groupBox_imap)
        self.lne_imap_server.setFrame(True)
        self.lne_imap_server.setObjectName("lne_imap_server")
        self.gridLayout_5.addWidget(self.lne_imap_server, 0, 1, 1, 1)
        self.lne_imap_port = QtWidgets.QLineEdit(self.groupBox_imap)
        self.lne_imap_port.setObjectName("lne_imap_port")
        self.gridLayout_5.addWidget(self.lne_imap_port, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_imap)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_imap)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_imap, 0, 1, 1, 1)
        self.groupBox_account = QtWidgets.QGroupBox(self.tab_mail)
        self.groupBox_account.setFlat(False)
        self.groupBox_account.setObjectName("groupBox_account")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_account)
        self.gridLayout.setObjectName("gridLayout")
        self.lne_password = QtWidgets.QLineEdit(self.groupBox_account)
        self.lne_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lne_password.setObjectName("lne_password")
        self.gridLayout.addWidget(self.lne_password, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_account)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lne_username = QtWidgets.QLineEdit(self.groupBox_account)
        self.lne_username.setObjectName("lne_username")
        self.gridLayout.addWidget(self.lne_username, 0, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.groupBox_account)
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_account, 0, 0, 1, 1)
        self.btn_save_mail = QtWidgets.QPushButton(self.tab_mail)
        self.btn_save_mail.setObjectName("btn_save_mail")
        self.gridLayout_7.addWidget(self.btn_save_mail, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_mail, "")
        self.tab_hotspot = QtWidgets.QWidget()
        self.tab_hotspot.setObjectName("tab_hotspot")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_hotspot)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.groupBox_hotspot_create = QtWidgets.QGroupBox(self.tab_hotspot)
        self.groupBox_hotspot_create.setObjectName("groupBox_hotspot_create")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_hotspot_create)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.lne_hotspot_name = QtWidgets.QLineEdit(self.groupBox_hotspot_create)
        self.lne_hotspot_name.setObjectName("lne_hotspot_name")
        self.gridLayout_16.addWidget(self.lne_hotspot_name, 0, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.groupBox_hotspot_create)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_16.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_hotspot_create)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_16.addWidget(self.label_16, 1, 0, 1, 1)
        self.btn_hotspot_on = QtWidgets.QPushButton(self.groupBox_hotspot_create)
        self.btn_hotspot_on.setObjectName("btn_hotspot_on")
        self.gridLayout_16.addWidget(self.btn_hotspot_on, 2, 1, 1, 1)
        self.lne_hotspot_password = QtWidgets.QLineEdit(self.groupBox_hotspot_create)
        self.lne_hotspot_password.setText("")
        self.lne_hotspot_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lne_hotspot_password.setObjectName("lne_hotspot_password")
        self.gridLayout_16.addWidget(self.lne_hotspot_password, 1, 1, 1, 2)
        self.btn_hotspot_off = QtWidgets.QPushButton(self.groupBox_hotspot_create)
        self.btn_hotspot_off.setObjectName("btn_hotspot_off")
        self.gridLayout_16.addWidget(self.btn_hotspot_off, 2, 2, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_hotspot_create, 0, 0, 1, 1)
        self.groupBox_hotspot_settings = QtWidgets.QGroupBox(self.tab_hotspot)
        self.groupBox_hotspot_settings.setObjectName("groupBox_hotspot_settings")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_hotspot_settings)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_20 = QtWidgets.QLabel(self.groupBox_hotspot_settings)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_17.addWidget(self.label_20, 0, 0, 1, 1)
        self.chb_hotspot_datausage = QtWidgets.QCheckBox(self.groupBox_hotspot_settings)
        self.chb_hotspot_datausage.setObjectName("chb_hotspot_datausage")
        self.gridLayout_17.addWidget(self.chb_hotspot_datausage, 1, 0, 1, 1)
        self.chb_startup_hotspot = QtWidgets.QCheckBox(self.groupBox_hotspot_settings)
        self.chb_startup_hotspot.setObjectName("chb_startup_hotspot")
        self.gridLayout_17.addWidget(self.chb_startup_hotspot, 4, 0, 1, 1)
        self.lne_sudo_password = QtWidgets.QLineEdit(self.groupBox_hotspot_settings)
        self.lne_sudo_password.setText("")
        self.lne_sudo_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lne_sudo_password.setObjectName("lne_sudo_password")
        self.gridLayout_17.addWidget(self.lne_sudo_password, 0, 1, 1, 1)
        self.chb_hotspot_advanced_settings = QtWidgets.QCheckBox(self.groupBox_hotspot_settings)
        self.chb_hotspot_advanced_settings.setObjectName("chb_hotspot_advanced_settings")
        self.gridLayout_17.addWidget(self.chb_hotspot_advanced_settings, 1, 1, 1, 1)
        self.bnt_hotspot_save_settings = QtWidgets.QPushButton(self.groupBox_hotspot_settings)
        self.bnt_hotspot_save_settings.setObjectName("bnt_hotspot_save_settings")
        self.gridLayout_17.addWidget(self.bnt_hotspot_save_settings, 4, 1, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_hotspot_settings, 0, 1, 1, 1)
        self.groupBox_hotspot_status = QtWidgets.QGroupBox(self.tab_hotspot)
        self.groupBox_hotspot_status.setObjectName("groupBox_hotspot_status")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBox_hotspot_status)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_21 = QtWidgets.QLabel(self.groupBox_hotspot_status)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_18.addWidget(self.label_21, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_hotspot_status)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_18.addWidget(self.label_17, 0, 0, 1, 1)
        self.lbl_hotspot_datausage = QtWidgets.QLabel(self.groupBox_hotspot_status)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hotspot_datausage.setFont(font)
        self.lbl_hotspot_datausage.setObjectName("lbl_hotspot_datausage")
        self.gridLayout_18.addWidget(self.lbl_hotspot_datausage, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_hotspot_status)
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_18.addWidget(self.label_23, 1, 0, 1, 1)
        self.lbl_hotspot_status = QtWidgets.QLabel(self.groupBox_hotspot_status)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hotspot_status.setFont(font)
        self.lbl_hotspot_status.setObjectName("lbl_hotspot_status")
        self.gridLayout_18.addWidget(self.lbl_hotspot_status, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_hotspot_status)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_18.addWidget(self.label_19, 0, 4, 1, 1)
        self.lbl_hotspot_connecteds = QtWidgets.QLabel(self.groupBox_hotspot_status)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hotspot_connecteds.setFont(font)
        self.lbl_hotspot_connecteds.setObjectName("lbl_hotspot_connecteds")
        self.gridLayout_18.addWidget(self.lbl_hotspot_connecteds, 2, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_hotspot_status)
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_18.addWidget(self.label_25, 1, 4, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_hotspot_status)
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_18.addWidget(self.label_27, 2, 4, 1, 1)
        self.lne_hotspot_inet = QtWidgets.QLineEdit(self.groupBox_hotspot_status)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lne_hotspot_inet.setFont(font)
        self.lne_hotspot_inet.setFrame(False)
        self.lne_hotspot_inet.setReadOnly(True)
        self.lne_hotspot_inet.setObjectName("lne_hotspot_inet")
        self.gridLayout_18.addWidget(self.lne_hotspot_inet, 0, 5, 1, 1)
        self.lne_hotspot_wlan = QtWidgets.QLineEdit(self.groupBox_hotspot_status)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lne_hotspot_wlan.setFont(font)
        self.lne_hotspot_wlan.setFrame(False)
        self.lne_hotspot_wlan.setReadOnly(True)
        self.lne_hotspot_wlan.setObjectName("lne_hotspot_wlan")
        self.gridLayout_18.addWidget(self.lne_hotspot_wlan, 1, 5, 1, 1)
        self.lne_hotspot_ip = QtWidgets.QLineEdit(self.groupBox_hotspot_status)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lne_hotspot_ip.setFont(font)
        self.lne_hotspot_ip.setFrame(False)
        self.lne_hotspot_ip.setReadOnly(True)
        self.lne_hotspot_ip.setObjectName("lne_hotspot_ip")
        self.gridLayout_18.addWidget(self.lne_hotspot_ip, 2, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem3, 0, 2, 3, 1)
        self.gridLayout_15.addWidget(self.groupBox_hotspot_status, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_hotspot, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        Faunus.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(Faunus)
        self.statusBar.setObjectName("statusBar")
        Faunus.setStatusBar(self.statusBar)

        self.retranslateUi(Faunus)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Faunus)

    def retranslateUi(self, Faunus):
        _translate = QtCore.QCoreApplication.translate
        Faunus.setWindowTitle(_translate("Faunus", "Faunus AlphaV0.1"))
        self.groupBox_home_status.setTitle(_translate("Faunus", "Status"))
        self.label_15.setText(_translate("Faunus", "ON"))
        self.label.setText(_translate("Faunus", "Unseen Mail : "))
        self.label_14.setText(_translate("Faunus", "Hotspot : "))
        self.lbl_main_unseen.setText(_translate("Faunus", "3"))
        self.groupBox_home_settings.setTitle(_translate("Faunus", "Settings"))
        self.chb_startup_faunus.setText(_translate("Faunus", "Startup Faunus"))
        self.btn_home_settings_save.setText(_translate("Faunus", "Save Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), _translate("Faunus", "Home"))
        self.groupBox_settings.setTitle(_translate("Faunus", "Settings"))
        self.chb_automail.setText(_translate("Faunus", "Automail Check"))
        self.chb_startup_automail.setText(_translate("Faunus", "Startup Automail"))
        self.groupBox_smtp.setTitle(_translate("Faunus", "Outgoing Settings (SMTP)"))
        self.label_4.setText(_translate("Faunus", "SMTP Server"))
        self.lne_smtp_server.setText(_translate("Faunus", "smtp.metu.edu.tr"))
        self.label_3.setText(_translate("Faunus", "SMTP Port"))
        self.lne_smtp_port.setText(_translate("Faunus", "587"))
        self.groupBox_imap.setTitle(_translate("Faunus", "Incoming Settings (IMAP)"))
        self.lne_imap_server.setText(_translate("Faunus", "imap.metu.edu.tr"))
        self.lne_imap_port.setText(_translate("Faunus", "993"))
        self.label_5.setText(_translate("Faunus", "IMAP Port"))
        self.label_6.setText(_translate("Faunus", "IMAP Server"))
        self.groupBox_account.setTitle(_translate("Faunus", "Login Mail"))
        self.label_2.setText(_translate("Faunus", "Password"))
        self.label_1.setText(_translate("Faunus", "Username"))
        self.btn_save_mail.setText(_translate("Faunus", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mail), _translate("Faunus", "Mail"))
        self.groupBox_hotspot_create.setTitle(_translate("Faunus", "Create Hotspot"))
        self.lne_hotspot_name.setText(_translate("Faunus", "I_am"))
        self.label_13.setText(_translate("Faunus", "Name : "))
        self.label_16.setText(_translate("Faunus", "Password : "))
        self.btn_hotspot_on.setText(_translate("Faunus", "On"))
        self.btn_hotspot_off.setText(_translate("Faunus", "Off"))
        self.groupBox_hotspot_settings.setTitle(_translate("Faunus", "Settings"))
        self.label_20.setText(_translate("Faunus", "Sudo Password : "))
        self.chb_hotspot_datausage.setText(_translate("Faunus", "Data Counter"))
        self.chb_startup_hotspot.setText(_translate("Faunus", "Startup Hotspot"))
        self.chb_hotspot_advanced_settings.setText(_translate("Faunus", "Advanced Settings"))
        self.bnt_hotspot_save_settings.setText(_translate("Faunus", "Save"))
        self.groupBox_hotspot_status.setTitle(_translate("Faunus", "Status"))
        self.label_21.setText(_translate("Faunus", "Connected Devices : "))
        self.label_17.setText(_translate("Faunus", "Hotspot : "))
        self.lbl_hotspot_datausage.setText(_translate("Faunus", "0Mb"))
        self.label_23.setText(_translate("Faunus", "Data Usage : "))
        self.lbl_hotspot_status.setText(_translate("Faunus", "OFF"))
        self.label_19.setText(_translate("Faunus", "Internet Source : "))
        self.lbl_hotspot_connecteds.setText(_translate("Faunus", "0"))
        self.label_25.setText(_translate("Faunus", "Wireless : "))
        self.label_27.setText(_translate("Faunus", "IP Adress : "))
        self.lne_hotspot_inet.setText(_translate("Faunus", "eth0"))
        self.lne_hotspot_wlan.setText(_translate("Faunus", "wlan0"))
        self.lne_hotspot_ip.setText(_translate("Faunus", "192.168.45.1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hotspot), _translate("Faunus", "Hotspot"))

