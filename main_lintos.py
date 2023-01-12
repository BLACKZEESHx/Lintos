import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import datetime as dt
import pyautogui as auto_press
from PyQt5.QtWebEngineWidgets import *
import os
import psutil
os.system("cls")
auto_press.FailSafeException(False)

class Desktop(QMainWindow):
    def __init__(self):
        super(Desktop, self).__init__()
        self.space_jugar = QShortcut(QKeySequence("ctrl+s"),self)
        self.space_jugar.activated.connect(lambda:self.raise_())
        pic = """Desktop 
        {
            background-image: url('D:/lintos/bg_images/bg1.png');
            background-position: center; 
            background-repeat: no-repeat;
        }
        """
        self.setStyleSheet(pic)
        self.taskbar = QHBoxLayout()
        self.start_button = QCheckBox(self)
        self.start_button.setShortcut(QKeySequence("Meta"))
        self.start_button.clicked.connect(self.animation_of_start_button)
        self.taskbar.addWidget(self.start_button)

        self.searchtask = QCheckBox(self)
        self.searchtask.setFixedSize(30,30)
        # self.searchtask.setShortcut(QKeySequence("ctrl+2"))
        self.searchtask.clicked.connect(lambda: print("sd"))
        self.taskbar.addWidget(self.searchtask)

        self.explorer = QCheckBox(self)
        self.explorer.setFixedSize(30,30)
        # self.explorer.setShortcut(QKeySequence("ctrl+2"))
        self.explorer.clicked.connect(self.showExplorer)
        self.taskbar.addWidget(self.explorer)
        self.explorer.setStyleSheet("""
        *{
            background-color: transparent;
            background-image: url(D:/lintos/taskbar_icon/explorer.png);
            background-position: center; 
            background-repeat: no-repeat;
        }

        QCheckBox::indicator {
            background-color: transparent;
            width: 45px;
            height: 45px;
        }
        """)
        
        self.browser = QCheckBox(self)
        self.browser.setFixedSize(30,30)
        # self.browser.setShortcut(QKeySequence("ctrl+2"))
        self.browser.clicked.connect(self.show_browser)
        self.taskbar.addWidget(self.browser)
        # self.browser.setStyleSheet
        

        self.taskbar_time = QLabel("00:00")
        self.taskbar_time.setFixedSize(50,38)
        self.taskbar.addWidget(self.taskbar_time)
        self.start_button.setFixedSize(30,30)
        self.start_button.setStyleSheet("""*{
            background-color: transparent;
            background-image: url(D:/lintos/taskbar_icon/start.png);
            background-position: center; 
            background-repeat: no-repeat;
        }
        *:hover{
            background-image: url(D:/lintos/taskbar_icon/start_h.png);
            background-position: center; 
            background-repeat: no-repeat;

        }
        *:pressed{
            background-image: url(D:/lintos/taskbar_icon/start.png);
        }
        QCheckBox::indicator {
            background: transparent; 
            width:45px; 
            height:45px;
        }
        """)
        self.widget = QWidget(self)
        self.widget.setStyleSheet("background-color: black;")
        self.widget.setGeometry(0,728,1360,40)
        self.widget.setLayout(self.taskbar)
    
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.searchbox = QLineEdit(self)
        self.searchbox.setStyleSheet("""
        *{
            width:80px;
            height: 80px;
            background-color: rgb(49, 49, 49);
            color: rgb(222,222,222);
            border-radius: 9px;
        }
        *:focus{
            color: white;
        }""")

        
        self.st_an = QWidget(self)
        self.st_an.setStyleSheet("background-color: gray;")
        self.st_an.setGeometry(0,0,1366,730)
        # self.st_an.setWindowOpacity(0.5)
        # self.st_an.setLayout()
        self.st_an.setVisible(False)

    def showExplorer(self):

        if self.explorer.isChecked():
            # layout
            self.exlay = QGridLayout()
            # main explorer widget 
            self.explorerw = QWidget(self)
            

            # doing some sst 
            # self.explorerw.setStyleSheet("background-color: transparent; ")
            # setting up
            self.explorerw.setGeometry(0,0,1366,728)
            # seting layout 
            self.explorerw.setLayout(self.exlay)
            
            self.nimatio_of_explorer1 = QPropertyAnimation(self.explorerw,b"geometry")
            self.nimatio_of_explorer1.setDuration(500)
            self.nimatio_of_explorer1.setStartValue(QRect(0,770,self.explorerw.geometry().width(),self.explorerw.geometry().height()))
            self.nimatio_of_explorer1.setEndValue(QRect(0,0,self.explorerw.geometry().width(),self.explorerw.geometry().height())) 
            self.nimatio_of_explorer1.setEasingCurve(QEasingCurve.OutBack)#OutQuad OutCubic InExpo OutExpo OutBack InOutBack
            self.explorerw.raise_()
            self.nimatio_of_explorer1.start()

            # making explorer similar to win 10 explorer
            self.maintoolexl = QToolBar()
            # adding in layout 
            # self.exlay.addWidget(self.maintoolexl,0,0)
            self.exlay.addChildWidget(self.maintoolexl)
            # setting main 
            # self.explorer.Wi (self.maintoolexl)
            # some css
            self.maintoolexl.setStyleSheet("background:transparent;")
            # Falsing movable
            self.maintoolexl.setMovable(False)
            # dropmenu
            self.dropbox_drive = QComboBox()
            self.dropbox_drive.addItem("C:")
            self.dropbox_drive.addItem("D:")
            # adding into widget
            self.maintoolexl.addWidget(self.dropbox_drive)
            # some css for it
            self.dropbox_drive.setStyleSheet("""
            *{
                color:white;
            }
            *:selected{
                background:#000000;
            }
                """)
            # adding seperator 
            self.maintoolexl.addSeparator()
        # maiking explorer's url
            self.searchbox_exl = QLineEdit(self)
        # setting place holder
            self.searchbox_exl.setPlaceholderText("This PC")
        # adding inot layout
            self.maintoolexl.addWidget(self.searchbox_exl)
        # some css for it
            self.searchbox_exl.setStyleSheet("""
            *{
                color:white;
                font:bold;

            } """)
            # self.exlay.addWidget(self.searchbox_exl,0,0)
            # setting size of tool bar 
            self.maintoolexl.setFixedHeight(60)
            # drive C 
            self.Clab = QPushButton(self)
            # css for it
            self.Clab.setStyleSheet("""*{
                background-image: url(D:/lintos/taskbar_icon/C_drive.png);
                background-position: left; 
                background-repeat: no repeat;
                width: 60px;
                height:60px;
                color:white;
                font:bold;
                font-size:15px;
                text-align:top left;
                padding-left:70px;

            }""")
            # self.maintoolexl.addWidget(self.Clab)
            # setting text 
            self.Clab.setText("  Local Disk (C:)")

            # adding into columnize 
            self.exlay.addWidget(self.Clab,1,0)

            # making d drive
            self.Dlab = QPushButton(self)
            # css for it
            self.Dlab.setStyleSheet("""*{
                background-image: url(D:/lintos/taskbar_icon/C_drive.png);
                background-position: left; 
                background-repeat: no repeat;
                width: 60px;
                height:60px;
                color:white;
                font:bold;
                font-size:15px;
                text-align:top left;
                padding-left:70px;

            }""")
            # self.maintoolexl.addWidget(self.Clab)
            # setting text 
            self.Dlab.setText("  Local Disk (D:)")
            # adding into widget 
            self.exlay.addWidget(self.Dlab,1,1)

            # cheking c free space 
            stats_c = psutil.disk_usage('C:')
            free_space = stats_c.free
            pro = free_space / (1024 ** 3)        
        
            # checking d free space 
            stats_d = psutil.disk_usage('D:')
            free_spaced = stats_d.free
            prod = free_spaced / (1024 ** 3)

        # making progressbar to show how much it full for d disk 
            self.disk_progress_d = QProgressBar(self.Dlab)
            # setting value of space 
            self.disk_progress_d.setValue(int(prod))
            # setting size
            self.disk_progress_d.setFixedHeight(20)
            self.disk_progress_d.setFixedWidth(200)
            # setiing geometry
            self.disk_progress_d.setGeometry(80,25,200,20)
            # css for it 
            self.disk_progress_d.setStyleSheet('''
            *{
                border-radius: 12px;
                background: gray;
                text-align:center;
                color: white;
            }

            *::chunk{
                background: black;
                border-radius: 12px;
            }

            ''')

            # making progressbar to show how much it full for c disk
            self.disk_progress_c = QProgressBar(self.Clab)
            # setting value 
            self.disk_progress_c.setValue(int(pro))
            # setting size 
            self.disk_progress_c.setFixedHeight(20)
            self.disk_progress_c.setFixedWidth(200)
            # setting geometry
            self.disk_progress_c.setGeometry(80,25,200,20)
        # some css for it 
            self.disk_progress_c.setStyleSheet('''
            *{
                border-radius: 12px;
                background: gray;
                text-align:center;
                color: white;
            }

            *::chunk{
                background: black;
                border-radius: 12px;
            }

            ''')

            # showing it
            # self.setCentralWidget(self.explorer)
            self.explorerw.setWindowOpacity(0.9)
            self.explorerw.showMaximized()
        elif self.explorer.isChecked()==False:
            self.nimatio_of_explorer = QPropertyAnimation(self.explorerw,b"geometry")
            self.nimatio_of_explorer.setDuration(500)
            self.nimatio_of_explorer.setStartValue(QRect(0,0,self.explorerw.geometry().width(),self.explorerw.geometry().height()))
            self.nimatio_of_explorer.setEndValue(QRect(0,770,self.explorerw.geometry().width(),self.explorerw.geometry().height())) 
            self.nimatio_of_explorer.setEasingCurve(QEasingCurve.OutBack)#OutQuad OutCubic InExpo OutExpo OutBack InOutBack
            self.nimatio_of_explorer.start()
            self.explorerw.setVisible(False)
            

        if self.explorer.isChecked() and self.start_button.isChecked():
            self.start_button.setChecked(False)
            self.nimatio_of_st2 = QPropertyAnimation(self.st_an,b"geometry")
            self.nimatio_of_st2.setDuration(400)
            self.nimatio_of_st2.setStartValue(QRect(0,self.st_an.geometry().y(),self.st_an.geometry().width(),self.st_an.geometry().height())) 
            self.nimatio_of_st2.setEndValue(QRect(0,770,self.st_an.geometry().width(),self.st_an.geometry().height())) 
            self.nimatio_of_st2.setEasingCurve(QEasingCurve.OutQuad)
            self.nimatio_of_st2.start()
        


            # self.explorer.

    def update_time(self):
        # Get the current time
        current_time = dt.datetime.now().strftime('%H:%M:%S\n%d:%M:%Y')

        # Update the time label
        self.taskbar_time.setText(current_time)
        self.taskbar
        self.taskbar_time.setMaximumWidth(56)
        self.taskbar_time.setStyleSheet("color: white;")



        # self.mousePressEvent = self.remove_widget

        
    def animation_of_start_button(self):
        # self.st_an.setGeometry(self.start_button.geometry().left(),self.start_button.geometry().y()+759,700,600)
        if self.start_button.isChecked():
            self.setVisible(True)
            # self.st_an.
            self.st_an.showFullScreen()
            self.st_an.raise_()
            self.nimatio_of_st = QPropertyAnimation(self.st_an,b"geometry")
            self.nimatio_of_st.setDuration(500)
            self.nimatio_of_st.setStartValue(QRect(0,770,self.st_an.geometry().width(),self.st_an.geometry().height()))
            self.nimatio_of_st.setEndValue(QRect(0,0,self.st_an.geometry().width(),self.st_an.geometry().height())) 
            self.nimatio_of_st.setEasingCurve(QEasingCurve.OutBack)#OutQuad OutCubic InExpo OutExpo OutBack InOutBack
            self.nimatio_of_st.start()
            
        elif self.start_button.isChecked()==False:
            self.nimatio_of_st2 = QPropertyAnimation(self.st_an,b"geometry")
            self.nimatio_of_st2.setDuration(400)
            self.nimatio_of_st2.setStartValue(QRect(0,self.st_an.geometry().y(),self.st_an.geometry().width(),self.st_an.geometry().height())) 
            self.nimatio_of_st2.setEndValue(QRect(0,770,self.st_an.geometry().width(),self.st_an.geometry().height())) 
            self.nimatio_of_st2.setEasingCurve(QEasingCurve.OutQuad)
            self.nimatio_of_st2.start()
            # self.st_an.setVisible(False)

            
    def event(self, event):
        if event.type() == QEvent.KeyPress:
            # Check if the Windows logo key was pressed
            if event.key() == Qt.Key_Meta:
                auto_press.press("ctrl")
                self.start_button.click()
                # Ignore the key press and do nothing
                return True
        return super().event(event)
        
        # self.st_an.setLayout(self.taskbar)


    # def remove_widget(self, event):
    #     # Hide the widget
    #     self.start_button.setChecked(False)
    #     if self.start_button.isChecked()==False:
    #         self.st_an.setHidden(True)
    def show_browser(self):
        if self.browser.isChecked():
            self.br_w = QWebEngineView(self)
            self.br_w.load(QUrl("http://www.youtube.com"))
            self.br_w.setGeometry(0,0,1366,728)
            self.br_w.show()



app = QApplication(sys.argv)
window = Desktop()
window.showFullScreen()
sys.exit(app.exec_())
# #######################################################################
'''        *:hover{
            background-image: url(D:/lintos/taskbar_icon/start_h.png);
            background-position: center; 
            background-repeat: no-repeat;

        }
        *:pressed{
            background-image: url(D:/lintos/taskbar_icon/start.png);
            padding:
        }'''
        ########################################################