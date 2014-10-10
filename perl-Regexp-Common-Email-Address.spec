%define upstream_name    Regexp-Common-Email-Address
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Returns a pattern for Email Addresses
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Regexp/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Regexp::Common)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
'$RE{Email}{Address}'
    Provides a regex to match email addresses as defined by RFC 2822. Under
    '{-keep}', the entire match is kept as '$1'. If you want to parse that
    further then pass it to 'Email::Address->parse()'. Don't worry, it's
    fast.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Regexp

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 404355
- rebuild using %%perl_convert_version

* Mon Jul 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
+ Revision: 235633
- import perl-Regexp-Common-Email-Address


* Mon Jul 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
- initial mdv release, generated with cpan2dist
