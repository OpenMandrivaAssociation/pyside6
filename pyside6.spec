%define _disable_ld_no_undefined 1
%undefine _debugsource_packages
%define api %(echo %{version} |cut -d. -f1-2)

# Just for builds where the cmake files are broken, such as
# early 6.0 betas.
# cmake is the better way to build this, since it knows where
# files are expected to go.
%bcond_without cmake

%global py_setup_args --qtpaths=%{_qtdir}/bin/qtpaths
#define gitdate 20240315

%define major %(echo %{version}|cut -d. -f1-3)

Summary:	The PySide project provides LGPL-licensed Python bindings for Qt6
Name:		pyside6
Version:	6.8.0.1
Release:	%{?gitdate:0.%{gitdate}.}1
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		https://wiki.qt.io/Qt_for_Python
%if 0%{?gitdate:1}
Source0:	pyside6-%{gitdate}.tar.zst
%else
Source0:	https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-%{version}-src/pyside-setup-everywhere-src-%{major}.tar.xz
%endif
Source100:	%{name}.rpmlintrc
# FIXME patches autogenerated code, evil...
#Source150:	pyside6-qt6.7-workaround.patch
#Patch0:		pyside-qt-6.7.0-rc.patch
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
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6DataVisualization)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Graphs)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6HttpServer)
BuildRequires:	cmake(Qt6Location)
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
BuildRequires:	cmake(Qt6Quick3DAssetImport)
BuildRequires:	cmake(Qt6Quick3DEffects)
BuildRequires:	cmake(Qt6Quick3DGlslParserPrivate)
BuildRequires:	cmake(Qt6Quick3DHelpers)
BuildRequires:	cmake(Qt6Quick3DIblBaker)
BuildRequires:	cmake(Qt6Quick3DParticles)
BuildRequires:	cmake(Qt6Quick3DParticleEffects)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6QuickTest)
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
BuildRequires:	cmake(Qt6WebView)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6BodymovinPrivate)
BuildRequires:	cmake(Qt6DesignerComponentsPrivate)
BuildRequires:	cmake(Qt6DeviceDiscoverySupportPrivate)
BuildRequires:	cmake(Qt6EglFSDeviceIntegrationPrivate)
BuildRequires:	cmake(Qt6EglFsKmsGbmSupportPrivate)
BuildRequires:	cmake(Qt6EglFsKmsSupportPrivate)
BuildRequires:	cmake(Qt6ExampleIconsPrivate)
BuildRequires:	cmake(Qt6FbSupportPrivate)
BuildRequires:	cmake(Qt6Graphs)
BuildRequires:	cmake(Qt6HunspellInputMethod)
BuildRequires:	cmake(Qt6InputSupportPrivate)
BuildRequires:	cmake(Qt6JsonRpcPrivate)
BuildRequires:	cmake(Qt6KmsSupportPrivate)
BuildRequires:	cmake(Qt6LabsAnimation)
BuildRequires:	cmake(Qt6LabsFolderListModel)
BuildRequires:	cmake(Qt6LabsQmlModels)
BuildRequires:	cmake(Qt6LabsSettings)
BuildRequires:	cmake(Qt6LabsSharedImage)
BuildRequires:	cmake(Qt6LabsWavefrontMesh)
BuildRequires:	cmake(Qt6LanguageServerPrivate)
BuildRequires:	cmake(Qt6PacketProtocolPrivate)
BuildRequires:	cmake(Qt6PdfQuick)
BuildRequires:	cmake(Qt6StateMachineQml)
BuildRequires:	cmake(Qt6QVirtualKeyboardPlugin)
BuildRequires:	cmake(Qt6DmaBufServerBufferPlugin)
BuildRequires:	cmake(Qt6DmaBufServerBufferIntegrationPlugin)
BuildRequires:	cmake(Qt6QWaylandEglPlatformIntegrationPlugin)
BuildRequires:	cmake(Qt6WaylandEglCompositorHwIntegrationPrivate)
BuildRequires:	cmake(Qt6DmaBufServerBufferPlugin)
BuildRequires:	cmake(Qt6QWebEngineWebViewPlugin)
BuildRequires:	cmake(Qt6WebViewQuick)
BuildRequires:	cmake(Qt6WlShellIntegrationPrivate)
BuildRequires:	cmake(Qt6XcbQpaPrivate)
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
BuildRequires:	qt6-qtbase-examples
# FIXME for some reason, if there's a previous version
# installed, it gets used instead of building the correct
# version.
# For now, let's just make sure there's no previous
# version installed.
BuildConflicts:	shiboken6
Requires:	pyside6-core
Requires:	pyside6-gui
Requires:	pyside6-help
Requires:	pyside6-location
Requires:	pyside6-multimedia
Requires:	pyside6-network
Requires:	pyside6-opengl
Requires:	pyside6-sql
Requires:	pyside6-test
Requires:	pyside6-xml
Requires:	pyside6-uitools
Requires:	pyside6-svg
Requires:	pyside6-webengine
Requires:	pyside6-charts
Requires:	pyside6-concurrent
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
%if %{with cmake}
BuildRequires:	cmake ninja
%endif

