%def_disable snapshot

%define _name Graphs
%define pypi_name graphs
%define ver_major 1.8
%define api_ver 1
%define rdn_name se.sjoerd.%_name

%def_enable check

Name: graphs
Version: %ver_major.0
Release: alt1

Summary: Plot and manipulate data with Graphs
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/Sjoerd1993/Graphs

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/Sjoerd1993/Graphs.git
Source: %name-%version.tar
%endif

%define adwaita_ver 1.5

Requires: dconf yelp

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir rpm-build-vala
BuildRequires: meson vala-tools blueprint-compiler /usr/bin/g-ir-compiler
BuildRequires: yelp-tools
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver gir(Adw) = 1
BuildRequires: pkgconfig(gee-0.8)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}
# TODO: python tests
#BuildRequires: python3(pytest) typelib(Adw) = 1}

%description
Graphs is a simple, yet powerful tool that allows you to plot and
manipulate your data with ease. New data can be imported from a wide
variety of filetypes, or generated by equation. All data can be
manipulated using a variety of operations.

%package -n lib%name
Summary: %_name shared library
Group: System/Libraries

%description -n lib%name
This package contains shared library needed %_name to work.

%prep
%setup -n %{?_disable_snapshot:%_name}%{?_enable_snapshot:%name}-%version
sed -i "s/'pytest'/'py.test3'/" tests/meson.build

%build
%meson -Dbuildtype=release
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%check
%__meson_test -v

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir_noarch/%pypi_name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%_datadir/mime/packages/%rdn_name.mime.xml
%doc README*

%files -n lib%name
%_libdir/lib%name.so
%_typelibdir/%_name-%api_ver.typelib

%changelog
* Tue Apr 23 2024 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Feb 06 2024 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- updated to v1.7.2-2-g975ae74

* Mon Jan 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- first build for Sisyphus (v1.7.1-8-g11b2692)


