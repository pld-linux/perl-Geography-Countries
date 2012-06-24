#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Geography
%define	pnam	Countries
Summary:	Geography::Countries - 2-letter, 3-letter, and numerical codes for countries
Summary(pl.UTF-8):	Geography::Countries - 2-, 3-literowe i numeryczne kody krajów
Name:		perl-Geography-Countries
Version:	2009041301
Release:	1
License:	Unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c9ef26b46bbeca9abbca5015cc748b9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module maps country names, and their 2-letter, 3-letter and
numerical codes, as defined by the ISO-3166 maintenance agency,
and defined by the UNSD.

%description -l pl.UTF-8
Ten moduł odwzorowuje nazwy krajów oraz ich 2-, 3-literowe i liczbowe
kody zgodnie z definicją ISO-3166.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Geography
%{perl_vendorlib}/Geography/*.pm
%{_mandir}/man3/*
