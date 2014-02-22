Summary:	PLD Linux guest OS definition for Ganeti
Name:		ganeti-instance-poldek
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://github.com/janekr/%{name}/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	ee3b30d4d24a84df462d60c8ffb1c33f
BuildRequires:	rpmbuild(macros) >= 1.647
Requires:	blockdev
Requires:	coreutils
Requires:	poldek
Requires:	dump
Requires:	e2fsprogs
Requires:	ganeti
Requires:	kpartx
Requires:	losetup
Requires:	mount
Requires:	sed
Requires:	tar
Requires:	util-linux
Requires:	xfsprogs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a guest OS definition for Ganeti.  It will install a minimal
version of PLD via poldek (thus it requires network access).

%prep
%setup -q

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_datadir}/ganeti/os/poldek/variants.list $RPM_BUILD_ROOT%{_sysconfdir}/ganeti/instance-poldek
ln -s %{_sysconfdir}/ganeti/instance-poldek/variants.list $RPM_BUILD_ROOT%{_datadir}/ganeti/os/poldek/variants.list

%{__rm} -r $RPM_BUILD_ROOT/%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/default/ganeti-instance-poldek
%dir %{_sysconfdir}/ganeti/instance-poldek
%dir %{_sysconfdir}/ganeti/instance-poldek/variants
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ganeti/instance-poldek/variants/*.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ganeti/instance-poldek/variants.list
%dir %{_datadir}/ganeti/os/poldek
%{_datadir}/ganeti/os/poldek/common.sh
%attr(755,root,root) %{_datadir}/ganeti/os/poldek/create
%attr(755,root,root) %{_datadir}/ganeti/os/poldek/export
%{_datadir}/ganeti/os/poldek/ganeti_api_version
%attr(755,root,root) %{_datadir}/ganeti/os/poldek/import
%{_datadir}/ganeti/os/poldek/packages*.list
%{_datadir}/ganeti/os/poldek/parameters.list
%attr(755,root,root) %{_datadir}/ganeti/os/poldek/rename
%{_datadir}/ganeti/os/poldek/variants.list
%attr(755,root,root) %{_datadir}/ganeti/os/poldek/verify
