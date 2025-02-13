%define brand alt
%define Brand ALT
%define theme education
%define Theme Education
%define codename FalcoVespertinus
%define status ALPHA
%define status_en ALPHA
%define flavour %brand-%theme

%define gtk_theme Breeze-Education
%define kde_theme Breeze
%define icon_theme Papirus-Edu
%define window_theme Smoothwall-Breeze

# Enable compositing on ix86 and x86_64 only
%ifarch %ix86 x86_64
%define xfwm4_compositing true
%else
%define xfwm4_compositing false
%endif

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

Name: branding-%flavour
Version: 11.0
Release: alt0.1.alpha

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel fribidi

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL-2.0+

%define distro_name ALT Education %version%status_en
%define distro_name_ru Альт Образование %version%status
%define distro_logo alt-education-desktop

%description
Distro-specific packages with design and texts for %distro_name.

%description -l ru_RU.UTF-8
Пакеты оформления для дистрибутива %distro_name_ru.

%package bootloader
Group:   System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
Summary(ru_RU.UTF-8): Тема для экрана выбора вариантов загрузки (lilo и syslinux)
License: GPL-2.0

Requires(pre): coreutils
%branding_add_conflicts %flavour bootloader

%description bootloader
Here you find the graphical boot logo for %distro_name.
Suitable for both lilo and syslinux.

%description bootloader -l ru_RU.UTF-8
В данном пакете находится тема для экрана выбора вариантов загрузки (lilo и syslinux)
для дистрибутива %distro_name_ru.

%package bootsplash
Summary:  Theme for splash animations during bootup
Summary(ru_RU.UTF-8): Тема для экрана загрузки для дистрибутива %distro_name_ru
License:  Distributable
Group:    System/Configuration/Boot and Init
Provides: plymouth-theme-%theme
Requires: plymouth-theme-bgrt-alt
Requires: plymouth-plugin-script
Requires: plymouth-plugin-label
Requires: fonts-ttf-dejavu
Requires(pre): plymouth

%branding_add_conflicts %flavour bootsplash

%description bootsplash
This package contains graphics for boot process for %distro_name
(needs console splash screen enabled).

%description bootsplash -l ru_RU.UTF-8
В данном пакете находится тема для экрана загрузки для дистрибутива
%distro_name_ru.

%package alterator
Summary: Design for alterator for %distro_name
Summary(ru_RU.UTF-8): Тема для "Центра управления системой" и QT для дистрибутива %distro_name_ru
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Requires: fonts-ttf-roboto

