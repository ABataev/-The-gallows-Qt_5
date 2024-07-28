import sys
import os
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtWidgets
from random import choice
from PyQt5.QtGui import QPixmap


DB_NAME = 'visilicha_db.sqlite'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Виселица")
        MainWindow.resize(833, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 140, 47, 13))
        self.label.setObjectName("label")
        self.label.resize(200, 200)
        self.line_slovo = QtWidgets.QLineEdit(self.centralwidget)
        self.line_slovo.setGeometry(QtCore.QRect(570, 70, 161, 20))
        self.line_slovo.setText("")
        self.line_slovo.setObjectName("line_slovo")
        self.line_slovo.setEnabled(False)
        self.but_new_game = QtWidgets.QPushButton(self.centralwidget)
        self.but_new_game.setGeometry(QtCore.QRect(290, 350, 121, 23))
        self.but_new_game.setObjectName("but_new_game")
        self.but_history = QtWidgets.QPushButton(self.centralwidget)
        self.but_history.setGeometry(QtCore.QRect(430, 350, 111, 23))
        self.but_history.setObjectName("but_history")
        self.but_file = QtWidgets.QPushButton(self.centralwidget)
        self.but_file.setGeometry(QtCore.QRect(570, 350, 231, 23))
        self.but_file.setObjectName("but_file")
        self.line_razgovora = QtWidgets.QLineEdit(self.centralwidget)
        self.line_razgovora.setGeometry(QtCore.QRect(430, 10, 371, 20))
        self.line_razgovora.setObjectName("line_razgovora")
        self.line_razgovora.setEnabled(False)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 245, 317))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.but_a = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_a.setObjectName("but_a")
        self.verticalLayout.addWidget(self.but_a)
        self.but_g = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_g.setObjectName("but_g")
        self.verticalLayout.addWidget(self.but_g)
        self.but_io = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_io.setObjectName("but_io")
        self.verticalLayout.addWidget(self.but_io)
        self.but_i = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_i.setObjectName("but_i")
        self.verticalLayout.addWidget(self.but_i)
        self.but_l = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_l.setObjectName("but_l")
        self.verticalLayout.addWidget(self.but_l)
        self.but_o = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_o.setObjectName("but_o")
        self.verticalLayout.addWidget(self.but_o)
        self.but_s = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_s.setObjectName("but_s")
        self.verticalLayout.addWidget(self.but_s)
        self.but_f = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_f.setObjectName("but_f")
        self.verticalLayout.addWidget(self.but_f)
        self.but_ch = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_ch.setObjectName("but_ch")
        self.verticalLayout.addWidget(self.but_ch)
        self.but_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_1.setObjectName("but_1")
        self.verticalLayout.addWidget(self.but_1)
        self.but_ea = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_ea.setObjectName("but_ea")
        self.verticalLayout.addWidget(self.but_ea)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.but_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_b.setObjectName("but_b")
        self.verticalLayout_2.addWidget(self.but_b)
        self.but_d = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_d.setObjectName("but_d")
        self.verticalLayout_2.addWidget(self.but_d)
        self.but_zj = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_zj.setObjectName("but_zj")
        self.verticalLayout_2.addWidget(self.but_zj)
        self.but_ie = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_ie.setObjectName("but_ie")
        self.verticalLayout_2.addWidget(self.but_ie)
        self.but_m = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_m.setObjectName("but_m")
        self.verticalLayout_2.addWidget(self.but_m)
        self.but_p = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_p.setObjectName("but_p")
        self.verticalLayout_2.addWidget(self.but_p)
        self.but_t = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_t.setObjectName("but_t")
        self.verticalLayout_2.addWidget(self.but_t)
        self.but_h = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_h.setObjectName("but_h")
        self.verticalLayout_2.addWidget(self.but_h)
        self.but_sh = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_sh.setObjectName("but_sh")
        self.verticalLayout_2.addWidget(self.but_sh)
        self.but_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_2.setObjectName("but_2")
        self.verticalLayout_2.addWidget(self.but_2)
        self.but_u = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_u.setObjectName("but_u")
        self.verticalLayout_2.addWidget(self.but_u)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.but_v = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_v.setObjectName("but_v")
        self.verticalLayout_3.addWidget(self.but_v)
        self.but_e = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_e.setObjectName("but_e")
        self.verticalLayout_3.addWidget(self.but_e)
        self.but_z = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_z.setObjectName("but_z")
        self.verticalLayout_3.addWidget(self.but_z)
        self.but_k = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_k.setObjectName("but_k")
        self.verticalLayout_3.addWidget(self.but_k)
        self.but_n = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_n.setObjectName("but_n")
        self.verticalLayout_3.addWidget(self.but_n)
        self.but_r = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_r.setObjectName("but_r")
        self.verticalLayout_3.addWidget(self.but_r)
        self.but_y = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_y.setObjectName("but_y")
        self.verticalLayout_3.addWidget(self.but_y)
        self.but_ts = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_ts.setObjectName("but_ts")
        self.verticalLayout_3.addWidget(self.but_ts)
        self.but_ssh = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_ssh.setObjectName("but_ssh")
        self.verticalLayout_3.addWidget(self.but_ssh)
        self.but_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_3.setObjectName("but_3")
        self.verticalLayout_3.addWidget(self.but_3)
        self.but_ia = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.but_ia.setObjectName("but_ia")
        self.verticalLayout_3.addWidget(self.but_ia)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Виселица"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.but_new_game.setText(_translate("MainWindow", "новая игра"))
        self.but_history.setText(_translate("MainWindow", "история"))
        self.but_file.setText(_translate("MainWindow", "изменить слова"))
        self.but_a.setText(_translate("MainWindow", "а"))
        self.but_g.setText(_translate("MainWindow", "г"))
        self.but_io.setText(_translate("MainWindow", "ё"))
        self.but_i.setText(_translate("MainWindow", "и"))
        self.but_l.setText(_translate("MainWindow", "л"))
        self.but_o.setText(_translate("MainWindow", "о"))
        self.but_s.setText(_translate("MainWindow", "с"))
        self.but_f.setText(_translate("MainWindow", "ф"))
        self.but_ch.setText(_translate("MainWindow", "ч"))
        self.but_1.setText(_translate("MainWindow", "ъ"))
        self.but_ea.setText(_translate("MainWindow", "э"))
        self.but_b.setText(_translate("MainWindow", "б"))
        self.but_d.setText(_translate("MainWindow", "д"))
        self.but_zj.setText(_translate("MainWindow", "ж"))
        self.but_ie.setText(_translate("MainWindow", "й"))
        self.but_m.setText(_translate("MainWindow", "м"))
        self.but_p.setText(_translate("MainWindow", "п"))
        self.but_t.setText(_translate("MainWindow", "т"))
        self.but_h.setText(_translate("MainWindow", "х"))
        self.but_sh.setText(_translate("MainWindow", "ш"))
        self.but_2.setText(_translate("MainWindow", "ы"))
        self.but_u.setText(_translate("MainWindow", "ю"))
        self.but_v.setText(_translate("MainWindow", "в"))
        self.but_e.setText(_translate("MainWindow", "е"))
        self.but_z.setText(_translate("MainWindow", "з"))
        self.but_k.setText(_translate("MainWindow", "к"))
        self.but_n.setText(_translate("MainWindow", "н"))
        self.but_r.setText(_translate("MainWindow", "р"))
        self.but_y.setText(_translate("MainWindow", "у"))
        self.but_ts.setText(_translate("MainWindow", "ц"))
        self.but_ssh.setText(_translate("MainWindow", "щ"))
        self.but_3.setText(_translate("MainWindow", "ь"))
        self.but_ia.setText(_translate("MainWindow", "я"))


