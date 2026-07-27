Name:		qps
Summary:	Visual process manager
Version:	2.13.0
Release:	2
URL:		https://github.com/lxqt/qps
Source0:	https://github.com/lxqt/qps/releases/download/%{version}/%{name}-%{version}.tar.xz
License:	GPL
Group:		Monitoring
BuildSystem:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(lxqt2-build-tools)
BuildRequires:	cmake(lxqt)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	imagemagick

%patchlist

%description
Qps is a visual process manager, an X11 version of "top" or "ps" that
displays processes in a window and lets you sort and manipulate them.

%files
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/qps
%{_datadir}/icons/*/*/*/qps.*
%{_datadir}/metainfo/org.lxqt.Qps.appdata.xml
%doc %{_mandir}/man1/*
