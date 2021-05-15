import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv);

Janela = QWidget()
#definições do tamanho da janela

Janela.setWindowTitle("Enne Downloder")
Janela.setFixedWidth(1000)
Janela.setFixedHeight(600)
Janela.setStyleSheet("background: #161219")

#definição de layort
Grid = QGridLayout()

logo_image = QPixmap("logo.png")
logo_set = QLabel()
logo_set.setPixmap(logo_image)
logo_set.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

entry = QLineEdit()

entry.setMinimumWidth(600)
entry.setMinimumHeight(30)
entry.setStyleSheet(
    "border: 2px solid '#11A720';" +
    "border-radius: 100px;" +
    "font-size: 20px;" +
    "background-color: #FFFFFF;" +
    "padding: 5px;"
    "margin: 10px;"
    "color: '#000000';"
    )
entry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

btn_download = QPushButton("Converter e baixar")
btn_download.setStyleSheet(
    "*{background-color: #11A720;" +
    "font-size: 20px;" +
    "border-radius: 15px;" +
    "color: 'white';"
    "padding: 5px;"
    "margin: 5px 300px;}" +
    "*:hover{background: '#076911'; }"
    )


Grid.addWidget(logo_set, 0, 0)
Grid.addWidget(entry, 1, 0)
Grid.addWidget(btn_download, 2,0)

Janela.setLayout(Grid)
Janela.show()
sys.exit(app.exec())
