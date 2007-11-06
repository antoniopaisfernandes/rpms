# $Id$
# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Find-Rule

Summary: Alternative interface to File::Find
Name: perl-File-Find-Rule
Version: 0.30
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Find-Rule/

Source: http://www.cpan.org/modules/by-module/File/File-Find-Rule-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains an alternative interface to File::Find.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man1/findrule.1*
%doc %{_mandir}/man3/File::Find::Rule.3pm*
%doc %{_mandir}/man3/File::Find::Rule::*.3pm*
%{_bindir}/findrule
%dir %{perl_vendorlib}/File/
%dir %{perl_vendorlib}/File/Find/
%{perl_vendorlib}/File/Find/Rule/
%{perl_vendorlib}/File/Find/Rule.pm

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Initial package.
