# $Id$
# Authority: dries
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-Raw-Bzip2

Summary: Low-Level Interface to bzip2 compression library
Name: perl-Compress-Raw-Bzip2
Version: 2.003
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-Raw-Bzip2/

Source: http://search.cpan.org//CPAN/authors/id/P/PM/PMQS/Compress-Raw-Bzip2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Low-Level Interface to bzip2 compression library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Compress::Raw::Bzip2*.3pm*
%dir %{perl_vendorarch}/Compress/
%dir %{perl_vendorarch}/Compress/Raw/
%{perl_vendorarch}/Compress/Raw/Bzip2.pm
%dir %{perl_vendorarch}/auto/Compress/
%dir %{perl_vendorarch}/auto/Compress/Raw/
%{perl_vendorarch}/auto/Compress/Raw/Bzip2/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.003-1
- Initial package.