%patchlist

%description
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework. PySide Qt bindings allow both free
open source and proprietary software development and ultimately aim to support
all of the platforms as Qt itself.

%files

#------------------------------------------------------------------------------
%define libshiboken %mklibname shiboken6.api3

%package -n %{libshiboken}
Summary:	Runtime library for Shiboken, the Qt python binding generator
Group:		System/Libraries

%description -n %{libshiboken}
Runtime library for Shiboken, the Qt python binding generator

%files -n %{libshiboken}
%{_libdir}/libshiboken6.abi3.so*

#------------------------------------------------------------------------------
%package -n shiboken6
Summary:	Python binding generator for Qt libraries
Group:		Development/KDE and Qt
Obsoletes:	shiboken2 < 5.13.0-2
Requires:	%{libshiboken} = %{EVRD}

%description -n shiboken6
Python binding generator for Qt libraries.

%files -n shiboken6
%{_bindir}/shiboken6
%{_bindir}/shiboken_tool.py

#------------------------------------------------------------------------------

%package core
Summary:	PySide core module
Group:		Development/KDE and Qt

%description core
PySide core module.

%files core
%dir %{py_platsitedir}/PySide6
%{py_platsitedir}/PySide6/QtCore.pyi
%{py_platsitedir}/PySide6/QtCore.*.so
%{py_platsitedir}/PySide6/__init__.py*
%{py_platsitedir}/PySide6/_config.py*
%{py_platsitedir}/PySide6/_git_pyside_version.py*
%{_libdir}/libpyside6.abi3.so*
%dir %{py_platsitedir}/PySide6/support
%{py_platsitedir}/PySide6/support/__init__.py
%{py_platsitedir}/PySide6/support/deprecated.py
%{py_platsitedir}/PySide6/support/generate_pyi.py
%{py_platsitedir}/PySide6/QtDBus.abi3.so
%{py_platsitedir}/PySide6/QtDBus.pyi
%{py_platsitedir}/PySide6/QtAsyncio

#------------------------------------------------------------------------------
%package graphs
Summary:	PySide Graphs module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description graphs
PySide Graphs module.

%files graphs
%{py_platsitedir}/PySide6/QtGraphs.abi3.so
%{py_platsitedir}/PySide6/QtGraphs.pyi

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
%{py_platsitedir}/PySide6/QtExampleIcons.abi3.so

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

#------------------------------------------------------------------------------

%package location
Summary:	PySide location module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description location
PySide location module.

%files location
%{py_platsitedir}/PySide6/QtLocation.*.so
%{py_platsitedir}/PySide6/QtLocation.pyi

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
%{py_platsitedir}/PySide6/QtPrintSupport.pyi

#------------------------------------------------------------------------------

%package qml
Summary:	PySide qml module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description qml
PySide qml module.

%files qml
%{_libdir}/libpyside6qml.abi3.so*
%{py_platsitedir}/PySide6/QtQml.*.so
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

#------------------------------------------------------------------------------

%package quicktest
Summary:	PySide quicktest module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}
Requires:	pyside6-quick = %{version}

%description quicktest
PySide quicktest module.

%files quicktest
%{py_platsitedir}/PySide6/QtQuickTest.*.so
%{py_platsitedir}/PySide6/QtQuickTest.pyi


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

#------------------------------------------------------------------------------

%package serialport
Summary:	PySide serial port module
Group:		Development/KDE and Qt
Requires:	pyside6-core = %{version}

%description serialport
PySide serial port module.

