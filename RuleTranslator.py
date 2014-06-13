import sys
from PyQt4 import QtCore, QtGui
from RuleTranslatorInterface import Ui_MainWindow

class StartQT(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.exportResults) #Conectamos el botón de exportar los parámetros con la función de exportar

    #Convierte los valores en letras de las notas en números (C = 1, C#/Db = 2...)
    def convertSerieToNumbers(self):
        serie = ''
        comboBoxList = [self.ui.comboBox_1, self.ui.comboBox_2, self.ui.comboBox_3, self.ui.comboBox_4, self.ui.comboBox_5, self.ui.comboBox_6, self.ui.comboBox_7, self.ui.comboBox_8, self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11, self.ui.comboBox_12]
        
        for comboBox in comboBoxList:
            
            if comboBox.currentText() == "C":
                serie += ' 1'
            elif comboBox.currentText() == "C#/Db":
                serie += ' 2'
            elif comboBox.currentText() == "D":
                serie += ' 3'
            elif comboBox.currentText() == "D#/Eb":
                serie += ' 4'
            elif comboBox.currentText() == "E":
                serie += ' 5'
            elif comboBox.currentText() == "F":
                serie += ' 6'
            elif comboBox.currentText() == "F#/Gb":
                serie += ' 7'
            elif comboBox.currentText() == "G":
                serie += ' 8'
            elif comboBox.currentText() == "G#/Ab":
                serie += ' 9'
            elif comboBox.currentText() == "A":
                serie += ' 10'
            elif comboBox.currentText() == "A#/Bb":
                serie += ' 11'
            elif comboBox.currentText() == "B":
                serie += ' 12'
            elif comboBox.currentText() == "":
                serie += ' 0'
            
            
        s = list(serie)
        
        serie = "".join(s)
        return serie
    
	
	#Exportamos el los valores de la interfaz en forma de lista a los ficheros para las series y para las partituras
    def exportResults(self):
        f = open('TFG OM workspace\in-files\parameters.txt','w')
        f.write('(' + str(self.ui.min_interval.value()) + ' ' + str(self.ui.max_interval.value()));
        
        serie = self.convertSerieToNumbers()
        
        f.write(serie + ')')
        f.close();
        
        f2 = open('TFG OM workspace\in-files\scoreParameters.txt','w')
        f2.write('(' + str(self.ui.seriesPerVoice.value()) + ' ' + str(self.ui.percentajeNotes.value()) + ' ' + str(self.ui.thresholdOctaves.value()) + ' ' + str(self.ui.minOctave.value()) + ' ' + str(self.ui.maxOctave.value()) + ' ' + str(self.ui.measure1.currentText()) + ' ' + str(self.ui.measure2.currentText()) + ' ' + str(self.ui.reRatios.value()) + ' ' + str(self.ui.reRatios2.value()) + ' ' + str(self.ui.maxDivision.value()) + ' ' + str(self.ui.maxFigure.value()) + ' ' + str(self.ui.minFigure.value()) + ' ' + str(self.ui.voices.value()) + ' ' + str(self.ui.transpose.value()) + ')');
        f2.close();
        
		
        self.ui.statusbar.showMessage("Parameters successfully exported", msecs=5000)

#Inicializamos la interfaz y la mostramos
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT()
    myapp.show()
    sys.exit(app.exec_())