class Ui_history_window(object):
    def setupUi(self, history_window):
        history_window.setObjectName("history_window")
        history_window.resize(489, 362)
        self.centralwidget = QtWidgets.QWidget(history_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.history_text = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.history_text.setObjectName("history_text")
        self.verticalLayout.addWidget(self.history_text)
        history_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(history_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 21))
        self.menubar.setObjectName("menubar")
        history_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(history_window)
        self.statusbar.setObjectName("statusbar")
        history_window.setStatusBar(self.statusbar)

        self.retranslateUi(history_window)
        QtCore.QMetaObject.connectSlotsByName(history_window)

    def retranslateUi(self, history_window):
        _translate = QtCore.QCoreApplication.translate
        history_window.setWindowTitle(_translate("history_window", "История"))


class history_window(QMainWindow, Ui_history_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def displayInfo(self):
        self.show()


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.his = history_window()
        self.history_sp = []
        self.label.setPixmap(QPixmap(resource_path('vis_1.png')))
        self.file_name = 'mixed.txt'
        self.sqlite = sqlite3.connect(DB_NAME)
        self.number_game = 0
        self.alphabet = {
            self.but_a: 'а',
            self.but_b: 'б',
            self.but_v: 'в',
            self.but_g: 'г',
            self.but_d: 'д',
            self.but_e: 'е',
            self.but_io: 'ё',
            self.but_zj: 'ж',
            self.but_z: 'з',
            self.but_i: 'и',
            self.but_ie: 'й',
            self.but_k: 'к',
            self.but_l: 'л',
            self.but_m: 'м',
            self.but_n: 'н',
            self.but_o: 'о',
            self.but_p: 'п',
            self.but_r: 'р',
            self.but_s: 'с',
            self.but_t: 'т',
            self.but_y: 'у',
            self.but_f: 'ф',
            self.but_h: 'х',
            self.but_ts: 'ц',
            self.but_ch: 'ч',
            self.but_sh: 'ш',
            self.but_ssh: 'щ',
            self.but_1: 'ъ',
            self.but_2: 'ы',
            self.but_3: 'ь',
            self.but_ea: 'э',
            self.but_u: 'ю',
            self.but_ia: 'я'

        }  # словарь букв

        # картинки
        self.pictures = [resource_path('vis_1.png'), resource_path('vis_2.png'),
                         resource_path('vis_3.png'), resource_path('vis_4.png'),
                         resource_path('vis_5.png'), resource_path('vis_6.png'),
                         resource_path('vis_7.png')]

        # присоединяем кнопки
        self.but_new_game.clicked.connect(self.new_game)
        self.but_file.clicked.connect(self.new_file)
        self.but_history.clicked.connect(self.history)


    # создаём функцию, которая стирает все значения и делает новую игру
    def new_game(self):
        f = open(self.file_name, encoding='utf-8')
        self.word = choice([i.lower()[:-1] for i in f])  # получаем слово из файла
        len_word = '#' * len(self.word)  # инвентируем слово в знак #
        self.line_slovo.setText(len_word)  # выводим len_word
        self.label.setPixmap(QPixmap(resource_path('vis_1.png')))  # вставляем картинку в label
        self.line_razgovora.clear()  # очищаем строку 'разговора'
        self.number_game += 1  # увеличиваем номер игры на 1
        self.wrong = 0  # очищаем количество ошибок
        self.history_sp.append(f'Номер игры {self.number_game}')

        #присоединяем кнопки к функции
        self.but_a.clicked.connect(self.click_bykv)
        self.but_b.clicked.connect(self.click_bykv)
        self.but_v.clicked.connect(self.click_bykv)
        self.but_g.clicked.connect(self.click_bykv)
        self.but_d.clicked.connect(self.click_bykv)
        self.but_e.clicked.connect(self.click_bykv)
        self.but_io.clicked.connect(self.click_bykv)
        self.but_zj.clicked.connect(self.click_bykv)
        self.but_z.clicked.connect(self.click_bykv)
        self.but_i.clicked.connect(self.click_bykv)
        self.but_ie.clicked.connect(self.click_bykv)
        self.but_k.clicked.connect(self.click_bykv)
        self.but_l.clicked.connect(self.click_bykv)
        self.but_m.clicked.connect(self.click_bykv)
        self.but_n.clicked.connect(self.click_bykv)
        self.but_o.clicked.connect(self.click_bykv)
        self.but_p.clicked.connect(self.click_bykv)
        self.but_r.clicked.connect(self.click_bykv)
        self.but_s.clicked.connect(self.click_bykv)
        self.but_t.clicked.connect(self.click_bykv)
        self.but_y.clicked.connect(self.click_bykv)
        self.but_f.clicked.connect(self.click_bykv)
        self.but_h.clicked.connect(self.click_bykv)
        self.but_ts.clicked.connect(self.click_bykv)
        self.but_ch.clicked.connect(self.click_bykv)
        self.but_sh.clicked.connect(self.click_bykv)
        self.but_ssh.clicked.connect(self.click_bykv)
        self.but_1.clicked.connect(self.click_bykv)
        self.but_2.clicked.connect(self.click_bykv)
        self.but_3.clicked.connect(self.click_bykv)
        self.but_ea.clicked.connect(self.click_bykv)
        self.but_u.clicked.connect(self.click_bykv)
        self.but_ia.clicked.connect(self.click_bykv)

        # делаем все буквы видимыми
        self.but_a.show()
        self.but_b.show()
        self.but_v.show()
        self.but_g.show()
        self.but_d.show()
        self.but_e.show()
        self.but_io.show()
        self.but_zj.show()
        self.but_z.show()
        self.but_i.show()
        self.but_ie.show()
        self.but_k.show()
        self.but_l.show()
        self.but_m.show()
        self.but_n.show()
        self.but_o.show()
        self.but_p.show()
        self.but_r.show()
        self.but_s.show()
        self.but_t.show()
        self.but_y.show()
        self.but_f.show()
        self.but_h.show()
        self.but_ts.show()
        self.but_ch.show()
        self.but_sh.show()
        self.but_ssh.show()
        self.but_1.show()
        self.but_2.show()
        self.but_3.show()
        self.but_ea.show()
        self.but_u.show()
        self.but_ia.show()

        self.but_new_game.clicked.disconnect(self.new_game)


    # проверка можно-ли дальше продолжать игру
    def check(self):
        if self.wrong < 6:
            if self.line_slovo.text() == self.word:
                self.line_razgovora.setText(f'Молодец, загаданное слово было {self.word.upper()}')
                self.history_sp.append(f'Пользователь угадал слово {self.word.upper()}  ヽ(✿ﾟ▽ﾟ)ノ')
                self.history_sp.append('------------------------>')
                # добавляем данные о игре в бд
                cur = self.sqlite.cursor()
                res = f'INSERT INTO visilicha (word, wrong, status) VALUES ("{self.word}", {self.wrong}, "угадано")'
                cur.execute(res)
                self.sqlite.commit()
                cur.close()
                # отсоединяем кнопки от функции
                self.but_a.clicked.disconnect(self.click_bykv)
                self.but_b.clicked.disconnect(self.click_bykv)
                self.but_v.clicked.disconnect(self.click_bykv)
                self.but_g.clicked.disconnect(self.click_bykv)
                self.but_d.clicked.disconnect(self.click_bykv)
                self.but_e.clicked.disconnect(self.click_bykv)
                self.but_io.clicked.disconnect(self.click_bykv)
                self.but_zj.clicked.disconnect(self.click_bykv)
                self.but_z.clicked.disconnect(self.click_bykv)
                self.but_i.clicked.disconnect(self.click_bykv)
                self.but_ie.clicked.disconnect(self.click_bykv)
                self.but_k.clicked.disconnect(self.click_bykv)
                self.but_l.clicked.disconnect(self.click_bykv)
                self.but_m.clicked.disconnect(self.click_bykv)
                self.but_n.clicked.disconnect(self.click_bykv)
                self.but_o.clicked.disconnect(self.click_bykv)
                self.but_p.clicked.disconnect(self.click_bykv)
                self.but_r.clicked.disconnect(self.click_bykv)
                self.but_s.clicked.disconnect(self.click_bykv)
                self.but_t.clicked.disconnect(self.click_bykv)
                self.but_y.clicked.disconnect(self.click_bykv)
                self.but_f.clicked.disconnect(self.click_bykv)
                self.but_h.clicked.disconnect(self.click_bykv)
                self.but_ts.clicked.disconnect(self.click_bykv)
                self.but_ch.clicked.disconnect(self.click_bykv)
                self.but_sh.clicked.disconnect(self.click_bykv)
                self.but_ssh.clicked.disconnect(self.click_bykv)
                self.but_1.clicked.disconnect(self.click_bykv)
                self.but_2.clicked.disconnect(self.click_bykv)
                self.but_3.clicked.disconnect(self.click_bykv)
                self.but_ea.clicked.disconnect(self.click_bykv)
                self.but_u.clicked.disconnect(self.click_bykv)
                self.but_ia.clicked.disconnect(self.click_bykv)

                self.but_new_game.clicked.connect(self.new_game)


            self.label.setPixmap(QPixmap(self.pictures[self.wrong]))
        else:
            self.label.setPixmap(QPixmap(resource_path('vis_7.png')))
            self.line_razgovora.setText(f'Эх ты, Эллочка-Людоедочка, загаданное слово было {self.word.upper()}')
            self.history_sp.append(f'Пользователь не угадал загаданное слово {self.word.upper()}  (⊙ˍ⊙)')
            self.history_sp.append('------------------------>')
            # добавляем данные о игре в бд
            cur = self.sqlite.cursor()
            res = f'INSERT INTO visilicha (word, wrong, status) VALUES ("{self.word}", {self.wrong}, "неугадано")'
            cur.execute(res)
            self.sqlite.commit()
            cur.close()
            # отсоединяем кнопки от функции
            self.but_a.clicked.disconnect(self.click_bykv)
            self.but_b.clicked.disconnect(self.click_bykv)
            self.but_v.clicked.disconnect(self.click_bykv)
            self.but_g.clicked.disconnect(self.click_bykv)
            self.but_d.clicked.disconnect(self.click_bykv)
            self.but_e.clicked.disconnect(self.click_bykv)
            self.but_io.clicked.disconnect(self.click_bykv)
            self.but_zj.clicked.disconnect(self.click_bykv)
            self.but_z.clicked.disconnect(self.click_bykv)
            self.but_i.clicked.disconnect(self.click_bykv)
            self.but_ie.clicked.disconnect(self.click_bykv)
            self.but_k.clicked.disconnect(self.click_bykv)
            self.but_l.clicked.disconnect(self.click_bykv)
            self.but_m.clicked.disconnect(self.click_bykv)
            self.but_n.clicked.disconnect(self.click_bykv)
            self.but_o.clicked.disconnect(self.click_bykv)
            self.but_p.clicked.disconnect(self.click_bykv)
            self.but_r.clicked.disconnect(self.click_bykv)
            self.but_s.clicked.disconnect(self.click_bykv)
            self.but_t.clicked.disconnect(self.click_bykv)
            self.but_y.clicked.disconnect(self.click_bykv)
            self.but_f.clicked.disconnect(self.click_bykv)
            self.but_h.clicked.disconnect(self.click_bykv)
            self.but_ts.clicked.disconnect(self.click_bykv)
            self.but_ch.clicked.disconnect(self.click_bykv)
            self.but_sh.clicked.disconnect(self.click_bykv)
            self.but_ssh.clicked.disconnect(self.click_bykv)
            self.but_1.clicked.disconnect(self.click_bykv)
            self.but_2.clicked.disconnect(self.click_bykv)
            self.but_3.clicked.disconnect(self.click_bykv)
            self.but_ea.clicked.disconnect(self.click_bykv)
            self.but_u.clicked.disconnect(self.click_bykv)
            self.but_ia.clicked.disconnect(self.click_bykv)

            self.but_new_game.clicked.connect(self.new_game)



    # функция выбора файла со словами
    def new_file(self):
        self.file_name = QFileDialog.getOpenFileName(self, 'Выберите файл со словами', '', '(*.txt)')[0]
        if self.file_name == '':
            self.file_name = 'mixed.txt'
        self.history_sp.append('Пользователь поменял файл')
        self.history_sp.append('------------------------>')


    # создаем функции для нажатий на кпопки букв
    def click_bykv(self):
        if self.line_slovo.text() != self.word:
            bykva = self.alphabet[self.sender()]  # получаем букву
            self.history_sp.append(f'Пользователь использовал букву {bykva.upper()}')
            if bykva in self.word:  # проверяем есть ли буква в слове
                self.line_razgovora.setText(f'Да, в слове есть буква {bykva.upper()}')
                new = ''  # создаём новую строку с уже известными буквами
                slovo = self.line_slovo.text()
                for i in range(len(self.word)):  # вставляем букву(ы) на своё место
                    if bykva == self.word[i]:
                        new += bykva
                    else:
                        new += slovo[i]
                self.line_slovo.setText(new)  # выводим новую строку
                self.check()
            else:
                self.line_razgovora.setText(f'К сожалению буквы {bykva.upper()} нет в слове')
                self.wrong += 1
                self.check()
        self.sender().hide()


    # записываем данные об игре в историю
    def history(self):
        stroka = ''
        for i in self.history_sp:
            stroka = stroka + i + '\n'
        self.his.history_text.setText(stroka)
        self.his.displayInfo()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
