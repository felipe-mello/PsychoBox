# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resourceGui_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1200, 790)
        Widget.setMinimumSize(QSize(1200, 790))
        Widget.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/img/psychobox.png", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        Widget.setStyleSheet(u"\n"
"QCheckBox{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QCheckBox::indicator{\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(241,102,55);\n"
"	border-radius:6px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	background-color: rgb(241,102,55);\n"
"	border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
" color: rgb(136, 138, 133);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled{\n"
"	background-color: rgb(136, 138, 133);\n"
"}")
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topContent = QFrame(Widget)
        self.topContent.setObjectName(u"topContent")
        self.topContent.setMinimumSize(QSize(0, 50))
        self.topContent.setMaximumSize(QSize(16777215, 70))
        self.topContent.setSizeIncrement(QSize(0, 0))
        self.topContent.setFrameShape(QFrame.NoFrame)
        self.topContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topContent)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.topContent)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(50, 50))
        self.frame_3.setMaximumSize(QSize(50, 70))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
"\n"
"QPushButton {\n"
"	padding-left: 10px;\n"
"	text-align: left;\n"
"	background-color: rgb(70,70,70);\n"
"	border:none;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(140,140,140)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 82, 26)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(70, 70, 70);\n"
"	padding-left: 5px;\n"
"	border-left: 5px solid  rgb(255, 82,26);\n"
"}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame_3)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(50, 50))
        self.menuButton.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"PF BeauSans Pro"])
        font.setPointSize(16)
        font.setBold(True)
        self.menuButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/menuEnabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon1)
        self.menuButton.setIconSize(QSize(30, 30))
        self.menuButton.setCheckable(False)
        self.menuButton.setChecked(False)
        self.menuButton.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.menuButton)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.infoBar = QFrame(self.topContent)
        self.infoBar.setObjectName(u"infoBar")
        self.infoBar.setStyleSheet(u"QFrame{\n"
"	background-color : rgb(117, 117, 117);\n"
"}")
        self.infoBar.setFrameShape(QFrame.NoFrame)
        self.infoBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.infoBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.infoBar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/logos/img/psychobox_logo2.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frameButtons = QFrame(self.infoBar)
        self.frameButtons.setObjectName(u"frameButtons")
        self.frameButtons.setMaximumSize(QSize(120, 30))
        self.frameButtons.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"}")
        self.frameButtons.setFrameShape(QFrame.NoFrame)
        self.frameButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frameButtons)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.minimizeButton = QPushButton(self.frameButtons)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMaximumSize(QSize(20, 20))
        self.minimizeButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #ffbe38;\n"
"	border: 2px solid  #d5a342;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 58)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/img/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon2)

        self.horizontalLayout_7.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.frameButtons)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMinimumSize(QSize(20, 20))
        self.maximizeButton.setMaximumSize(QSize(20, 20))
        self.maximizeButton.setStyleSheet(u"QPushButton {\n"
"	background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"	border: 2px solid  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(220, 147, 0)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/logos/img/maximizar-janela.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon3)
        self.maximizeButton.setIconSize(QSize(12, 16))

        self.horizontalLayout_7.addWidget(self.maximizeButton)

        self.closeAllButton = QPushButton(self.frameButtons)
        self.closeAllButton.setObjectName(u"closeAllButton")
        self.closeAllButton.setMaximumSize(QSize(20, 20))
        self.closeAllButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #fc5753;\n"
"	border: 2px solid  #cf5254;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 119, 119)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/img/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAllButton.setIcon(icon4)
        self.closeAllButton.setIconSize(QSize(12, 12))

        self.horizontalLayout_7.addWidget(self.closeAllButton)


        self.horizontalLayout_5.addWidget(self.frameButtons)


        self.horizontalLayout_2.addWidget(self.infoBar)


        self.verticalLayout.addWidget(self.topContent)

        self.centerContent = QFrame(Widget)
        self.centerContent.setObjectName(u"centerContent")
        self.centerContent.setFrameShape(QFrame.NoFrame)
        self.centerContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.centerContent)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.centerContent)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(50, 0))
        self.leftMenu.setMaximumSize(QSize(50, 16777215))
        self.leftMenu.setSizeIncrement(QSize(0, 0))
        self.leftMenu.setFrameShape(QFrame.NoFrame)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftMenu)
        self.frame.setObjectName(u"frame")
        font1 = QFont()
        font1.setFamilies([u"PF BeauSans Pro"])
        font1.setBold(True)
        self.frame.setFont(font1)
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"}\n"
"QPushButton {\n"
"	padding-left: 10px;\n"
"	text-align: left;\n"
"	background-color: rgb(182, 182, 182);\n"
"	border:none;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(80, 184, 158)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80, 184, 158);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:rgb(80, 184, 158);\n"
"	padding-left: 5px;\n"
"	border-left: 5px solid  rgb(80, 184, 158);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.frame)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setMinimumSize(QSize(50, 49))
        self.homeButton.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"PF BeauSans Pro"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.homeButton.setFont(font2)
        self.homeButton.setStyleSheet(u"QPushButton:checked {\n"
"	background-color:#rgb(80, 184, 158);\n"
"	padding-left:5px;\n"
"	border-left: 5px solid  rgb(241, 102, 55);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/img/homeEnabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon5)
        self.homeButton.setIconSize(QSize(30, 30))
        self.homeButton.setCheckable(True)
        self.homeButton.setChecked(True)
        self.homeButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.homeButton)

        self.filterButton = QPushButton(self.frame)
        self.filterButton.setObjectName(u"filterButton")
        self.filterButton.setEnabled(True)
        self.filterButton.setMinimumSize(QSize(50, 50))
        self.filterButton.setMaximumSize(QSize(16777215, 16777215))
        self.filterButton.setFont(font2)
        self.filterButton.setStyleSheet(u"QPushButton:checked {\n"
"	background-color:#rgb(80, 184, 158);\n"
"	padding-left:5px;\n"
"	border-left: 5px solid  rgb(241, 102, 55);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/img/equalizerEnable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filterButton.setIcon(icon6)
        self.filterButton.setIconSize(QSize(30, 30))
        self.filterButton.setCheckable(True)
        self.filterButton.setChecked(False)
        self.filterButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.filterButton)

        self.calibrationButton = QPushButton(self.frame)
        self.calibrationButton.setObjectName(u"calibrationButton")
        self.calibrationButton.setEnabled(True)
        self.calibrationButton.setMinimumSize(QSize(50, 50))
        self.calibrationButton.setMaximumSize(QSize(16777215, 16777215))
        self.calibrationButton.setFont(font2)
        self.calibrationButton.setStyleSheet(u"QPushButton{\n"
"	padding-left:6px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color:#rgb(80, 184, 158);\n"
"	padding-left:1px;\n"
"	border-left: 5px solid  rgb(241, 102, 55);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/img/calibration.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calibrationButton.setIcon(icon7)
        self.calibrationButton.setIconSize(QSize(40, 40))
        self.calibrationButton.setCheckable(True)
        self.calibrationButton.setChecked(False)
        self.calibrationButton.setAutoRepeat(False)
        self.calibrationButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.calibrationButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 100))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 0, 0, -1)
        self.userButton = QPushButton(self.frame_9)
        self.userButton.setObjectName(u"userButton")
        self.userButton.setEnabled(False)
        self.userButton.setMinimumSize(QSize(50, 50))
        self.userButton.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"PF BeauSans Pro"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.userButton.setFont(font3)
        self.userButton.setLayoutDirection(Qt.LeftToRight)
        self.userButton.setStyleSheet(u"QPushButton:checked {\n"
"	color: rgb(0, 196, 204);\n"
"	border-radius:25px;\n"
"	padding-left:9px\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/img/userEnabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userButton.setIcon(icon8)
        self.userButton.setIconSize(QSize(20, 20))
        self.userButton.setCheckable(True)
        self.userButton.setChecked(False)

        self.verticalLayout_4.addWidget(self.userButton)

        self.settingsButton = QPushButton(self.frame_9)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(50, 50))
        self.settingsButton.setMaximumSize(QSize(16777215, 16777215))
        self.settingsButton.setFont(font3)
        self.settingsButton.setLayoutDirection(Qt.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u":/icons/img/settingsEnable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon9)
        self.settingsButton.setIconSize(QSize(20, 20))
        self.settingsButton.setCheckable(True)
        self.settingsButton.setChecked(False)

        self.verticalLayout_4.addWidget(self.settingsButton)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.rightContent = QStackedWidget(self.centerContent)
        self.rightContent.setObjectName(u"rightContent")
        self.rightContent.setEnabled(True)
        self.rightContent.setFont(font1)
        self.rightContent.setFrameShape(QFrame.NoFrame)
        self.rightContent.setFrameShadow(QFrame.Raised)
        self.welcomePage = QWidget()
        self.welcomePage.setObjectName(u"welcomePage")
        self.horizontalLayout_4 = QHBoxLayout(self.welcomePage)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainContent_2 = QFrame(self.welcomePage)
        self.mainContent_2.setObjectName(u"mainContent_2")
        self.mainContent_2.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(237, 237, 237);\n"
"}")
        self.mainContent_2.setFrameShape(QFrame.StyledPanel)
        self.mainContent_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.mainContent_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.mainContent_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_7)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 0))
        self.frame_17.setMaximumSize(QSize(16777215, 100))
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 10)
        self.welcomeUser = QFrame(self.frame_17)
        self.welcomeUser.setObjectName(u"welcomeUser")
        self.welcomeUser.setMinimumSize(QSize(0, 0))
        self.welcomeUser.setMaximumSize(QSize(16777215, 16777215))
        self.welcomeUser.setFrameShape(QFrame.NoFrame)
        self.welcomeUser.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.welcomeUser)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 5, 0, 0)
        self.welcome = QLabel(self.welcomeUser)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setMinimumSize(QSize(0, 50))
        self.welcome.setMaximumSize(QSize(16777215, 50))
        font4 = QFont()
        font4.setFamilies([u"PF BeauSans Pro"])
        font4.setPointSize(28)
        font4.setBold(True)
        self.welcome.setFont(font4)
        self.welcome.setStyleSheet(u"color: rgb(70, 70, 70); ")
        self.welcome.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_10.addWidget(self.welcome)


        self.horizontalLayout_6.addWidget(self.welcomeUser)


        self.verticalLayout_8.addWidget(self.frame_17)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 450))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_19)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.logo_2 = QLabel(self.frame_19)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setMinimumSize(QSize(300, 125))
        self.logo_2.setMaximumSize(QSize(300, 125))
        self.logo_2.setPixmap(QPixmap(u":/logos/img/psychobox_logo.png"))
        self.logo_2.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.logo_2)


        self.verticalLayout_11.addWidget(self.frame_19)

        self.settings = QFrame(self.frame_16)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(0, 250))
        self.settings.setFrameShape(QFrame.NoFrame)
        self.settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.settings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.settings)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(6, 0, 6, 6)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(0, 0))
        self.frame_44.setMaximumSize(QSize(16777215, 16777215))
        self.frame_44.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px\n"
