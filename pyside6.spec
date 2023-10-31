%define _disable_ld_no_undefined 1
%undefine _debugsource_packages

%define py3verflags %(python3 -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))")
%define api %(echo %{version} |cut -d. -f1-2)

Summary:	The PySide project provides LGPL-licensed Python bindings for Qt6
Name:		pyside6
Version:	6.5.3
Release:	1
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		https://wiki.qt.io/Qt_for_Python
Source0:	https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-%{version}-src/pyside-setup-everywhere-src-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
#Patch0:		pyside-5.15.2-dont-use-unrecognized-option.patch
BuildRequires:	clang-devel
BuildRequires:	llvm-devel
BuildRequires:	patchelf
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt63DAnimation)
BuildRequires:	cmake(Qt63DCore)
BuildRequires:	cmake(Qt63DExtras)
BuildRequires:	cmake(Qt63DInput)
BuildRequires:	cmake(Qt63DLogic)
BuildRequires:	cmake(Qt63DRender)
BuildRequires:	cmake(Qt6Bluetooth)
BuildRequires:	cmake(Qt6Charts)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DataVisualization)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6HttpServer)
#BuildRequires:	cmake(Qt6Location)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6MultimediaWidgets)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6NetworkAuth)
BuildRequires:	cmake(Qt6Nfc)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6PdfWidgets)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Quick3D)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6RemoteObjects)
BuildRequires:	cmake(Qt6Scxml)
BuildRequires:	cmake(Qt6Sensors)
BuildRequires:	cmake(Qt6SerialBus)
BuildRequires:	cmake(Qt6SerialPort)
BuildRequires:	cmake(Qt6SpatialAudio)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6StateMachine)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6TextToSpeech)
BuildRequires:	cmake(Qt6UiTools)
BuildRequires:	cmake(Qt6WebChannel)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineQuick)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(sdbus-c++)
BuildRequires:	pkgconfig(phonon4qt6)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	qt6-qttools-linguist
BuildRequires:	qt6-qttools-designer
BuildRequires:	qt6-qttools-assistant
Requires:	pyside6-core
Requires:	pyside6-gui
Requires:	pyside6-help
Requires:	pyside6-multimedia
Requires:	pyside6-network
Requires:	pyside6-opengl
Requires:	pyside6-script
Requires:	pyside6-scripttools
Requires:	pyside6-sql
Requires:	pyside6-test
Requires:	pyside6-xml
Requires:	pyside6-uitools
Requires:	pyside6-svg
Requires:	pyside6-webengine
Requires:	pyside6-charts
Requires:	pyside6-concurrent
Requires:	pyside6-location
Requires:	pyside6-multimediawidgets
Requires:	pyside6-positioning
Requires:	pyside6-printsupport
Requires:	pyside6-qml
Requires:	pyside6-quick
Requires:	pyside6-quickcontrols
Requires:	pyside6-quickwidgets
Requires:	pyside6-serialport
Requires:	pyside6-sensors
Requires:	pyside6-texttospeech
Requires:	pyside6-webchannel
Requires:	pyside6-websockets
Requires:	pyside6-widgets
# cmake files act up when running into obsolete-ish Qt5Declarative
BuildConflicts:	pkgconfig(Qt6Declarative)

%description
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework. PySide Qt bindings allow both free
open source and proprietary software development and ultimately aim to support
all of the platforms as Qt itself.

%files

#------------------------------------------------------------------------------
%package -n shiboken6
Summary:	Python binding generator for Qt libraries
Group:		Development/KDE and Qt
Obsoletes:	shiboken2 < 5.13.0-2

%description -n shiboken6
Python binding generator for Qt libraries.

%files -n shiboken6
%{_bindir}/shiboken6
#{py_platsitedir}/shiboken6
#{py_platsitedir}/shiboken6_generator
%{py_platsitedir}/shiboken6-%{version}-py%{py_ver}.egg-info
%{py_platsitedir}/shiboken6_generator-%{version}-py%{py_ver}.egg-info
%{_bindir}/shiboken6-genpyi

#------------------------------------------------------------------------------

