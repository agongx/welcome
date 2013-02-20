# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from .Ui_Dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_buttonHello_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.labelMessage.setText("Hello " + self.lineUserNam.text())
