# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import shutil
import subprocess
from errno import ENOENT
from distutils import log
from distutils.command.build_clib import build_clib
from distutils.command.build_ext import build_ext

import codecs
from setuptools import setup, Extension
from setuptools.command.bdist_egg import NATIVE_EXTENSIONS


# determine Qt version to build for
qt_api = os.environ.get('QT_SELECT', '5')

if qt_api not in ('4', '5'):
    print("Qt version {} not supported for pyqxtgs build".format(qt_api))
    sys.exit(1)

pyqxtgs = "pyqxtgs{}".format(qt_api)

def makedirs(name):
    if not os.path.exists(name):
        os.makedirs(name)


def try_initialize_compiler(compiler):
    if not getattr(compiler, 'initialized', True) and hasattr(compiler, 'initialize'):
        compiler.initialize()


def check_call(command, cwd):
    try:
        subprocess.check_call(command, cwd=cwd)
    except OSError as ex:
        if ex.errno == ENOENT:
            ex.strerror = "{0} not found, please make sure {0} is in PATH".format(command[0])
        raise ex


class build_clib_with_qmake(build_clib):

    def build_libraries(self, libraries):
        clib_not_qmake = []
        for (lib_name, build_info) in libraries:
            if build_info['qmake']:
                log.info("building '%s' library", lib_name)

                # init
                try_initialize_compiler(self.compiler)
                makedirs(self.build_temp)

                # qmake
                sources = os.path.abspath(build_info['sources'][0])
                check_call(["qmake", sources], cwd=self.build_temp)

                # make
                make = "nmake" if self.compiler.compiler_type == 'msvc' else "make"  # FIXME
                check_call([make], cwd=self.build_temp)

            else:
                clib_not_qmake.append((lib_name, build_info))
        build_clib.build_libraries(self, clib_not_qmake)


class build_ext_with_sip(build_ext):

    def build_extensions(self):
        build_ext.build_extensions(self)

        # copy libs to ext dir
        pyqt = 'PyQt%s' % os.environ.get('QT_SELECT', '5')
        ext_dir = os.path.join(os.path.dirname(self.get_ext_fullpath('_')),'pyqxtgs')
        for filename in os.listdir(self.build_temp):
            if os.path.splitext(filename)[1].lower() in NATIVE_EXTENSIONS:
                shutil.copy(os.path.join(self.build_temp, filename), ext_dir)

    def build_extension(self, ext):
        if ext.language == 'sip':
            log.info("building '%s' extension", ext.name)

            # init
            try_initialize_compiler(self.compiler)
            makedirs(self.build_temp)

            # configure
            config = os.path.abspath(ext.sources[0])
            check_call([sys.executable, config], cwd=self.build_temp)

            # make
            make = "nmake" if self.compiler.compiler_type == 'msvc' else "make"  # FIXME
            check_call([make], cwd=self.build_temp)

        else:
            build_ext.build_libraries(self, ext)


with codecs.open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="PyQxtGlobalShortcut",
    version="0.2.4",
    description="Python bindings to libqxt's QxtGlobalShortcut",
    long_description=long_description,
    url="https://github.com/frispete/PyQxtGlobalShortcut",
    author="Hans-Peter Jansen",
    author_email="hpj@urpla.net",
    license="GPLv3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: Developers",
        "Topic :: Desktop Environment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=['pyqxtgs'],
    package_data={'pyqxtgs': ['pyqxtgs/PyQxtGlobalShortcut.so']},
    keywords="shortcut hotkey QxtGlobalShortcut libqxt pyqt qt",
    ext_modules=[
        Extension(
            name=pyqxtgs,
            sources=["pyqxtgs/configure.py"],
            language="sip",
        ),
    ],
    libraries=[
        ("QxtGlobalShortcut", {
            'sources': ['lib/qxtglobalshortcut.pro'],
            'qmake': True,
        }),
    ],
    cmdclass={
        'build_clib': build_clib_with_qmake,
        'build_ext': build_ext_with_sip,
    }
)
