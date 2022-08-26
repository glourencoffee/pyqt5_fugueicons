import unittest
import pyqt5_fugueicons as fugue
from PyQt5 import QtCore, QtGui, QtWidgets

class TestIcon(unittest.TestCase):
    def setUp(self) -> None:
        self.app = QtWidgets.QApplication([])
    
    def testReturns16x16(self):
        icon = fugue.icon('application-blue')
        size = self.assertHasAvailableSize(icon)
        
        self.assertEqual(size, QtCore.QSize(16, 16))
    
    def testReturns24x24(self):
        icon = fugue.icon('application-blue', size=24)
        size = self.assertHasAvailableSize(icon)
        
        self.assertEqual(size, QtCore.QSize(24, 24))
    
    def testReturns32x32(self):
        icon = fugue.icon('application-blue', size=32)
        size = self.assertHasAvailableSize(icon)
        
        self.assertEqual(size, QtCore.QSize(32, 32))

    def testReturnsShadowless16x16(self):
        icon = fugue.icon('application-blue', shadowless=True)
        size = self.assertHasAvailableSize(icon)
        
        self.assertEqual(size, QtCore.QSize(16, 16))
    
    def testReturnsShadowless24x24(self):
        icon = fugue.icon('application-blue', shadowless=True, size=24)
        size = self.assertHasAvailableSize(icon)
        
        self.assertEqual(size, QtCore.QSize(24, 24))
    
    def testReturnsShadowless32x32(self):
        icon = fugue.icon('application-blue', shadowless=True, size=32)
        size = self.assertHasAvailableSize(icon)
        
        self.assertEqual(size, QtCore.QSize(32, 32))

    def testReturnsEmptyOnInvalidName(self):
        icon = fugue.icon('application-red-pilled-lmao')
        
        self.assertTrue(icon.isNull())
    
    def testReturnsEmptyOnInvalidSize(self):
        app_blue_icon = fugue.icon('application-blue', size=64)
        abacus_icon   = fugue.icon('abacus',           size=24)
        
        self.assertTrue(app_blue_icon.isNull())
        self.assertTrue(abacus_icon.isNull())

    def testReturnsFallbackSizeOnInvalidSize(self):
        icon = fugue.icon('abacus', size=24, fallback_size=True)
        size = self.assertHasAvailableSize(icon)
        
        self.assertEqual(size, QtCore.QSize(16, 16))

    def assertHasAvailableSize(self, icon: QtGui.QIcon) -> QtCore.QSize:
        available_sizes = icon.availableSizes()

        self.assertEqual(len(available_sizes), 1)
        
        return available_sizes[0]