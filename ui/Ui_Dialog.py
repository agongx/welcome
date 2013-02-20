# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Dropbox\python\project\Welcome2\ui\welcome.ui'
#
# Created: Sun Feb 17 13:26:43 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 302)
        Dialog.setSizeGripEnabled(True)
        self.labelEnterName = QtGui.QLabel(Dialog)
        self.labelEnterName.setGeometry(QtCore.QRect(50, 30, 101, 20))
        self.labelEnterName.setObjectName(_fromUtf8("labelEnterName"))
        self.lineUserNam = QtGui.QLineEdit(Dialog)
        self.lineUserNam.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.lineUserNam.setObjectName(_fromUtf8("lineUserNam"))
        self.ButtonClear = QtGui.QPushButton(Dialog)
        self.ButtonClear.setGeometry(QtCore.QRect(200, 130, 75, 23))
        self.ButtonClear.setObjectName(_fromUtf8("ButtonClear"))
        self.labelMessage = QtGui.QLabel(Dialog)
        self.labelMessage.setGeometry(QtCore.QRect(180, 80, 54, 12))
        self.labelMessage.setText(_fromUtf8(""))
        self.labelMessage.setObjectName(_fromUtf8("labelMessage"))
        self.buttonHello = QtGui.QPushButton(Dialog)
        self.buttonHello.setGeometry(QtCore.QRect(290, 130, 75, 23))
        self.buttonHello.setObjectName(_fromUtf8("buttonHello"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.ButtonClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineUserNam.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelEnterName.setText(_translate("Dialog", "Enter your name", None))
        self.ButtonClear.setText(_translate("Dialog", "clear", None))
        self.buttonHello.setText(_translate("Dialog", "hello", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

