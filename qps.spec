Name:		qps
Summary:	Visual process manager
Version:	2.6.0
Release:	1
URL:		https://github.com/lxqt/qps
Source0:	https://github.com/lxqt/qps/releases/download/%{version}/%{name}-%{version}.tar.xz
License:	GPL
Group:		Monitoring
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(lxqt-build-tools)
BuildRequires:	cmake(lxqt)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	imagemagick

%description
Qps is a visual process manager, an X11 version of "top" or "ps" that 
displays processes in a window and lets you sort and manipulate them. 

Qps can:
  o  Change nice value of a process.
  o  Alter the scheduling policy and soft realtime priority of a process.
  o  Display the TCP/UDP sockets used by a process, and names of the 
      connected hosts (Linux only).
  o  Display the memory mappings of the process (which files and shared 
  o  libraries are loaded   where).
  o  Display the open files of a process, and the state of unix domain sockets.
  o  Kill or send any other signal to selected processes.
  o  Display the load average as a graph, and use this as its icon when 
      iconified.
  o  Show (as graph or numbers) current CPU, memory and swap usage.
  o  Sort the process table on any attribute (size, cpu usage, owner etc).
  o  On SMP systems running Linux 2.1 or later (or Solaris), display cpu usage 
      for each processor, and which CPU a process is running on.
  o  Display the environment variables of any process. 
  o  Show the process table in tree form, showing the parent-child 
      relationship. 
  o  Execute user-defined commands on selected processes. 
  o  Display MOSIX-specific fields and migrate processes to other nodes
      in a cluster. 

  Qps runs on Linux and Solaris.

%prep
%autosetup -p1

%build
%cmake_qt5 -G Ninja
%ninja_build

%install
%ninja_install -C build

%files
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/qps
%{_datadir}/icons/*/*/*/qps.*
%doc %{_mandir}/man1/*
