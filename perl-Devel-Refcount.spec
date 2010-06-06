#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Refcount
Summary:	Devel::Refcount - obtain the REFCNT value of a referent
Summary(pl.UTF-8):	Devel::Refcount - pozyskuje wartość REFCNT referenta
Name:		perl-Devel-Refcount
Version:	0.07
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f0517077c8189d0d2620bf1db070472
URL:		http://search.cpan.org/dist/Devel-Refcount/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a single function which obtains the reference
count of the object being pointed to by the passed reference value.

%description -l pl.UTF-8
Moduł ten dostracza pojedynczą funkcję, która pozyskuje licznik
odwołań do obiektu wskazanego przez przekazaną referencję.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Devel/*.pm
%dir %{perl_vendorarch}/auto/Devel/Refcount
%{perl_vendorarch}/auto/Devel/Refcount/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/Refcount/*.so
%{_mandir}/man3/*
