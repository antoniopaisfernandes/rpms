# $Id$

# Authority: dries

Summary: ncurses based dvorak typing tutor
Name: dvorak7min
Version: 1.6.1
Release: 2
License: GPL
Group: Applications/System
URL: http://www.linalco.com/comunidad.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.linalco.com/ragnar/dvorak7min-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Dvorak7min is a ncurses based dvorak typing tutor. It features well chosen
lessons, color for easy visual feedback, and a real time characters per
second display. It's called 7min because it originally was a personal hack
written in 7 min.

%prep
%setup

%build
# force rebuild
rm -f dvorak7min *.o
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
sed -i "s/^INSTALL =.*/INSTALL = ${RPM_BUILD_ROOT//\//\\/}\/usr\/bin/g;" Makefile
strip dvorak7min
%{__make} install

%files
%defattr(-,root,root, 0755)
%doc README ChangeLog COPYING
%{_bindir}/%{name}

%changelog
* Tue Feb 24 2004 Dries Verachtert <dries@ulyssis.org> 1.6.1-2
- force rebuild
- check build requirements with mach

* Sun Feb 1 2004 Dries Verachtert <dries@ulyssis.org> 1.6.1-1
- first packaging for Fedora Core 1
