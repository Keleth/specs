%define variant alt-education
%define Variant ALT Education

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 10.2
Release: alt5

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Conflicts: %(for n in %variants ; do [ "$n" = %name ] || echo -n "$n "; done)

BuildRequires(pre):rpm-build-licenses
BuildRequires: publican
BuildRequires: perl-podlators
BuildRequires: libwebp-tools

%description
%Variant documentation.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docsinstalldir install
ln -s $(relative %_docsinstalldir %_documentationdir) %buildroot%_documentationdir
sed -i 's/src="images\/\(.*\).png"/src="images\/\1.webp"/g' %buildroot%_docsinstalldir/ru-RU/index.html
for file in %buildroot%_docsinstalldir/ru-RU/images/*.png; do cwebp $file -o %buildroot%_docsinstalldir/ru-RU/images/$(basename $file .png).webp -quiet && rm $file; done

%files
%_docsinstalldir
%_documentationdir

%changelog
* Thu Apr 18 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt5
- small improvements
- fix some typos (closes: 48145)
- fix name partition (closes: 48207)
- update screen

* Thu Oct 12 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt4
- update educational-resources: nextcloud, veyon, moodle (closes: 47958)
- fix typo

* Wed Oct 04 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt3
- update support
- update screen

* Sun Oct 01 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt2
- update recoll

* Fri Sep 22 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt1
- update to ALT Education 10.2

* Mon Nov 07 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt3
- update to ALT Education 10.1

* Tue Sep 13 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt2
- update to ALT Education 10.1rc

* Fri May 06 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt1
- update to ALT Education 10.1Beta

* Wed Apr 06 2022 Elena Mishina <lepata@altlinux.org> 10.0-alt4
- update documentation
- add geany, idle3

* Wed Dec 08 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt3
- update to ALT Education 10.0

* Mon Nov 15 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt2
- update to ALT Education 10.0rc
- reduce package size

* Wed Oct 13 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt1
- update to ALT Education 10.0Beta

* Wed Apr 28 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt2
- update to latest public distr
- add alterator-update-kernel, synfigstudio

* Thu Apr 15 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt1
- update to ALT Education 9.2Beta
- educational-resources: add veyon, trik-studio
- system-management: add group-policy, network configuration
- install-packages-advanced: add epm

* Thu Oct 15 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt2
- update thunderbird
- added recoll settings

* Tue Jul 14 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt1
- update to latest public distr of ALT Education 9.1

* Tue Jun 30 2020 Elena Mishina <lepata@altlinux.org>9.0-alt3
Beta version of ALT Education 9.1
- added jitsi-meet
- added grub-customizer

* Mon Oct 21 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt2
- added recoll
- fix typo

* Tue Oct 15 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to latest public distr of ALT Education 9.0

* Wed Jul 31 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt2
Beta version of ALT Education 9.0

* Tue Jun 25 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
Alpha version of ALT Education 9.0

* Wed Feb 13 2019 Elena Mishina <lepata@altlinux.org> 8.2-alt5
- added moodle, mediawiki, owncloud, rujel
- added install fonts (closes: 35820)

* Tue Jan 15 2019 Elena Mishina <lepata@altlinux.org> 8.2-alt4
- added kde
- added boot option

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- update documentation

* Mon Dec 4 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- updated to 8.2

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt4
- fix typo
- update documentation

* Fri Feb 10 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt3
- update Conflicts list
- update documentation

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt2
- updated to latest public distr

* Fri Oct 28 2016 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt1
- updated to 8.1
- added 'guest session' description

* Sun Aug 07 2016 Artem Zolochevskiy <azol@altlinux.ru> 8.0-alt2
- removed obsolete stuff

* Thu Aug 04 2016 Artem Zolochevskiy <azol@altlinux.ru> 8.0-alt1
- initial build for Sisyphus