%package core
Summary:	PySide core module
Group:		Development/KDE and Qt

%description core
PySide core module.

%files core
%dir %{py_platsitedir}/PySide6
%{py_platsitedir}/PySide6/__feature__.pyi
%{py_platsitedir}/PySide6/QtCore.pyi
%{py_platsitedir}/PySide6/QtCore.*.so
%{py_platsitedir}/PySide6/__init__.py*
%{py_platsitedir}/PySide6/_config.py*
%{py_platsitedir}/PySide6/_git_pyside_version.py*
%{py_platsitedir}/PySide6-%{version}-py%{py_ver}.egg-info
%dir %{py_platsitedir}/PySide6/Qt
%dir %{py_platsitedir}/PySide6/Qt/modules
%{py_platsitedir}/PySide6/Qt/modules/Core.json
%{py_platsitedir}/PySide6/libpyside6.abi3.so.6.5
%dir %{py_platsitedir}/PySide6/support
%{py_platsitedir}/PySide6/support/__init__.py
%{py_platsitedir}/PySide6/support/deprecated.py
%{py_platsitedir}/PySide6/support/generate_pyi.py
%{py_platsitedir}/PySide6/QtDBus.abi3.so
%{py_platsitedir}/PySide6/QtDBus.pyi

#------------------------------------------------------------------------------
%package bluetooth
Summary:	PySide Bluetooth module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description bluetooth
PySide Bluetooth module.

%files bluetooth
%{py_platsitedir}/PySide6/QtBluetooth.abi3.so
%{py_platsitedir}/PySide6/QtBluetooth.pyi

#------------------------------------------------------------------------------
%package httpserver
Summary:	PySide HTTP server module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description httpserver
PySide HTTP server module.

%files httpserver
%{py_platsitedir}/PySide6/QtHttpServer.abi3.so
%{py_platsitedir}/PySide6/QtHttpServer.pyi

#------------------------------------------------------------------------------
%package nfc
Summary:	PySide NFC module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description nfc
PySide NFC module.

%files nfc
%{py_platsitedir}/PySide6/QtNfc.abi3.so
%{py_platsitedir}/PySide6/QtNfc.pyi

#------------------------------------------------------------------------------
%package serialbus
Summary:	PySide Serial Bus module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description serialbus
PySide Serial Bus module.

%files serialbus
%{py_platsitedir}/PySide6/QtSerialBus.abi3.so
%{py_platsitedir}/PySide6/QtSerialBus.pyi

#------------------------------------------------------------------------------
%package spatialaudio
Summary:	PySide spatial audio module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description spatialaudio
PySide spatialaudio module.

%files spatialaudio
%{py_platsitedir}/PySide6/QtSpatialAudio.abi3.so
%{py_platsitedir}/PySide6/QtSpatialAudio.pyi

#------------------------------------------------------------------------------
%package statemachine
Summary:	PySide state machine module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description statemachine
PySide state machine module.

%files statemachine
%{py_platsitedir}/PySide6/QtStateMachine.abi3.so
%{py_platsitedir}/PySide6/QtStateMachine.pyi

#------------------------------------------------------------------------------
%package gui
Summary:	PySide gui module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description gui
PySide gui module.

%files gui
%{py_platsitedir}/PySide6/QtGui.pyi
%{py_platsitedir}/PySide6/QtGui.*.so
%{py_platsitedir}/PySide6/Qt/modules/Gui.json

#------------------------------------------------------------------------------

%package 3d
Summary:	PySide 3D module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description 3d
PySide 3D module.

%files 3d
%{py_platsitedir}/PySide6/Qt3DAnimation.*.so
%{py_platsitedir}/PySide6/Qt3DCore.*.so
%{py_platsitedir}/PySide6/Qt3DExtras.*.so
%{py_platsitedir}/PySide6/Qt3DInput.*.so
%{py_platsitedir}/PySide6/Qt3DLogic.*.so
%{py_platsitedir}/PySide6/Qt3DRender.*.so
%{py_platsitedir}/PySide6/Qt/modules/3D*.json
%{py_platsitedir}/PySide6/Qt3DAnimation.pyi
%{py_platsitedir}/PySide6/Qt3DCore.pyi
%{py_platsitedir}/PySide6/Qt3DExtras.pyi
%{py_platsitedir}/PySide6/Qt3DInput.pyi
%{py_platsitedir}/PySide6/Qt3DLogic.pyi
%{py_platsitedir}/PySide6/Qt3DRender.pyi

