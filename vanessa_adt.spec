Summary:	Library of Abstract Data Types
Summary(pl):	Biblioteka abstrakcyjnych typów danych (ADT)
Name:		vanessa_adt
Version:	0.0.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.vergenet.net/linux/vanessa/download/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a569c913da992786608523c469061e2a
URL:		http://www.vergenet.net/linux/vanessa/
BuildRequires:	vanessa_logger-devel >= 0.0.4
Requires:	vanessa_logger >= 0.0.4
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
Requires:	%{name} = %{version}-%{release}
Requires:	vanessa_logger-devel >= 0.0.4

%description devel
Headers required to develop against vanessa_adt.

%description devel -l pl
Pliki nag³ówkowe potrzebne do tworzenia prógramów z u¿yciem
vanessa_adt.

%package static
Summary:	Static libraries for vanessa_adt development
Summary(pl):	Biblioteki statyczne vanessa_adt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries to develop against vanessa_adt.

%description static -l pl
Biblioteki statyczne vanessa_adt.

%prep
%setup -q

%build
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
