Summary:	Library of Abstract Data Types
Summary(pl):	Biblioteka abstrakcyjnych typów danych (ADT)
Name:		vanessa_adt
Version:	0.0.2
Release:	2
License:	LGPL
Group:		Libraries
Source0:	ftp://vergenet.net/pub/vanessa_adt/vanessa_adt/%{name}-%{version}.tar.gz
URL:		http://vanessa.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	vanessa_logger-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library of Abstract Data Types (ADTs) that may be useful. Includes
queue, dynamic array and key value ADT.

%description -l pl
Biblioteka abstrakcyjnych typów danych (ADT = Abstract Data Types),
które mog± byæ przydatne. Zawiera kolejki, dynamiczne tablice...

%package devel
Summary:	Headers for vanessa_adt development
Summary(pl):	Pliki nag³ówkowe vanessa_adt
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headers required to develop against vanessa_adt.

%description devel -l pl
Pliki nag³ówkowe potrzebne do tworzenia prógramów z u¿yciem
vanessa_adt.

%package static
Summary:	Static libraries for vanessa_adt development
Summary(pl):	Biblioteki statyczne vanessa_adt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries to develop against vanessa_adt.

%description static -l pl
Biblioteki statyczne vanessa_adt.

%prep
%setup -q

%build
sed -e s/AC_PROG_RANLIB/AC_PROG_LIBTOOL/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in

rm -f missing
libtoolize --copy --force
aclocal
%{__autoconf}
%{__automake}
%configure
CFLAGS="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_prefix}/{lib,bin,doc}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README ChangeLog NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%attr(644,root,root) %{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
