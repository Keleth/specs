%define rname plasma-nm
%def_disable libreswan

Name: plasma5-nm
Version: 5.27.11
Release: alt2
Epoch: 1
%K5init

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Plasma applet written in QML for managing network connections
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: NetworkManager-daemon
Requires: NetworkManager-adsl NetworkManager-wifi
Requires: mobile-broadband-provider-info
Requires: qca-qt5-ossl
#Requires: wireguard-tools

Provides: kf5-plasma-nm = %EVR
Obsoletes: kf5-plasma-nm < %EVR

Source: %rname-%version.tar
Source1: plasmanetworkmanagement-kded-ru-add.po
Source10: 01-plasma-nm.js
# ALT
Patch11: alt-old-openconnectauth.patch
Patch12: alt-def-allow-all.patch
Patch13: alt-explain-password-request.patch
Patch14: alt-revert.patch
Patch15: alt-add-bond-xor-mode.patch

# Automatically added by buildreq on Tue Mar 03 2015 (-bi)
# optimized out: cmake cmake-modules elfutils glib2-devel kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libgio-devel libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms pkg-config python-base qt5-base-devel ruby ruby-stdlibs
#BuildRequires: ModemManager-devel extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libmm-qt-devel kf5-networkmanager-qt-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libnm-devel libopenconnect-devel python-module-google qt5-declarative-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-declarative-devel qt5-tools-devel-static
BuildRequires: mobile-broadband-provider-info libqca-qt5-devel
BuildRequires: ModemManager-devel libopenconnect-devel
BuildRequires: libnm-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel kf5-kdesignerplugin-devel
#kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-kpackage-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-plasma-framework-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-modemmanager-qt-devel kf5-networkmanager-qt-devel kf5-kcmutils-devel

%description
Plasma applet and editor for managing your network connections in KDE using
the default NetworkManager service.

%package maxi
Group: Graphical desktop/KDE
Summary: %name maximum package
BuildArch: noarch
Requires: %name
Requires: %name-connect-mobile
Requires: %name-connect-openvpn
Requires: %name-connect-fortisslvpn
Requires: %name-connect-vpnc
Requires: %name-connect-openconnect
Requires: %name-connect-libreswan
Requires: %name-connect-strongswan
Requires: %name-connect-iodine
Requires: %name-connect-l2tp
Requires: %name-connect-pptp
Requires: %name-connect-sstp
Requires: %name-connect-ssh
Provides: kf5-plasma-nm-maxi = %EVR
Obsoletes: kf5-plasma-nm-maxi < %EVR
%description maxi
%summary.

%package connect-mobile
Group: Graphical desktop/KDE
Summary: Mobile support for %name
BuildArch: noarch
Requires: %name
Requires: ModemManager NetworkManager-bluetooth NetworkManager-wwan mobile-broadband-provider-info
Provides: kf5-plasma-nm-connect-mobile = %EVR
Obsoletes: kf5-plasma-nm-connect-mobile < %EVR
%description connect-mobile
%summary.

%package connect-openvpn
Group: Graphical desktop/KDE
Summary: OpenVPN support for %name
Requires: %name
Requires: NetworkManager-openvpn
Provides: kf5-plasma-nm-connect-openvpn = %EVR
Obsoletes: kf5-plasma-nm-connect-openvpn < %EVR
%description connect-openvpn
%summary.

%package connect-fortisslvpn
Group: Graphical desktop/KDE
Summary: Fortinet SSLVPN support for %name
Requires: %name
Provides: kf5-plasma-nm-connect-fortisslvpn = %EVR
Obsoletes: kf5-plasma-nm-connect-fortisslvpn < %EVR
%description connect-fortisslvpn
%summary.

%package connect-vpnc
Group: Graphical desktop/KDE
Summary: Vpnc support for %name
Requires: %name
Requires: NetworkManager-vpnc
Provides: kf5-plasma-nm-connect-vpnc = %EVR
Obsoletes: kf5-plasma-nm-connect-vpnc < %EVR
%description connect-vpnc
%summary.

