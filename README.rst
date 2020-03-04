===================
PyQxtGlobalShortcut
===================

.. image:: http://img.shields.io/pypi/v/PyGlobalShortcut.png
   :target: https://pypi.python.org/pypi/PyGlobalShortcut
   :alt: Latest PyPI version

.. image:: http://img.shields.io/pypi/dm/PyGlobalShortcut.png
   :target: https://pypi.python.org/pypi/PyGlobalShortcut/
   :alt: Number of PyPI downloads

.. image:: https://travis-ci.org/frispete/PyQxtGlobalShortcut.svg?branch=master
   :target: https://travis-ci.org/frispete/PyQxtGlobalShortcut
   :alt: Travis-CI build status

|

.. image:: http://libqxt.bitbucket.org/doc/logo.png


Overview
--------

PyQxtGlobalShortcut provides cross-platform global hotkey / shortcuts for python using PyQt5.

PyQxtGlobalShortcut is a wrapper for `libqxt <http://www.libqxt.org/>`_'s `QxtGlobalShortcut <http://doc.libqxt.org/tip/qxtglobalshortcut.html>`_.

My aim is to provide cross-platform support for global hotkeys (shortcuts) in python. Ideally I would like to remove the PyQt and libqxt dependency but that remains a (distant) future goal. I believe it is definitely possible and potentially quite useful though.

This fork support  PyQt5 on Python  >3.6 within a proper namespace.


Installation
------------

Requirements
~~~~~~~~~~~~

Minimal for working:

* `PyQt5 <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_

For building from source:

* `Qt <http://qt-project.org/>`_
* `SIP <http://www.riverbankcomputing.co.uk/software/sip/intro>`_

*None of them could be installed automatic, please download and install them manually.*

*If you install them from a package manager, please also install development packages (if exist).*

Install from Source Code
~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ pip install PyQxtGlobalShortcut

or

::

    $ pip install . 



Usage
-----

**See examples/simple.py**

::

    $ python simple.py

| ``Ctrl+Alt+G`` - activate shortcut
| ``Ctrl+Alt+Q`` - quit application

NOTE: Ctrl maps to COMMAND on macs!!!! Yeah this is crazy confusing. But it's Qt not me :)


Testing
-------

There is a minimal test suite that check the compilation process for various
environments and ensure QxtGlobalShortcut can be properly imported and used.

To run the tests, you must first install tox::

    $ pip install tox


Then you can run the tests by running the following command::

    $ tox

To run the tests against a specific environment, use the -e option. E.g. to run
tests with Python 2.7 and PyQt4, you would run::

    $ tox -e py27-pyqt4

Here is the list of available test environments:

- py32-pyqt5
- py33-pyqt5
- py34-pyqt5
- py35-pyqt5
- py36-pyqt5


Acknowledgements
----------------

PyQxtGlobalShortcut uses

* `Digia <http://www.digia.com/>`_'s `Qt <http://qt-project.org/>`_

* `Riverbank Computing Limited <http://www.riverbankcomputing.co.uk>`_'s `SIP <http://www.riverbankcomputing.co.uk/software/sip/intro>`_

* `Riverbank Computing Limited <http://www.riverbankcomputing.co.uk>`_'s `PyQt <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_

* `libqxt <http://www.libqxt.org/>`_

Thanks!


License
-------

PyQxtGlobalShortcut - Python bindings to libqxt's QxtGlobalShortcut using SIP and PyQt. In other words, global hotkeys for PyQt.

| Copyright (C) 2010  J. Matt Peterson
| Copyright (C) 2014  Asvel
| Copyright (C) 2016 Hans-Peter Jansen

You may use PyQxtGlobalShortcut under the terms of the General Public License (GPL) Version 3 or you may contact the author for permission or a commercial license. The commercial license option is specifically provided for those who are unable or unwilling to use the GPL.

http://www.gnu.org/licenses/gpl-3.0.txt