#------------------------------------------------------------------------------

%package help
Summary:	PySide help module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description help
PySide help module.

%files help
%{py_platsitedir}/PySide6/QtHelp.*.so
%{py_platsitedir}/PySide6/Qt/modules/Help.json
%{py_platsitedir}/PySide6/QtHelp.pyi

#------------------------------------------------------------------------------

%package multimedia
Summary:	PySide multimedia module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description multimedia
PySide multimedia module.

%files multimedia
%{py_platsitedir}/PySide6/QtMultimedia.*.so
%{py_platsitedir}/PySide6/Qt/modules/Multimedia*.json
%{py_platsitedir}/PySide6/QtMultimedia.pyi
%{py_platsitedir}/PySide6/QtMultimediaWidgets.pyi

#------------------------------------------------------------------------------

%package network
Summary:	PySide network module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description network
PySide network module.

%files network
%{py_platsitedir}/PySide6/QtNetwork.*.so
%{py_platsitedir}/PySide6/Qt/modules/Network*.json
%{py_platsitedir}/PySide6/QtNetwork.pyi
%{py_platsitedir}/PySide6/QtNetworkAuth.abi3.so
%{py_platsitedir}/PySide6/QtNetworkAuth.pyi

#------------------------------------------------------------------------------

%package datavisualization
Summary:	PySide data visualization module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description datavisualization
PySide data visualization module.

%files datavisualization
%{py_platsitedir}/PySide6/QtDataVisualization.*.so
%{py_platsitedir}/PySide6/Qt/modules/DataVisualization*.json
%{py_platsitedir}/PySide6/QtDataVisualization.pyi

#------------------------------------------------------------------------------

%package remoteobjects
Summary:	PySide remote objects module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description remoteobjects
PySide remote objects module.

%files remoteobjects
%{py_platsitedir}/PySide6/QtRemoteObjects.*.so
%{py_platsitedir}/PySide6/Qt/modules/RemoteObjects*.json
%{py_platsitedir}/PySide6/QtRemoteObjects.pyi

#------------------------------------------------------------------------------

%package scxml
Summary:	PySide XML Scene Graph module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description scxml
PySide XML Scene Graph module.

%files scxml
%{py_platsitedir}/PySide6/QtScxml.*.so
%{py_platsitedir}/PySide6/Qt/modules/Scxml*.json
%{py_platsitedir}/PySide6/QtScxml.pyi

#------------------------------------------------------------------------------

%package opengl
Summary:	PySide opengl module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description opengl
PySide opengl module.

%files opengl
%{py_platsitedir}/PySide6/QtOpenGL.*.so
%{py_platsitedir}/PySide6/Qt/modules/OpenGL*.json
%{py_platsitedir}/PySide6/QtOpenGL.pyi
%{py_platsitedir}/PySide6/QtOpenGLWidgets.abi3.so
%{py_platsitedir}/PySide6/QtOpenGLWidgets.pyi

#------------------------------------------------------------------------------

%package sql
Summary:	PySide sql module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description sql
PySide sql module.

%files sql
%{py_platsitedir}/PySide6/QtSql.*.so
%{py_platsitedir}/PySide6/Qt/modules/Sql.json
%{py_platsitedir}/PySide6/QtSql.pyi

#------------------------------------------------------------------------------

%package svg
Summary:	PySide svg module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description svg
PySide svg module.

%files svg
%{py_platsitedir}/PySide6/QtSvg.*.so
%{py_platsitedir}/PySide6/Qt/modules/Svg*.json
%{py_platsitedir}/PySide6/QtSvg.pyi
%{py_platsitedir}/PySide6/QtSvgWidgets.abi3.so
%{py_platsitedir}/PySide6/QtSvgWidgets.pyi

#------------------------------------------------------------------------------

