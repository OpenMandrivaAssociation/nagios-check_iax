Summary:	A Nagios plugin to check IAX/IAX2 devices
Name:		nagios-check_iax
Version:	1.0.0
Release:	%mkrel 1
License:	BSD
Group:		Networking/Other
URL:		http://samm.kiev.ua/check_iax/
Source0:	http://samm.kiev.ua/check_iax/check_iax-%{version}.tar.gz
Source1:	check_iax.cfg
Requires:	nagios
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Nagios plugin check_iax allows system administrators to monitor IAX/IAX2
devices.

%prep

%setup -q -n check_iax-%{version}

cp %{SOURCE1} check_iax.cfg
perl -pi -e "s|_LIBDIR_|%{_libdir}|g" check_iax.cfg

%build
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/nagios/plugins.d
install -d %{buildroot}%{_libdir}/nagios/plugins

install -m0755 check_iax %{buildroot}%{_libdir}/nagios/plugins/
install -m0644 *.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/

%post
/sbin/service nagios condrestart > /dev/null 2>/dev/null || :

%postun
/sbin/service nagios condrestart > /dev/null 2>/dev/null || :

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_iax.cfg
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_iax

