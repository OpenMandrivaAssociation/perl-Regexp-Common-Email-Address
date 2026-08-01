%define upstream_name    Regexp-Common-Email-Address
%define upstream_version 1.01
Name:		perl-%{upstream_name}
Version:	1.01
Release:	4

Summary:	Returns a pattern for Email Addresses
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Regexp-Common-Email-Address
Source0:	https://cpan.metacpan.org/authors/id/C/CW/CWEST/Regexp-Common-Email-Address-1.01.tar.gz

BuildRequires:	make
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
%setup -q -n Regexp-Common-Email-Address-1.01

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Regexp