%package test
Summary:	PySide test module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description test
PySide test module.

%files test
%{py_platsitedir}/PySide6/QtTest.*.so
%{py_platsitedir}/PySide6/Qt/modules/Test.json
%{py_platsitedir}/PySide6/QtTest.pyi

#------------------------------------------------------------------------------

%package uitools
Summary:	PySide uitools module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description uitools
PySide uitools module.

%files uitools
%{py_platsitedir}/PySide6/QtUiTools.*.so
%{py_platsitedir}/PySide6/Qt/modules/UiPlugin.json
%{py_platsitedir}/PySide6/Qt/modules/UiTools.json
%{py_platsitedir}/PySide6/QtUiTools.pyi

#------------------------------------------------------------------------------

%package webengine
Summary:	PySide webengine module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description webengine
PySide webengine module.

%files webengine
%{py_platsitedir}/PySide6/QtWebEngine*.so
%{py_platsitedir}/PySide6/Qt/libexec/QtWebEngineProcess
%{py_platsitedir}/PySide6/Qt/modules/WebEngine*.json
%{py_platsitedir}/PySide6/QtWebEngineCore.pyi
%{py_platsitedir}/PySide6/QtWebEngineQuick.pyi
%{py_platsitedir}/PySide6/QtWebEngineWidgets.pyi
%{py_platsitedir}/PySide6/QtPdf.abi3.so
%{py_platsitedir}/PySide6/QtPdf.pyi
%{py_platsitedir}/PySide6/QtPdfWidgets.abi3.so
%{py_platsitedir}/PySide6/QtPdfWidgets.pyi

#------------------------------------------------------------------------------

%package xml
Summary:	PySide xml module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description xml
PySide xml module.

%files xml
%{py_platsitedir}/PySide6/QtXml.*.so
%{py_platsitedir}/PySide6/Qt/modules/Xml.json
%{py_platsitedir}/PySide6/QtXml.pyi

#------------------------------------------------------------------------------

%package charts
Summary:	PySide charts module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description charts
PySide charts module.

%files charts
%{py_platsitedir}/PySide6/QtCharts.pyi
%{py_platsitedir}/PySide6/QtCharts.*.so
%{py_platsitedir}/PySide6/Qt/modules/Charts*.json

#------------------------------------------------------------------------------

%package concurrent
Summary:	PySide concurrent module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description concurrent
PySide concurrent module.

%files concurrent
%{py_platsitedir}/PySide6/QtConcurrent.pyi
%{py_platsitedir}/PySide6/QtConcurrent.*.so
%{py_platsitedir}/PySide6/Qt/modules/Concurrent.json

#------------------------------------------------------------------------------

%package multimediawidgets
Summary:	PySide multimediawidgets module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description multimediawidgets
PySide multimediawidgets module.

%files multimediawidgets
%{py_platsitedir}/PySide6/QtMultimediaWidgets.*.so

#------------------------------------------------------------------------------

%package positioning
Summary:	PySide positioning module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description positioning
PySide positioning module.

%files positioning
%{py_platsitedir}/PySide6/QtPositioning.*.so
%{py_platsitedir}/PySide6/Qt/modules/Positioning*.json
%{py_platsitedir}/PySide6/QtPositioning.pyi

#------------------------------------------------------------------------------

%package printsupport
Summary:	PySide printsupport module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description printsupport
PySide printsupport module.

%files printsupport
%{py_platsitedir}/PySide6/QtPrintSupport.*.so
%{py_platsitedir}/PySide6/Qt/modules/PrintSupport.json
%{py_platsitedir}/PySide6/QtPrintSupport.pyi

#------------------------------------------------------------------------------

%package qml
Summary:	PySide qml module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description qml
PySide qml module.

%files qml
%{py_platsitedir}/PySide6/libpyside6qml.abi3.so.6.5
%{py_platsitedir}/PySide6/QtQml.*.so
%{py_platsitedir}/PySide6/Qt/modules/Qml*.json
%{py_platsitedir}/PySide6/QtQml.pyi
%{py_platsitedir}/PySide6/QtQuick.pyi
%{py_platsitedir}/PySide6/QtQuick3D.abi3.so
%{py_platsitedir}/PySide6/QtQuick3D.pyi
%{py_platsitedir}/PySide6/QtQuickControls2.pyi
%{py_platsitedir}/PySide6/QtQuickWidgets.pyi

