from PyQt5.QtWidgets import *

app = QApplication([])

label = QLabel('Hello World')
label.show()

button = QPushButton()
button.show()

app.exec()