"}")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_44)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(11, 11, 11, 11)
        self.label_43 = QLabel(self.frame_44)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 40))
        self.label_43.setMaximumSize(QSize(16777215, 40))
        self.label_43.setFont(font)
        self.label_43.setStyleSheet(u"color: rgb(237, 237, 237);")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_43)

        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.label_32 = QLabel(self.frame_45)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(100, 100))
        self.label_32.setMaximumSize(QSize(100, 100))
        self.label_32.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"\n"
"border-radius: 50px;\n"
"padding: 20px;\n"
"border: 5px  solid rgb(237, 237, 237);")
        self.label_32.setPixmap(QPixmap(u":/icons/img/importAudio.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_32)


        self.verticalLayout_23.addWidget(self.frame_45)

        self.label_45 = QLabel(self.frame_44)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 70))
        self.label_45.setMaximumSize(QSize(16777215, 80))
        font5 = QFont()
        font5.setFamilies([u"PF BeauSans Pro"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.label_45.setFont(font5)
        self.label_45.setStyleSheet(u"color: rgb(237, 237, 237);")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_45)


        self.horizontalLayout_25.addWidget(self.frame_44)

        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px\n"
"}")
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_46)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_46 = QLabel(self.frame_46)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 40))
        self.label_46.setMaximumSize(QSize(16777215, 40))
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(u"color: rgb(237, 237, 237);")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_46)

        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.label_47 = QLabel(self.frame_47)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(100, 100))
        self.label_47.setMaximumSize(QSize(100, 100))
        self.label_47.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"border-radius: 50px;\n"
"padding: 20px;\n"
"border: 5px  inset rgb(237, 237, 237);")
        self.label_47.setPixmap(QPixmap(u":/icons/img/filter.png"))
        self.label_47.setScaledContents(True)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_47)


        self.verticalLayout_24.addWidget(self.frame_47)

        self.label_48 = QLabel(self.frame_46)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 70))
        self.label_48.setMaximumSize(QSize(16777215, 80))
        self.label_48.setFont(font5)
        self.label_48.setStyleSheet(u"color: rgb(237, 237, 237);")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_48)


        self.horizontalLayout_25.addWidget(self.frame_46)

        self.frame_48 = QFrame(self.frame_43)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px\n"
"}")
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_48)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_49 = QLabel(self.frame_48)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 40))
        self.label_49.setMaximumSize(QSize(16777215, 40))
        self.label_49.setFont(font)
        self.label_49.setStyleSheet(u"color: rgb(237, 237, 237);")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_49)

        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, 0)
        self.label_50 = QLabel(self.frame_49)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(100, 100))
        self.label_50.setMaximumSize(QSize(100, 100))
        self.label_50.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"border-radius: 50px;\n"
