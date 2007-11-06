# $Id$
# Authority: dries
# Upstream: Darren Chamberlain <darren$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Plugin-Number-Format

Summary: Plugin/filter interface to Number::Format
Name: perl-Template-Plugin-Number-Format
Version: 1.01
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Plugin-Number-Format/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DARREN/Template-Plugin-Number-Format-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Plugin/filter interface to Number::Format.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Template/
%dir %{perl_vendorlib}/Template/Plugin/
%dir %{perl_vendorlib}/Template/Plugin/Number/
%{perl_vendorlib}/Template/Plugin/Number/Format.pm

%changelog
* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
