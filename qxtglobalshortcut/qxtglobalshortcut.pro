
TEMPLATE = lib
TARGET = QxtGlobalShortcut

DESTDIR = ./

CONFIG += qt release
QT = core gui

QXT = core
DEFINES += BUILD_QXT_CORE BUILD_QXT_GUI

INCLUDEPATH = ../libqxt/src/core ../libqxt/src/widgets
VPATH += $$INCLUDEPATH
HEADERS += qxtglobalshortcut.h
SOURCES += qxtglobal.cpp qxtglobalshortcut.cpp

unix:!macx {
CONFIG += static
SOURCES += x11/qxtglobalshortcut_x11.cpp
}

macx {
CONFIG += static
SOURCES += mac/qxtglobalshortcut_mac.cpp
LIBS += -framework Carbon
}

win32 {
SOURCES += win/qxtglobalshortcut_win.cpp
LIBS += -luser32
}
