# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

if len(sys.argv) > 1 and sys.argv[1] == '4' or os.environ.get('QT_SELECT') == '4':
    from PyQt4.QtGui import QApplication, QKeySequence
    from PyQt4.QxtGlobalShortcut import QxtGlobalShortcut
else:
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QKeySequence
    from PyQt5.QxtGlobalShortcut import QxtGlobalShortcut


SHORTCUT_SHOW = "Ctrl+Alt+G"  # Ctrl maps to Command on Mac OS X
SHORTCUT_EXIT = "Ctrl+Alt+Q"  # again, Ctrl maps to Command on Mac OS X

app = QApplication([])

shortcut_show = QxtGlobalShortcut()
shortcut_show.setShortcut(QKeySequence(SHORTCUT_SHOW))
shortcut_show.activated.connect(lambda: print("Shortcut Activated!"))

shortcut_exit = QxtGlobalShortcut()
shortcut_exit.setShortcut(QKeySequence(SHORTCUT_EXIT))
shortcut_exit.activated.connect(app.exit)

print('Global show shortcut: {}'.format(SHORTCUT_SHOW))
print('Global exit shortcut: {}'.format(SHORTCUT_EXIT))

return_code = app.exec_()

del shortcut_show
del shortcut_exit
sys.exit(return_code)
