# $Id$
# Authority: dries
# Upstream: Zbigniew Lukasiak <tmp$zby,aster,net,pl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Controller-PathArgs

Summary: Syntactic sugar for Catalyst::DispatchType::Chained
Name: perl-Catalyst-Controller-PathArgs
Version: 0.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Controller-PathArgs/

Source: http://search.cpan.org//CPAN/authors/id/Z/ZB/ZBY/Catalyst-Controller-PathArgs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Syntactic sugar for Catalyst::DispatchType::Chained.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Catalyst::Controller::PathArgs*
%{perl_vendorlib}/Catalyst/Controller/PathArgs.pm
%dir %{perl_vendorlib}/Catalyst/Controller/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