%branding_add_conflicts %flavour alterator
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop design-altertor-browser-server branding-altlinux-backup-server-alterator
Requires(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for %distro_name.

%description alterator -l ru_RU.UTF-8
В данном пакете находится тема для "Центра управления системой" (Alterator)
и модулей библиотеки QT для дистрибутива %distro_name_ru.

%package graphics
Summary: Design for %distro_name
Summary(ru_RU.UTF-8): Тема для дистрибутива %distro_name_ru
License: Different licenses
Group: Graphics
BuildArch: noarch
Provides: design-graphics-%theme
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix

Requires(post,preun): alternatives >= 0.2
%branding_add_conflicts %flavour graphics

%description graphics
This package contains some graphics for %distro_name design.

%description graphics -l ru_RU.UTF-8
В данном пакете находится необходимые графические элементы для дистрибутива
%distro_name_ru.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release

%package release
BuildArch: noarch
Summary:  %distro_name release file
Summary(ru_RU.UTF-8): Описание дистрибутива %distro_name_ru
License:  Distributable
Group:    System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list
%branding_add_conflicts %flavour release
Requires: pam-limits-desktop
Requires: alt-os-release

%description release
%distro_name release file.

%description release -l ru_RU.UTF-8
В данном пакете находится описание дистрибутива %distro_name_ru.

%package notes
BuildArch: noarch
Provides:  alt-license-theme = %version alt-notes-%theme
Summary:   Distribution license and release notes
Summary(ru_RU.UTF-8): Лицензия и дополнительные сведения для дистрибутива %distro_name_ru
License:   Distributable
Group:     Documentation
%branding_add_conflicts %flavour notes

%description notes
Distribution license and release notes

%description notes -l ru_RU.UTF-8
В данном пакете находится лицензия и дополнительные сведения
для дистрибутива %distro_name_ru.

%package kde-settings
BuildArch: noarch
Summary: KDE settings for %distro_name (for KDE4 and KF5)
License: Distributable
Group:   Graphical desktop/KDE
Requires(pre): %name-graphics
Requires: %name-graphics = %EVR
Requires: kde5-konsole-colorscheme-SolarizedPastel
Requires: papirus-icon-theme
Requires: gtk-theme-breeze-education
Requires: plasma5-breeze
Requires: fonts-ttf-liberation
Requires: fonts-ttf-google-droid-sans-mono
Requires: document-templates
Provides: branding-%flavour-kde4-settings = %version-%release
Obsoletes: branding-%flavour-kde4-settings < %version-%release
%branding_add_conflicts %flavour kde-settings
%branding_add_conflicts %flavour kde4-settings

%description kde-settings
KDE settings for %distro_name (for KDE4 and KF5)

%package xfce-settings
Summary: Default settings for XFCE for %distro_name
License: Distributable
Group: Graphical desktop/XFce
Requires: etcskel
Requires: fonts-ttf-liberation
Requires: fonts-ttf-google-droid-sans-mono
Requires: fonts-ttf-google-noto-sans
Requires: gnome-icon-theme
# Specified themes
Requires: papirus-icon-theme
Requires: gtk-theme-breeze-education
Requires: xfwm4-theme-Smoothwall-Breeze
Requires(post): lightdm-gtk-greeter
# XFCE plugins
Requires: xfce4-whiskermenu-plugin
Requires: xfce4-pulseaudio-plugin
Requires: branding-%brand-%theme-graphics
Requires(pre): libgtk+2
%branding_add_conflicts %flavour xfce-settings

%description xfce-settings
XFCE settings for %distro_name

%package fvwm-settings
BuildArch: noarch
Summary: FVWM2 settings for %distro_name
License: Distributable
Group:   Graphical desktop/FVWM based
Requires: altlinux-freedesktop-menu-gnomish-menu
%branding_add_conflicts %flavour fvwm-settings

%description fvwm-settings
FVWM2 settings for %distro_name

%package mate-settings
BuildArch: noarch
Summary: MATE settings for %distro_name
License: Distributable
Group:   Graphical desktop/GNOME
Requires: beesu
Requires: dconf
# Specified themes
Requires: papirus-icon-theme
Requires: gtk-theme-breeze-education
#
%branding_add_conflicts %flavour mate-settings
Requires(post): lightdm-gtk-greeter
Requires(post): libgio

%description mate-settings
MATE settings for %distro_name

%package slideshow
Summary: Slideshow for %distro_name installer
Summary(ru_RU.UTF-8): Изображения для организации "слайдшоу" в установщике дистрибутива %distro_name_ru
License: Distributable
Group: System/Configuration/Other
BuildArch: noarch
%branding_add_conflicts %flavour slideshow

%description slideshow
Slideshow for %distro_name installer.

%description slideshow -l ru_RU.UTF-8
В данном пакете находятся изображения для организации "слайдшоу" в установщике
дистрибутива %distro_name_ru.

%package indexhtml
BuildArch: noarch
Summary:  HTML welcome page for %distro_name
Summary(ru_RU.UTF-8): Стартовая страница для дистрибутива %distro_name_ru
License:  distributable
Group:    System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
%branding_add_conflicts %flavour indexhtml

Requires: xdg-utils
Requires: docs-alt-%theme
Requires: shared-desktop-icons
Requires(post): indexhtml-common

%description indexhtml
%distro_name welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
%distro_name_ru.

%package menu
Summary: Menu for %distro_name
License: Distributable
Group: Graphical desktop/Other
Requires(pre): altlinux-freedesktop-menu-common
Requires: altlinux-freedesktop-menu-common
%branding_add_conflicts %flavour menu

%description menu
Menu for %distro_name

%package system-settings
BuildArch: noarch
Summary: Some system settings for %distro_name
License: GPL-2.0
Group: System/Base
# Really we need lightdm only, but it can pull another greeter.
Requires: lightdm-gtk-greeter
%branding_add_conflicts %flavour system-settings

%description system-settings
Some system settings for %distro_name.

%prep
%setup -n branding
%ifarch %e2k %ix86
# 2021: no chromium port available
grep -rl chromium xfce-settings/etcskel/.config/xfce4/panel |
	xargs -r -- sed -i 's,chromium,firefox,g;s,Chromium,Firefox,g'
%endif
%ifarch %e2k
# cf. rm#115880
sed -i 's,#alt-education,&-e2k,' indexhtml/index-*.html.in
%endif

%build
autoconf
THEME=%theme CTHEME=%Theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' PRODUCT_LOGO='%distro_logo' CODENAME='%codename' GTK_THEME='%gtk_theme' KDE_THEME='%kde_theme' ICON_THEME='%icon_theme' WINDOW_THEME='%window_theme' XFWM4_COMPOSITING='%xfwm4_compositing' ./configure
make

%install
%makeinstall

# Move os-release to /usr/lib
mkdir -p %buildroot%_libexecdir
mv %buildroot%_sysconfdir/os-release %buildroot%_libexecdir/os-release
touch %buildroot%_sysconfdir/os-release

find %buildroot -name \*.in -delete

%post bootloader
%ifarch %ix86 x86_64 aarch64
. shell-config
shell_config_del /etc/sysconfig/grub2 GRUB_THEME
shell_config_del /etc/sysconfig/grub2 GRUB_BACKGROUND
%endif

%post indexhtml
%_sbindir/indexhtml-update

%post system-settings
#chown _ldm:_ldm %_localstatedir/ldm/.pam_environment
sed -i '/pam_env\.so/ {
		/user_readenv/ b
		s/pam_env\.so/pam_env.so user_readenv=1/ }
