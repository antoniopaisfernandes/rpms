# $Id$

# Authority: dag
# Upstream: Dug Song <dugsong@monkey.org>

Summary: Intercepts, modifies, and rewrites egress traffic
Name: fragroute
Version: 1.2
Release: 0
License: BSD
Group: Applications/Internet
URL: http://www.monkey.org/~dugsong/fragroute/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.monkey.org/~dugsong/fragroute/fragroute-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libdnet, libpcap, libevent-devel

%description
Fragroute intercepts, modifies, and rewrites egress traffic destined
for a specified host, implementing most of the attacks described in
the Secure Networks "Insertion, Evasion, and Denial of Service:
Eluding Network Intrusion Detection" paper of January 1998.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README TODO scripts/
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*.conf
%{_sbindir}/*

%changelog
* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial package. (using DAR)
