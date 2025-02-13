%define popIF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define popIF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define popIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define popIF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

%def_disable compat
%def_enable jpeg2000

%if_disabled compat
%def_enable cpp
%def_enable glib
%def_enable qt6
%def_enable qt5
%def_disable qt4
%def_enable devel
%def_enable utils
%def_enable xpdfheaders
%def_enable gir
%else
%def_disable cpp
%def_disable glib
%def_disable qt6
%def_disable qt5
%def_disable qt4
%def_disable devel
%def_disable utils
%def_disable xpdfheaders
%def_disable gir
%endif

%define rname poppler
%define somajor 134
%define somajor_cpp 0
%define somajor_qt 3
%define somajor_qt4 4
%define somajor_qt5 1
%define somajor_qt6 3
%define somajor_glib 8
%define major 24
%define minor 02
%define bugfix 0

%if_disabled compat
%define pkgname %rname-current
%else
%define pkgname %rname%somajor
%endif
Name: %pkgname
Version: %major.%minor.%bugfix
Release: alt1

%if_disabled compat
%define poppler_devel lib%rname-devel
%define poppler_cpp_devel lib%rname-cpp-devel
%define poppler_glib_devel lib%rname-glib-devel
%define poppler_qt_devel lib%rname-qt-devel
%define poppler_qt4_devel lib%rname-qt4-devel
%define poppler_qt5_devel lib%rname-qt5-devel
%define poppler_qt6_devel lib%rname-qt6-devel
%else
%define poppler_devel lib%rname%somajor-devel
%define poppler_cpp_devel lib%rname%somajor-cpp-devel
%define poppler_glib_devel lib%rname%somajor-glib-devel
%define poppler_qt_devel lib%rname%somajor-qt-devel
%define poppler_qt4_devel lib%rname%somajor-qt4-devel
%define poppler_qt5_devel lib%rname%somajor-qt5-devel
%define poppler_qt6_devel lib%rname%somajor-qt6-devel
%endif
%define libpoppler libpoppler%somajor
%define libpoppler_qt4 lib%rname%somajor_qt4-qt4
%define libpoppler_qt5 lib%rname%somajor_qt5-qt5
%define libpoppler_qt6 lib%rname%somajor_qt6-qt6
%define libpoppler_glib lib%rname%somajor_glib-glib
%define libpoppler_cpp lib%rname%somajor_cpp-cpp
%define _cmake__builddir BUILD

