# $Id$

# Authority: dries
# Upstream: Benjamin Holzman <bholzman$earthlink,net>

%define real_name XML-Generator
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Perl extension for generating XML
Name: perl-XML-Generator
Version: 0.99_02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Generator/

Source: http://search.cpan.org/CPAN/authors/id/B/BH/BHOLZMAN/XML-Generator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module allows you to generate XML documents.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/Generator.pm
%{perl_vendorlib}/XML/Generator

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.99_02-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.99_02-1
- Updated to release 0.99_02.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 0.99_02-1
- Initial package.
