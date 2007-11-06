# $Id$
# Authority: dries
# Upstream: Tassilo von Parseval <tassilo,parseval$post,rwth-aachen,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-MboxParser

Summary: Read-only access to UNIX-mailboxes
Name: perl-Mail-MboxParser
Version: 0.55
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-MboxParser/

Source: http://search.cpan.org/CPAN/authors/id/V/VP/VPARSEVAL/Mail-MboxParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Mail::MboxParser is a module for working with UNIX-flavoured mailboxes.

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
%doc Changelog README
%doc %{_mandir}/man3/Mail::MboxParser*
%{perl_vendorlib}/Mail/MboxParser.pm
%{perl_vendorlib}/Mail/MboxParser/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.55-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Updated to release 0.55.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.
