%def_enable snapshot
%define _unpackaged_files_terminate_build 1

%define _name robots
%define xdg_name org.gnome.Robots
%define __name gnome-%_name
%define ver_major 40
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt2

Summary: Gnome version of robots game for BSD games collection
License: GPL-3.0-or-later
Group: Games/Boards
Url: https://wiki.gnome.org/Apps/Robots

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz
%else
Source: %__name-%version.tar
%endif

Provides:  %__name = %EVR
Obsoletes: gnome-games-gnobots
Provides:  gnome-games-gnobots = %EVR

%define glib_ver 2.36.0
%define gtk_ver 4.10
%define adw_ver 1.2

Requires: gst-plugins-base1.0

BuildRequires(pre): meson
BuildRequires: vala-tools yelp-tools
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libgio-devel >= %glib_ver pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libgnome-games-support-2)
BuildRequires: pkgconfig(gstreamer-1.0)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
GNOME Robots is a development of the original Gnome Robots game which
was itself based on the text based robots game which can be found on a
number of UNIX systems, and comes with the BSD games package on Linux
systems.

%prep
%setup -n %__name-%version

%build
%add_optflags -lm
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %__name

%check
%__meson_test

%files -f gnome-%_name.lang
%_bindir/%__name
%_desktopdir/%xdg_name.desktop
%_datadir/%__name
%_iconsdir/hicolor/*/*/*.*
%_man6dir/%__name.*
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml

%changelog
* Tue Apr 16 2024 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt2
- updated to 40.0-106-g6aa594b (ported to GTK4/Libadwaita)

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Mar 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Fri Mar 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Sat Jan 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Sun Sep 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Sat Sep 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Fri Apr 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0.1-alt1
- 3.20.0.1

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Fri Oct 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Sun Jun 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Dec 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Mar 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.92-alt1
- 3.7.92

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