' %_sysconfdir/pam.d/lightdm-greeter

%files bootloader

#bootsplash
%post bootsplash
%ifarch %ix86 x86_64 aarch64
subst "s/Theme=.*/Theme=bgrt-alt/" /etc/plymouth/plymouthd.conf
%endif

%post mate-settings
subst 's/^#\?theme-name=.*/theme-name=%gtk_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?icon-theme-name=.*/icon-theme-name=%icon_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?indicators=.*/indicators=~clock;~spacer;~host;~spacer;~session;~layout;~a11y;~power/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?clock-format=.*/clock-format=%A, %x %H:%M/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas

%post xfce-settings
subst 's/^#\?theme-name=.*/theme-name=%gtk_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?icon-theme-name=.*/icon-theme-name=%icon_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?indicators=.*/indicators=~clock;~spacer;~host;~spacer;~session;~layout;~a11y;~power/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?clock-format=.*/clock-format=%A, %x %H:%M/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
# Set gtk+2 theme for root too
grep -q '^gtk-theme-name' /etc/gtk-2.0/gtkrc || cat /etc/skel/.gtkrc-2.0 >> /etc/gtk-2.0/gtkrc

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
%_iconsdir/hicolor/*/apps/alt-%theme.svg
%exclude %_datadir/design/%theme/icons/system-logo.png

%files bootsplash
%_datadir/design/%theme/icons/system-logo.png

%files release
%_sysconfdir/altlinux-release
%_sysconfdir/fedora-release
%_sysconfdir/redhat-release
%_sysconfdir/system-release
%ghost %_sysconfdir/os-release
%_libexecdir/os-release
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files kde-settings
%_datadir/kf5/konsole/%Theme.profile
/etc/skel/.config/autostart/nm-applet.desktop
/etc/skel/.config/kdeglobals
/etc/skel/.config/konsolerc

%files fvwm-settings
%_sysconfdir/skel/.fvwm2rc

%files mate-settings
%_datadir/glib-2.0/schemas/*.gschema.override

%files xfce-settings
%_sysconfdir/X11/profile.d/zdg-move-templates.sh
/etc/skel/XDG-Templates.skel/
/etc/skel/.wm-select
/etc/skel/.config
%exclude /etc/skel/.config/autostart/nm-applet.desktop
%exclude /etc/skel/.config/konsolerc
%exclude /etc/skel/.config/kdeglobals
/etc/skel/.face
/etc/skel/.gconf
/etc/skel/.gtkrc-2.0
/etc/skel/.local
/etc/skel/.vimrc
/etc/skel/.recoll

%files slideshow
/etc/alterator/slideshow.conf
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %_defaultdocdir/indexhtml/index.html
%_defaultdocdir/indexhtml/*
%_desktopdir/*
%_datadir/kf5/kio_desktop/DesktopLinks/indexhtml.desktop
%attr(0755,root,root) %_datadir/Desktop/indexhtml.desktop
%_iconsdir/hicolor/*/apps/alt-%theme-desktop.svg

