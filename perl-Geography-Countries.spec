#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Geography
%define	pnam	Countries
Summary:	Geography::Countries - 2-letter, 3-letter, and numerical codes for countries
Summary(pl):	Geography::Countries - 2, 3-literowe i numeryczne kody krajów
Name:		perl-Geography-Countries
Version:	1.4
Release:	0.7
License:	Unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	693426ab59ce3d51fcd48dfe3b402107
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module maps country names, and their 2-letter, 3-letter and
numerical codes, as defined by the ISO-3166 maintenance agency [1],
and defined by the UNSD.

=head2 The C<country> subroutine.

This subroutine is exported by default. It takes a 2-letter, 3-letter or
numerical code, or a country name as argument. In scalar context, it will
return the country name, in list context, it will return a list consisting
of the 2-letter code, the 3-letter code, the numerical code, the country
name, and a flag, which is explained below. Note that not all countries
have all 3 codes; if a code is unknown, the undefined value is returned.

There are 3 categories of countries. The largest category are the 
current countries. Then there is a small set of countries that no
longer exist. The final set consists of areas consisting of multiple
countries, like I<Africa>. No 2-letter or 3-letter codes are available
for the second two sets. (ISO 3166-3 [3] defines 4 letter codes for the
set of countries that no longer exist, but the author of this module
was unable to get her hands on that standard.) By default, C<country>
only returns countries from the first set, but this can be changed
by giving C<country> an optional second argument.

The module optionally exports the constants C<CNT_F_REGULAR>,
C<CNT_F_OLD>, C<CNT_F_REGION> and C<CNT_F_ANY>. These constants can also
be important all at once by using the tag C<:FLAGS>. C<CNT_F_ANY> is just
the binary or of the three other flags. The second argument of C<country>
should be the binary or of a subset of the flags C<CNT_F_REGULAR>,
C<CNT_F_OLD>, and C<CNT_F_REGION> - if no, or a false, second argument is
given, C<CNT_F_REGULAR> is assumed. If C<CNT_F_REGULAR> is set, regular
(current) countries will be returned; if C<CNT_F_OLD> is set, old,
no longer existing, countries will be returned, while C<CNT_F_REGION>
is used in case a region (not necessarely) a country might be returned.
If C<country> is used in list context, the fifth returned element is
one of C<CNT_F_REGULAR>, C<CNT_F_OLD> and C<CNT_F_REGION>, indicating
whether the result is a regular country, an old country, or a region.

In list context, C<country> returns a 5 element list. To avoid having
to remember which element is in which index, the constants C<CNT_I_CODE2>,
C<CNT_I_CODE3>, C<CNT_I_NUMCODE>, C<CNT_I_COUNTRY> and C<CNT_I_FLAG>
can be imported. Those constants contain the indices of the 2-letter code,
the 3-letter code, the numerical code, the country, and the flag explained
above, respectively. All index constants can be imported by using the
C<:INDICES> tag.

=head2 The C<code2>, C<code3>, C<numcode> and C<countries> routines.

All known 2-letter codes, 3-letter codes, numerical codes and country
names can be returned by the routines C<code2>, C<code3>, C<numcode> and
C<countries>. None of these methods is exported by default; all need to
be imported if one wants to use them. The tag C<:LISTS> imports them 
all. In scalar context, the number of known codes or countries is returned.

# %description -l pl
# TODO

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
%{perl_vendorlib}/Geography/*.pm
%{_mandir}/man3/*