"padding: 20px;\n"
"border: 5px  inset rgb(237, 237, 237);")
        self.label_50.setPixmap(QPixmap(u":/icons/img/metricas.png"))
        self.label_50.setScaledContents(True)
        self.label_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_50)


        self.verticalLayout_25.addWidget(self.frame_49)

        self.label_51 = QLabel(self.frame_48)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 70))
        self.label_51.setMaximumSize(QSize(16777215, 80))
        self.label_51.setFont(font5)
        self.label_51.setStyleSheet(u"color: rgb(237, 237, 237);")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_51)


        self.horizontalLayout_25.addWidget(self.frame_48)


        self.verticalLayout_13.addWidget(self.frame_43)


        self.verticalLayout_11.addWidget(self.settings)


        self.horizontalLayout_10.addWidget(self.frame_16)


        self.verticalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_7.addWidget(self.frame_7)


        self.horizontalLayout_4.addWidget(self.mainContent_2)

        self.rightContent.addWidget(self.welcomePage)
        self.filterPage = QWidget()
        self.filterPage.setObjectName(u"filterPage")
        self.filterPage.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(237, 237, 237);\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.filterPage)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.title = QFrame(self.filterPage)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 80))
        self.title.setMaximumSize(QSize(16777215, 16777215))
        self.title.setFrameShape(QFrame.NoFrame)
        self.title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.title)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.title)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(464, 80))
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 10, 0, 0)
        self.label_9 = QLabel(self.frame_20)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(16777215, 50))
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"color: rgb(70, 70, 70); ")
        self.label_9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_14.addWidget(self.label_9)


        self.horizontalLayout_9.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.title)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_21)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 12, 11, 0)
        self.logo = QLabel(self.frame_21)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(130, 50))
        self.logo.setMaximumSize(QSize(130, 50))
        self.logo.setPixmap(QPixmap(u":/logos/img/psychobox_logo.png"))
        self.logo.setScaledContents(True)

        self.verticalLayout_26.addWidget(self.logo, 0, Qt.AlignRight)


        self.horizontalLayout_9.addWidget(self.frame_21)


        self.verticalLayout_28.addWidget(self.title)

        self.controlFrame = QFrame(self.filterPage)
        self.controlFrame.setObjectName(u"controlFrame")
        self.controlFrame.setEnabled(True)
        self.controlFrame.setMinimumSize(QSize(0, 0))
        self.controlFrame.setSizeIncrement(QSize(0, 0))
        self.controlFrame.setStyleSheet(u"\n"
"\n"
"QSlider::groove:vertical {\n"
"				background:  rgb(80, 184, 158);\n"
"                 width:10px;\n"
"				height: 100px;\n"
"				border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"            border: 0px rgb(255, 255, 255);\n"
"            border-style: outset;\n"
"			 border-radius: 2px;\n"
"            margin: 0px -2px;\n"
"            width: 10px;\n"
"            height: 10px;\n"
"            background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"       background-color:  rgb(182,182,182);\n"
"	   border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:disabled{\n"
"			background-color: rgb(32, 59, 60); \n"
"}\n"
"QSlider::groove:vertical:disabled {\n"
"           background-color:  #006d34;\n"
"			\n"
"}\n"
"QSlider::sub-page:vertical:disabled{\n"
"		background: #4B4B4B;\n"
"}\n"
"")
        self.controlFrame.setFrameShape(QFrame.NoFrame)
        self.controlFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.controlFrame)
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 6)
        self.playerFrame = QFrame(self.controlFrame)
        self.playerFrame.setObjectName(u"playerFrame")
        self.playerFrame.setMaximumSize(QSize(16777212, 160))
        self.playerFrame.setFrameShape(QFrame.NoFrame)
        self.playerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.playerFrame)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 6, -1)
        self.playerFrame_2 = QFrame(self.playerFrame)
        self.playerFrame_2.setObjectName(u"playerFrame_2")
        self.playerFrame_2.setEnabled(True)
        self.playerFrame_2.setFrameShape(QFrame.NoFrame)
        self.playerFrame_2.setFrameShadow(QFrame.Raised)
        self.playerFrame_2.setLineWidth(0)
        self.horizontalLayout_14 = QHBoxLayout(self.playerFrame_2)
        self.horizontalLayout_14.setSpacing(30)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, 0, 20, 0)
        self.importAudio = QFrame(self.playerFrame_2)
        self.importAudio.setObjectName(u"importAudio")
        self.importAudio.setMinimumSize(QSize(0, 100))
        self.importAudio.setMaximumSize(QSize(16777215, 16777215))
        self.importAudio.setFrameShape(QFrame.NoFrame)
        self.importAudio.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.importAudio)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.importAudio)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 0))
        self.frame_52.setMaximumSize(QSize(16777215, 16777215))
        self.frame_52.setSizeIncrement(QSize(0, 0))
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.frame_52)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamilies([u"PF BeauSans Pro"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.listWidget.setFont(font6)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	color: rgb(255, 255, 255);\n"
"	border : 4px solid rgb(80, 184, 158);\n"
"	border-radius:10px;\n"
"	background : rgb(70, 70, 70);\n"
"}\n"
"\n"
"QListWidget:hover {\n"
"	border : 4px solid rgb(255, 161, 78);\n"
"}\n"
"\n"
"\n"
" QListView::item:selected {\n"
"	border : 2px solid #009b4a;\n"
"	background : rgb(97, 176, 155);\n"
"}\n"
"\n"
"QListView::item {\n"
"	padding-right:10px;\n"
"	text-align: right;\n"
"}\n"
"\n"
"")
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listWidget.setItemAlignment(Qt.AlignLeading)

        self.horizontalLayout_30.addWidget(self.listWidget)


        self.horizontalLayout_29.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.importAudio)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(150, 0))
        self.frame_53.setMaximumSize(QSize(16777215, 16777215))
        self.frame_53.setStyleSheet(u"\n"
"QPushButton {\n"
"	padding-left: 5px;\n"
"	text-align: left;\n"
"	background-color: rgb(80, 184, 158);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 161, 78);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(237, 105, 59)\n"
"}\n"
"")
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_53)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.importButton = QPushButton(self.frame_53)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setMinimumSize(QSize(0, 30))
        self.importButton.setFont(font5)
        self.importButton.setIconSize(QSize(20, 20))

        self.verticalLayout_55.addWidget(self.importButton)

        self.removeButton = QPushButton(self.frame_53)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setMinimumSize(QSize(0, 30))
        self.removeButton.setFont(font5)
        self.removeButton.setIconSize(QSize(16, 16))

        self.verticalLayout_55.addWidget(self.removeButton)

        self.removeAllButton = QPushButton(self.frame_53)
        self.removeAllButton.setObjectName(u"removeAllButton")
        self.removeAllButton.setMinimumSize(QSize(0, 30))
        self.removeAllButton.setFont(font5)

        self.verticalLayout_55.addWidget(self.removeAllButton)


        self.horizontalLayout_29.addWidget(self.frame_53, 0, Qt.AlignLeft)


        self.horizontalLayout_14.addWidget(self.importAudio)

        self.buttons = QFrame(self.playerFrame_2)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(0, 0))
        self.buttons.setMaximumSize(QSize(300, 16777215))
        self.buttons.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"")
        self.buttons.setFrameShape(QFrame.NoFrame)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.buttons)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.frame_55 = QFrame(self.buttons)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"")
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Plain)
        self.verticalLayout_57 = QVBoxLayout(self.frame_55)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frameButtonsSE = QFrame(self.frame_55)
        self.frameButtonsSE.setObjectName(u"frameButtonsSE")
        self.frameButtonsSE.setEnabled(True)
        self.frameButtonsSE.setStyleSheet(u"QPushButton {\n"
"	padding-left: 2px;\n"
"	text-align: center;\n"
"	background-color:rgb(80, 184, 158);\n"
"	border: 3px solid rgb(237, 105, 59);\n"
"	border-radius:18px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"")
        self.frameButtonsSE.setFrameShape(QFrame.NoFrame)
        self.frameButtonsSE.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frameButtonsSE)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.playButton = QPushButton(self.frameButtonsSE)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setEnabled(False)
        self.playButton.setMinimumSize(QSize(36, 36))
        self.playButton.setMaximumSize(QSize(36, 36))
        self.playButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/img/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon10)
        self.playButton.setIconSize(QSize(15, 25))

        self.horizontalLayout_31.addWidget(self.playButton)

        self.pauseButton = QPushButton(self.frameButtonsSE)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setEnabled(False)
        self.pauseButton.setMinimumSize(QSize(36, 36))
        self.pauseButton.setMaximumSize(QSize(36, 36))
        self.pauseButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/img/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseButton.setIcon(icon11)
        self.pauseButton.setIconSize(QSize(15, 25))

        self.horizontalLayout_31.addWidget(self.pauseButton)

        self.stopButton = QPushButton(self.frameButtonsSE)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setMinimumSize(QSize(36, 36))
        self.stopButton.setMaximumSize(QSize(36, 36))
        self.stopButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/img/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon12)
        self.stopButton.setIconSize(QSize(13, 25))

        self.horizontalLayout_31.addWidget(self.stopButton)


        self.verticalLayout_57.addWidget(self.frameButtonsSE)


        self.verticalLayout_5.addWidget(self.frame_55)

        self.frame_4 = QFrame(self.buttons)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(True)
        self.frame_4.setStyleSheet(u"QSlider::groove:horizontal {				\n"
"				background-color: rgb(218, 218, 218);\n"
"				height: 10px;\n"
"				 border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"            border: 0px rgb(255, 255, 255);\n"
"            border-style: outset;\n"
"			 border-radius: 2px;\n"
"            margin: -2px 0;\n"
"            width: 20px;\n"
"            height: 20px;\n"
"            background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"       background-color: rgb(80, 184, 158);\n"
"	   border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:disabled{\n"
"			background-color: rgb(32, 59, 60); \n"
"	 		border: 0px rgb(48, 82, 83);\n"
"}\n"
"QSlider::groove:horizontal:disabled {\n"
"           background-color: #4B4B4B;\n"
"			\n"
"}\n"
"QSlider::sub-page:horizontal:disabled{\n"
"		background:  #006d34;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: qradi"
                        "algradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:#fc5753;	\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color:#006d34;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #009b4a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer)

        self.muteButton = QPushButton(self.frame_4)
        self.muteButton.setObjectName(u"muteButton")
        self.muteButton.setEnabled(False)
        self.muteButton.setMinimumSize(QSize(20, 20))
        self.muteButton.setMaximumSize(QSize(20, 20))
        self.muteButton.setStyleSheet(u"QPushButton {\n"
"	border-radius:10px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/img/volume-alto.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/icons/img/volume-mute.png", QSize(), QIcon.Normal, QIcon.On)
        icon13.addFile(u":/icons/img/volume-mute.png", QSize(), QIcon.Active, QIcon.On)
        self.muteButton.setIcon(icon13)
        self.muteButton.setCheckable(True)
        self.muteButton.setChecked(False)
        self.muteButton.setAutoRepeat(False)

        self.horizontalLayout_17.addWidget(self.muteButton)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_4)

        self.volumeSlider = QSlider(self.frame_4)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setEnabled(False)
        self.volumeSlider.setMinimumSize(QSize(200, 0))
        self.volumeSlider.setMaximumSize(QSize(16777215, 16777215))
        self.volumeSlider.setStyleSheet(u"QSlider::groove:horizontal {				\n"
"        width:200px;\n"
"}\n"
"")
        self.volumeSlider.setValue(50)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_17.addWidget(self.volumeSlider)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.buttons)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 150))
        self.frame_2.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(79,186,160,255), stop:1 rgba(0,124,132, 255));\n"
"	}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(70, 70, 70);\n"
"	color: rgb(136,138,133);\n"
"	}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.filterAudioButton = QPushButton(self.frame_2)
        self.filterAudioButton.setObjectName(u"filterAudioButton")
        self.filterAudioButton.setEnabled(False)
        self.filterAudioButton.setMinimumSize(QSize(100, 30))
        self.filterAudioButton.setMaximumSize(QSize(100, 30))
        self.filterAudioButton.setFont(font5)

        self.horizontalLayout_12.addWidget(self.filterAudioButton)

        self.resetButton = QPushButton(self.frame_2)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setEnabled(False)
        self.resetButton.setMinimumSize(QSize(100, 30))
        self.resetButton.setMaximumSize(QSize(100, 30))
        self.resetButton.setFont(font5)
        self.resetButton.setLayoutDirection(Qt.RightToLeft)
        self.resetButton.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.resetButton)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.horizontalLayout_14.addWidget(self.buttons)


        self.verticalLayout_59.addWidget(self.playerFrame_2)


        self.verticalLayout_29.addWidget(self.playerFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_2)

        self.uperSliders = QFrame(self.controlFrame)
        self.uperSliders.setObjectName(u"uperSliders")
        self.uperSliders.setEnabled(True)
        self.uperSliders.setMaximumSize(QSize(16777215, 160))
        self.uperSliders.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	background-color: rgb(80, 184, 158);\n"