#------------------------------------------------------------------------------

%package quick
Summary:	PySide quick module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description quick
PySide quick module.

%files quick
%{py_platsitedir}/PySide6/QtQuick.*.so
%{py_platsitedir}/PySide6/Qt/modules/Quick*.json

#------------------------------------------------------------------------------

%package quickwidgets
Summary:	PySide quickwidgets module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description quickwidgets
PySide quickwidgets module.

%files quickwidgets
%{py_platsitedir}/PySide6/QtQuickWidgets.*.so

#------------------------------------------------------------------------------

%package sensors
Summary:	PySide sensors module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description sensors
PySide sensors module.

%files sensors
%{py_platsitedir}/PySide6/QtSensors.*.so
%{py_platsitedir}/PySide6/Qt/modules/Sensors*.json
%{py_platsitedir}/PySide6/QtSensors.pyi

#------------------------------------------------------------------------------

%package texttospeech
Summary:	PySide texttospeech module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description texttospeech
PySide texttospeech module.

%files texttospeech
%{py_platsitedir}/PySide6/QtTextToSpeech.*.so
%{py_platsitedir}/PySide6/Qt/modules/TextToSpeech.json
%{py_platsitedir}/PySide6/QtTextToSpeech.pyi

#------------------------------------------------------------------------------

%package webchannel
Summary:	PySide webchannel module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description webchannel
PySide webchannel module.

%files webchannel
%{py_platsitedir}/PySide6/QtWebChannel.*.so
%{py_platsitedir}/PySide6/Qt/modules/WebChannel*.json
%{py_platsitedir}/PySide6/QtWebChannel.pyi

#------------------------------------------------------------------------------

%package websockets
Summary:	PySide websockets module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description websockets
PySide websockets module.

%files websockets
%{py_platsitedir}/PySide6/QtWebSockets.*.so
%{py_platsitedir}/PySide6/Qt/modules/WebSockets*.json
%{py_platsitedir}/PySide6/QtWebSockets.pyi

#------------------------------------------------------------------------------

%package widgets
Summary:	PySide widgets module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description widgets
PySide widgets module.

%files widgets
%{py_platsitedir}/PySide6/QtWidgets.*.so
%{py_platsitedir}/PySide6/Qt/modules/Widgets*.json
%{py_platsitedir}/PySide6/QtWidgets.pyi

#------------------------------------------------------------------------------

%package quickcontrols
Summary:	PySide QtQuick Controls module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description quickcontrols
PySide QtQuick Controls module.

%files quickcontrols
%{py_platsitedir}/PySide6/QtQuickControls2.*.so
%{py_platsitedir}/PySide6/Qt/modules/QuickControls*.json

#------------------------------------------------------------------------------

%package serialport
Summary:	PySide serial port module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description serialport
PySide serial port module.

%files serialport
%{py_platsitedir}/PySide6/QtSerialPort.*.so
%{py_platsitedir}/PySide6/Qt/modules/SerialPort*.json
%{py_platsitedir}/PySide6/QtSerialPort.pyi

#------------------------------------------------------------------------------

%package devel
Summary:	PySide devel files
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}-%{release}
Requires:	shiboken6 = %{EVRD}

%description devel
PySide devel files.

