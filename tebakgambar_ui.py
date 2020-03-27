#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tebakgambar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from googletrans import Translator
kamus = Translator()

db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('kamus.db')
db.open()
query = QtSql.QSqlQuery()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 680)
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_Tampilkan_Gambar = QtWidgets.QLabel(self.centralwidget)
        self.label_Tampilkan_Gambar.setGeometry(QtCore.QRect(19, 40, 620, 480))
        self.label_Tampilkan_Gambar.setMaximumSize(QtCore.QSize(800, 800))
        self.label_Tampilkan_Gambar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_Tampilkan_Gambar.setText("")
        self.label_Tampilkan_Gambar.setPixmap(QtGui.QPixmap("img/contoh.jpg"))
        self.label_Tampilkan_Gambar.setObjectName("label_Tampilkan_Gambar")
        
        self.lineEdit_Tebak = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Tebak.setGeometry(QtCore.QRect(20, 540, 511, 80))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Tebak.setFont(font)
        self.lineEdit_Tebak.setObjectName("lineEdit_Tebak")
        
        self.label_Gambar_Status = QtWidgets.QLabel(self.centralwidget)
        self.label_Gambar_Status.setGeometry(QtCore.QRect(680, 40, 240, 240))
        self.label_Gambar_Status.setMaximumSize(QtCore.QSize(800, 800))
        self.label_Gambar_Status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_Gambar_Status.setText("")
        self.label_Gambar_Status.setPixmap(QtGui.QPixmap("img/helmet.png"))
        self.label_Gambar_Status.setScaledContents(True)
        self.label_Gambar_Status.setObjectName("label_Gambar_Status")
        
        self.pushButton_Tebak = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Tebak.setGeometry(QtCore.QRect(540, 540, 99, 81))
        self.pushButton_Tebak.setObjectName("pushButton_Tebak")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(680, 360, 661, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.pushButton_Kamus_En_Id = QtWidgets.QPushButton(self.frame)
        self.pushButton_Kamus_En_Id.setGeometry(QtCore.QRect(450, 180, 99, 81))
        self.pushButton_Kamus_En_Id.setObjectName("pushButton_Kamus_En_Id")
        self.pushButton_Kamus_Id_En = QtWidgets.QPushButton(self.frame)
        self.pushButton_Kamus_Id_En.setGeometry(QtCore.QRect(550, 180, 99, 81))
        self.pushButton_Kamus_Id_En.setObjectName("pushButton_Kamus_Id_En")
        self.lineEdit_Kamus = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Kamus.setGeometry(QtCore.QRect(10, 180, 441, 80))
        font = QtGui.QFont()
        font.setPointSize(18)
        
        self.lineEdit_Kamus.setFont(font)
        self.lineEdit_Kamus.setObjectName("lineEdit_Kamus")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 40, 641, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.label_Kamus_Indonesia = QtWidgets.QLabel(self.frame)
        self.label_Kamus_Indonesia.setGeometry(QtCore.QRect(10, 60, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_Kamus_Indonesia.setFont(font)
        self.label_Kamus_Indonesia.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_Kamus_Indonesia.setObjectName("label_Kamus_Indonesia")
        self.label_Kamus_English = QtWidgets.QLabel(self.frame)
        self.label_Kamus_English.setGeometry(QtCore.QRect(270, 60, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Kamus_English.setFont(font)
        self.label_Kamus_English.setStyleSheet("color: rgb(85, 170, 0);")
        self.label_Kamus_English.setScaledContents(True)
        self.label_Kamus_English.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Kamus_English.setObjectName("label_Kamus_English")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 7, 51, 31))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/indonesia.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(600, 10, 51, 31))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/uk.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(960, 40, 381, 241))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(177, 23, 201, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(290, 5, 81, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(40, 46, 68, 22))
        self.label_8.setObjectName("label_8")
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setGeometry(QtCore.QRect(40, 80, 301, 22))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_9 = QtWidgets.QLabel(self.splitter)
        self.label_9.setObjectName("label_9")
        self.label_Jawaban_benar = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        
        self.label_Jawaban_benar.setFont(font)
        self.label_Jawaban_benar.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_Jawaban_benar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Jawaban_benar.setObjectName("label_Jawaban_benar")
        self.splitter_2 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_2.setGeometry(QtCore.QRect(40, 120, 301, 22))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_10 = QtWidgets.QLabel(self.splitter_2)
        self.label_10.setObjectName("label_10")
        self.label_Jawaban_salah = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        
        self.label_Jawaban_salah.setFont(font)
        self.label_Jawaban_salah.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Jawaban_salah.setObjectName("label_Jawaban_salah")
        self.splitter_3 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_3.setGeometry(QtCore.QRect(40, 160, 301, 22))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_11 = QtWidgets.QLabel(self.splitter_3)
        self.label_11.setObjectName("label_11")
        
        self.label_Jawaban_kamus_en_id = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Jawaban_kamus_en_id.setFont(font)
        self.label_Jawaban_kamus_en_id.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Jawaban_kamus_en_id.setObjectName("label_Jawaban_kamus_en_id")
        self.splitter_4 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_4.setGeometry(QtCore.QRect(40, 200, 301, 22))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_12 = QtWidgets.QLabel(self.splitter_4)
        self.label_12.setObjectName("label_12")
        self.label_Jawaban_kamus_id_en = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Jawaban_kamus_id_en.setFont(font)
        self.label_Jawaban_kamus_id_en.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Jawaban_kamus_id_en.setObjectName("label_Jawaban_kamus_id_en")
        
        self.pushButton_Random = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Random.setGeometry(QtCore.QRect(510, 470, 99, 32))
        self.pushButton_Random.setObjectName("pushButton_Random")
        
        self.comboBox_Category = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Category.setGeometry(QtCore.QRect(165, 470, 240, 32))
        self.comboBox_Category.setObjectName("comboBox_Category")
        #panggil dr db
        query.exec_('select * from category')
        while query.next():
            self.comboBox_Category.addItem(query.value('category_name'))
        
        self.pushButton_Tampilkan_Image = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Tampilkan_Image.setGeometry(QtCore.QRect(407, 470, 99, 32))
        self.pushButton_Tampilkan_Image.setObjectName("pushButton_Tampilkan_Image")
        
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(680, 290, 661, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_Tampilkan_Jawaban = QtWidgets.QLabel(self.frame_3)
        self.label_Tampilkan_Jawaban.setGeometry(QtCore.QRect(80, 10, 571, 41))
        self.label_Tampilkan_Jawaban.setObjectName("label_Tampilkan_Jawaban")
        self.label_Gambar_en = QtWidgets.QLabel(self.centralwidget)
        self.label_Gambar_en.setGeometry(QtCore.QRect(170, 410, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        
        self.label_Gambar_en.setFont(font)
        self.label_Gambar_en.setAutoFillBackground(False)
        self.label_Gambar_en.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_Gambar_en.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Gambar_en.setObjectName("label_Gambar_en")
        self.label_Gambar_Id = QtWidgets.QLabel(self.centralwidget)
        self.label_Gambar_Id.setGeometry(QtCore.QRect(170, 387, 431, 50))
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_Gambar_Id.setFont(font)
        self.label_Gambar_Id.setAutoFillBackground(False)
        self.label_Gambar_Id.setStyleSheet("color: rgb(170, 170, 127);")
        self.label_Gambar_Id.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Gambar_Id.setObjectName("label_Gambar_Id")
        self.label_Gambar_Id_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Gambar_Id_2.setGeometry(QtCore.QRect(170, 360, 431, 50))
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        
        self.label_Gambar_Id_2.setFont(font)
        self.label_Gambar_Id_2.setAutoFillBackground(False)
        self.label_Gambar_Id_2.setStyleSheet("color: rgb(85, 85, 0);")
        self.label_Gambar_Id_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Gambar_Id_2.setObjectName("label_Gambar_Id_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_Kamus_Id_En.clicked.connect(self.klik_kamus_id_en)
        self.pushButton_Kamus_En_Id.clicked.connect(self.klik_kamus_en_id)
        self.pushButton_Random.clicked.connect(self.klik_random)
        self.pushButton_Tampilkan_Image.clicked.connect(self.klik_tampilkan_by_kategori)
        self.pushButton_Tebak.clicked.connect(self.cek_tebakan)
        self.lineEdit_Tebak.returnPressed.connect(self.cek_tebakan)
        self.stats_jawaban_benar()
        self.stats_jawaban_salah()
        self.stats_kamus_en_to_id()
        self.stats_kamus_id_to_en()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Debian's English learning system ver. 1.0"))
        #self.lineEdit_Tebak.setText(_translate("MainWindow", "Welcome to Debian App"))
        self.pushButton_Tebak.setText(_translate("MainWindow", "Shoot!"))
        self.pushButton_Kamus_En_Id.setText(_translate("MainWindow", "Indonesia"))
        self.pushButton_Kamus_Id_En.setText(_translate("MainWindow", "English"))
        #self.lineEdit_Kamus.setText(_translate("MainWindow", "Kamus"))
        #self.label_Kamus_Indonesia.setText(_translate("MainWindow", "Terima Kasih"))
        #self.label_Kamus_English.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Statistik"))
        self.label_8.setText(_translate("MainWindow", "LEVEL"))
        self.label_9.setText(_translate("MainWindow", "Jumlah jawaban benar"))
        #self.label_Jawaban_benar.setText(_translate("MainWindow", "100"))
        self.label_10.setText(_translate("MainWindow", "Jumlah jawaban salah"))
        #self.label_Jawaban_salah.setText(_translate("MainWindow", "100"))
        self.label_11.setText(_translate("MainWindow", "Jumlah translate EN-ID"))
        #self.label_Jawaban_kamus_en_id.setText(_translate("MainWindow", "100"))
        self.label_12.setText(_translate("MainWindow", "Jumlah translate ID-EN"))
        #self.label_Jawaban_kamus_id_en.setText(_translate("MainWindow", "100"))
        self.pushButton_Random.setText(_translate("MainWindow", "Random"))
        self.pushButton_Tampilkan_Image.setText(_translate("MainWindow", "Tampilkan"))
        #self.label_Tampilkan_Jawaban.setText(_translate("MainWindow", "Jawaban Tebakan"))
        #self.label_Gambar_en.setText(_translate("MainWindow", "Nama Gambar"))
        self.label_Gambar_Id.setText(_translate("MainWindow", "Nama Gambar"))
        self.label_Gambar_Id_2.setText(_translate("MainWindow", "Nama Gambar"))

    
    
    def stats_kamus_en_to_id(self):
        query.exec_('select count(*) from dictionary WHERE language_id=2')
        while query.next():
            kata_en_id = query.value(0)
            self.label_Jawaban_kamus_en_id.setText(str(kata_en_id))


    def stats_kamus_id_to_en(self):
        query.exec_('select count(*) from dictionary WHERE language_id=1')
        while query.next():
            kata_id_en = query.value(0)
            self.label_Jawaban_kamus_id_en.setText(str(kata_id_en))
    
    def stats_jawaban_benar(self):
        query.exec_('select count(*) from statistic where answer_status="Benar"')
        while query.next():
            jawaban_benar = query.value(0)
            self.label_Jawaban_benar.setText(str(jawaban_benar))


    def stats_jawaban_salah(self):
        query.exec_('select count(*) from statistic where answer_status="Salah"')
        while query.next():
            jawaban_salah = query.value(0)
            self.label_Jawaban_salah.setText(str(jawaban_salah))

    def klik_kamus_id_en(self):
        x = self.lineEdit_Kamus.text()
        if (x == "") or (x == " ") or (x == "  ") or (x == "    "):
            self.label_Tampilkan_Jawaban.setText("Isian kata yang ingin diterjemahkan tidak boleh kosong!")
        else:
            self.label_Kamus_Indonesia.setText(self.lineEdit_Kamus.text().title())
            kata = kamus.translate(self.lineEdit_Kamus.text(), src='id', dest='en')
            self.label_Kamus_English.setText(kata.text.title())

            query.prepare('insert into dictionary (word, language_id) values(?,?)')
            query.addBindValue(self.lineEdit_Kamus.text().title())
            query.addBindValue(1)
            query.exec_()


            self.stats_kamus_id_to_en()

    def klik_kamus_en_id(self):
        x = self.lineEdit_Kamus.text()
        if (x == "") or (x == " ") or (x == "  ") or (x == "    "):
            self.label_Tampilkan_Jawaban.setText("Isian kata yang ingin diterjemahkan tidak boleh kosong!")
        else:
            self.label_Kamus_English.setText(self.lineEdit_Kamus.text().title())
            kata = kamus.translate(self.lineEdit_Kamus.text(), src='en', dest='id')
            self.label_Kamus_Indonesia.setText(kata.text.title())
            self.stats_kamus_en_to_id()

            query.prepare('insert into dictionary (word, language_id) values(?,?)')
            query.addBindValue(self.lineEdit_Kamus.text().title())
            query.addBindValue(2)
            query.exec_()

            self.stats_kamus_en_to_id()
    
    def klik_random(self):
        global namafile
        query.exec_('select english from vocabulary order by RANDOM() LIMIT 1')
        while query.next():
            namafile = query.value('english')
        
            pathfile = "img/"+str(namafile.lower())+".jpg"
            self.label_Tampilkan_Gambar.setPixmap(QtGui.QPixmap(pathfile))
            self.label_Gambar_en.setText(namafile.title()) 
    
    def klik_tampilkan_by_kategori_v2(self):
        query.exec_('SELECT english from vocabulary LEFT JOIN category ON vocabulary.category_id = category.category_id WHERE category.category_name=:coba ORDER by random() LIMIT 1', {"coba": self.comboBox_Category.currentText()})
        while query.next():
                namafile = query.value('english')
                pathfile = "img/"+str(namafile.lower())+".jpg"
                self.label_Tampilkan_Gambar.setPixmap(QtGui.QPixmap(pathfile))
                self.label_Gambar_en.setText(namafile.title())

    def klik_tampilkan_by_kategori(self):
        global namafile
        if (self.comboBox_Category.currentText() == 'Fruits'):
            query.exec_('select english from vocabulary where category_id = 1  ORDER by RANDOM() limit 1')
            while query.next():
                namafile = query.value('english')
                pathfile = "img/"+str(namafile.lower())+".jpg"
                self.label_Tampilkan_Gambar.setPixmap(QtGui.QPixmap(pathfile))
                self.label_Gambar_en.setText(namafile.title())
        elif (self.comboBox_Category.currentText() == 'Kitchen Utensils'):
            query.exec_('select english from vocabulary where category_id = 2  ORDER by RANDOM() limit 1')
            while query.next():
                namafile = query.value('english')
                pathfile = "img/"+str(namafile.lower())+".jpg"
                self.label_Tampilkan_Gambar.setPixmap(QtGui.QPixmap(pathfile))
                self.label_Gambar_en.setText(namafile.title())
        elif (self.comboBox_Category.currentText() == 'Spices'):
            query.exec_('select english from vocabulary where category_id = 3  ORDER by RANDOM() limit 1')
            while query.next():
                namafile = query.value('english')
                pathfile = "img/"+str(namafile.lower())+".jpg"
                self.label_Tampilkan_Gambar.setPixmap(QtGui.QPixmap(pathfile))
                self.label_Gambar_en.setText(namafile.title())
        elif (self.comboBox_Category.currentText() == 'Vegetables'):
            query.exec_('select english from vocabulary where category_id = 4  ORDER by RANDOM() limit 1')
            while query.next():
                namafile = query.value('english')
                pathfile = "img/"+str(namafile.lower())+".jpg"
                self.label_Tampilkan_Gambar.setPixmap(QtGui.QPixmap(pathfile))
                self.label_Gambar_en.setText(namafile.title())
        else:
            self.label_Tampilkan_Gambar.setPixmap(QtGui.QPixmap("img/contoh.jpg"))

    def cek_tebakan(self):
        if (self.lineEdit_Tebak.text().lower() == namafile.lower()):
            self.label_Tampilkan_Jawaban.setText("Jawaban BENAR!")
            query.prepare('insert into statistic (vocabulary, answer_status) values(?,?)')
            query.addBindValue(namafile.title())
            query.addBindValue("Benar")
            query.exec_()
            
            self.label_Gambar_Status.setPixmap(QtGui.QPixmap("img/benar.jpeg"))

            self.stats_jawaban_benar()
            #query.exec_('select count(*) from statistic where answer_status="Benar"')
            #while query.next():
             #   jawaban_benar = query.value(0)
              #  self.label_Jawaban_benar.setText(str(jawaban_benar))

        else: 
            self.label_Tampilkan_Jawaban.setText("Jawaban SALAH!")
            query.prepare('insert into statistic (vocabulary, answer_status) values(?,?)')
            query.addBindValue(namafile.title())
            query.addBindValue("Salah")
            query.exec_()

            self.label_Gambar_Status.setPixmap(QtGui.QPixmap("img/salah.jpeg"))

            self.stats_jawaban_salah()


   #def status_jawaban(self):
   #     return 0
    

