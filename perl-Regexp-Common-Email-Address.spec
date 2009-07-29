%define upstream_name    Regexp-Common-Email-Address
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Returns a pattern for Email Addresses
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Regexp/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Email::Address)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'$RE{Email}{Address}'
    Provides a regex to match email addresses as defined by RFC 2822. Under
    '{-keep}', the entire match is kept as '$1'. If you want to parse that
    further then pass it to 'Email::Address->parse()'. Don't worry, it's
    fast.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Regexp
