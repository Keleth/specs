Name: templates
Version: 1.2
Release: alt2
Summary: Standard templates for the user directory
Summary(ru_RU.UTF-8): Стандартные шаблоны для каталога пользователя
License: GPLv3
Group: Graphical desktop/Other
Url: http://git.altlinux.org/people/antohami/packages/templates
Source: %name-%version.tar
Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch

%description
Standard templates for the user directory and the script for automatic
installation template, if template directory user is empty.

%description -l ru_RU.UTF-8
Стандартные шаблоны для каталога пользователя и скрипт для автоматической
установки шаблонов для случая, когда каталог шаблонов пользователя пуст.

%prep
%setup
chmod 755 make-lang.sh

%build
./make-lang.sh

%install
install -D -m755 templates.sh %buildroot/%_sysconfdir/X11/profile.d/templates.sh
install -d -m755 %buildroot/%_sysconfdir/xdg/autostart/
install -m644 update_templates.desktop %buildroot/%_sysconfdir/xdg/autostart/
install -d -m755 %buildroot/%_datadir/Templates
install -m644 Templates/* %buildroot/%_datadir/Templates
cp -R locale %buildroot/%_datadir
%find_lang %name

#pre
#rm -f %_datadir/Templates/*.odt
#rm -f %_datadir/Templates/*.odp
#rm -f %_datadir/Templates/*.ods
#rm -f %_datadir/Templates/*.odg

%files -f %name.lang
%_datadir/Templates
%_sysconfdir/X11/profile.d/templates.sh
%_sysconfdir/xdg/autostart/update_templates.desktop

%changelog
* Sun Mar 31 2024 Roman Alifanov <ximper@altlinux.org> 1.2-alt2
- return to sisyphus

* Wed Oct 19 2022 Anton Midyukov <antohami@altlinux.org> 1.2-alt1
- replace script from %_sysconfdir/profile.d to %_sysconfdir/X11/profile.d

* Fri Sep 25 2015 Anton Midyukov <antohami@altlinux.org> 1.1-alt1
- New version.

* Fri Sep 04 2015 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build for ALT Linux Sisyphus.
