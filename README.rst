====
pygs
====

.. image:: http://dl.dropbox.com/u/750959/pygs_strike.png


Overview
--------

pygs provides cross-platform global hotkey / shortcuts for python using PyQt.

pygs is a wrapper for `libqxt <http://www.libqxt.org/>`_'s `QxtGlobalShortcut <http://doc.libqxt.org/tip/qxtglobalshortcut.html>`_.

My aim is to provide cross-platform support for global hotkeys (shortcuts) in python. Ideally I would like to remove the PyQt and libqxt dependency but that remains a (distant) future goal. I believe it is definitely possible and potentially quite useful though.

This fork support PyQt4 / PyQt5 on Python 2.x / 3.x.


Installation
------------

**Requirements** (sufficient not necessary)

* Python
* Qt
* SIP
* PyQt

To Install

``setup.py install``


Usage
-----

**See examples/simple.py**

``python simple.py``

| ``Ctrl+Alt+S`` - activate shortcut
| ``Ctrl+Alt+F`` - quit application

NOTE: Ctrl maps to COMMAND on macs!!!! Yeah this is crazy confusing. But it's Qt not me :)


Acknowledgements
----------------

pygs uses

* `Digia <http://www.digia.com/>`_'s `Qt <http://qt-project.org/>`_

* `Riverbank Computing Limited <http://www.riverbankcomputing.co.uk>`_'s `SIP <http://www.riverbankcomputing.co.uk/software/sip/intro>`_

* `Riverbank Computing Limited <http://www.riverbankcomputing.co.uk>`_'s `PyQt <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_

* `libqxt <http://www.libqxt.org/>`_

Thanks!


License
-------

pygs  - Python bindings to libqxt's QxtGlobalShortcut using SIP and PyQt. In other words, global hotkeys for PyQt.

| Copyright (C) 2010  J. Matt Peterson
| Copyright (C) 2014  Asvel

You may use pygs under the terms of the General Public License (GPL) Version 3 or you may contact the author for permission or a commercial license. The commercial license option is specifically provided for those who are unable or unwilling to use the GPL.

http://www.gnu.org/licenses/gpl-3.0.txt
