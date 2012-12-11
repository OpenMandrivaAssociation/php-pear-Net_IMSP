%define prj    Net_IMSP

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          php-pear-Net_IMSP
Version:       0.0.6
Release:       %mkrel 3
Summary:       Net_IMSP
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear
Requires:      php-pear-channel-horde
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
Provides an API into an IMSP server for Addressbooks and Options

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Net/IMSP
%{peardir}/Net/IMSP.php
%{peardir}/Net/IMSP/Auth.php
%{peardir}/Net/IMSP/Auth/imtest.php
%{peardir}/Net/IMSP/Auth/plaintext.php
%{peardir}/Net/IMSP/Auth/cram_md5.php
%{peardir}/Net/IMSP/Book.php
%{peardir}/Net/IMSP/Utils.php
%{peardir}/Net/IMSP/Options.php


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.6-3mdv2011.0
+ Revision: 613728
- the mass rebuild of 2010.1 packages

* Fri Mar 19 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.6-2mdv2010.1
+ Revision: 525161
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased rel ver to 2

* Sat Feb 27 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.6-1mdv2010.1
+ Revision: 512489
- added Requires: php-pear-channel-horde
- added: Requires(pre): %%{_bindir}/pear
  added: Requires:      php-pear
  added: BuildRequires: php-pear
  added: BuildRequires: php-pear-channel-horde
- import php-pear-Net_IMSP