%package connect-openconnect
Group: Graphical desktop/KDE
Summary: OpenConnect support for %name
Requires: %name
Requires: NetworkManager-openconnect
Provides: kf5-plasma-nm-connect-openconnect = %EVR
Obsoletes: kf5-plasma-nm-connect-openconnect < %EVR
%description connect-openconnect
%summary.

%package connect-iodine
Group: Graphical desktop/KDE
Summary: Iodine DNS tunnel support for %name
Requires: %name
Requires: NetworkManager-iodine
Provides: kf5-plasma-nm-connect-iodine = %EVR
Obsoletes: kf5-plasma-nm-connect-iodine < %EVR
%description connect-iodine
%summary.

%package connect-libreswan
Group: Graphical desktop/KDE
Summary: Openswan support for %name
Requires: %name
%if_enabled libreswan
Requires: NetworkManager-libreswan
%endif
Obsoletes: plasma5-nm-connect-openswan < %EVR
%description connect-libreswan
%summary.

%package connect-strongswan
Group: Graphical desktop/KDE
Summary: Strongswan support for %name
Requires: %name
Requires: NetworkManager-strongswan
Provides: kf5-plasma-nm-connect-strongswan = %EVR
Obsoletes: kf5-plasma-nm-connect-strongswan < %EVR
%description connect-strongswan
%summary.

%package connect-l2tp
Group: Graphical desktop/KDE
Summary: L2TP support for %name
Requires: %name
Requires: NetworkManager-l2tp
Provides: kf5-plasma-nm-connect-l2tp = %EVR
Obsoletes: kf5-plasma-nm-connect-l2tp < %EVR
%description connect-l2tp
%summary.

%package connect-pptp
Group: Graphical desktop/KDE
Summary: PPTP support for %name
Requires: %name
Requires: NetworkManager-pptp
Provides: kf5-plasma-nm-connect-pptp = %EVR
Obsoletes: kf5-plasma-nm-connect-pptp < %EVR
%description connect-pptp
%summary.

%package connect-sstp
Group: Graphical desktop/KDE
Summary: SSTP support for %name
Requires: %name
Requires: NetworkManager-sstp
Provides: kf5-plasma-nm-connect-sstp = %EVR
Obsoletes: kf5-plasma-nm-connect-sstp < %EVR
%description connect-sstp
%summary.

%package connect-ssh
Group: Graphical desktop/KDE
Summary: SSH support for %name
Requires: %name
Requires: ssh-provider-openssh-clients NetworkManager-ssh
Provides: kf5-plasma-nm-connect-ssh = %EVR
Obsoletes: kf5-plasma-nm-connect-ssh < %EVR
%description connect-ssh
%summary.

%prep
%setup -n %rname-%version
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

cat %SOURCE1 >> po/ru/plasmanetworkmanagement-kded.po

%build
%K5build

%install
%K5install
%K5install_move data kcm_networkmanagement

install -m0644 -p -D %SOURCE10 %buildroot/%_K5data/plasma/updates/01-plasma-nm.js

%find_lang %name --all-name