"	padding: 2px;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 161, 78);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(237, 105, 59)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255))\n"
"};\n"
"\n"
"\n"
"")
        self.uperSliders.setFrameShape(QFrame.NoFrame)
        self.uperSliders.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.uperSliders)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.uperSliders)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(76, 150))
        self.frame_56.setMaximumSize(QSize(76, 150))
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_56)
        self.verticalLayout_32.setSpacing(3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.switch_50 = QPushButton(self.frame_56)
        self.switch_50.setObjectName(u"switch_50")
        self.switch_50.setEnabled(True)
        self.switch_50.setMinimumSize(QSize(66, 20))
        self.switch_50.setMaximumSize(QSize(65, 20))
        font7 = QFont()
        font7.setFamilies([u"PF BeauSans Pro"])
        font7.setPointSize(11)
        font7.setBold(False)
        self.switch_50.setFont(font7)
        self.switch_50.setCheckable(True)
        self.switch_50.setChecked(False)

        self.verticalLayout_32.addWidget(self.switch_50)

        self.slider_50 = QSlider(self.frame_56)
        self.slider_50.setObjectName(u"slider_50")
        self.slider_50.setEnabled(False)
        self.slider_50.setMinimumSize(QSize(45, 100))
        self.slider_50.setStyleSheet(u"")
        self.slider_50.setMinimum(-50)
        self.slider_50.setMaximum(50)
        self.slider_50.setValue(0)
        self.slider_50.setOrientation(Qt.Vertical)

        self.verticalLayout_32.addWidget(self.slider_50, 0, Qt.AlignHCenter)

        self.label_12 = QLabel(self.frame_56)
        self.label_12.setObjectName(u"label_12")
        font8 = QFont()
        font8.setFamilies([u"PF BeauSans Pro"])
        font8.setPointSize(10)
        font8.setBold(True)
        self.label_12.setFont(font8)
        self.label_12.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_12.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_32.addWidget(self.label_12)


        self.horizontalLayout_13.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.uperSliders)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(76, 150))
        self.frame_57.setMaximumSize(QSize(76, 150))
        self.frame_57.setStyleSheet(u"")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_57)
        self.verticalLayout_33.setSpacing(3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.switch_63 = QPushButton(self.frame_57)
        self.switch_63.setObjectName(u"switch_63")
        self.switch_63.setMinimumSize(QSize(66, 20))
        self.switch_63.setMaximumSize(QSize(65, 20))
        self.switch_63.setFont(font7)
        self.switch_63.setCheckable(True)
        self.switch_63.setChecked(False)

        self.verticalLayout_33.addWidget(self.switch_63)

        self.slider_63 = QSlider(self.frame_57)
        self.slider_63.setObjectName(u"slider_63")
        self.slider_63.setEnabled(False)
        self.slider_63.setMinimumSize(QSize(45, 100))
        self.slider_63.setMinimum(-50)
        self.slider_63.setMaximum(50)
        self.slider_63.setValue(0)
        self.slider_63.setOrientation(Qt.Vertical)

        self.verticalLayout_33.addWidget(self.slider_63, 0, Qt.AlignHCenter)

        self.label_13 = QLabel(self.frame_57)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font8)
        self.label_13.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_13.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_33.addWidget(self.label_13)


        self.horizontalLayout_13.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.uperSliders)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(76, 150))
        self.frame_58.setMaximumSize(QSize(76, 150))
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_58)
        self.verticalLayout_34.setSpacing(3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.switch_80 = QPushButton(self.frame_58)
        self.switch_80.setObjectName(u"switch_80")
        self.switch_80.setMinimumSize(QSize(66, 20))
        self.switch_80.setMaximumSize(QSize(65, 20))
        self.switch_80.setFont(font7)
        self.switch_80.setCheckable(True)
        self.switch_80.setChecked(False)

        self.verticalLayout_34.addWidget(self.switch_80)

        self.slider_80 = QSlider(self.frame_58)
        self.slider_80.setObjectName(u"slider_80")
        self.slider_80.setEnabled(False)
        self.slider_80.setMinimumSize(QSize(45, 100))
        self.slider_80.setMinimum(-50)
        self.slider_80.setMaximum(50)
        self.slider_80.setValue(0)
        self.slider_80.setOrientation(Qt.Vertical)

        self.verticalLayout_34.addWidget(self.slider_80, 0, Qt.AlignHCenter)

        self.label_14 = QLabel(self.frame_58)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font8)
        self.label_14.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_14.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_34.addWidget(self.label_14)


        self.horizontalLayout_13.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.uperSliders)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(76, 150))
        self.frame_59.setMaximumSize(QSize(76, 150))
        self.frame_59.setLayoutDirection(Qt.LeftToRight)
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_59)
        self.verticalLayout_35.setSpacing(3)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.switch_100 = QPushButton(self.frame_59)
        self.switch_100.setObjectName(u"switch_100")
        self.switch_100.setMinimumSize(QSize(66, 20))
        self.switch_100.setMaximumSize(QSize(65, 20))
        self.switch_100.setFont(font7)
        self.switch_100.setCheckable(True)
        self.switch_100.setChecked(False)

        self.verticalLayout_35.addWidget(self.switch_100)

        self.slider_100 = QSlider(self.frame_59)
        self.slider_100.setObjectName(u"slider_100")
        self.slider_100.setEnabled(False)
        self.slider_100.setMinimumSize(QSize(45, 100))
        self.slider_100.setMinimum(-50)
        self.slider_100.setMaximum(50)
        self.slider_100.setValue(0)
        self.slider_100.setOrientation(Qt.Vertical)

        self.verticalLayout_35.addWidget(self.slider_100, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.frame_59)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_15.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_35.addWidget(self.label_15)


        self.horizontalLayout_13.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.uperSliders)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(76, 150))
        self.frame_60.setMaximumSize(QSize(76, 150))
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_60)
        self.verticalLayout_37.setSpacing(3)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.switch_125 = QPushButton(self.frame_60)
        self.switch_125.setObjectName(u"switch_125")
        self.switch_125.setMinimumSize(QSize(66, 20))
        self.switch_125.setMaximumSize(QSize(65, 20))
        self.switch_125.setFont(font7)
        self.switch_125.setCheckable(True)
        self.switch_125.setChecked(False)

        self.verticalLayout_37.addWidget(self.switch_125)

        self.slider_125 = QSlider(self.frame_60)
        self.slider_125.setObjectName(u"slider_125")
        self.slider_125.setEnabled(False)
        self.slider_125.setMinimumSize(QSize(45, 100))
        self.slider_125.setMinimum(-50)
        self.slider_125.setMaximum(50)
        self.slider_125.setValue(0)
        self.slider_125.setOrientation(Qt.Vertical)

        self.verticalLayout_37.addWidget(self.slider_125, 0, Qt.AlignHCenter)

        self.label_16 = QLabel(self.frame_60)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_16.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_37.addWidget(self.label_16)


        self.horizontalLayout_13.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.uperSliders)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(76, 150))
        self.frame_61.setMaximumSize(QSize(76, 150))
        self.frame_61.setFrameShape(QFrame.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_61)
        self.verticalLayout_38.setSpacing(3)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.switch_160 = QPushButton(self.frame_61)
        self.switch_160.setObjectName(u"switch_160")
        self.switch_160.setMinimumSize(QSize(66, 20))
        self.switch_160.setMaximumSize(QSize(65, 20))
        self.switch_160.setFont(font7)
        self.switch_160.setCheckable(True)
        self.switch_160.setChecked(False)

        self.verticalLayout_38.addWidget(self.switch_160)

        self.slider_160 = QSlider(self.frame_61)
        self.slider_160.setObjectName(u"slider_160")
        self.slider_160.setEnabled(False)
        self.slider_160.setMinimumSize(QSize(45, 100))
        self.slider_160.setMinimum(-50)
        self.slider_160.setMaximum(50)
        self.slider_160.setValue(0)
        self.slider_160.setOrientation(Qt.Vertical)

        self.verticalLayout_38.addWidget(self.slider_160, 0, Qt.AlignHCenter)

        self.label_17 = QLabel(self.frame_61)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_17.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_38.addWidget(self.label_17)


        self.horizontalLayout_13.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.uperSliders)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(76, 150))
        self.frame_62.setMaximumSize(QSize(76, 150))
        self.frame_62.setFrameShape(QFrame.NoFrame)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_62)
        self.verticalLayout_39.setSpacing(3)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.switch_200 = QPushButton(self.frame_62)
        self.switch_200.setObjectName(u"switch_200")
        self.switch_200.setMinimumSize(QSize(66, 20))
        self.switch_200.setMaximumSize(QSize(65, 20))
        self.switch_200.setFont(font7)
        self.switch_200.setCheckable(True)
        self.switch_200.setChecked(False)

        self.verticalLayout_39.addWidget(self.switch_200)

        self.slider_200 = QSlider(self.frame_62)
        self.slider_200.setObjectName(u"slider_200")
        self.slider_200.setEnabled(False)
        self.slider_200.setMinimumSize(QSize(45, 100))
        self.slider_200.setMinimum(-50)
        self.slider_200.setMaximum(50)
        self.slider_200.setValue(0)
        self.slider_200.setOrientation(Qt.Vertical)

        self.verticalLayout_39.addWidget(self.slider_200, 0, Qt.AlignHCenter)

        self.label_18 = QLabel(self.frame_62)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_18.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_39.addWidget(self.label_18)


        self.horizontalLayout_13.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.uperSliders)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(76, 150))
        self.frame_63.setMaximumSize(QSize(76, 150))
        self.frame_63.setFrameShape(QFrame.NoFrame)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_63)
        self.verticalLayout_40.setSpacing(3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.switch_250 = QPushButton(self.frame_63)
        self.switch_250.setObjectName(u"switch_250")
        self.switch_250.setMinimumSize(QSize(66, 20))
        self.switch_250.setMaximumSize(QSize(65, 20))
        self.switch_250.setFont(font7)
        self.switch_250.setCheckable(True)
        self.switch_250.setChecked(False)

        self.verticalLayout_40.addWidget(self.switch_250)

        self.slider_250 = QSlider(self.frame_63)
        self.slider_250.setObjectName(u"slider_250")
        self.slider_250.setEnabled(False)
        self.slider_250.setMinimumSize(QSize(45, 100))
        self.slider_250.setMinimum(-50)
        self.slider_250.setMaximum(50)
        self.slider_250.setValue(0)
        self.slider_250.setOrientation(Qt.Vertical)

        self.verticalLayout_40.addWidget(self.slider_250, 0, Qt.AlignHCenter)

        self.label_19 = QLabel(self.frame_63)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font8)
        self.label_19.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_19.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_40.addWidget(self.label_19)


        self.horizontalLayout_13.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.uperSliders)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(76, 150))
        self.frame_64.setMaximumSize(QSize(76, 150))
        self.frame_64.setFrameShape(QFrame.NoFrame)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_64)
        self.verticalLayout_41.setSpacing(3)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.switch_315 = QPushButton(self.frame_64)
        self.switch_315.setObjectName(u"switch_315")
        self.switch_315.setEnabled(True)
        self.switch_315.setMinimumSize(QSize(66, 20))
        self.switch_315.setMaximumSize(QSize(65, 20))
        self.switch_315.setFont(font7)
        self.switch_315.setCheckable(True)
        self.switch_315.setChecked(False)

        self.verticalLayout_41.addWidget(self.switch_315)

        self.slider_315 = QSlider(self.frame_64)
        self.slider_315.setObjectName(u"slider_315")
        self.slider_315.setEnabled(False)
        self.slider_315.setMinimumSize(QSize(45, 100))
        self.slider_315.setMinimum(-50)
        self.slider_315.setMaximum(50)
        self.slider_315.setValue(0)
        self.slider_315.setOrientation(Qt.Vertical)

        self.verticalLayout_41.addWidget(self.slider_315, 0, Qt.AlignHCenter)

        self.label_22 = QLabel(self.frame_64)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font8)
        self.label_22.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_22.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_41.addWidget(self.label_22)


        self.horizontalLayout_13.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.uperSliders)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setEnabled(True)
        self.frame_65.setMinimumSize(QSize(76, 150))
        self.frame_65.setMaximumSize(QSize(76, 150))
        self.frame_65.setFrameShape(QFrame.NoFrame)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_65)
        self.verticalLayout_42.setSpacing(3)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.switch_400 = QPushButton(self.frame_65)
        self.switch_400.setObjectName(u"switch_400")
        self.switch_400.setMinimumSize(QSize(66, 20))
        self.switch_400.setMaximumSize(QSize(65, 20))
        self.switch_400.setFont(font7)
        self.switch_400.setCheckable(True)
        self.switch_400.setChecked(False)

        self.verticalLayout_42.addWidget(self.switch_400)

        self.slider_400 = QSlider(self.frame_65)
        self.slider_400.setObjectName(u"slider_400")
        self.slider_400.setEnabled(False)
        self.slider_400.setMinimumSize(QSize(45, 100))
        self.slider_400.setMinimum(-50)
        self.slider_400.setMaximum(50)
        self.slider_400.setValue(0)
        self.slider_400.setOrientation(Qt.Vertical)

        self.verticalLayout_42.addWidget(self.slider_400, 0, Qt.AlignHCenter)

        self.label_52 = QLabel(self.frame_65)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font8)
        self.label_52.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_52.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_42.addWidget(self.label_52)


        self.horizontalLayout_13.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.uperSliders)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(76, 150))
        self.frame_66.setMaximumSize(QSize(76, 150))
        self.frame_66.setFrameShape(QFrame.NoFrame)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_66)
        self.verticalLayout_43.setSpacing(3)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.switch_500 = QPushButton(self.frame_66)
        self.switch_500.setObjectName(u"switch_500")
        self.switch_500.setMinimumSize(QSize(66, 20))
        self.switch_500.setMaximumSize(QSize(65, 20))
        self.switch_500.setFont(font7)
        self.switch_500.setCheckable(False)
        self.switch_500.setChecked(False)

        self.verticalLayout_43.addWidget(self.switch_500)

        self.slider_500 = QSlider(self.frame_66)
        self.slider_500.setObjectName(u"slider_500")
        self.slider_500.setEnabled(False)
        self.slider_500.setMinimumSize(QSize(45, 100))
        self.slider_500.setMinimum(-50)
        self.slider_500.setMaximum(50)
        self.slider_500.setValue(0)
        self.slider_500.setOrientation(Qt.Vertical)

        self.verticalLayout_43.addWidget(self.slider_500, 0, Qt.AlignHCenter)

        self.label_53 = QLabel(self.frame_66)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font8)
        self.label_53.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_53.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_43.addWidget(self.label_53)


        self.horizontalLayout_13.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.uperSliders)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(76, 150))
        self.frame_67.setMaximumSize(QSize(76, 150))
        self.frame_67.setFrameShape(QFrame.NoFrame)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_67)
        self.verticalLayout_44.setSpacing(3)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.switch_630 = QPushButton(self.frame_67)
        self.switch_630.setObjectName(u"switch_630")
        self.switch_630.setEnabled(True)
        self.switch_630.setMinimumSize(QSize(66, 20))
        self.switch_630.setMaximumSize(QSize(65, 20))
        self.switch_630.setFont(font7)
        self.switch_630.setCheckable(True)
        self.switch_630.setChecked(False)

        self.verticalLayout_44.addWidget(self.switch_630)

        self.slider_630 = QSlider(self.frame_67)
        self.slider_630.setObjectName(u"slider_630")
        self.slider_630.setEnabled(False)
        self.slider_630.setMinimumSize(QSize(45, 100))
        self.slider_630.setMinimum(-50)
        self.slider_630.setMaximum(50)
        self.slider_630.setValue(0)
        self.slider_630.setOrientation(Qt.Vertical)

        self.verticalLayout_44.addWidget(self.slider_630, 0, Qt.AlignHCenter)

        self.label_54 = QLabel(self.frame_67)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font8)
        self.label_54.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_54.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_44.addWidget(self.label_54)


        self.horizontalLayout_13.addWidget(self.frame_67)


        self.verticalLayout_29.addWidget(self.uperSliders)

        self.lowerSliders = QFrame(self.controlFrame)
        self.lowerSliders.setObjectName(u"lowerSliders")
        self.lowerSliders.setMaximumSize(QSize(16777215, 160))
        self.lowerSliders.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	background-color: rgb(80, 184, 158);\n"
