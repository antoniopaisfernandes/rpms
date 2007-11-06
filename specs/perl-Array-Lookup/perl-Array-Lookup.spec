# $Id$
# Authority: dries
# Upstream: Alan K. Stebbens <aks$stebbens,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Array-Lookup

Summary: Lookup strings in arrays or hash tables with abbreviation
Name: perl-Array-Lookup
Version: 2.1
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Array-Lookup/

Source: http://search.cpan.org/CPAN/authors/id/A/AK/AKSTE/Array-Lookup-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This is a perl module which performs a search through an array of strings,
allowing for abbreviation of the search key.

The Lookup subroutine is especially handy for doing keyword lookups in
an array or hash table, where the keyword may be abbreviated.  Exact
matches are give priority over abbreviated matches.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Array/Lookup.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.1-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Initial package.
