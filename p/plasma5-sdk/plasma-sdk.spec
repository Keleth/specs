%define rname plasma-sdk
%filter_from_requires /inkscape/d

Name: plasma5-sdk
Version: 5.27.11
Release: alt2
%K5init

Group: Development/KDE and QT
Summary: KDE Workspace 5 Applications useful for Plasma Development
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf5-kirigami
Provides: kf5-plasma-sdk = %EVR
Obsoletes: kf5-plasma-sdk < %EVR

Source: %rname-%version.tar
Patch: alt-cuttlefish-external-open.patch
Patch1: alt-fix-lnf-double-create.patch

# Automatically added by buildreq on Tue Apr 28 2015 (-bi)
# optimized out: cmake cmake-modules elfutils kf5-attica-devel libEGL-devel libGL-devel libcloog-isl4 libdbusmenu-qt52 libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base qt5-base-devel qt5-declarative-devel ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-kpackage-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libdb4-devel python-module-google qt5-svg-devel qt5-webkit-devel rpm-build-gir rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-svg-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-kpackage-devel kf5-kparts-devel kf5-kservice-devel
BuildRequires: kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel kf5-kdbusaddons-devel kf5-kitemmodels-devel
BuildRequires: kf5-kdoctools-devel kf5-syntax-highlighting-devel

%description
Applications useful for Plasma Development.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-plasma-sdk-common = %EVR
Obsoletes: kf5-plasma-sdk-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kf5-plasma-sdk-devel = %EVR
Obsoletes: kf5-plasma-sdk-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5plasma-sdk
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5plasma-sdk
KF5 library


%prep
%setup -n %rname-%version
%patch -p1
%patch1 -p1

%build
%K5build \
    #
#    -DPLASMATE_BUILD_WITH_KDEVPLATFORM=ON \

%install
%K5install
%K5install_move data kpackage
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/*
%_K5xdgapp/*.desktop
%_K5plug/ktexteditor/
%_kf5_data/plasma/shells/*/
%_K5data/kpackage/
%_K5srv/*.desktop
%_datadir/zsh/site-functions/_*
%_datadir/metainfo/*.xml

%changelog
* Tue May 07 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 5.27.11-alt2
- fix Open with External Program option in cuttlefish (Closes: 45136)
  fix lookandfeelexplorer creating theme called twice (Closes: 46601)

* Thu Mar 07 2024 Sergey V Turchin <zerg@altlinux.org> 5.27.11-alt1
- new version

* Thu Dec 07 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.10-alt1
- new version

* Thu Nov 02 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.9-alt2
- dont force alternate placement

* Thu Oct 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.9-alt1
- new version

* Tue Sep 12 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.8-alt1
- new version

* Tue Aug 01 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.7-alt1
- new version

* Wed Jul 05 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.6-alt1
- new version

* Wed May 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.5-alt1
- new version

* Thu Apr 06 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.4-alt1
- new version

* Thu Mar 16 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.3-alt1
- new version

* Tue Feb 28 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.2-alt1
- new version

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt1
- new version

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.4-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.2-alt1
- new version

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.4-alt1
- new version

* Fri Jul 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt2
- fix package

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- new version

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt1
- new version

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt1
- new version

* Wed Feb 17 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt2
- update build requries

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt1
- new version

* Wed Dec 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.4-alt1
- new version

* Wed Oct 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.2-alt1
- new version

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.5-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.4-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.3-alt1
- new version

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- new version

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.17.5-alt1
- new version

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt1
- new version

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt1
- new version

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1%ubt
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1%ubt
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1%ubt
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1%ubt
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2%ubt
- renamed kf5-plasma-sdk -> plasma5-sdk

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1%ubt
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1%ubt
- new version

* Mon Aug 21 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt2%ubt
- fix requires

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1%ubt
- new version

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1%ubt
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1%ubt
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
