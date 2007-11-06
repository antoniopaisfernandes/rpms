# $Id$
# Authority: dries
# Upstream: Nick Ing-Simmons <nick$ing-simmons,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Audio

Summary: Represents audio data
Name: perl-Audio
Version: 1.029
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Audio/

Source: http://search.cpan.org/CPAN/authors/id/N/NI/NI-S/Audio-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This is the beginings of Audio manipulation routines for perl.
Currently can load or save Sun/Next .au/.snd files and play them
via Network Audio Server (from ftp.x.org) or native /dev/audio
on Suns.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/Audio/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/tkscope
%{_bindir}/dial
%{_bindir}/morse
%{_bindir}/pplay
%{perl_vendorarch}/Audio/
%{perl_vendorarch}/Tk/
%{perl_vendorarch}/auto/Audio/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.029-1
- Initial package.
