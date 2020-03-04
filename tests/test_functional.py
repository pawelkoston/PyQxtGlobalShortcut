# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys


try:
    if os.environ['QT_SELECT'] == '4':
        from PyQt4.QtCore import QTimer
        from PyQt4.QtGui import QApplication, QKeySequence
    else:
        from PyQt5.QtCore import QTimer
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtGui import QKeySequence
except ImportError:
    print("Test skipped because of corresponding PyQt not found.", file=sys.stderr)
else:
    if os.environ['QT_SELECT'] == '4':
        from pyqxtgs.QxtGlobalShortcut import QxtGlobalShortcut
    else:
        from pyqxtgs.QxtGlobalShortcut import QxtGlobalShortcut

    def test_functional():
        app = QApplication(sys.argv)
        shortcut = QxtGlobalShortcut()
        shortcut.setShortcut(QKeySequence('Ctrl+Alt+E'))
        shortcut.activated.connect(app.exit)
        QTimer.singleShot(100, shortcut.activated.emit)
        app.exec_()