"	padding: 2px;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 161, 78);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255))\n"
"};\n"
"\n"
"")
        self.lowerSliders.setFrameShape(QFrame.NoFrame)
        self.lowerSliders.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.lowerSliders)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_84 = QFrame(self.lowerSliders)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(76, 150))
        self.frame_84.setMaximumSize(QSize(76, 150))
        self.frame_84.setFrameShape(QFrame.NoFrame)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_84)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.switch_800 = QPushButton(self.frame_84)
        self.switch_800.setObjectName(u"switch_800")
        self.switch_800.setMinimumSize(QSize(66, 20))
        self.switch_800.setMaximumSize(QSize(65, 20))
        self.switch_800.setFont(font7)
        self.switch_800.setCheckable(True)
        self.switch_800.setChecked(False)

        self.verticalLayout_30.addWidget(self.switch_800)

        self.slider_800 = QSlider(self.frame_84)
        self.slider_800.setObjectName(u"slider_800")
        self.slider_800.setEnabled(False)
        self.slider_800.setMinimumSize(QSize(45, 100))
        self.slider_800.setMinimum(-50)
        self.slider_800.setMaximum(50)
        self.slider_800.setValue(0)
        self.slider_800.setOrientation(Qt.Vertical)

        self.verticalLayout_30.addWidget(self.slider_800, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.frame_84)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_30.addWidget(self.label_6)


        self.horizontalLayout_15.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.lowerSliders)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(76, 150))
        self.frame_85.setMaximumSize(QSize(76, 150))
        self.frame_85.setFrameShape(QFrame.NoFrame)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_85)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.switch_1000 = QPushButton(self.frame_85)
        self.switch_1000.setObjectName(u"switch_1000")
        self.switch_1000.setMinimumSize(QSize(66, 20))
        self.switch_1000.setMaximumSize(QSize(65, 20))
        self.switch_1000.setFont(font7)
        self.switch_1000.setCheckable(True)
        self.switch_1000.setChecked(False)

        self.verticalLayout_31.addWidget(self.switch_1000)

        self.slider_1000 = QSlider(self.frame_85)
        self.slider_1000.setObjectName(u"slider_1000")
        self.slider_1000.setEnabled(False)
        self.slider_1000.setMinimumSize(QSize(45, 100))
        self.slider_1000.setMinimum(-50)
        self.slider_1000.setMaximum(50)
        self.slider_1000.setValue(0)
        self.slider_1000.setOrientation(Qt.Vertical)

        self.verticalLayout_31.addWidget(self.slider_1000, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.frame_85)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font8)
        self.label_7.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_31.addWidget(self.label_7)


        self.horizontalLayout_15.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.lowerSliders)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(76, 150))
        self.frame_86.setMaximumSize(QSize(76, 150))
        self.frame_86.setFrameShape(QFrame.NoFrame)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_86)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.switch_1250 = QPushButton(self.frame_86)
        self.switch_1250.setObjectName(u"switch_1250")
        self.switch_1250.setMinimumSize(QSize(66, 20))
        self.switch_1250.setMaximumSize(QSize(65, 20))
        self.switch_1250.setFont(font7)
        self.switch_1250.setCheckable(True)
        self.switch_1250.setChecked(False)

        self.verticalLayout_45.addWidget(self.switch_1250)

        self.slider_1250 = QSlider(self.frame_86)
        self.slider_1250.setObjectName(u"slider_1250")
        self.slider_1250.setEnabled(False)
        self.slider_1250.setMinimumSize(QSize(45, 100))
        self.slider_1250.setMinimum(-50)
        self.slider_1250.setMaximum(50)
        self.slider_1250.setValue(0)
        self.slider_1250.setOrientation(Qt.Vertical)

        self.verticalLayout_45.addWidget(self.slider_1250, 0, Qt.AlignHCenter)

        self.label_55 = QLabel(self.frame_86)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font8)
        self.label_55.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_55.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_45.addWidget(self.label_55)


        self.horizontalLayout_15.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.lowerSliders)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(76, 150))
        self.frame_87.setMaximumSize(QSize(76, 150))
        self.frame_87.setFrameShape(QFrame.NoFrame)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_87)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.switch_1600 = QPushButton(self.frame_87)
        self.switch_1600.setObjectName(u"switch_1600")
        self.switch_1600.setMinimumSize(QSize(66, 20))
        self.switch_1600.setMaximumSize(QSize(65, 20))
        self.switch_1600.setFont(font7)
        self.switch_1600.setCheckable(True)
        self.switch_1600.setChecked(False)

        self.verticalLayout_46.addWidget(self.switch_1600)

        self.slider_1600 = QSlider(self.frame_87)
        self.slider_1600.setObjectName(u"slider_1600")
        self.slider_1600.setEnabled(False)
        self.slider_1600.setMinimumSize(QSize(45, 100))
        self.slider_1600.setMinimum(-50)
        self.slider_1600.setMaximum(50)
        self.slider_1600.setValue(0)
        self.slider_1600.setOrientation(Qt.Vertical)

        self.verticalLayout_46.addWidget(self.slider_1600, 0, Qt.AlignHCenter)

        self.label_56 = QLabel(self.frame_87)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font8)
        self.label_56.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_56.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_46.addWidget(self.label_56)


        self.horizontalLayout_15.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.lowerSliders)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(76, 150))
        self.frame_88.setMaximumSize(QSize(76, 150))
        self.frame_88.setFrameShape(QFrame.NoFrame)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_88)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.switch_2000 = QPushButton(self.frame_88)
        self.switch_2000.setObjectName(u"switch_2000")
        self.switch_2000.setMinimumSize(QSize(66, 20))
        self.switch_2000.setMaximumSize(QSize(65, 20))
        self.switch_2000.setFont(font7)
        self.switch_2000.setCheckable(True)
        self.switch_2000.setChecked(False)

        self.verticalLayout_47.addWidget(self.switch_2000)

        self.slider_2000 = QSlider(self.frame_88)
        self.slider_2000.setObjectName(u"slider_2000")
        self.slider_2000.setEnabled(False)
        self.slider_2000.setMinimumSize(QSize(45, 100))
        self.slider_2000.setMinimum(-50)
        self.slider_2000.setMaximum(50)
        self.slider_2000.setValue(0)
        self.slider_2000.setOrientation(Qt.Vertical)

        self.verticalLayout_47.addWidget(self.slider_2000, 0, Qt.AlignHCenter)

        self.label_57 = QLabel(self.frame_88)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font8)
        self.label_57.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_57.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_47.addWidget(self.label_57)


        self.horizontalLayout_15.addWidget(self.frame_88)

        self.frame_89 = QFrame(self.lowerSliders)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(76, 150))
        self.frame_89.setMaximumSize(QSize(76, 150))
        self.frame_89.setFrameShape(QFrame.NoFrame)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_89)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.switch_2500 = QPushButton(self.frame_89)
        self.switch_2500.setObjectName(u"switch_2500")
        self.switch_2500.setMinimumSize(QSize(66, 20))
        self.switch_2500.setMaximumSize(QSize(65, 20))
        self.switch_2500.setFont(font7)
        self.switch_2500.setCheckable(True)
        self.switch_2500.setChecked(False)

        self.verticalLayout_48.addWidget(self.switch_2500)

        self.slider_2500 = QSlider(self.frame_89)
        self.slider_2500.setObjectName(u"slider_2500")
        self.slider_2500.setEnabled(False)
        self.slider_2500.setMinimumSize(QSize(45, 100))
        self.slider_2500.setMinimum(-50)
        self.slider_2500.setMaximum(50)
        self.slider_2500.setValue(0)
        self.slider_2500.setOrientation(Qt.Vertical)

        self.verticalLayout_48.addWidget(self.slider_2500, 0, Qt.AlignHCenter)

        self.label_58 = QLabel(self.frame_89)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font8)
        self.label_58.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_58.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_48.addWidget(self.label_58)


        self.horizontalLayout_15.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.lowerSliders)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(76, 150))
        self.frame_90.setMaximumSize(QSize(76, 150))
        self.frame_90.setFrameShape(QFrame.NoFrame)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_90)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.switch_3150 = QPushButton(self.frame_90)
        self.switch_3150.setObjectName(u"switch_3150")
        self.switch_3150.setMinimumSize(QSize(66, 20))
        self.switch_3150.setMaximumSize(QSize(65, 20))
        self.switch_3150.setFont(font7)
        self.switch_3150.setCheckable(True)
        self.switch_3150.setChecked(False)

        self.verticalLayout_49.addWidget(self.switch_3150)

        self.slider_3150 = QSlider(self.frame_90)
        self.slider_3150.setObjectName(u"slider_3150")
        self.slider_3150.setEnabled(False)
        self.slider_3150.setMinimumSize(QSize(45, 100))
        self.slider_3150.setMinimum(-50)
        self.slider_3150.setMaximum(50)
        self.slider_3150.setValue(0)
        self.slider_3150.setOrientation(Qt.Vertical)

        self.verticalLayout_49.addWidget(self.slider_3150, 0, Qt.AlignHCenter)

        self.label_59 = QLabel(self.frame_90)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font8)
        self.label_59.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_59.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_49.addWidget(self.label_59)


        self.horizontalLayout_15.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.lowerSliders)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(76, 150))
        self.frame_91.setMaximumSize(QSize(76, 150))
        self.frame_91.setFrameShape(QFrame.NoFrame)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_91)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.switch_4000 = QPushButton(self.frame_91)
        self.switch_4000.setObjectName(u"switch_4000")
        self.switch_4000.setMinimumSize(QSize(66, 20))
        self.switch_4000.setMaximumSize(QSize(65, 20))
        self.switch_4000.setFont(font7)
        self.switch_4000.setCheckable(True)
        self.switch_4000.setChecked(False)

        self.verticalLayout_50.addWidget(self.switch_4000)

        self.slider_4000 = QSlider(self.frame_91)
        self.slider_4000.setObjectName(u"slider_4000")
        self.slider_4000.setEnabled(False)
        self.slider_4000.setMinimumSize(QSize(45, 100))
        self.slider_4000.setMinimum(-50)
        self.slider_4000.setMaximum(50)
        self.slider_4000.setValue(0)
        self.slider_4000.setOrientation(Qt.Vertical)

        self.verticalLayout_50.addWidget(self.slider_4000, 0, Qt.AlignHCenter)

        self.label_60 = QLabel(self.frame_91)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font8)
        self.label_60.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_60.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_50.addWidget(self.label_60)


        self.horizontalLayout_15.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.lowerSliders)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(76, 150))
        self.frame_92.setMaximumSize(QSize(76, 150))
        self.frame_92.setFrameShape(QFrame.NoFrame)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_92)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.switch_5000 = QPushButton(self.frame_92)
        self.switch_5000.setObjectName(u"switch_5000")
        self.switch_5000.setMinimumSize(QSize(66, 20))
        self.switch_5000.setMaximumSize(QSize(65, 20))
        self.switch_5000.setFont(font7)
        self.switch_5000.setCheckable(True)
        self.switch_5000.setChecked(False)

        self.verticalLayout_51.addWidget(self.switch_5000)

        self.slider_5000 = QSlider(self.frame_92)
        self.slider_5000.setObjectName(u"slider_5000")
        self.slider_5000.setEnabled(False)
        self.slider_5000.setMinimumSize(QSize(45, 100))
        self.slider_5000.setMinimum(-50)
        self.slider_5000.setMaximum(50)
        self.slider_5000.setValue(0)
        self.slider_5000.setOrientation(Qt.Vertical)

        self.verticalLayout_51.addWidget(self.slider_5000, 0, Qt.AlignHCenter)

        self.label_61 = QLabel(self.frame_92)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font8)
        self.label_61.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_61.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_51.addWidget(self.label_61)


        self.horizontalLayout_15.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.lowerSliders)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(76, 150))
        self.frame_93.setMaximumSize(QSize(76, 150))
        self.frame_93.setFrameShape(QFrame.NoFrame)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_93)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.switch_6300 = QPushButton(self.frame_93)
        self.switch_6300.setObjectName(u"switch_6300")
        self.switch_6300.setMinimumSize(QSize(66, 20))
        self.switch_6300.setMaximumSize(QSize(65, 20))
        self.switch_6300.setFont(font7)
        self.switch_6300.setCheckable(True)
        self.switch_6300.setChecked(False)

        self.verticalLayout_52.addWidget(self.switch_6300)

        self.slider_6300 = QSlider(self.frame_93)
        self.slider_6300.setObjectName(u"slider_6300")
        self.slider_6300.setEnabled(False)
        self.slider_6300.setMinimumSize(QSize(45, 100))
        self.slider_6300.setMinimum(-50)
        self.slider_6300.setMaximum(50)
        self.slider_6300.setValue(0)
        self.slider_6300.setOrientation(Qt.Vertical)

        self.verticalLayout_52.addWidget(self.slider_6300, 0, Qt.AlignHCenter)

        self.label_62 = QLabel(self.frame_93)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font8)
        self.label_62.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_62.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_52.addWidget(self.label_62)


        self.horizontalLayout_15.addWidget(self.frame_93)

        self.frame_94 = QFrame(self.lowerSliders)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(76, 150))
        self.frame_94.setMaximumSize(QSize(76, 150))
        self.frame_94.setFrameShape(QFrame.NoFrame)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_94)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.switch_8000 = QPushButton(self.frame_94)
        self.switch_8000.setObjectName(u"switch_8000")
        self.switch_8000.setMinimumSize(QSize(66, 20))
        self.switch_8000.setMaximumSize(QSize(65, 20))
        self.switch_8000.setFont(font7)
        self.switch_8000.setCheckable(True)
        self.switch_8000.setChecked(False)

        self.verticalLayout_53.addWidget(self.switch_8000)

        self.slider_8000 = QSlider(self.frame_94)
        self.slider_8000.setObjectName(u"slider_8000")
        self.slider_8000.setEnabled(False)
        self.slider_8000.setMinimumSize(QSize(45, 100))
        self.slider_8000.setMinimum(-50)
        self.slider_8000.setMaximum(50)
        self.slider_8000.setValue(0)
        self.slider_8000.setOrientation(Qt.Vertical)

        self.verticalLayout_53.addWidget(self.slider_8000, 0, Qt.AlignHCenter)

        self.label_63 = QLabel(self.frame_94)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font8)
        self.label_63.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_63.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_53.addWidget(self.label_63)


        self.horizontalLayout_15.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.lowerSliders)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(76, 150))
        self.frame_95.setMaximumSize(QSize(76, 140))
        self.frame_95.setFrameShape(QFrame.NoFrame)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_95)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.switch_10000 = QPushButton(self.frame_95)
        self.switch_10000.setObjectName(u"switch_10000")
        self.switch_10000.setMinimumSize(QSize(66, 20))
        self.switch_10000.setMaximumSize(QSize(65, 20))
        self.switch_10000.setFont(font7)
        self.switch_10000.setCheckable(True)
        self.switch_10000.setChecked(False)

        self.verticalLayout_54.addWidget(self.switch_10000)

        self.slider_10000 = QSlider(self.frame_95)
        self.slider_10000.setObjectName(u"slider_10000")
        self.slider_10000.setEnabled(False)
        self.slider_10000.setMinimumSize(QSize(45, 100))
        self.slider_10000.setMinimum(-50)
        self.slider_10000.setMaximum(50)
        self.slider_10000.setValue(0)
        self.slider_10000.setOrientation(Qt.Vertical)

        self.verticalLayout_54.addWidget(self.slider_10000, 0, Qt.AlignHCenter)

        self.label_64 = QLabel(self.frame_95)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font8)
        self.label_64.setStyleSheet(u"color: rgb(80, 184, 158)")
        self.label_64.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_54.addWidget(self.label_64)


        self.horizontalLayout_15.addWidget(self.frame_95)


        self.verticalLayout_29.addWidget(self.lowerSliders)

        self.frame_100 = QFrame(self.controlFrame)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setLayoutDirection(Qt.RightToLeft)
        self.frame_100.setStyleSheet(u"")
        self.frame_100.setFrameShape(QFrame.NoFrame)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 20, 0)

        self.verticalLayout_29.addWidget(self.frame_100)


        self.verticalLayout_28.addWidget(self.controlFrame)

        self.rightContent.addWidget(self.filterPage)
        self.calibrationPage = QWidget()
        self.calibrationPage.setObjectName(u"calibrationPage")
        self.calibrationPage.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(237, 237, 237);\n"
