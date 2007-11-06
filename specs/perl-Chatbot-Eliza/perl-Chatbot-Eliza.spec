# $Id$
# Authority: dries
# Upstream: John Nolan <jpnolan$sonic,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chatbot-Eliza

Summary: Clone of the classic Eliza program
Name: perl-Chatbot-Eliza
Version: 1.04
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Chatbot-Eliza/

Source: http://search.cpan.org/CPAN/authors/id/J/JN/JNOLAN/Chatbot-Eliza-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module implements the classic Eliza algorithm. The original
Eliza program was written by Joseph Weizenbaum and described in
the Communications of the ACM in 1966. Eliza is a mock Rogerian
psychotherapist. It prompts for user input, and uses a simple
transformation algorithm to change user input into a follow-up
question. The program is designed to give the appearance of
understanding.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Chatbot/Eliza.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
