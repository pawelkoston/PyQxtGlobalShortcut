#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
from importlib import import_module
from distutils.dep_util import newer_group

import sipconfig


here = os.path.abspath(os.path.dirname(__file__))

# determine Qt version to build for
qt_api = os.environ.get('QT_SELECT', '5')

pyqxtgs = "pyqxtgs{}".format(qt_api)

build_file = "{}.sbf".format(pyqxtgs)


# exit if up-to-date
sources = []
for root, dirs, files in os.walk(here):
    sources += [os.path.join(root, file) for file in files]
if not newer_group(sources, build_file):
    print("{} is up-to-date, skip configure".format(pyqxtgs))
    sys.exit(0)


try:
    if qt_api != '4':
        raise ImportError()
    from PyQt4.pyqtconfig import Configuration
except ImportError:
    # This global variable will be resolved by sipconfig in a strange way
    _default_macros = sipconfig._default_macros.copy()

    class Configuration(sipconfig.Configuration):
        def __init__(self):
            if qt_api == '4':
                import PyQt4 as PyQt
            elif qt_api == '5':
                import PyQt5 as PyQt
            else:
                try:
                    import PyQt5 as PyQt
                except ImportError:
                    import PyQt4 as PyQt
            print("building for {}".format(PyQt.__name__))
            QtCore = import_module('.'.join([PyQt.__name__, 'QtCore']))

            qmake_props = subprocess.check_output(["qmake", "-query"], universal_newlines=True)
            qmake_props = dict(x.split(":", 1) for x in qmake_props.splitlines())

            qt_version = list(map(int, qmake_props['QT_VERSION'].split('.')))
            if qt_version[0] != QtCore.PYQT_VERSION >> 16:
                raise RuntimeError("The main version of Qt and PyQt is different, "
                                   "try setting environment variable 'QT_SELECT'")
            qt_version = qt_version[0] * 0x10000 + qt_version[1] * 0x100 + qt_version[2]

            pkg_config = sipconfig._pkg_config

            cfg = {}
            cfg['pyqt_sip_dir'] = os.path.join(PyQt.__file__, "../sip", PyQt.__name__)
            if not os.path.exists(cfg['pyqt_sip_dir']):
                cfg['pyqt_sip_dir'] = os.path.join(pkg_config['default_sip_dir'], PyQt.__name__)
            cfg['pyqt_sip_flags'] = QtCore.PYQT_CONFIGURATION['sip_flags']
            cfg['qt_data_dir'] = qmake_props['QT_INSTALL_DATA']
            cfg['qt_dir'] = qmake_props['QT_INSTALL_PREFIX']
            cfg['qt_edition'] = "free"
            cfg['qt_framework'] = pkg_config['qt_framework']
            cfg['qt_inc_dir'] = qmake_props['QT_INSTALL_HEADERS']
            cfg['qt_lib_dir'] = qmake_props['QT_INSTALL_LIBS']
            cfg['qt_threaded'] = 1  # FIXME
            cfg['qt_version'] = qt_version
            cfg['qt_winconfig'] = 'shared'  # FIXME

            _default_macros['INCDIR_QT'] = cfg['qt_inc_dir']
            _default_macros['LIBDIR_QT'] = cfg['qt_lib_dir']
            _default_macros['MOC'] = os.path.join(qmake_props['QT_INSTALL_BINS'], "moc")
            if qt_api == '5':
                _default_macros['CXXFLAGS'] = _default_macros['CXXFLAGS'] + ' -std=c++11'

            sipconfig.Configuration.__init__(self, [cfg])

config = Configuration()
#config.py_module_dir += 'PyQt%s' % qt_api

# adjust module name according to Qt version
if qt_api == '4':
    sip_path = os.path.join(here, "sip/pyqxtgs4mod.sip")
elif qt_api == '5':
    sip_path = os.path.join(here, "sip/pyqxtgs5mod.sip")
else:
    print('invalid Qt version: %s' % qt_api)

# Run SIP to generate the code.
command = [
    config.sip_bin,
    "-c", ".",
    "-b", build_file,
    "-I", config.pyqt_sip_dir,
    "-e"
] + config.pyqt_sip_flags.split() + [sip_path]
print(' '.join(command))
subprocess.check_call(command)

# Create the Makefile.

makefile = sipconfig.SIPModuleMakefile(config, build_file,
                                       strip = 0, qt=["QtCore", "QtGui"])
makefile.extra_include_dirs.append(os.path.join(here, "../libqxt/src/core"))
makefile.extra_include_dirs.append(os.path.join(here, "../libqxt/src/widgets"))
makefile.extra_lib_dirs.append(os.path.abspath(os.curdir))
makefile.extra_libs.append("QxtGlobalShortcut")
makefile.generate()