"}")
        self.verticalLayout_89 = QVBoxLayout(self.calibrationPage)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.SupCalibrationSetup = QFrame(self.calibrationPage)
        self.SupCalibrationSetup.setObjectName(u"SupCalibrationSetup")
        self.SupCalibrationSetup.setMinimumSize(QSize(0, 80))
        self.SupCalibrationSetup.setMaximumSize(QSize(16777215, 140))
        self.SupCalibrationSetup.setFrameShape(QFrame.NoFrame)
        self.SupCalibrationSetup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.SupCalibrationSetup)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_128 = QFrame(self.SupCalibrationSetup)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setFrameShape(QFrame.NoFrame)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_128)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(8, 14, 0, 0)
        self.label_96 = QLabel(self.frame_128)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(0, 50))
        self.label_96.setMaximumSize(QSize(16777215, 50))
        self.label_96.setFont(font4)
        self.label_96.setStyleSheet(u"color: rgb(70, 70, 70); ")

        self.horizontalLayout_66.addWidget(self.label_96)


        self.horizontalLayout_65.addWidget(self.frame_128)

        self.frame_129 = QFrame(self.SupCalibrationSetup)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setFrameShape(QFrame.NoFrame)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_129)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 12, 11, 0)
        self.logo_3 = QLabel(self.frame_129)
        self.logo_3.setObjectName(u"logo_3")
        self.logo_3.setMinimumSize(QSize(130, 50))
        self.logo_3.setMaximumSize(QSize(130, 50))
        self.logo_3.setPixmap(QPixmap(u":/logos/img/psychobox_logo.png"))
        self.logo_3.setScaledContents(True)

        self.verticalLayout_88.addWidget(self.logo_3, 0, Qt.AlignRight)


        self.horizontalLayout_65.addWidget(self.frame_129)


        self.verticalLayout_89.addWidget(self.SupCalibrationSetup)

        self.InfCalibrationSetup = QFrame(self.calibrationPage)
        self.InfCalibrationSetup.setObjectName(u"InfCalibrationSetup")
        self.InfCalibrationSetup.setMinimumSize(QSize(0, 0))
        self.InfCalibrationSetup.setStyleSheet(u"b")
        self.InfCalibrationSetup.setFrameShape(QFrame.NoFrame)
        self.InfCalibrationSetup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.InfCalibrationSetup)
        self.horizontalLayout_54.setSpacing(6)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(6, 6, 6, 6)
        self.Import = QFrame(self.InfCalibrationSetup)
        self.Import.setObjectName(u"Import")
        self.Import.setMaximumSize(QSize(16777215, 16777215))
        self.Import.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px\n"
