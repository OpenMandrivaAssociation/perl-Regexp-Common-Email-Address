%define module   Regexp-Common-Email-Address
%define version    1.01
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Returns a pattern for Email Addresses
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Regexp/%{module}-%{version}.tar.gz
BuildRequires: perl(Email::Address)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
'$RE{Email}{Address}'
    Provides a regex to match email addresses as defined by RFC 2822. Under
    '{-keep}', the entire match is kept as '$1'. If you want to parse that
    further then pass it to 'Email::Address->parse()'. Don't worry, it's
    fast.





%prep
%setup -q -n %{module}-%{version} 

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

