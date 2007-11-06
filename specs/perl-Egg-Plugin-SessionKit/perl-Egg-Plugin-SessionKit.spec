# $Id$
# Authority: dries
# Upstream: Masatoshi Mizuno <mizuno$bomcity,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Egg-Plugin-SessionKit

Summary: Session plugin for Egg
Name: perl-Egg-Plugin-SessionKit
Version: 2.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Egg-Plugin-SessionKit/

Source: http://search.cpan.org//CPAN/authors/id/L/LU/LUSHE/Egg-Plugin-SessionKit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Install)

%description
Session plugin for Egg.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Egg::Plugin::SessionKit*.3*
%dir %{perl_vendorlib}/Egg/
%dir %{perl_vendorlib}/Egg/Plugin/
%{perl_vendorlib}/Egg/Plugin/SessionKit.pm
%{perl_vendorlib}/Egg/Plugin/SessionKit/

%changelog
* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Updated to release 2.01.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
