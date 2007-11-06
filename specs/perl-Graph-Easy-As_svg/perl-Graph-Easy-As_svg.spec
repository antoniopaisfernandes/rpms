# $Id$
# Authority: dries
# Upstream: Tels <nospam-abuse$bloodgate,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graph-Easy-As_svg

Summary: Render Graph-Easy as SVG
Name: perl-Graph-Easy-As_svg
Version: 0.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graph-Easy-As_svg/

Source: http://search.cpan.org/CPAN/authors/id/T/TE/TELS/graph/Graph-Easy-As_svg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Graph-Easy >= 0.5, perl(Image::Info) >= 1.22

%description
Render Graph-Easy as SVG (Scalable Vector Graphics).

Graphs can be generated by Perl code, or parsed from a simple text format
that is human readable and maintainable.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README TODO
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Graph/Easy/As_svg.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Updated to release 0.17.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Initial package.
