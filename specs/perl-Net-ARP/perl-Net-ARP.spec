# $Id$
# Authority: dries
# Upstream: Bastian Ballmann <Crazydj$chaostal,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-ARP

Summary: Create and send ARP packets
Name: perl-Net-ARP
Version: 0.8
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-ARP/

Source: http://search.cpan.org/CPAN/authors/id/C/CR/CRAZYDJ/Net-ARP-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module is a Perl extension to create and send ARP packets.
You do not need to install any additionally libraries like Libnet to compile
this extension. It uses kernel header files to create the packets.

%prep
%setup -n %{real_name}

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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/ARP.pm
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/ARP/

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Initial package.
