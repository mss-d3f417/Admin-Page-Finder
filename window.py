# Coded By MR.D3F417
# https://zil.ink/mrd3f417
# https://github.com/mrd3f417
# https://soundcloud.com/mr-d3f417

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from main import Ui_Form
import sys
from worker import FindPageWeb

class main(QWidget , Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setFixedSize(429,385)
        self.pushButton_2.clicked.connect(self.clear)
        self.pagefind = FindPageWeb()
        self.pushButton.clicked.connect(self.start)
        self.pagefind.output.connect(self.printOutPut)

    def start(self):
        web = self.lineEdit.text()
        self.pagefind.run_command(web)

    def printOutPut(self,string):
        self.textBrowser.insertPlainText(string.strip() + "\n")

    def clear(self):
        self.lineEdit.clear()


app = QApplication(sys.argv)
w = main()
w.show()
sys.exit(app.exec_())