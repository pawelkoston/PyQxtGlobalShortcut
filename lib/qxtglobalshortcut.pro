
TEMPLATE = lib
TARGET = QxtGlobalShortcut

CONFIG += qt release
QT = core gui
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

QXT = core
DEFINES += BUILD_QXT_CORE BUILD_QXT_GUI

INCLUDEPATH = ../libqxt/src/core ../libqxt/src/widgets
VPATH += $$INCLUDEPATH
HEADERS += qxtglobalshortcut.h
SOURCES += qxtglobal.cpp qxtglobalshortcut.cpp

unix: {
CONFIG += static
greaterThan(QT_MAJOR_VERSION, 4): QT += gui-private
}

unix:!macx {
SOURCES += x11/qxtglobalshortcut_x11.cpp
}

macx {
SOURCES += mac/qxtglobalshortcut_mac.cpp
LIBS += -framework Carbon
}

win32 {
SOURCES += win/qxtglobalshortcut_win.cpp
LIBS += -luser32
}