Group: Publishing
Summary: PDF rendering library
License: (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Url: http://poppler.freedesktop.org/
Packager: Sergey V Turchin <zerg at altlinux dot org>

Source: %rname-%version.tar
# ALT
Patch10: alt-e2k.patch
Patch11: alt-openjpeg-version.patch

# Automatically added by buildreq on Fri Apr 01 2011 (-bi)
#BuildRequires: gcc-c++ glib-networking glibc-devel-static gtk-doc gvfs imake libXt-devel libcurl-devel libgtk+2-devel libgtk+2-gir-devel libjpeg-devel liblcms-devel libopenjpeg-devel libqt3-devel libqt4-devel libqt4-gui libqt4-xml libxml2-devel python-modules-compiler python-modules-encodings time xorg-cf-files

BuildRequires(pre): rpm-utils rpm-build-ubt
BuildRequires: cmake
%if_enabled qt6
BuildRequires: qt6-base-devel
%endif
%if_enabled qt5
BuildRequires: qt5-base-devel
%endif
%if_enabled qt4
BuildRequires: libqt4-devel
%endif
%if_enabled glib
BuildRequires: glib2-devel
%endif
BuildRequires: gcc-c++ glibc-devel libcurl-devel zlib-devel libnss-devel libpcre-devel
BuildRequires: libjpeg-devel liblcms2-devel libtiff-devel libpng-devel
BuildRequires: libgtk+3-gir-devel libgtk+3-devel
%if_enabled jpeg2000
BuildRequires: libopenjpeg2.0-devel openjpeg-tools2.0
%endif
BuildRequires: libxml2-devel gtk-doc libcairo-gobject-devel
BuildRequires: libXt-devel poppler-data
BuildRequires: boost-devel libgpgme-devel

%description
Poppler is a fork of the xpdf PDF viewer developed by Derek Noonburg
of Glyph and Cog, LLC.  The purpose of forking xpdf is twofold.
First, we want to provide PDF rendering functionality as a shared
library, to centralize the maintenence effort.  Today a number of
applications incorporate the xpdf code base, and whenever a security
issue is discovered, all these applications exchange patches and put
out new releases.  In turn, all distributions must package and release
new version of these xpdf based viewers.  It's safe to say that
there's a lot of duplicated effort with the current situaion.  Even if
poppler in the short term introduces yet another xpdf derived code
base to the world, we hope that over time these applications will
adopt poppler.  After all, we only need one application to use poppler
to break even.

%package -n %libpoppler
Summary: PDF rendering library
Group: System/Libraries
Requires: poppler-data
%description -n %libpoppler
Poppler is a fork of the xpdf PDF viewer developed by Derek Noonburg
of Glyph and Cog, LLC.  The purpose of forking xpdf is twofold.
First, we want to provide PDF rendering functionality as a shared
library, to centralize the maintenence effort.  Today a number of
applications incorporate the xpdf code base, and whenever a security
issue is discovered, all these applications exchange patches and put
out new releases.  In turn, all distributions must package and release
new version of these xpdf based viewers.  It's safe to say that
there's a lot of duplicated effort with the current situaion.  Even if
poppler in the short term introduces yet another xpdf derived code
base to the world, we hope that over time these applications will
adopt poppler.  After all, we only need one application to use poppler
to break even.

%package -n %rname
Group: Publishing
Summary: PDF rendering library utils
Requires: %libpoppler
Provides: poppler-utils = %version-%release
Provides: xpdf-utils = 3.02-alt6
Obsoletes: xpdf-utils <= 3.02-alt5
Conflicts: xpdf-reader <= 3.02-alt5
Conflicts: pdftohtml
%description -n %rname
Poppler is a fork of the xpdf PDF viewer developed by Derek Noonburg
of Glyph and Cog, LLC.  The purpose of forking xpdf is twofold.
First, we want to provide PDF rendering functionality as a shared
library, to centralize the maintenence effort.  Today a number of
applications incorporate the xpdf code base, and whenever a security
issue is discovered, all these applications exchange patches and put
out new releases.  In turn, all distributions must package and release
new version of these xpdf based viewers.  It's safe to say that
there's a lot of duplicated effort with the current situaion.  Even if
poppler in the short term introduces yet another xpdf derived code
base to the world, we hope that over time these applications will
adopt poppler.  After all, we only need one application to use poppler
to break even.

%package -n %libpoppler_qt5
Summary: Qt5 frontend library for %rname
Group: System/Libraries
Requires: %libpoppler
%description -n %libpoppler_qt5
Qt5 frontend library for %rname

%package -n %libpoppler_qt6
Summary: Qt6 frontend library for %rname
Group: System/Libraries
Requires: %libpoppler
%description -n %libpoppler_qt6
Qt6 frontend library for %rname

%package -n %libpoppler_qt4
Summary: Qt4 frontend library for %rname
Group: System/Libraries
Requires: %libpoppler
%popIF_ver_gteq "%major.%minor" "0.10"
Provides: libpoppler08-qt4 = %version-%release
Obsoletes: libpoppler08-qt4 < %version-%release
%if "%somajor_qt4" != "4"
Provides: libpoppler4-qt4 = %version-%release
Obsoletes: libpoppler4-qt4 < %version-%release
%endif
%endif
%description -n %libpoppler_qt4
Qt4 frontend library for %rname

%package -n %libpoppler_glib
Summary: Glib frontend library for %rname
Group: System/Libraries
Requires: %libpoppler
%description -n %libpoppler_glib
Glib frontend library for %rname

%package -n %libpoppler_cpp
Summary: Pure C++ wrapper for poppler
Group: System/Libraries
Requires: %libpoppler
%description -n %libpoppler_cpp
Pure C++ wrapper for poppler

%package -n %poppler_devel
Summary: Development files for %rname
Group: Development/C
Provides: %libpoppler-devel = %version-%release
Obsoletes: %libpoppler-devel < %version-%release
Requires: %libpoppler
%if_enabled compat
Conflicts: lib%rname-devel
%endif
%description -n %poppler_devel
Libraries, include files, etc you can use to develop poppler applications

%package -n %poppler_cpp_devel
Summary: Development files for C++ wrapper
Group: Development/C++
Requires: %libpoppler_cpp
%if_enabled xpdfheaders
Requires: %poppler_devel
%endif
%if_enabled compat
Conflicts: lib%rname-cpp-devel
%endif
%description -n %poppler_cpp_devel
Libraries, include files, etc you can use to develop
poppler applications with pure C++

%package -n %poppler_glib_devel
Summary: Development files for %rname-glib
Group: Development/GNOME and GTK+
Requires: %libpoppler_glib
%if_enabled xpdfheaders
Requires: %poppler_devel
%endif
%if_enabled compat
Conflicts: lib%rname-glib-devel
%endif
%description -n %poppler_glib_devel
Libraries, include files, etc you can use to develop
poppler applications with Glib/Gtk+

%package -n %poppler_qt6_devel
Summary: Development files for %rname-qt6
Group: Development/KDE and QT
Requires: %libpoppler_qt6
%if_enabled xpdfheaders
Requires: %poppler_devel
%endif
%if_enabled compat
Conflicts: lib%rname-qt6-devel
%endif
%description -n %poppler_qt6_devel
Libraries, include files, etc you can use to develop
poppler applications with Qt6

%package -n %poppler_qt5_devel
Summary: Development files for %rname-qt5
Group: Development/KDE and QT
Requires: %libpoppler_qt5
%if_enabled xpdfheaders
Requires: %poppler_devel
%endif
%if_enabled compat
Conflicts: lib%rname-qt5-devel
%endif
%description -n %poppler_qt5_devel
Libraries, include files, etc you can use to develop
poppler applications with Qt5

%package -n %poppler_qt4_devel
Summary: Development files for %rname-qt4
Group: Development/KDE and QT
Requires: %libpoppler_qt4
%if_enabled xpdfheaders
Requires: %poppler_devel
%endif
%if_enabled compat
Conflicts: lib%rname-qt4-devel
%endif
%description -n %poppler_qt4_devel
Libraries, include files, etc you can use to develop
poppler applications with Qt4

%package -n lib%rname-gir
Summary: GObject introspection data for the Poppler library
Group: System/Libraries
Requires: %libpoppler_glib
%description -n lib%rname-gir
GObject introspection data for the Poppler library

%package -n lib%rname-gir-devel
Summary: GObject introspection devel data for the Poppler library
Group: System/Libraries
BuildArch: noarch
Requires: lib%rname-gir
Requires: %poppler_glib_devel
%description -n lib%rname-gir-devel
GObject introspection devel data for the Poppler library

%prep
%setup -n %rname-%version
%patch10 -p1
%patch11 -p1

%build
%if_enabled qt4
export QT4DIR=%_qt4dir
%endif
%cmake \
    -DSHARE_INSTALL_DIR=%_datadir \
    -DBUILD_SHARED_LIBS=ON \
    -DENABLE_GPGME=ON \
    -DENABLE_LIBCURL=ON \
    -DENABLE_ZLIB=OFF \
    -DENABLE_CMS=lcms2 \
    -DENABLE_DCTDECODER=libjpeg \
%if_enabled jpeg2000
    -DENABLE_LIBOPENJPEG=openjpeg2 \
%else
    -DENABLE_LIBOPENJPEG=unmaintained \
%endif
    -DENABLE_XPDF_HEADERS=%{?_enable_xpdfheaders:ON}%{!?_enable_xpdfheaders:OFF} \
    -DENABLE_UNSTABLE_API_ABI_HEADERS=%{?_enable_xpdfheaders:ON}%{!?_enable_xpdfheaders:OFF} \
    -DENABLE_UTILS=%{?_enable_utils:ON}%{!?_enable_utils:OFF} \
    -DENABLE_CPP=%{?_enable_cpp:ON}%{!?_enable_cpp:OFF} \
    -DENABLE_GLIB=%{?_enable_glib:ON}%{!?_enable_glib:OFF} \
    -DENABLE_QT4=%{?_enable_qt4:ON}%{!?_enable_qt4:OFF} \
    -DENABLE_QT5=%{?_enable_qt5:ON}%{!?_enable_qt5:OFF} \
    -DENABLE_QT6=%{?_enable_qt6:ON}%{!?_enable_qt6:OFF} \
    #
#    -DBUILD_GTK_TESTS=OFF \
#    -DBUILD_QT4_TESTS=OFF \
#    -DBUILD_QT5_TESTS=OFF \
#    -DBUILD_QT6_TESTS=OFF \
#    -DBUILD_CPP_TESTS=OFF \
%cmake_build

%install
make install DESTDIR=%buildroot -C BUILD
#cmakeinstall_std

%if_enabled utils
%files -n %rname
%_bindir/pdf*
%_man1dir/pdf*
%endif

%files -n %libpoppler
%doc AUTHORS ChangeLog NEWS README*
%_libdir/libpoppler.so.%somajor
%_libdir/libpoppler.so.%somajor.*

%if_enabled gir
%files -n lib%rname-gir
%_typelibdir/Poppler-*.typelib
%if_enabled devel
%files -n lib%rname-gir-devel
%_girdir/Poppler-*.gir
%endif
%endif

%if_enabled glib
%files -n %libpoppler_glib
%_libdir/libpoppler-glib.so.%somajor_glib
%_libdir/libpoppler-glib.so.%somajor_glib.*
%if_enabled devel
%files -n %poppler_glib_devel
%_includedir/poppler/glib/
%_libdir/libpoppler-glib.so
#%_pkgconfigdir/poppler-cairo.pc
%_pkgconfigdir/poppler-glib.pc
%endif
%endif

%if_enabled qt4
%files -n %libpoppler_qt4
%_libdir/libpoppler-qt4.so.%somajor_qt4
%_libdir/libpoppler-qt4.so.%somajor_qt4.*
%if_enabled devel
%files -n %poppler_qt4_devel
%_includedir/poppler/qt4/
%_libdir/libpoppler-qt4.so
%_pkgconfigdir/poppler-qt4.pc
%endif
%endif

%if_enabled qt5
%files -n %libpoppler_qt5
%_libdir/libpoppler-qt5.so.%somajor_qt5
%_libdir/libpoppler-qt5.so.%somajor_qt5.*
%if_enabled devel
%files -n %poppler_qt5_devel
%_includedir/poppler/qt5/
%_libdir/libpoppler-qt5.so
%_pkgconfigdir/poppler-qt5.pc
%endif
%endif

%if_enabled qt6
%files -n %libpoppler_qt6
%_libdir/libpoppler-qt6.so.%somajor_qt6
%_libdir/libpoppler-qt6.so.%somajor_qt6.*
%if_enabled devel
%files -n %poppler_qt6_devel
%_includedir/poppler/qt6/
%_libdir/libpoppler-qt6.so
%_pkgconfigdir/poppler-qt6.pc
%endif
%endif

%if_enabled cpp
%files -n %libpoppler_cpp
%_libdir/libpoppler-cpp.so.%somajor_cpp
%_libdir/libpoppler-cpp.so.%somajor_cpp.*
%if_enabled devel
%files -n %poppler_cpp_devel
%_includedir/poppler/cpp/
%_libdir/libpoppler-cpp.so
%_pkgconfigdir/poppler-cpp.pc
%endif
%endif

%if_enabled devel
%if_enabled xpdfheaders
%files -n %poppler_devel
%dir %_includedir/poppler
%_includedir/poppler/*.h
%_includedir/poppler/fofi
%_includedir/poppler/splash/
%_includedir/poppler/goo/
%_libdir/libpoppler.so
%_pkgconfigdir/poppler.pc
#%_pkgconfigdir/poppler-splash.pc

%endif
%endif

%changelog
* Tue May 14 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.0-alt1
- new version

* Tue Feb 27 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.0-alt4
- fix to build with new openjpeg

* Thu Jan 25 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.0-alt3
- add upstream fix against crash in nss backend

* Mon Jan 22 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.0-alt2
- build with gpgme
- don't disable boost

* Wed Jan 17 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.0-alt1
- new version

* Thu Jul 27 2023 Sergey V Turchin <zerg@altlinux.org> 23.02.0-alt1
- new version

* Fri Jan 20 2023 Sergey V Turchin <zerg@altlinux.org> 23.01.0-alt1
- new version

* Mon Nov 28 2022 Sergey V Turchin <zerg@altlinux.org> 22.11.0-alt1
- new version

* Wed Mar 09 2022 Sergey V Turchin <zerg@altlinux.org> 22.03.0-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 21.11.0-alt3
- fix libpoppler_cpp package name

* Tue Nov 30 2021 Sergey V Turchin <zerg@altlinux.org> 21.11.0-alt2
- rename source package name

* Tue Nov 30 2021 Sergey V Turchin <zerg@altlinux.org> 21.11.0-alt1
- new version

* Mon Jun 07 2021 Sergey V Turchin <zerg@altlinux.org> 21.05.0-alt2
- fix to build against new cmake

* Tue May 18 2021 Sergey V Turchin <zerg@altlinux.org> 21.05.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 0.86.1-alt2
- fix build requires

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 0.86.1-alt1
- new version

* Tue Mar 10 2020 Nikita Ermakov <arei@altlinux.org> 0.84.0-alt2
- Disable Qt4 for riscv64.

* Fri Jan 10 2020 Sergey V Turchin <zerg@altlinux.org> 0.84.0-alt1
- new version

* Fri Oct 04 2019 Sergey V Turchin <zerg@altlinux.org> 0.81.0-alt1
- new version

* Thu Jun 27 2019 Sergey V Turchin <zerg@altlinux.org> 0.80.0-alt1
- new version
- restore Qt4 backend

* Thu Jun 27 2019 Sergey V Turchin <zerg@altlinux.org> 0.78.0-alt1
- new version

* Mon Apr 08 2019 Sergey V Turchin <zerg@altlinux.org> 0.77.0-alt1
- new version

* Mon Apr 08 2019 Sergey V Turchin <zerg@altlinux.org> 0.75.0-alt1
- new version
- fix build on E2K (thanks mike@alt) (ALT#36538)

* Fri Feb 08 2019 Sergey V Turchin <zerg@altlinux.org> 0.74.0-alt1
- new version

* Wed Nov 07 2018 Sergey V Turchin <zerg@altlinux.org>  0.71.0-alt2
- new version

* Wed Nov 07 2018 Sergey V Turchin <zerg@altlinux.org>  0.71.0-alt1
- new version

* Mon Jul 23 2018 Sergey V Turchin <zerg@altlinux.org> 0.67.0-alt1%ubt
- new version

* Mon Apr 23 2018 Sergey V Turchin <zerg@altlinux.org> 0.61.1-alt1%ubt
- new version

* Tue Oct 24 2017 Sergey V Turchin <zerg@altlinux.org> 0.60.1-alt1%ubt
- new version

* Mon Jul 03 2017 Sergey V Turchin <zerg@altlinux.org> 0.56.0-alt1%ubt
- new version

* Thu Feb 09 2017 Sergey V Turchin <zerg@altlinux.org> 0.51.0-alt1%ubt
- new version

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 0.48.0-alt1
- new version

* Fri Jul 22 2016 Sergey V Turchin <zerg@altlinux.org> 0.45.0-alt1
- new version

* Mon May 16 2016 Sergey V Turchin <zerg@altlinux.org> 0.42.0-alt2
- add fix against crash on certain PDF form item activation actions

* Tue Mar 29 2016 Sergey V Turchin <zerg@altlinux.org> 0.42.0-alt1
- new version

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 0.41.0-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 0.40.0-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 0.39.0-alt1
- new version

* Thu Dec 03 2015 Sergey V Turchin <zerg@altlinux.org> 0.38.0-alt1
- new version

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 0.37.0-alt1
- new version

* Fri Sep 04 2015 Sergey V Turchin <zerg@altlinux.org> 0.35.0-alt1
- new version

* Wed Aug 05 2015 Sergey V Turchin <zerg@altlinux.org> 0.34.0-alt1
- new version

* Thu May 28 2015 Sergey V Turchin <zerg@altlinux.org> 0.33.0-alt1
- new version

* Thu Mar 26 2015 Sergey V Turchin <zerg@altlinux.org> 0.32.0-alt1
- new version

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 0.31.0-alt1
- new version

* Wed Dec 24 2014 Sergey V Turchin <zerg@altlinux.org> 0.29.0-alt1
- new version

* Fri Nov 14 2014 Sergey V Turchin <zerg@altlinux.org> 0.28.1-alt1
- new version

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 0.26.4-alt1
- new version

* Wed Jul 09 2014 Sergey V Turchin <zerg@altlinux.org> 0.26.2-alt1
- new version

* Thu May 29 2014 Sergey V Turchin <zerg@altlinux.org> 0.26.1-alt1
- new version

* Tue May 13 2014 Sergey V Turchin <zerg@altlinux.org> 0.26.0-alt1
- new version

* Fri Jan 17 2014 Sergey V Turchin <zerg@altlinux.org> 0.24.5-alt1
- new version

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 0.24.4-alt1
- new version

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 0.24.3-alt1.M70P.1
- built for M70P

* Fri Nov 22 2013 Sergey V Turchin <zerg@altlinux.org> 0.24.3-alt2
- don't build static libs by default

* Thu Nov 21 2013 Sergey V Turchin <zerg@altlinux.org> 0.24.3-alt0.M70P.2
- disable qt5 for p7

* Thu Nov 21 2013 Sergey V Turchin <zerg@altlinux.org> 0.24.3-alt0.M70P.1
- built for M70P

* Mon Nov 11 2013 Sergey V Turchin <zerg@altlinux.org> 0.24.3-alt1
- new version

* Wed Oct 23 2013 Sergey V Turchin <zerg@altlinux.org> 0.24.2-alt2
- built Qt5 backend

* Thu Oct 10 2013 Sergey V Turchin <zerg@altlinux.org> 0.24.2-alt1
- new version

* Tue Sep 03 2013 Sergey V Turchin <zerg@altlinux.org> 0.24.1-alt1
- new version

* Tue Jul 23 2013 Sergey V Turchin <zerg@altlinux.org> 0.22.5-alt1
- new version

* Tue Apr 23 2013 Sergey V Turchin <zerg@altlinux.org> 0.22.3-alt1
- new version

* Thu Mar 14 2013 Sergey V Turchin <zerg@altlinux.org> 0.22.2-alt1
- new version

* Wed Feb 13 2013 Sergey V Turchin <zerg@altlinux.org> 0.22.1-alt1
- new version

* Thu Nov 08 2012 Sergey V Turchin <zerg@altlinux.org> 0.20.5-alt1
- new version

* Mon Sep 17 2012 Dmitry V. Levin <ldv@altlinux.org> 0.20.3-alt4
- Rebuilt with libpng15.

* Sun Sep 02 2012 Dmitry V. Levin <ldv@altlinux.org> 0.20.3-alt3
- Built with system libtiff again.

* Sun Sep 02 2012 Sergey V Turchin <zerg@altlinux.org> 0.20.3-alt2
- built with libtiff5

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 0.20.3-alt1
- new version

* Thu Jul 12 2012 Sergey V Turchin <zerg@altlinux.org> 0.20.2-alt1
- new version

* Wed Jun 20 2012 Sergey V Turchin <zerg@altlinux.org> 0.20.1-alt1
- new version

* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.18.4-alt0.M60P.1
- built for M60P

* Fri Mar 23 2012 Sergey V Turchin <zerg@altlinux.org> 0.18.4-alt1
- new version

* Thu Jan 19 2012 Sergey V Turchin <zerg@altlinux.org> 0.18.3-alt1
- new version

* Sat Dec 17 2011 Sergey V Turchin <zerg@altlinux.org> 0.18.2-alt1
- new version

* Tue Nov 08 2011 Sergey V Turchin <zerg@altlinux.org> 0.18.1-alt2
- fix to build

* Mon Nov 07 2011 Sergey V Turchin <zerg@altlinux.org> 0.18.1-alt1
- new version

* Tue Aug 30 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.7-alt0.M60P.1
- built for M60P

* Mon Aug 29 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.7-alt1
- new version

* Fri Apr 15 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.4-alt2
- provide poppler-utils (ALT#25422)
- don't package glib-demo

* Fri Apr 01 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.4-alt1
- new version

* Fri Mar 18 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.3-alt1
- new version

* Fri Feb 11 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.2-alt1
- new version

* Mon Nov 08 2010 Sergey V Turchin <zerg@altlinux.org> 0.14.5-alt1
- new version

* Thu Oct 14 2010 Sergey V Turchin <zerg@altlinux.org> 0.14.4-alt1
- new version

* Thu Aug 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.14.2-alt1
- new version

* Mon Aug 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.14.1-alt1
- new version (ALT#23738)

* Fri Feb 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.12.4-alt0.M51.1
- built for M51

* Fri Feb 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.12.4-alt1
- new version
- built with lcms
- update version scripts

* Tue Dec 29 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.3-alt0.M51.1
- built for M51

* Tue Dec 29 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.3-alt1
- new version

* Fri Dec 11 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.2-alt0.M51.1
- built for M51

* Fri Dec 11 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.2-alt1
- new version
- CVE-2009-3607

* Mon Oct 19 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.1-alt1
- new version
- add linker version script for libpoppler
- security fixes:
    - CVE-2009-3608 ObjectStream integer overflow

* Mon Sep 14 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.0-alt1
- new version

* Tue Jul 07 2009 Sergey V Turchin <zerg@altlinux.org> 0.10.7-alt2
- obsolete xpdf-utils

* Tue May 19 2009 Sergey V Turchin <zerg@altlinux.org> 0.10.7-alt1
- new version

* Tue Apr 21 2009 Sergey V Turchin <zerg@altlinux.org> 0.10.6-alt2
- built for sisyphus

* Mon Apr 20 2009 Vladimir Lettiev <crux@altlinux.ru> 0.10.6-alt1
- new version
- security fixes:
    - CVE-2009-0799 xpdf OOB Read
    - CVE-2009-0800 xpdf Multiple Input Validation Flaws
    - CVE-2009-1179 xpdf Integer Overflow
    - CVE-2009-1180 xpdf Invalid free()
    - CVE-2009-1181 xpdf NULL dereference DoS
    - CVE-2009-1182 xpdf MMR Decoder Buffer Overflows
    - CVE-2009-1183 xpdf MMR Infinite Loop DoS
    - CVE-2009-1187 poppler CairoOutputDev integer overflow
    - CVE-2009-1188 poppler SplashBitmap integer overflow

* Mon Mar 16 2009 Sergey V Turchin <zerg@altlinux.org> 0.10.5-alt1
- new version

* Tue Feb 17 2009 Sergey V Turchin <zerg at altlinux dot org> 0.10.4-alt3
- fix build requires

* Mon Feb 16 2009 Sergey V Turchin <zerg at altlinux dot org> 0.10.4-alt1
- new version (fixes SA:33853)

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 0.10.3-alt1
- new version

* Tue Dec 16 2008 Sergey V Turchin <zerg at altlinux dot org> 0.10.2-alt1
- new version
- remove deprecated macroses from specfile

* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 0.10.0-alt3
- fix provides/obsoletes

* Tue Oct 14 2008 Sergey V Turchin <zerg at altlinux dot org> 0.10.0-alt2
- fix provides/obsoletes
- add versioning to qt4 subpackage

* Mon Oct 13 2008 Sergey V Turchin <zerg at altlinux dot org> 0.10.0-alt1
- new version

* Thu Oct 09 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.7-alt2
- don't use cmake (fix #17493)

* Thu Sep 11 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.7-alt1
- new version

* Fri Aug 22 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.6-alt1
- new version
- add conflict to pdftohtml

* Tue Jul 29 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.5-alt1
- new version
- built with zlib
- CVE-2008-2950

* Mon Jun 09 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.3-alt2
- fix conflicts to xpdf-reader

* Sat Jun 07 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.3-alt1
- new version

* Fri Apr 18 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt4
- fix to install OptionalContent.h

* Fri Apr 18 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt3
- rename devel subpackages to real names
- rebuilt with new cairo
- add patch from RH to fix a crash when no optional content groups are defined

* Tue Apr 15 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt2
- fix lib install dir on x86_64

* Tue Apr 15 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt1
- new version

* Mon Apr 14 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 0.6.4-alt1
- new version
- add patch from FC to make ObjStream usable

* Thu Dec 27 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.3-alt1
- new version

* Thu Nov 08 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt3
- add patch to fix CVE-2007-4352, CVE-2007-5392, CVE-2007-5393

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt2
- fix tarball

* Fri Oct 12 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt1
- new version

* Mon Oct 08 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt6
- fix provides/obsoletes

* Mon Oct 08 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt5
- replace poppler-0.5

* Wed Sep 26 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt4
- include unsupported xpdf headers into devel package

* Mon Sep 24 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt3
- add obsoletes instead conflicts

* Wed Sep 19 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt2
- provide devel packages to override poppler-devel-0.5

* Tue Sep 04 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- new version

* Mon Aug 06 2007 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt6
- add patch to fix CVE-2007-3387

* Mon Jun 25 2007 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt5
- fix %%files intersections (#11804)

* Wed Nov 01 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt4
- fix patch for cairo

* Tue Oct 31 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt3
- fix compile with cairo < 0.9

* Tue Oct 03 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt2
- fix find Qt4 on x86_64

* Mon Oct 02 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt1
- new version
- built with Qt4

* Mon Jul 17 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.3-alt1
- new version

* Mon Jun 05 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.1-alt2
- built without Qt4

* Tue May 16 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.1-alt1
- new version
- fix %%files in -devel subpackages
- built with Qt4

* Fri Mar 31 2006 Sergey V Turchin <zerg at altlinux dot org> 0.4.5-alt2
- fix lib*.so list in *-devel packages

* Tue Feb 14 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.5-alt1
- Updated to 0.4.5.
- Cleaned up the spec a bit.

* Wed Feb 08 2006 Sergey V Turchin <zerg at altlinux dot org> 0.4.4-alt2
- fix linking with qt
- split qt,glib,devel libraries to subpackages
- fix %%url
- fix requires
- fix build requires

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.4-alt1.1
- Rebuilt for new pkg-config dependencies.

* Wed Jan 11 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.4.4-alt1
- new  version

* Tue Dec 13 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.4.3-alt1
- new version

* Mon Sep 05 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Mon Aug 29 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.4.1-alt1
- new version

* Tue Jun 21 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Mon Jun 06 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.3.2-alt2
- Change package summary

* Wed May 25 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.3.2-alt1
- First version of RPM

