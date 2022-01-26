from PyQt6 import QtGui, QtWidgets, QtDesigner
import time

class MainUiClass(QtGui.QMainWindow, QtDesigner.Ui_MainWindow):
     def __init__(self, parent=None):
          super(MainUiClass, self).__init__(parent)
          
          self.setupUi(self)
          self.btn.pressed.connect(self.openWindow)

     def openWindow(self):
          window = Window()
          QtWidgets.QWidget.createWindowContainer(window, self)
          time.sleep(0.1)
          window.show()

class Window(QtGui.QWindow):
     def __init__(self,parent=None):
          super(Window,self).__init__(parent)

if __name__=='__main__':
      app=QtWidgets.QApplication(sys.argv)
      GUI=MainUiClass()
      GUI.show()
      app.exec_()