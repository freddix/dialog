%define		ver   1.1
%define		sdate 20120706
#
Summary:	A program to build tty dialog boxes
Name:		dialog
Version:	%{ver}.%{sdate}
Release:	11
Epoch:		1
License:	LGPL v2.1
Group:		Applications/Terminal
Source0:	ftp://invisible-island.net/dialog/%{name}-%{ver}-%{sdate}.tgz
# Source0-md5:	2e538305977178eb085a9859511c299d
Patch0:		%{name}-link.patch
URL:		http://invisible-island.net/dialog/dialog.html
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dialog is a utility that allows you to build user interfaces in a TTY
(text mode only). You can call dialog from within a shell script to
ask the user questions or present with choices in a more user friendly
manner.

%package devel
Summary:	Libraries and headers files for dialog
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Libraries and header files for dialog.

%prep
%setup -qn %{name}-%{ver}-%{sdate}
%patch0 -p1

%build
%configure \
	--disable-static	\
	--enable-nls		\
	--with-libtool		\
	--with-ncursesw
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/dialog
%attr(755,root,root) %ghost %{_libdir}/libdialog.so.10
%attr(755,root,root) %{_libdir}/libdialog.so.*.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dialog-config
%attr(755,root,root) %{_libdir}/libdialog.so
%{_libdir}/libdialog.la
%{_includedir}/*.h
%{_mandir}/man3/dialog.3*

