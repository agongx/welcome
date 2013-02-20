import sys
from PyQt4.QtGui import QApplication 
from ui.Dialog import * 

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myapp = Dialog()
	myapp.show()
	sys.exit(app.exec_())
