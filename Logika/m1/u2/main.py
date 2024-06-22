from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QMessageBox, QRadioButton

app = QApplication([])
main_wind = QWidget()
main_wind.setWindowTitle("Конкурс від Crazy People")
main_wind.resize(400,200)

question  = QLabel("Коли помер Тарас Шевченко")

btn1 = QRadioButton("1862")
btn2 = QRadioButton("1861")
btn3 = QRadioButton("2024")
btn4 = QRadioButton("1860")

main_layout = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

def win():
    victory_win = QMessageBox()
    victory_win.setText("Ти виграв 3 бесплатні квитки на концерт Артьома Півавора.ВІТАЮ!")
    victory_win.exec_()

def losee():
    losee = QMessageBox()
    losee.setText("ТИ програв твій приз фірмовий плакат")
    losee.exec_()

layoutH1.addWidget(question, alignment= Qt.AlignCenter)
layoutH2.addWidget(btn1, alignment= Qt.AlignCenter)
layoutH2.addWidget(btn2, alignment= Qt.AlignCenter)
layoutH3.addWidget(btn3, alignment= Qt.AlignCenter)
layoutH3.addWidget(btn4, alignment= Qt.AlignCenter)

main_layout.addLayout(layoutH1)
main_layout.addLayout(layoutH2)
main_layout.addLayout(layoutH3)

btn1.clicked.connect(losee)
btn2.clicked.connect(win)
btn3.clicked.connect(losee)
btn4.clicked.connect(losee)

main_wind.setLayout(main_layout)
main_wind.show()
app.exec_()