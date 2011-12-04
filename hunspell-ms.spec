Name: hunspell-ms
Summary: Malay hunspell dictionaries
%define upstreamid 20050117
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/ms_MY.zip
Group: Applications/Text
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GFDL and GPL+
BuildArch: noarch

Requires: hunspell

%description
Malay hunspell dictionaries.

%prep
%setup -q -c -n hunspell-ms

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ms_MY_aliases="ms_BN"
for lang in $ms_MY_aliases; do
        ln -s ms_MY.aff $lang.aff
        ln -s ms_MY.dic $lang.dic
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_ms_MY.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20050117-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050117-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050117-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 0.20050117-2
- clarify license, the .aff apparently is GPL+ while the wordlist is GFDL

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20050117-1
- initial version
