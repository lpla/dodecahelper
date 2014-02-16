import sys
from PyQt4 import QtCore, QtGui
from RuleTranslatorInterface import Ui_MainWindow

class StartQT(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.exportResults)
        
    def convertSerieToNumbers(self):
        serie = ''
        comboBoxList = [self.ui.comboBox_1, self.ui.comboBox_2, self.ui.comboBox_3, self.ui.comboBox_4, self.ui.comboBox_5, self.ui.comboBox_6, self.ui.comboBox_7, self.ui.comboBox_8, self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11, self.ui.comboBox_12]
        
        for comboBox in comboBoxList:
            
            if comboBox.currentText() == "C":
                serie += ',1'
            elif comboBox.currentText() == "C#/Db":
                serie += ',2'
            elif comboBox.currentText() == "D":
                serie += ',3'
            elif comboBox.currentText() == "D#/Eb":
                serie += ',4'
            elif comboBox.currentText() == "E":
                serie += ',5'
            elif comboBox.currentText() == "F":
                serie += ',6'
            elif comboBox.currentText() == "F#/Gb":
                serie += ',7'
            elif comboBox.currentText() == "G":
                serie += ',8'
            elif comboBox.currentText() == "G#/Ab":
                serie += ',9'
            elif comboBox.currentText() == "A":
                serie += ',10'
            elif comboBox.currentText() == "A#/Bb":
                serie += ',11'
            elif comboBox.currentText() == "B":
                serie += ',12'
            elif comboBox.currentText() == "":
                serie += ',0'
            
            
        s = list(serie)
        s[0] = '{'
        
        serie = "".join(s)
        serie += '}'
        return serie
    
    def exportResults(self):
        f = open('parameters','w')
        f.write('['+str(self.ui.min_interval.value()) + '-' + str(self.ui.max_interval.value()) + '];');
        
        serie = self.convertSerieToNumbers()
        
        f.write(serie)
        f.close();
		        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT()
    myapp.show()
    sys.exit(app.exec_())
