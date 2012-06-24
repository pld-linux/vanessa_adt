Summary:	Library of Abstract Data Types
Name:		vanessa_adt
Version:	0.0.2
Release:	1
License:	LGPL
Group:		Libraries
Group(cs):	Knihovny
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(ja):	�饤�֥��
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����
Source0:	ftp://vergenet.net/pub/vanessa_adt/vanessa_adt/%{name}-%{version}.tar.gz
URL:		http://vanessa.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	sed
Provides:	%{name}-%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Library of Abstract Data Types (ADTs) that may be useful. Includes
queue, dynamic array and key value ADT.

%package devel
Summary:	Headers and static libraries for development
Group:		Development/Libraries
Group(cs):	V�vojov� prost�edky/Knihovny
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(ja):	��ȯ/�饤�֥��
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-%{version}

%description devel
Headers and static libraries required to develop against vanessa_adt.


%prep
%setup -q

%build
sed -e s/AC_PROG_RANLIB/AC_PROG_LIBTOOL/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in

rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
CFLAGS="${RPM_OPT_FLAGS}"
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}/{etc,%{_prefix}/{lib,bin,doc}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README ChangeLog NEWS TODO

%clean
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.*a
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.so.0
%attr(644,root,root) %{_includedir}/*.h
%doc *.gz