%files menu
/usr/share/slinux-style
/etc/xdg/menus/xfce-applications-merged/50-xfce-applications.menu
/usr/share/desktop-directories/altlinux-wine.directory

%files system-settings
%config %_sysconfdir/polkit-1/rules.d/*.rules
#config %_localstatedir/ldm/.pam_environment

%changelog
* Fri Apr 19 2024 Andrey Cherepanov <cas@altlinux.org> 11.0-alt0.1.alpha
- Alpha version of 11.0.
- xfce-settings: use clock applet instead of datetime.
- kde-settings: use themed profile instead of hardcoded.
- bootspash: use plymouth-theme-bgrt-alt.

* Thu Nov 02 2023 Michael Shigorin <mike@altlinux.org> 10.2-alt3.1
- E2K: link to platform-specific distribution manual (rm#115880)

* Tue Sep 26 2023 Andrey Cherepanov <cas@altlinux.org> 10.2-alt3
- menu: hided duplicate menu entries for desktop files from xfce4-settings.

* Mon Aug 28 2023 Andrey Cherepanov <cas@altlinux.org> 10.2-alt2
- os-release: added LOGO to /etc/os-release (ALT #47292).
- xfce-settings: reduced size for power and sound icons on panel.

* Mon Jul 31 2023 Andrey Cherepanov <cas@altlinux.org> 10.2-alt1
- New version.
- Generated well-formed desktop files for hidden menu items.
- Updated Russian license text.

* Wed Jan 18 2023 Andrey Cherepanov <cas@altlinux.org> 10.1-alt8
- Fixed missing chromium for panel icon (ALT #44938).

* Mon Nov 07 2022 Andrey Cherepanov <cas@altlinux.org> 10.1-alt7
- indexhtml: rewrite indexhtml pages.

* Fri Sep 30 2022 Andrey Cherepanov <cas@altlinux.org> 10.1-alt6
- Added wallpapers from ALT Education 9.0.

* Wed Sep 07 2022 Andrey Cherepanov <cas@altlinux.org> 10.1-alt5
- Used Papirus-Edu name for icon theme.

* Wed Sep 07 2022 Andrey Cherepanov <cas@altlinux.org> 10.1-alt4
- Required complete icon pack papirus-icon-theme for all desktop environments.

* Fri Sep 02 2022 Andrey Cherepanov <cas@altlinux.org> 10.1-alt3
- Use icon theme Papirus-Education.

* Wed Jul 27 2022 Andrey Cherepanov <cas@altlinux.org> 10.1-alt2
- xfce-settings: Add search action to thunar menu (thanks sem@).

* Thu Apr 07 2022 Andrey Cherepanov <cas@altlinux.org> 10.1-alt1
- Remove overrided Veyon menu items because they are now localized.
- Remove unsupported Facebook group.
- bootsplash: more narrow and short progressbar.
- slides: update QR-code for Youtube channel.
- xfce-settings: add power-manager-plugin to panel.

* Tue Dec 21 2021 Andrey Cherepanov <cas@altlinux.org> 10.0-alt3
- Add missing TryExec for overrided menu entries.

* Tue Nov 30 2021 Andrey Cherepanov <cas@altlinux.org> 10.0-alt2
- Use gtk theme Breeze-Education.

* Thu Nov 11 2021 Andrey Cherepanov <cas@altlinux.org> 10.0-alt1
- Release 10.0.

* Tue Nov 09 2021 Andrey Cherepanov <cas@altlinux.org> 10.0-alt0.5rc
- 10.0 RC1.

* Wed Oct 20 2021 Andrey Cherepanov <cas@altlinux.org> 10.0-alt0.4.beta
- browser-qt: use widget and icon theme from branding.
- slideshow: update slides.
- kde5: add krunner with calculator and search for applications in menu.
- kde5: disable NumLock at startup.
- xfce-settings: disable CSD for dialogs.
- Set default user face to alt-education-desktop.svg.
- browser-qt: set darkgray color for section link in main window.
- ahttp: adapt css for brand colors.
- indexhtml: set pale background for links in brand color.
- indexhtml: update company logo.
- xfce-settings: decrease clock fonts to fit clock on panel.
- browser-qt: new naming for password show/hide icons.
- browser-qt: set solid color #FF9631 for prosgressbar chunk.
- menu: localize menu items on Russian.

* Fri Oct 08 2021 Andrey Cherepanov <cas@altlinux.org> 10.0-alt0.3.beta
- Use filetrigger from alt-os-release for storing installed release.
- Update slides for ALT Education 10.
- Alterator: use icons from Papirus icon theme and themed colors.
- Set gtk+2 theme for root too.
- browser-qt: use open and closed eye as password entry show/hide icons.
- gfxboot: use wallpaper with logotype.

* Thu Sep 30 2021 Andrey Cherepanov <cas@altlinux.org> 10.0-alt0.2.beta
- Use corparate colors and Roboto font.

* Mon Sep 20 2021 Andrey Cherepanov <cas@altlinux.org> 10.0-alt0.1.beta
- 10.0 beta.
- Store old values in /etc/os-release with ALT_installed_ prefix.

* Thu Aug 05 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt5
- Fix trembling hovered buttons in ahttpd.
- Move templates to package document-templates.

* Mon May 17 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt4
- Replace smplayer by vlc as default player (it has best perfomance on aarch64).

* Wed May 12 2021 Dmitry Terekhin <jqt4@altlinux.org> 9.2-alt3
- Convert xfce-settings to architecture-dependent

* Thu May 06 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt2
- Disable forced icon theme Oxygen for LibreOffice

* Fri Apr 30 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt1
- 9.2 release.

* Thu Apr 29 2021 Michael Shigorin <mike@altlinux.org> 9.2-alt0.9.rc1.1
- E2K: s/chromium/firefox/g

* Tue Apr 27 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt0.9.rc1
- Use Smoothwall-Breeze window theme in XFCE.

* Mon Apr 26 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt0.8.rc1
- 9.2 rc1.
- whisker menu: Use dm-tool to switch users.

* Fri Apr 23 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt0.7.beta
- Do not obsolete packages itself without version.
- Replace gksu by beesu.

* Thu Apr 15 2021 Evgeny Sinelnikov <sin@altlinux.org> 9.2-alt0.6.beta
- Enable boot branding for all platforms

* Thu Apr 15 2021 Evgeny Sinelnikov <sin@altlinux.org> 9.2-alt0.5.beta
- Enable xfce4 compositing on ix86 and x86_64 only

* Thu Apr 15 2021 Evgeny Sinelnikov <sin@altlinux.org> 9.2-alt0.4.beta
- Disable gfxboot and splash building for aarch64

* Wed Apr 14 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt0.3.beta
- Package grub theme for aarch64.

* Mon Apr 12 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt0.2.beta
- installer: add logo to bottom left corner.

* Sat Apr 03 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt0.1.beta
- 9.2 beta
- Fix links and update copyright years in indexhtml.
- Fix overrided menu item for missing application behaviour.

* Tue Jun 30 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt1
- 9.1
- Return idle3 to menu and complete its localization.

* Mon Jun 22 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt0.3
- 9.1rc1.
- menu: add localization to some menu items, hide idle3.

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt0.2
- 9.1beta.
- bootsplash: adjust bar to fit discrete step and complete fill.

* Mon May 25 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt0.1
- 9.1alpha.
- Fix License tag according to SPDX.

* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 9.0-alt3
- Add OpenDocument templates for KDE5.

* Fri Nov 08 2019 Andrey Cherepanov <cas@altlinux.org> 9.0-alt2
- Package system-logo.png for Plymouth.

* Fri Aug 30 2019 Andrey Cherepanov <cas@altlinux.org> 9.0-alt1
- Release 9.0.

* Mon Aug 19 2019 Andrey Cherepanov <cas@altlinux.org> 8.93-alt1
- Beta2.
- Use icon theme Papirus-Light instead of Papirus for more contrast symbol icons.

* Fri Jul 19 2019 Andrey Cherepanov <cas@altlinux.org> 8.92-alt1
- Beta version of ALT Education 9.0.
- xfce-settings: use random screensaver by default.
- plasma: remove empty bookmarks tab in menu.

* Fri Jun 14 2019 Andrey Cherepanov <cas@altlinux.org> 8.91-alt2
- Make progressbar label brighter

* Tue Jun 11 2019 Andrey Cherepanov <cas@altlinux.org> 8.91-alt1
- Replace gnome-system-monitor for xfce4-taskmanager for Ctrl+Alt+Delete.
- Fix Plasma panel: change menu to Kickoff, set distro icon, remove lock and logout icons.

* Tue Apr 30 2019 Andrey Cherepanov <cas@altlinux.org> 8.90-alt1
- Alpha version of ALT Education 9.0.

* Thu Jan 31 2019 Andrey Cherepanov <cas@altlinux.org> 8.2-alt0.M80P.2
- Add Droid fonts used in XFCE.
- Remove overrided desktop file for system-config-printer.
- Fix menu on window key.
- Add xfce4-clipman.desktop.
- Replace standard XFCE menu by Whisker menu, mixer plugin by pulseaudio plugin.
- Simplify panel in XFCE.
- Remove Simply Linux logo and wallpapers.

* Fri May 12 2017 Andrey Cherepanov <cas@altlinux.org> 8.2-alt0.M80P.1
- New release
- Use pam-limits-desktop instead of own limits rules
- Remove altlinux.ru from files

* Fri Oct 21 2016 Andrey Cherepanov <cas@altlinux.org> 8.1-alt0.M80P.1
- Increase release number

* Thu Oct 20 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.5.M80P.1
- Complete Russian localization of menu
- Update indexhtml: fix URLs of official site sections URL and books location

* Mon Sep 05 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.4.M80P.1
- Use bright Education icon suitable both for light and dark backgrounds
- Rename kde4-settings to kde-settings, package Konsole profile and
  disable nm-applet.desktop autostart in KDE

* Tue Aug 30 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.3.M80P.1
- Set yellow labels for gfxboot
- Use predefined boot.png with logo for grub
- Set bright color for menubar in grub

* Fri Aug 26 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.2.M80P.1
- Do not require polkit-gnome
- Set SimpleSL icon theme in XFCE settings

* Fri Aug 26 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.1.M80P.2
- Rebuild with conflict with branding-xalt-kworkstation

* Fri Jul 22 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.1.M80P.1
- Initial build
