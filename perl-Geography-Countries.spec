#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Geography
%define	pnam	Countries
Summary:	Geography::Countries - 2-letter, 3-letter, and numerical codes for countries
Summary(pl):	Geography::Countries - 2-, 3-literowe i numeryczne kody kraj�w
Name:		perl-Geography-Countries
Version:	1.4
Release:	2
License:	Unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	693426ab59ce3d51fcd48dfe3b402107
BuildRequires:	perl-devel >= 1:5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-112.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module maps country names, and their 2-letter, 3-letter and
numerical codes, as defined by the ISO-3166 maintenance agency,
and defined by the UNSD.

%description -l pl
Ten modu� odwzorowuje nazwy kraj�w oraz ich 2-, 3-literowe i liczbowe
kody zgodnie z definicj� ISO-3166.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=site
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
%dir %{perl_sitelib}/Geography
%{perl_sitelib}/Geography/*.pm
%{_mandir}/man3/*