%files devel
%{_bindir}/pyside6-android-deploy
%{_bindir}/pyside6-assistant
%{_bindir}/pyside6-deploy
%{_bindir}/pyside6-genpyi
%{_bindir}/pyside6-linguist
%{_bindir}/pyside6-lrelease
%{_bindir}/pyside6-metaobjectdump
%{_bindir}/pyside6-project
%{_bindir}/pyside6-qml
%{_bindir}/pyside6-qmlcachegen
%{_bindir}/pyside6-qmlformat
%{_bindir}/pyside6-qmlimportscanner
%{_bindir}/pyside6-qmllint
%{_bindir}/pyside6-qmlls
%{_bindir}/pyside6-qmltyperegistrar
%{_bindir}/pyside6-qtpy2cpp
%{_bindir}/pyside6-rcc
%{_bindir}/pyside6-uic
%{_bindir}/pyside6-lupdate
%{_bindir}/pyside6-designer
%{py_platsitedir}/PySide6/assistant
%{py_platsitedir}/PySide6/QtDesigner.abi3.so
%{py_platsitedir}/PySide6/QtDesigner.pyi
%{py_platsitedir}/PySide6/designer
%{py_platsitedir}/PySide6/linguist
%{py_platsitedir}/PySide6/lrelease
%{py_platsitedir}/PySide6/lupdate
%{py_platsitedir}/PySide6/py.typed
%{py_platsitedir}/PySide6/qmlformat
%{py_platsitedir}/PySide6/qmllint
%{py_platsitedir}/PySide6/qmlls
# FIXME do glue, typesystems etc. need to move to the various
# subpackages or are they really devel-only?
%{py_platsitedir}/PySide6/include
%{py_platsitedir}/PySide6/glue
%{py_platsitedir}/PySide6/Qt/libexec/qmlcachegen
%{py_platsitedir}/PySide6/Qt/libexec/qmlimportscanner
%{py_platsitedir}/PySide6/Qt/libexec/qmltyperegistrar
%{py_platsitedir}/PySide6/Qt/libexec/rcc
%{py_platsitedir}/PySide6/Qt/libexec/uic
%{py_platsitedir}/PySide6/Qt/metatypes
%dir %{py_platsitedir}/PySide6/typesystems
%{py_platsitedir}/PySide6/typesystems/common.xml
%{py_platsitedir}/PySide6/typesystems/core_common.xml
%{py_platsitedir}/PySide6/typesystems/datavisualization_common.xml
%{py_platsitedir}/PySide6/typesystems/glue/plugins.h
%{py_platsitedir}/PySide6/typesystems/glue/qeasingcurve_glue.cpp
%{py_platsitedir}/PySide6/typesystems/glue/qeasingcurve_glue.h
%{py_platsitedir}/PySide6/typesystems/gui_common.xml
%{py_platsitedir}/PySide6/typesystems/opengl_common.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_3danimation.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_3dcore.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_3dextras.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_3dinput.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_3dlogic.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_3drender.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_bluetooth.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_charts.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_concurrent.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_core.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_core_common.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_core_win.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_datavisualization.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_dbus.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_designer.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_glgeti_v_includes.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_glgeti_v_modifications.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_glgetv_includes.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_glgetv_modifications.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_gui.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_gui_common.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_gui_mac.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_gui_win.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_gui_x11.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_help.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_httpserver.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_multimedia.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_multimediawidgets.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_network.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_networkauth.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_nfc.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications1_0.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications1_0_compat.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications1_1.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications1_1_compat.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications1_2_compat.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications1_3_compat.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications1_4.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications1_4_compat.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications2_0.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications2_0_compat.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications2_1.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications3_0.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications3_3.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications3_3a.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications4_0.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications4_1.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications4_3.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications4_4.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications4_4_core.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications4_5.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications4_5_core.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_opengl_modifications_va.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_openglwidgets.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_pdf.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_pdfwidgets.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_positioning.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_printsupport.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_printsupport_common.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_qml.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_quick.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_quick3d.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_quickcontrols2.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_quickwidgets.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_remoteobjects.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_scxml.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_sensors.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_serialbus.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_serialport.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_spatialaudio.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_sql.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_statemachine.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_svg.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_svgwidgets.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_test.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_texttospeech.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_uitools.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_webchannel.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_webenginecore.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_webenginequick.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_webenginewidgets.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_websockets.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_widgets.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_widgets_common.xml
%{py_platsitedir}/PySide6/typesystems/typesystem_xml.xml
%{py_platsitedir}/PySide6/typesystems/widgets_common.xml
%{py_platsitedir}/PySide6/Qt/modules/Quick3DHelpers.json
%{py_platsitedir}/PySide6/Qt/modules/Quick3DIblBaker.json
%{py_platsitedir}/PySide6/Qt/modules/Core.json
%{py_platsitedir}/PySide6/Qt/modules/WebChannel.json
%{py_platsitedir}/PySide6/Qt/modules/Qml.json
%{py_platsitedir}/PySide6/Qt/modules/Pdf.json
%{py_platsitedir}/PySide6/Qt/modules/Quick3DParticles.json
%{py_platsitedir}/PySide6/Qt/modules/Quick3DUtils.json
%{py_platsitedir}/PySide6/Qt/modules/ShaderTools.json
%{py_platsitedir}/PySide6/Qt/modules/Concurrent.json
%{py_platsitedir}/PySide6/Qt/modules/Scxml.json
%{py_platsitedir}/PySide6/Qt/modules/UiTools.json
%{py_platsitedir}/PySide6/Qt/modules/HttpServer.json
%{py_platsitedir}/PySide6/Qt/modules/SerialBus.json
%{py_platsitedir}/PySide6/Qt/modules/Quick3DAssetImport.json
%{py_platsitedir}/PySide6/Qt/modules/Widgets.json
%{py_platsitedir}/PySide6/Qt/modules/QDocCatchGeneratorsPrivate.json
%{py_platsitedir}/PySide6/Qt/modules/Quick3D.json
%{py_platsitedir}/PySide6/Qt/modules/Network.json
%{py_platsitedir}/PySide6/Qt/modules/Charts.json
%{py_platsitedir}/PySide6/Qt/modules/Svg.json
%{py_platsitedir}/PySide6/Qt/modules/Nfc.json
%{py_platsitedir}/PySide6/Qt/modules/DataVisualization.json
%{py_platsitedir}/PySide6/Qt/modules/SerialPort.json
%{py_platsitedir}/PySide6/Qt/modules/Sql.json
%{py_platsitedir}/PySide6/Qt/modules/Designer.json
%{py_platsitedir}/PySide6/Qt/modules/PrintSupport.json
%{py_platsitedir}/PySide6/Qt/modules/Core5Compat.json
%{py_platsitedir}/PySide6/Qt/modules/OpenGLWidgets.json
%{py_platsitedir}/PySide6/Qt/modules/QuickControls2.json
%{py_platsitedir}/PySide6/Qt/modules/3DLogic.json
%{py_platsitedir}/PySide6/Qt/modules/3DInput.json
%{py_platsitedir}/PySide6/Qt/modules/QmlDebugPrivate.json
%{py_platsitedir}/PySide6/Qt/modules/Tools.json
%{py_platsitedir}/PySide6/Qt/modules/RemoteObjects.json
%{py_platsitedir}/PySide6/Qt/modules/3DExtras.json
%{py_platsitedir}/PySide6/Qt/modules/3DCore.json
%{py_platsitedir}/PySide6/Qt/modules/WebEngineQuick.json
%{py_platsitedir}/PySide6/Qt/modules/OpenGL.json
%{py_platsitedir}/PySide6/Qt/modules/Quick3DEffects.json
%{py_platsitedir}/PySide6/Qt/modules/QmlModels.json
%{py_platsitedir}/PySide6/Qt/modules/PdfWidgets.json
%{py_platsitedir}/PySide6/Qt/modules/Quick.json
%{py_platsitedir}/PySide6/Qt/modules/QuickWidgets.json
%{py_platsitedir}/PySide6/Qt/modules/QmlIntegration.json
%{py_platsitedir}/PySide6/Qt/modules/Xml.json
%{py_platsitedir}/PySide6/Qt/modules/3DRender.json
%{py_platsitedir}/PySide6/Qt/modules/TextToSpeech.json
%{py_platsitedir}/PySide6/Qt/modules/Sensors.json
%{py_platsitedir}/PySide6/Qt/modules/QDocCatchConversionsPrivate.json
%{py_platsitedir}/PySide6/Qt/modules/DBus.json
%{py_platsitedir}/PySide6/Qt/modules/Help.json
%{py_platsitedir}/PySide6/Qt/modules/QuickTemplates2.json
%{py_platsitedir}/PySide6/Qt/modules/Bluetooth.json
%{py_platsitedir}/PySide6/Qt/modules/RepParser.json
%{py_platsitedir}/PySide6/Qt/modules/MultimediaWidgets.json
%{py_platsitedir}/PySide6/Qt/modules/UiPlugin.json
%{py_platsitedir}/PySide6/Qt/modules/WebEngineCore.json
%{py_platsitedir}/PySide6/Qt/modules/QDocCatchPrivate.json
%{py_platsitedir}/PySide6/Qt/modules/Quick3DGlslParserPrivate.json
%{py_platsitedir}/PySide6/Qt/modules/Gui.json
%{py_platsitedir}/PySide6/Qt/modules/Quick3DParticleEffects.json
%{py_platsitedir}/PySide6/Qt/modules/WebSockets.json
%{py_platsitedir}/PySide6/Qt/modules/StateMachine.json
%{py_platsitedir}/PySide6/Qt/modules/3DAnimation.json
%{py_platsitedir}/PySide6/Qt/modules/Quick3DRuntimeRender.json
%{py_platsitedir}/PySide6/Qt/modules/NetworkAuth.json
%{py_platsitedir}/PySide6/Qt/modules/SpatialAudio.json
%{py_platsitedir}/PySide6/Qt/modules/Multimedia.json
%{py_platsitedir}/PySide6/Qt/modules/Linguist.json
%{py_platsitedir}/PySide6/Qt/modules/WebChannelQuick.json
%{py_platsitedir}/PySide6/Qt/modules/SvgWidgets.json
%{py_platsitedir}/PySide6/Qt/modules/Positioning.json
%{py_platsitedir}/PySide6/Qt/modules/WebEngineWidgets.json
%{py_platsitedir}/PySide6/Qt/modules/Test.json
%dir %{py_platsitedir}/PySide6
%dir %{py_platsitedir}/PySide6/scripts
%{py_platsitedir}/PySide6/scripts/__init__.py
%{py_platsitedir}/PySide6/scripts/android_deploy.py
%{py_platsitedir}/PySide6/scripts/deploy.py
%{py_platsitedir}/PySide6/scripts/deploy_lib
%{py_platsitedir}/PySide6/scripts/metaobjectdump.py
%{py_platsitedir}/PySide6/scripts/project.py
%dir %{py_platsitedir}/PySide6/scripts/project
%{py_platsitedir}/PySide6/scripts/project/__init__.py
%{py_platsitedir}/PySide6/scripts/project/newproject.py
%{py_platsitedir}/PySide6/scripts/project/project_data.py
%{py_platsitedir}/PySide6/scripts/project/utils.py
%{py_platsitedir}/PySide6/scripts/pyside_tool.py
%{py_platsitedir}/PySide6/scripts/qml.py
%{py_platsitedir}/PySide6/scripts/qtpy2cpp.py
%dir %{py_platsitedir}/PySide6/scripts/qtpy2cpp_lib
%{py_platsitedir}/PySide6/scripts/qtpy2cpp_lib/astdump.py
%{py_platsitedir}/PySide6/scripts/qtpy2cpp_lib/formatter.py
%{py_platsitedir}/PySide6/scripts/qtpy2cpp_lib/nodedump.py
%{py_platsitedir}/PySide6/scripts/qtpy2cpp_lib/qt.py
%{py_platsitedir}/PySide6/scripts/qtpy2cpp_lib/tokenizer.py
%{py_platsitedir}/PySide6/scripts/qtpy2cpp_lib/visitor.py

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n pyside-setup-everywhere-src-%{version}

%build
#python setup.py --qtpaths=%{_qtdir}/bin/qtpaths build
%define py_setup_args --qtpaths=%{_qtdir}/bin/qtpaths build
%py_build

%install
#python setup.py --qtpaths=%{_qtdir}/bin/qtpaths install --prefix %{_prefix} --root %{buildroot}
%define py_setup_args --qtpaths=%{_qtdir}/bin/qtpaths install --prefix %{_prefix}
%py_install

