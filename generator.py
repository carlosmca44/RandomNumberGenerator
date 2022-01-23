#se importa el modulo creado a partir del archivo '.ui' generado por qtdesigner
from generator_ui import *

import random

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.generateResultButton.clicked.connect(self.generateNumber)

    def generateNumber(self): 
        if (self.spinBox.value() != 0): 
            self.labelResultado.setText(random.randint(0, self.spinBox.value()).__str__())
        else: self.labelResultado.setText("Seleciona una valor diferente")
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_() 