"}")
        self.Import.setFrameShape(QFrame.StyledPanel)
        self.Import.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.Import)
        self.verticalLayout_84.setSpacing(5)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(10, 5, 5, 5)
        self.frame_121 = QFrame(self.Import)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setMinimumSize(QSize(0, 50))
        self.frame_121.setMaximumSize(QSize(16777215, 50))
        self.frame_121.setFrameShape(QFrame.NoFrame)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_59.setSpacing(5)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.frame_121)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(50, 50))
        self.label_86.setMaximumSize(QSize(50, 50))
        self.label_86.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(70,70,70);\n"
"	border-radius: 25px;\n"
"}")
        self.label_86.setPixmap(QPixmap(u":/icons/img/shopping-basket.png"))
        self.label_86.setScaledContents(True)
        self.label_86.setMargin(10)

        self.horizontalLayout_59.addWidget(self.label_86)

        self.label_87 = QLabel(self.frame_121)
        self.label_87.setObjectName(u"label_87")
        font9 = QFont()
        font9.setFamilies([u"PF BeauSans Pro"])
        font9.setPointSize(18)
        font9.setBold(True)
        self.label_87.setFont(font9)
        self.label_87.setStyleSheet(u"color: rgb(70, 70, 70); ")

        self.horizontalLayout_59.addWidget(self.label_87)

        self.checkHold = QCheckBox(self.frame_121)
        self.checkHold.setObjectName(u"checkHold")
        font10 = QFont()
        font10.setFamilies([u"PF BeauSans Pro"])
        font10.setPointSize(10)
        self.checkHold.setFont(font10)
        self.checkHold.setChecked(False)

        self.horizontalLayout_59.addWidget(self.checkHold, 0, Qt.AlignRight)


        self.verticalLayout_84.addWidget(self.frame_121)

        self.frame_122 = QFrame(self.Import)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_122)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.listWidget2 = QListWidget(self.frame_122)
        self.listWidget2.setObjectName(u"listWidget2")
        self.listWidget2.setFont(font6)
        self.listWidget2.setStyleSheet(u"QListWidget {\n"
"	color: rgb(255, 255, 255);\n"
"	border : 4px solid rgb(80, 184, 158);\n"
"	border-radius:10px;\n"
"	background : rgb(70, 70, 70);\n"
"}\n"
"\n"
"QListWidget:hover {\n"
"	border : 4px solid rgb(255, 161, 78);\n"
"}\n"
"\n"
"\n"
" QListView::item:selected {\n"
"	border : 2px solid #009b4a;\n"
"	background : rgb(97, 176, 155);\n"
"}\n"
"\n"
"QListView::item {\n"
"	padding-right:10px;\n"
"	text-align: right;\n"
"}\n"
"\n"
"")

        self.verticalLayout_85.addWidget(self.listWidget2)

        self.frame_123 = QFrame(self.frame_122)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMinimumSize(QSize(0, 130))
        self.frame_123.setStyleSheet(u"\n"
"QPushButton {\n"
"	padding-left: 5px;\n"
"	text-align: left;\n"
"	background-color: rgb(80, 184, 158);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 161, 78);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(237, 105, 59)\n"
"}\n"
"")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_6 = QFrame(self.frame_123)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.importGraph = QPushButton(self.frame_6)
        self.importGraph.setObjectName(u"importGraph")
        self.importGraph.setMinimumSize(QSize(0, 30))
        self.importGraph.setMaximumSize(QSize(120, 16777215))
        font11 = QFont()
        font11.setFamilies([u"PF BeauSans Pro"])
        font11.setPointSize(12)
        self.importGraph.setFont(font11)

        self.verticalLayout_9.addWidget(self.importGraph)

        self.removeGraph = QPushButton(self.frame_6)
        self.removeGraph.setObjectName(u"removeGraph")
        self.removeGraph.setMinimumSize(QSize(0, 30))
        self.removeGraph.setMaximumSize(QSize(120, 16777215))
        self.removeGraph.setFont(font11)

        self.verticalLayout_9.addWidget(self.removeGraph)

        self.removeAllGraph = QPushButton(self.frame_6)
        self.removeAllGraph.setObjectName(u"removeAllGraph")
        self.removeAllGraph.setMinimumSize(QSize(0, 30))
        self.removeAllGraph.setMaximumSize(QSize(120, 16777215))
        self.removeAllGraph.setFont(font11)

        self.verticalLayout_9.addWidget(self.removeAllGraph)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_123)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px;\n"