%files -f %name.lang
%dir %_K5plug/plasma/network/
%dir %_K5plug/plasma/network/vpn/
%doc LICENSES/*
%_K5lib/libplasmanm_*.so
%_K5plug/kf5/kded/networkmanagement.so
%_K5plug/plasma/kcms/systemsettings_qwidgets/*networkmanagement*.so
%_K5qml/org/kde/plasma/networkmanagement/
%_K5xdgapp/*networkmanagement*.desktop
%_K5data/*networkmanagement/
%_kf5_data/plasma/plasmoids/org.kde.plasma.networkmanagement/
%_K5data/plasma/updates/*nm*
%_K5notif/networkmanagement.notifyrc
%_datadir/qlogging-categories5/*.*categories
%_datadir/metainfo/*.xml

%files maxi
%files connect-mobile

%files connect-iodine
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_iodineui.so
%files connect-openvpn
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_openvpnui.so
%files connect-fortisslvpn
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so
%files connect-vpnc
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_vpncui.so
%files connect-openconnect
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_openconnect_*.so
%files connect-libreswan
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_libreswanui.so
%files connect-strongswan
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_strongswanui.so
%files connect-l2tp
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_l2tpui.so
%files connect-pptp
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_pptpui.so
%files connect-sstp
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_sstpui.so
%files connect-ssh
%_K5plug/plasma/network/vpn/plasmanetworkmanagement_sshui.so

%changelog
* Sat Apr 27 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1:5.27.11-alt2
- add xor mode for Bond (closes: 48393)

* Thu Mar 07 2024 Sergey V Turchin <zerg@altlinux.org> 1:5.27.11-alt1
- new version

* Thu Dec 07 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.10-alt1
- new version

* Thu Nov 02 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.9-alt2
- dont force alternate placement

* Thu Oct 26 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.9-alt1
- new version

* Fri Oct 20 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.8-alt2
- update requires

* Tue Sep 12 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.8-alt1
- new version

* Tue Aug 01 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.7-alt1
- new version

* Wed Jul 05 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.6-alt1
- new version

* Wed May 10 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.5-alt1
- new version

* Thu Apr 06 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.4-alt1
- new version

* Thu Mar 16 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.3-alt1
- new version

* Tue Feb 28 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.2-alt1
- new version

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.26.5-alt1
- new version

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.4-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.6-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.4-alt1
- new version

* Mon Mar 21 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.23.5-alt2
- require NetworkManager-strongswan (closes: 42179)

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.2-alt1
- new version

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.4-alt1
- new version

* Fri Jul 16 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.3-alt2
- fix package

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.2-alt1
- new version

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.5-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.4-alt1
- new version

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.3-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.20.5-alt1
- new version

* Mon Dec 21 2020 Oleg Solovyov <mcpain@altlinux.org> 1:5.20.4-alt2
- Fix bold text on wireless passphrase request dialog

* Wed Dec 02 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.20.4-alt1
- new version

* Wed Oct 28 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.20.2-alt1
- new version

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.5-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.4-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.3-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.2-alt1
- new version

* Thu Jun 18 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.5-alt2
- don't require ssh module

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.5-alt1
- new version

* Mon Apr 27 2020 Oleg Solovyov <mcpain@altlinux.org> 1:5.18.4-alt2
- fix wifi password asking

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.4-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.3-alt1
- new version

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.1-alt1
- new version

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.17.5-alt1
- new version

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.4-alt1
- new version

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.0-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.3-alt1
- new version

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt1
- new version

* Tue May 07 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.15.4-alt2
- password dialog: validate wireless keys

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.4-alt1
- new version

* Thu Apr 25 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt5
- applet: fix disappearing wireless connections

* Thu Apr 04 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt4
- fix package

* Thu Apr 04 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt3
- fix package

* Wed Apr 03 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt2
- password dialog: explain why password is requested

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.12.8-alt1
- new version

* Thu Dec 20 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.7-alt2
- fix to build with networkmanager

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.7-alt1
- new version

* Wed Aug 08 2018 Ivan Razzhivin <underwit@altlinux.org> 1:5.12.6-alt3
- fix a text label in the password dialog

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.6-alt2
- fix version

* Tue Jul 03 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2
- update russian translation

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2
- renamed kf5-plasma-nm -> plasma5-nm

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1
- new version

* Mon Dec 04 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt2
- store passwords for all users by default

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1
- new version

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1
- new version

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1
- new version

* Tue Apr 18 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt2
- fix compile with old openconnect

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt0.M80P.1
- build for M80P

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Mon Oct 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1.M80P.1
- build for M80P

* Mon Oct 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt2
- rebuild with new openconnect

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

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
