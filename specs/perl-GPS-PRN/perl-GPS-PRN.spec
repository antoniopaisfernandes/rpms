# $Id$
# Authority: dag
# Upstream: Michael R. Davis <account=>perl,tld=>com,domain=>michaelrdavis>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GPS-PRN

Summary: Perl module that implements PRN - Object ID conversions
Name: perl-GPS-PRN
Version: 0.06
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GPS-PRN/

Source: http://search.cpan.org/CPAN/authors/id/M/MR/MRDVT/GPS-PRN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Simple)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
Requires: perl(Test::Simple)
Requires: perl(strict)
Requires: perl(vars)

%filter_from_requires /^perl*/d
%filter_setup


%description
GPS-PRN is a Perl module that implements PRN - Object ID conversions.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/GPS::PRN.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/GPS/
#%{perl_vendorlib}/GPS/PRN/
%{perl_vendorlib}/GPS/PRN.pm

%changelog
* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 0.06-1
- Updated to version 0.06.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
