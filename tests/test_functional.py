# -*- coding: utf-8 -*-

import os
import sys


try:
    if os.environ['QT_SELECT'] == '4':
        from PyQt4.QtCore import QTimer
        from PyQt4.QtGui import QApplication, QKeySequence, QWidget
        from PyQt4.QtTest import QTest
    else:
        from PyQt5.QtCore import QTimer
        from PyQt5.QtWidgets import QApplication, QWidget
        from PyQt5.QtGui import QKeySequence
        from PyQt5.QtTest import QTest
except ImportError:
    print("Test skipped because of corresponding PyQt not found.", file=sys.stderr)
else:
    from pygs import QxtGlobalShortcut

    def test_functional():
        app = QApplication(sys.argv)
        shortcut = QxtGlobalShortcut()
        shortcut.setShortcut(QKeySequence('Ctrl+Alt+E'))
        shortcut.activated.connect(app.exit)
        QTimer.singleShot(100, shortcut.activated.emit)
        app.exec_()
