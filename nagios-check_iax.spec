Summary:	A Nagios plugin to check IAX/IAX2 devices
Name:		nagios-check_iax
Version:	1.0.0
Release:	5
License:	BSD
Group:		Networking/Other
URL:		https://samm.kiev.ua/check_iax/
Source0:	http://samm.kiev.ua/check_iax/check_iax-%{version}.tar.gz
Requires:	nagios
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Nagios plugin check_iax allows system administrators to monitor IAX/IAX2
devices.

%prep
%setup -q -n check_iax-%{version}

%build
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/nagios/plugins.d
install -d %{buildroot}%{_libdir}/nagios/plugins

install -m0755 check_iax %{buildroot}%{_libdir}/nagios/plugins/
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_iax.cfg <<'EOF'
define command {
	command_name	check_iax
	command_line	%{_libdir}/nagios/plugins/check_iax -H $HOSTADDRESS$ -w 100 -c 500
}
EOF

%if %mdkversion < 200900
%post
/sbin/service nagios condrestart > /dev/null 2>/dev/null || :

%postun
/sbin/service nagios condrestart > /dev/null 2>/dev/null || :
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_iax.cfg
%{_libdir}/nagios/plugins/check_iax


%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdv2011.0
+ Revision: 620458
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2010.0
+ Revision: 440200
- rebuild

* Mon Dec 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-2mdv2009.1
+ Revision: 314633
- use a herein document for configuration
- reply on filetrigger for reloading nagios

* Sun Jul 27 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2009.0
+ Revision: 250423
- import nagios-check_iax


* Sun Jul 27 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2009.0
- initial Mandriva package
