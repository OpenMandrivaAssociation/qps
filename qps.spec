Name:         qps
Summary:      Visual process manager
Version:      1.9.18.2
Release:      %mkrel 2
URL:          http://qps.kldp.net
Source:       %{name}-%{version}.tar.bz2
License:      GPL
Group:        Monitoring
BuildRoot:  %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:  qt3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libx11-devel 
BuildRequires:  ImageMagick

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
%setup -q 

%build
qmake
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

##install missing
install -D -p -m 0755 -s qps %{buildroot}%{_bindir}/qps
install -D -p -m 0644 qps.1 %{buildroot}%{_mandir}/man1/qps.1
install -D -p -m 0644 icon/icon.xpm %{buildroot}%{_datadir}/pixmaps/qps.xpm
install  -D -p -m 0644 qps.desktop %{buildroot}%{_datadir}/applications/gps.desktop


convert -size 48x48 icon/icon.xpm $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png 
convert -size 32x32 icon/icon.xpm $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png 
convert -size 16x16 icon/icon.xpm $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

desktop-file-install --vendor="" \
--remove-category="Application" \
--add-category=Monitor \
--add-category=X-MandrivaLinux-System-Monitoring \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/* 

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files 
%defattr(-,root,root)
%doc CHANGES COPYING README_INSTALL
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/qps.xpm
%{_mandir}/man1/qps.1*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

