# $Id$
# Authority: dries
# Upstream: Rocco Caputo <rcaputo$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CDDB

Summary: High-level interface to cddb protocol servers (freedb and CDDB)
Name: perl-CDDB
Version: 1.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CDDB/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCAPUTO/CDDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
CDDB is a high-level interface to databases based on the Compact Disc
Database protocol.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CDDB.pm

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Initial package.
