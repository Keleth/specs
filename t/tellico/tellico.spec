%define _unpackaged_files_terminate_build 1

Name: 	 tellico
Version: 3.5.4
Release: alt1

Summary: A collection manager for KDE
License: GPL-2.0+
Group:   Graphical desktop/KDE
Url:     http://tellico-project.org/
VCS:	 https://invent.kde.org/office/tellico.git

ExcludeArch: armh ppc64le

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt5-declarative-devel
BuildRequires: kde5-libkcddb-devel
BuildRequires: kde5-libksane-devel
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-kfilemetadata-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-khtml-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-kjs-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel
BuildRequires: libdiscid-devel
BuildRequires: libexempi-devel
BuildRequires: libpoppler-qt5-devel
BuildRequires: libtag-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: libyaz-devel
BuildRequires: qimageblitz5-devel
BuildRequires: qjson-qt5-devel
%ifarch %qt5_qtwebengine_arches
BuildRequires: qt5-webengine-devel
%else
BuildRequires: kf5-khtml-devel
%endif
BuildRequires: qt5-charts-devel
BuildRequires: libcdio-devel

%ifarch %qt5_qtwebengine_arches
%define use_khtml FALSE
%else
%define use_khtml TRUE
%endif

%description
Tellico is a KDE application for organizing your collections. It
provides default templates for books, bibliographies, videos, music,
video games, coins, stamps, trading cards, comic books, and wines.

%prep
%setup

%build

%K5init no_altplace
%K5build -DUSE_KHTML:BOOL=%use_khtml

%install
%K5install

# fix python shebangs
find %buildroot -type f -print0 |
      xargs -r0 grep -lZ '^#![[:space:]]*%_bindir/.*python$' -- |
      xargs -r0 sed -E -i '1 s@^(#![[:space:]]*)%_bindir/(env[[:space:]]+)?python$@\1%__python3@'

%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS README.md
%_K5bin/*
%_datadir/%name
%_K5xdgapp/*.desktop
%_K5icon/hicolor/*/apps/%name.png
%_K5icon/hicolor/*/mimetypes/application-x-%name.png
%_datadir/kconf_update/*
%_K5cfg/*.kcfg
%_K5xdgconf/%{name}*
%_K5xdgmime/%name.xml
%_K5xmlgui/%name
%_datadir/metainfo/org.kde.tellico.appdata.xml
%_datadir/knsrcfiles/tellico-*.knsrc

%changelog
* Fri Mar 29 2024 Andrey Cherepanov <cas@altlinux.org> 3.5.4-alt1
- New version.

* Wed Jan 03 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 3.5.3-alt2
- NMU: use KHTML on architectures where qt5-webengine is not available.
  Build for more architectures (including LoongArch).

* Wed Jan 03 2024 Andrey Cherepanov <cas@altlinux.org> 3.5.3-alt1
- New version.

* Mon Oct 23 2023 Andrey Cherepanov <cas@altlinux.org> 3.5.2-alt1
- New version.

* Tue Jul 04 2023 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version.

* Tue May 16 2023 Andrey Cherepanov <cas@altlinux.org> 3.5-alt1
- New version.

* Tue Jan 24 2023 Andrey Cherepanov <cas@altlinux.org> 3.4.6-alt1
- New version.

* Wed Nov 16 2022 Andrey Cherepanov <cas@altlinux.org> 3.4.5-alt1
- New version.

* Thu Feb 17 2022 Andrey Cherepanov <cas@altlinux.org> 3.4.4-alt1
- New version.

* Mon Jan 03 2022 Andrey Cherepanov <cas@altlinux.org> 3.4.3-alt1
- New version.

* Tue Nov 09 2021 Andrey Cherepanov <cas@altlinux.org> 3.4.2-alt1
- New version.

* Thu Jun 03 2021 Arseny Maslennikov <arseny@altlinux.org> 3.4.1-alt1.1
- NMU: spec: use KF5 macros.

* Mon May 10 2021 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version.
- Enable localization.
- Package knsrc files.

* Mon Mar 15 2021 Andrey Cherepanov <cas@altlinux.org> 3.4-alt1
- New version.

* Fri Feb 26 2021 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt1
- New version.

* Thu Nov 26 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.4-alt1
- New version.

* Thu Sep 17 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.3-alt1
- New version.

* Sat Aug 22 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.2-alt1
- New version.

* Mon Jun 01 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- New version.
- Fix License tag according to SPDX.

* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 3.3-alt1
- New version.

* Mon Dec 02 2019 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- New version.
- Package appdata file.

* Wed Jul 10 2019 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version.

* Sun Jun 02 2019 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- New version.
- Remove old libraries required Qt4.
- Build only for Intel.

* Thu Dec 20 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.4-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt1
- New version.

* Wed Mar 28 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version.

* Tue Jan 16 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- New version.

* Fri Nov 03 2017 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- New version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 3.0.2-alt1.1
- NMU: rebuild with new libkcddb
- NMU: clean build requires

* Tue Mar 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version

* Tue Feb 21 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- new version 3.0.1

* Sun Jan 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.0-alt1
- new version 3.0 for KF5

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.11-alt2
- Build without Nepomuk support

* Tue Dec 08 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.11-alt1
- New version

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 2.3.10-alt2
- rebuild with new libyaz 5.13

* Sun Mar 08 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.10-alt1
 Initial build in Sisyphus
