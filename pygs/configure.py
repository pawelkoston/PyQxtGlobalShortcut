#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
from distutils.dep_util import newer_group

import sipconfig


here = os.path.abspath(os.path.dirname(__file__))

build_file = "pygs.sbf"


# exit if up-to-date
sources = []
for root, dirs, files in os.walk(here):
    sources += [os.path.join(root, file) for file in files]
if not newer_group(sources, build_file):
    print("pygs is up-to-date, skip configure")
    sys.exit(0)


try:
    from PyQt4.pyqtconfig import Configuration
except ImportError:
    # This global variable will be resolved by sipconfig in a strange way
    _default_macros = sipconfig._default_macros.copy()

    class Configuration(sipconfig.Configuration):
        def __init__(self):
            try:
                import PyQt5 as PyQt
                from PyQt5 import QtCore
            except ImportError:
                import PyQt4 as PyQt
                from PyQt4 import QtCore

            qmake_props = subprocess.check_output(["qmake", "-query"], universal_newlines=True)
            qmake_props = dict(x.split(":", 1) for x in qmake_props.splitlines())

            qt_version = list(map(int, qmake_props['QT_VERSION'].split('.')))
            qt_version = qt_version[0] * 0x10000 + qt_version[1] * 0x100 + qt_version[2]

            cfg = {}
            cfg['pyqt_bin_dir'] = os.path.dirname(PyQt.__file__)
            cfg['pyqt_config_args'] = "--confirm-license -b" + cfg['pyqt_bin_dir']
            cfg['pyqt_mod_dir'] = cfg['pyqt_bin_dir']
            cfg['pyqt_modules'] = "QtCore QtGui"  # FIXME
            cfg['pyqt_sip_dir'] = os.path.join(cfg['pyqt_mod_dir'], "sip", PyQt.__name__)
            cfg['pyqt_sip_flags'] = QtCore.PYQT_CONFIGURATION['sip_flags']
            cfg['pyqt_version'] = QtCore.PYQT_VERSION
            cfg['pyqt_version_str'] = QtCore.PYQT_VERSION_STR
            cfg['qt_data_dir'] = qmake_props['QT_INSTALL_DATA']
            cfg['qt_dir'] = qmake_props['QT_INSTALL_PREFIX']
            cfg['qt_edition'] = "free"
            cfg['qt_framework'] = 0  # FIXME
            cfg['qt_inc_dir'] = qmake_props['QT_INSTALL_HEADERS']
            cfg['qt_lib_dir'] = qmake_props['QT_INSTALL_LIBS']
            cfg['qt_threaded'] = 1  # FIXME
            cfg['qt_version'] = qt_version
            cfg['qt_winconfig'] = 'shared'  # FIXME

            _default_macros['INCDIR_QT'] = cfg['qt_inc_dir']
            _default_macros['LIBDIR_QT'] = cfg['qt_lib_dir']
            _default_macros['MOC'] = os.path.join(qmake_props['QT_INSTALL_BINS'], "moc")

            sipconfig.Configuration.__init__(self, [cfg])

config = Configuration()

sip_path = os.path.join(here, "sip/pygsmod.sip")

# Run SIP to generate the code.
command = [
    config.sip_bin,
    "-c", ".",
    "-b", build_file,
    "-I", config.pyqt_sip_dir,
    "-e"
] + config.pyqt_sip_flags.split() + [sip_path]
subprocess.check_call(command)

# Create the Makefile.
makefile = sipconfig.SIPModuleMakefile(config, build_file, qt=["QtCore", "QtGui"])
makefile.extra_include_dirs.append(os.path.join(here, "../libqxt/src/core"))
makefile.extra_include_dirs.append(os.path.join(here, "../libqxt/src/widgets"))
makefile.extra_libs.append("QxtGlobalShortcut")
makefile.generate()
