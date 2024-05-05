from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QComboBox, QLineEdit, QHBoxLayout, QVBoxLayout
)

import requests

def get_rate(target_curency):
    url = 'https://www.cbr-xml-daily.ru/latest.js'
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_curency]

def convert_currency():
    target_curency = need_cur_l.currentText()
    amount = float(select_v.text())
    exchange_rate = get_rate(target_curency)
    result = amount * exchange_rate
    result_l.setText(f"{result:.10f} {target_curency}")

app = QApplication([])
winn = QWidget()
winn.setWindowTitle('Конвертер валют')
winn.setFixedSize(800, 600)


result_l = QLabel('0.000 RUB')
result_l.setAlignment(Qt.AlignCenter)
result_l.setStyleSheet('font-size: 20px;')

convert_but = QPushButton('Конвертировать')

select_v = QLineEdit()
select_v.setFixedWidth(150)


select_cur_l = QComboBox()
select_cur_l.addItem('RUB')
select_cur_l.setStyleSheet('font-size: 16px;')


need_cur_l = QComboBox()
need_cur_l.addItems(['USD', 'EUR', 'KZT', 'BRL'])
need_cur_l.setStyleSheet('font-size: 16px;')


main_l = QVBoxLayout()
r1 = QHBoxLayout()
r1.addWidget(select_cur_l)
r1.addWidget(need_cur_l)


main_l.addWidget(result_l)
main_l.addLayout(r1)
main_l.addWidget(select_v, alignment=Qt.AlignCenter)
main_l.addWidget(convert_but, alignment=Qt.AlignCenter)

winn.setLayout(main_l)

convert_but.clicked.connect(convert_currency)

winn.show()
app.exec_()