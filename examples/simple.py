# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

try:
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QKeySequence
except ImportError:
    from PyQt4.QtGui import QApplication, QKeySequence
from pygs import QxtGlobalShortcut


SHORTCUT_SHOW = "Ctrl+Alt+S"  # Ctrl maps to Command on Mac OS X
SHORTCUT_EXIT = "Ctrl+Alt+F"  # again, Ctrl maps to Command on Mac OS X


def show_activated():
    print("Shortcut Activated!")

app = QApplication([])

shortcut_show = QxtGlobalShortcut()
shortcut_show.setShortcut(QKeySequence(SHORTCUT_SHOW))
shortcut_show.activated.connect(show_activated)

shortcut_exit = QxtGlobalShortcut()
shortcut_exit.setShortcut(QKeySequence(SHORTCUT_EXIT))
shortcut_exit.activated.connect(app.exit)

return_code = app.exec_()

del shortcut_show
del shortcut_exit
sys.exit(return_code)
