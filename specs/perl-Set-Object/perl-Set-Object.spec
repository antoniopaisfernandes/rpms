# $Id$
# Authority: dries
# Upstream: Sam Vilain <sam$vilain,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Set-Object

Summary: Set of objects and strings
Name: perl-Set-Object
Version: 1.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-Object/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SAMV/Set-Object-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This modules implements a set of objects, that is, an unordered
collection of objects without duplication.

The term *objects* is applied loosely - for the sake of Set::Object,
anything that is a reference is considered an object.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes.pod README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Set/
%{perl_vendorarch}/Set/Object.pm
%dir %{perl_vendorarch}/auto/Set/
%{perl_vendorarch}/auto/Set/Object/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
