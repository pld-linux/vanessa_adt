Summary:	Library of Abstract Data Types
Summary(pl.UTF-8):	Biblioteka abstrakcyjnych typów danych (ADT)
Name:		vanessa_adt
Version:	0.0.8
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.vergenet.net/linux/vanessa/download/vanessa_adt/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	10cc585ce849cf852e03985f08ae5473
URL:		http://www.vergenet.net/linux/vanessa/
BuildRequires:	autoconf
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	vanessa_logger-devel >= 0.0.8
Requires:	vanessa_logger >= 0.0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library of Abstract Data Types (ADTs) that may be useful. Includes
queue, dynamic array and key value ADT.

%description -l pl.UTF-8
Biblioteka abstrakcyjnych typów danych (ADT = Abstract Data Types),
które mogą być przydatne. Zawiera kolejki, dynamiczne tablice...

%package devel
Summary:	Headers for vanessa_adt development
Summary(pl.UTF-8):	Pliki nagłówkowe vanessa_adt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	vanessa_logger-devel >= 0.0.4

%description devel
Headers required to develop against vanessa_adt.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia prógramów z użyciem
vanessa_adt.

%package static
Summary:	Static libraries for vanessa_adt development
Summary(pl.UTF-8):	Biblioteki statyczne vanessa_adt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries to develop against vanessa_adt.

%description static -l pl.UTF-8
Biblioteki statyczne vanessa_adt.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO
%attr(755,root,root) %{_libdir}/libvanessa_adt.so.*.*
%attr(755,root,root) %{_libdir}/libvanessa_adt.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvanessa_adt.so
%{_libdir}/libvanessa_adt.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libvanessa_adt.a