%files serialport
%{py_platsitedir}/PySide6/QtSerialPort.*.so
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
%{_bindir}/android_deploy.py
%{_bindir}/balsam
%{_bindir}/balsamui
%{_bindir}/pyside
%{_bindir}/project
%{_bindir}/qmlcachegen
%{_bindir}/qmlimportscanner
%{_bindir}/qmllint
%{_bindir}/deploy.py
%{_bindir}/deploy_lib
%{_bindir}/metaobjectdump.py
%{_bindir}/project.py
%{_bindir}/pyside_tool.py
%{_bindir}/qml.py
%{_bindir}/qmlls
%{_bindir}/qsb
%{_bindir}/qtpy2cpp.py
%{_bindir}/qtpy2cpp_lib
%{_prefix}/plugins/designer/libPySidePlugin.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
%{py_platsitedir}/shiboken6
%{py_platsitedir}/shiboken6_generator
%{py_platsitedir}/PySide6/QtDesigner.abi3.so
%{py_platsitedir}/PySide6/QtDesigner.pyi
%{_includedir}/*
# FIXME do glue, typesystems etc. need to move to the various
# subpackages or are they really devel-only?
%{_datadir}/PySide6
%dir %{py_platsitedir}/PySide6

#------------------------------------------------------------------------------

%prep
%if 0%{?gitdate:1}
%autosetup -p1 -n pyside-setup
%else
%autosetup -p1 -n pyside-setup-everywhere-src-%{major}
%endif
# bootstrap build since the cmake files try to call into
# shiboken before building it
%py_build -- --build-type=shiboken6
mv build/qfp-py*-release/package_for_wheels bootstrap

%if %{with cmake}
# There is already a "build" subdirectory
export CMAKE_BUILD_DIR=rpm.build
sed -i -e '/CMAKE_BUILD_TYPE/iinclude_directories(SYSTEM %{_includedir}/python%{pyver})' CMakeLists.txt
# Fix installation dir
sed -i 's#purelib#platlib#' sources/shiboken6/cmake/ShibokenHelpers.cmake
%cmake \
	-DUSE_PYTHON_VERSION=%{pyver} \
	-G Ninja
%endif

%build
%if %{with cmake}
export PYTHONPATH=$(pwd)/bootstrap
%ninja_build -C rpm.build
%endif

%install
%if %{with cmake}
export PYTHONPATH=$(pwd)/bootstrap
%ninja_install -C rpm.build

# Don't conflict with regular Qt bits
cd %{buildroot}%{_bindir}
mkdir pyside
mv \
	assistant designer linguist lrelease lupdate \
	qmlformat qmltyperegistrar rcc uic \
	pyside/
cd -
%else
%py_install -- --prefix %{_prefix}

# Move headers where compilers can find them
mkdir -p %{buildroot}%{_includedir}
mv %{buildroot}%{py_platsitedir}/PySide6/include/* %{buildroot}%{_includedir}/
rmdir %{buildroot}%{py_platsitedir}/PySide6/include

# According to the cmake files, typesystems belong in %{_datadir}/PySide6
mkdir -p %{buildroot}%{_datadir}/PySide6

mv \
	%{buildroot}%{py_platsitedir}/PySide6/typesystems \
	%{buildroot}%{py_platsitedir}/PySide6/glue \
	%{buildroot}%{_datadir}/PySide6/

# The build system seems to forget about installing some components...
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_qtdir}/bin
cp -a build/qfp-*-release/install/bin/shiboken_tool.py %{buildroot}%{_qtdir}/bin/
cp -a build/qfp-*-release/install/lib/libshiboken6.abi*.so* %{buildroot}%{py_platsitedir}/PySide6/
cp -a build/qfp-*-release/install/lib/{pkgconfig,cmake} %{buildroot}%{_libdir}
cp -a build/qfp-*-release/install/lib/python*/site-packages/* %{buildroot}%{py_platsitedir}/
cp -a build/qfp-*-release/install/include/shiboken6 %{buildroot}%{_includedir}/

# Those are actual shared libraries, and need to be found by ld.so when
# doing `from PySide6.QtCore import Qt`
cd %{buildroot}%{py_platsitedir}/PySide6
LIBS=$(ls -1 lib*.abi*.so.%{api})
cd %{buildroot}%{_libdir}
for i in $LIBS; do
	ln -s python*/site-packages/PySide6/$i .
done
for i in *.so.%{api}; do
	ln -s $i ${i}.0
done
%if "%{_lib}" != "lib"
sed -i -e "s,/lib/,/%{_lib}/,g" %{buildroot}%{_libdir}/cmake/*/*.cmake
%endif
%endif
# This seems to be wrong, at least in that location
rm -f %{buildroot}%{_bindir}/requirements-android.txt