"}	\n"
"\n"
"QPushButton {\n"
"	padding-left: 8px;\n"
"	text-align: left;\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"	border-radius:18px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(79,186,160,255), stop:1 rgba(0,124,132, 255));\n"
"	}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.plot = QPushButton(self.frame_8)
        self.plot.setObjectName(u"plot")
        self.plot.setEnabled(False)
        self.plot.setMinimumSize(QSize(130, 36))
        self.plot.setMaximumSize(QSize(130, 36))
        font12 = QFont()
        font12.setFamilies([u"PF BeauSans Pro"])
        font12.setPointSize(13)
        font12.setBold(False)
        self.plot.setFont(font12)
        icon14 = QIcon()
        icon14.addFile(u":/icons/img/bar-graph.png", QSize(), QIcon.Normal, QIcon.Off)
        icon14.addFile(u":/icons/img/bar-graph_dis.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.plot.setIcon(icon14)
        self.plot.setIconSize(QSize(20, 20))

        self.verticalLayout_15.addWidget(self.plot, 0, Qt.AlignRight)


        self.horizontalLayout_8.addWidget(self.frame_8)


        self.verticalLayout_85.addWidget(self.frame_123)


        self.verticalLayout_84.addWidget(self.frame_122)


        self.horizontalLayout_54.addWidget(self.Import)


        self.verticalLayout_89.addWidget(self.InfCalibrationSetup)

        self.rightContent.addWidget(self.calibrationPage)

        self.horizontalLayout.addWidget(self.rightContent)


        self.verticalLayout.addWidget(self.centerContent)

        self.bottomContent = QFrame(Widget)
        self.bottomContent.setObjectName(u"bottomContent")
        self.bottomContent.setMinimumSize(QSize(0, 50))
        self.bottomContent.setMaximumSize(QSize(16777215, 70))
        self.bottomContent.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 70, 70);\n"
"}")
        self.bottomContent.setFrameShape(QFrame.NoFrame)
        self.bottomContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.bottomContent)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.bottomContent)
        self.label.setObjectName(u"label")
        self.label.setFont(font10)
        self.label.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_11.addWidget(self.label)

        self.label_23 = QLabel(self.bottomContent)
        self.label_23.setObjectName(u"label_23")
        font13 = QFont()
        font13.setFamilies([u"PF BeauSans Pro"])
        font13.setPointSize(10)
        font13.setBold(False)
        self.label_23.setFont(font13)
        self.label_23.setStyleSheet(u"color: rgb(238, 238, 236);")
        self.label_23.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.horizontalLayout_11.addWidget(self.label_23)


        self.verticalLayout.addWidget(self.bottomContent)


        self.retranslateUi(Widget)

        self.rightContent.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"PsychoBox | v.003", None))
        self.menuButton.setText("")
        self.label_2.setText("")
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.closeAllButton.setText("")
        self.homeButton.setText("")
        self.filterButton.setText("")
        self.calibrationButton.setText("")
#if QT_CONFIG(accessibility)
        self.userButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.userButton.setText("")
#if QT_CONFIG(accessibility)
        self.settingsButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.settingsButton.setText("")
#if QT_CONFIG(accessibility)
        self.rightContent.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.welcome.setText(QCoreApplication.translate("Widget", u"Welcome", None))
        self.logo_2.setText("")
        self.label_43.setText(QCoreApplication.translate("Widget", u"IMPORT YOUR FILES", None))
        self.label_32.setText("")
        self.label_45.setText(QCoreApplication.translate("Widget", u"Work directly \n"
"with audio extensions \n"
"(.wav, .acc, .mp3)", None))
        self.label_46.setText(QCoreApplication.translate("Widget", u"EDIT YOUR SIGNAL", None))
        self.label_47.setText("")
        self.label_48.setText(QCoreApplication.translate("Widget", u"\n"
"Process and listen to \n"
" signals using filters and windows", None))
        self.label_49.setText(QCoreApplication.translate("Widget", u"APPLY METRICS", None))
        self.label_50.setText("")
        self.label_51.setText(QCoreApplication.translate("Widget", u"Use psychoacoustic \n"
" metrics to analyze your signal", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Signal Editor", None))
        self.logo.setText("")
        self.importButton.setText(QCoreApplication.translate("Widget", u"import", None))
        self.removeButton.setText(QCoreApplication.translate("Widget", u"remove", None))
        self.removeAllButton.setText(QCoreApplication.translate("Widget", u"remove all", None))
        self.playButton.setText("")
        self.pauseButton.setText("")
        self.stopButton.setText("")
        self.muteButton.setText("")
        self.filterAudioButton.setText(QCoreApplication.translate("Widget", u"filter", None))
        self.resetButton.setText(QCoreApplication.translate("Widget", u"reset", None))
        self.switch_50.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"50 Hz", None))
        self.switch_63.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"63 Hz", None))
        self.switch_80.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"80 Hz", None))
        self.switch_100.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"100 Hz", None))
        self.switch_125.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"125 Hz", None))
        self.switch_160.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"160 Hz", None))
        self.switch_200.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"200 Hz", None))
        self.switch_250.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"250 Hz", None))
        self.switch_315.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"315 Hz", None))
        self.switch_400.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_52.setText(QCoreApplication.translate("Widget", u"400 Hz", None))
        self.switch_500.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_53.setText(QCoreApplication.translate("Widget", u"500 Hz", None))
        self.switch_630.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_54.setText(QCoreApplication.translate("Widget", u"630 Hz", None))
        self.switch_800.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"800 Hz", None))
        self.switch_1000.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"1 kHz", None))
        self.switch_1250.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_55.setText(QCoreApplication.translate("Widget", u"1.25 kHz", None))
        self.switch_1600.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_56.setText(QCoreApplication.translate("Widget", u"1.6 kHz", None))
        self.switch_2000.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_57.setText(QCoreApplication.translate("Widget", u"2 kHz", None))
        self.switch_2500.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_58.setText(QCoreApplication.translate("Widget", u"2.5 kHz", None))
        self.switch_3150.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_59.setText(QCoreApplication.translate("Widget", u"3.15 kHz", None))
        self.switch_4000.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_60.setText(QCoreApplication.translate("Widget", u"4 kHz", None))
        self.switch_5000.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_61.setText(QCoreApplication.translate("Widget", u"5 kHz", None))
        self.switch_6300.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_62.setText(QCoreApplication.translate("Widget", u"6.3 kHz", None))
        self.switch_8000.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_63.setText(QCoreApplication.translate("Widget", u"8 kHz", None))
        self.switch_10000.setText(QCoreApplication.translate("Widget", u"off", None))
        self.label_64.setText(QCoreApplication.translate("Widget", u"10 kHz", None))
        self.label_96.setText(QCoreApplication.translate("Widget", u"Calibration Setup", None))
        self.logo_3.setText("")
        self.label_86.setText("")
        self.label_87.setText(QCoreApplication.translate("Widget", u"Basket", None))
        self.checkHold.setText(QCoreApplication.translate("Widget", u"Hold on", None))
        self.importGraph.setText(QCoreApplication.translate("Widget", u"import", None))
        self.removeGraph.setText(QCoreApplication.translate("Widget", u"remove", None))
        self.removeAllGraph.setText(QCoreApplication.translate("Widget", u"remove all", None))
        self.plot.setText(QCoreApplication.translate("Widget", u"plot", None))
        self.label.setText("")
        self.label_23.setText(QCoreApplication.translate("Widget", u"Develop by Henrique Silveira\n"
"Juc\u00e9lio Tavares and Ricardo Brum", None))
    # retranslateUi

