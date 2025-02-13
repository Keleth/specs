%define _libexecdir %_prefix/libexec
%define qIF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define _localstatedir %_var
%filter_from_requires /^sudo$/d

%define pkg_version 6.6
%define xdg_name org.a11y.brlapi
%define api_ver 0.8.5
%define _exec_prefix %nil
%define _jnidir %_libdir/java

%def_with at_spi2
%def_with python3
%def_with speech_dispatcher
%if_with speech_dispatcher
%define libspeechd_ver %{get_version libspeechd}
%endif

%def_without at_spi1
%def_without ocaml
%def_without tcl
%if_with tcl
%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %prefix/%_lib/tcl%tcl_version}
%endif

Name: brltty
Version: %pkg_version
Release: alt2

Summary: Braille display driver for Linux/Unix
Group: System/Servers
License: GPL-2.0-or-later
Url: http://mielke.cc/brltty/

Vcs: https://github.com/brltty/brltty.git
# Source-url: http://mielke.cc/brltty/archive/%name-%version.tar.xz
Source: %name-%version.tar
# from fc
Source1: %name.service
Source2: ru_brltty.tar
Source44: import.info
Patch1: brltty-4.5-alt-fix-python-syntax.patch
Patch2: fix-speechd-includes.patch
Patch4: brltty-5.6-fix_brltty-systemd-wrapper_path.patch
# from https://src.fedoraproject.org/rpms/brltty/c/ee571d6d4793c76970cd5930c3769c0f029dd38f?branch=rawhide
Patch5: brltty-6.6-cython3.patch

%define cython_ver 0.18

BuildRequires(pre): rpm-build-java
BuildRequires: libappstream-glib-devel
BuildRequires: gcc-c++ libbluez-devel libalsa-devel libgpm-devel
# for updusbdevs and udev rules
BuildRequires: tcl
BuildRequires: byacc glibc-kernheaders
BuildRequires: /proc java-devel
BuildRequires: pkgconfig(systemd) libudev-devel
BuildRequires: doxygen python3-module-docutils
%{?_with_at_spi2:BuildRequires: libat-spi2-core-devel}
%{?_with_speech_dispatcher:BuildRequires: libspeechd-devel}
%{?_with_python3:
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-Cython >= %cython_ver}
%{?_with_tcl:BuildRequires: tcl-devel}
%{?_with_ocaml:BuildRequires: ocaml findlib}
# for XWindow driver
BuildRequires: libSM-devel libICE-devel libX11-devel libXaw-devel libXext-devel libXt-devel libXtst-devel

%description
BRLTTY is a background process (daemon) which provides
access to the Linux/Unix console (when in text mode)
for a blind person using a refreshable braille display.
It drives the braille display and provides complete
screen review functionality.

%if_with speech_dispatcher
BRLTTY can also work with speech synthesizers; if you want to use it with
Speech Dispatcher, please install also package %name-speech-dispatcher.

%package speech-dispatcher
Summary: Speech Dispatcher driver for BRLTTY
Group: System/Servers
License: GPL-2.0-or-later
Requires: %name = %pkg_version-%release

%description speech-dispatcher
This package provides the Speech Dispatcher driver for BRLTTY.
%endif

%package xw
Summary: XWindow driver for BRLTTY
Group: System/Servers
License: GPL-2.0-or-later

Requires: %name = %pkg_version-%release
%description xw
This package provides the XWindow driver for BRLTTY.

%if_with at_spi1
%package at-spi
Summary: AtSpi driver for BRLTTY
Group: System/Servers
# The data files are licensed under LGPLv2+, see the README file.
License: GPL-2.0-or-later and LGPL-2.0-or-later
BuildRequires: libat-spi-devel
Requires: %name = %pkg_version-%release
%description at-spi
This package provides the AtSpi driver for BRLTTY.
%endif

%if_with at_spi2
%package at-spi2
Summary: AtSpi2 driver for BRLTTY
Group: System/Servers
# The data files are licensed under LGPLv2+, see the README file.
License: GPL-2.0-or-later and LGPL-2.0-or-later
Requires: %name = %pkg_version-%release

%description at-spi2
This package provides the AtSpi2 driver for BRLTTY.
%endif

%package -n brlapi
Version: %api_ver
Group: File tools
License: LGPL-2.0-or-later
Summary: Application Programming Interface for BRLTTY
Requires: %name = %pkg_version-%release

%description -n brlapi
This package provides the run-time support for the Application
Programming Interface to BRLTTY.

Install this package if you have an application which directly accesses
a refreshable braille display.

%package -n brlapi-devel
Version: %api_ver
Group: Development/C
License: LGPL-2.0-or-later
Requires: brlapi = %api_ver-%release
Summary: Headers, static archive, and documentation for BrlAPI

%description -n brlapi-devel
This package provides the header files, static archive, shared object
linker reference, and reference documentation for BrlAPI (the
Application Programming Interface to BRLTTY).  It enables the
implementation of applications which take direct advantage of a
refreshable braille display in order to present information in ways
which are more appropriate for blind users and/or to provide user
interfaces which are more specifically attuned to their needs.

Install this package if you are developing or maintaining an application
which directly accesses a refreshable braille display.

%package -n tcl-brlapi
Version: %api_ver
Summary: Tcl binding for BrlAPI
Group: Development/Tcl
License: LGPL-2.0-or-later
Requires: brlapi = %api_ver-%release

%description -n tcl-brlapi
This package provides the Tcl binding for BrlAPI.

%package -n python3-module-brlapi
Version: %api_ver
Summary: Python binding for BrlAPI
Group: Development/Python
License: LGPL-2.0-or-later
Requires: brlapi = %api_ver-%release

%description -n python3-module-brlapi
This package provides the Python3 binding for BrlAPI.

%package -n brlapi-java
Version: %api_ver
Summary: Java binding for BrlAPI
Group: Development/Java
License: LGPL-2.0-or-later
Requires: brlapi = %api_ver-%release

%description -n brlapi-java
This package provides the Java binding for BrlAPI.

%if_with ocaml
%package -n ocaml-brlapi
Version: %api_ver
Summary: OCaml binding for BrlAPI
Group: Development/Other
License: LGPL-2.0-or-later
Requires: brlapi = %api_ver-%release

%description -n ocaml-brlapi
This package provides the OCaml binding for BrlAPI.
%endif

%prep
%setup
%qIF_ver_gteq %libspeechd_ver 0.8
%patch2 -p2
%endif
%patch5 -p1
sed -i 's;\/usr\(/bin/true\);\1;' Autostart/Systemd/brltty-device@.service

%build
%add_optflags %(getconf LFS_CFLAGS)

# Patch6 changes aclocal.m4:
autoconf

# Add the openjdk include directories to CPPFLAGS
for i in -I/usr/lib/jvm/java/include{,/linux}; do
      java_inc="$java_inc $i"
done
export CPPFLAGS="$java_inc"

# there is no curses packages in BuildRequires, so the package builds
# without them in mock; let's express this decision explicitly
opts="--disable-stripping --without-curses --libdir=/%_lib \
%if_with speech_dispatcher
  --with-speechd=%prefix \
%endif
  --with-install-root=%buildroot"

%configure $opts PYTHON=%__python3
%make_build

find . \( -path ./doc -o -path ./Documents \) -prune -o \
  \( -name 'README*' -o -name '*.txt' -o -name '*.html' -o \
     -name '*.sgml' -o -name '*.patch' -o \
     \( -path './Bootdisks/*' -type f -perm /ugo=x \) \) -print |
while read file; do
   mkdir -p doc/${file%%/*} && cp -rp $file doc/$file || exit 1
done

find . -name '*.sgml' |
while read file; do
   iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
done
find . -name '*.txt' |
while read file; do
   iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
done
find . -name 'README*' |
while read file; do
   iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
done

%install
%define install_opts JAVA_JNI_DIR=%_jnidir INSTALL_X11_AUTOSTART_DIRECTORY=%buildroot%_x11sysconfdir/xsession.user.d INSTALL_PKGCONFIG_DIRECTORY=%buildroot%_pkgconfigdir
%make %install_opts install

install -d -m755 %buildroot{%_sysconfdir,%_man5dir}
install -m644 Documents/brltty.conf %buildroot%_sysconfdir
echo ".so man1/brltty.1" > %buildroot%_man5dir/brltty.conf.5

%if %_lib == "lib64"
	#Manually place java plugin on 64-bit arches
	mkdir -p %buildroot%prefix/%_lib/java/
	install -m 755 Bindings/Java/libbrlapi_java.so "%buildroot%prefix/%_lib/java/"
%endif

# clean up the manuals:
rm -rf Documents/BrlAPIref/BrlAPIref/html
mv -f Documents/BrlAPIref/{html,BrlAPIref}

# Don't want static lib
rm -rf %buildroot/%_lib/libbrlapi.a

%__subst s/'#text-table.ru'/'text-table ru'/ %buildroot/etc/brltty.conf
%__cp %SOURCE2 ru_brltty.tar
tar xf ru_brltty.tar
%__cp ru_brltty/* %buildroot%_sysconfdir/brltty/

# create temporary directory
mkdir -p %buildroot%_tmpfilesdir
cat > %buildroot%_tmpfilesdir/%name.conf << _EOF_
d /run/%name 0755 root root -
_EOF_

# install polkit rules
pushd Authorization/Polkit
%makeinstall_std
popd

# udev rules
#install -pD -m644 Autostart/Udev/ %buildroot%_udevrulesdir/95-%name.rules
pushd Autostart/Udev
%makeinstall_std UDEV_PARENT_LOCATION=/lib
popd

# systemd unit
%make -C Autostart/Systemd SYSTEMD_UNITS_DIRECTORY=%buildroot%_unitdir install
mkdir -p %buildroot%_unitdir
install -m 644 Autostart/Systemd/*.{service,path} %buildroot%_unitdir/

chmod +x %buildroot%_bindir/%name-config.sh

%find_lang %name

%files -f %name.lang
%config(noreplace) %_sysconfdir/brltty.conf
%_sysconfdir/brltty/
/lib/sysusers.d/%name.conf
%_udevrulesdir/90-%name-hid.rules
%_udevrulesdir/90-%name-uinput.rules
%_udevrulesdir/90-%name-usb-customized.rules
%_udevrulesdir/90-%name-usb-generic.rules
%_tmpfilesdir/%name.conf
%_unitdir/brltty@.service
%_unitdir/%name-device@.service
%_unitdir/*.path
%_datadir/polkit-1/rules.d/org.a11y.brlapi.rules
%dir %_libexecdir/%name
# bash script
%_libexecdir/%name/systemd-wrapper
%_libexecdir/%name/udev-wrapper
%_datadir/polkit-1/actions/%xdg_name.policy
%_bindir/brltty
%_bindir/brltty-*
%exclude %_bindir/brltty-config.sh
%_bindir/eutp
/%_lib/brltty/
%exclude /%_lib/brltty/libbrlttybba.so
%exclude /%_lib/brltty/libbrlttybxw.so
%if_with speech_dispatcher
%exclude /%_lib/brltty/libbrlttyssd.so
%endif
%if_with at_spi1
%exclude /%_lib/brltty/libbrlttyxas.so
%endif
%if_with at_spi2
%exclude /%_lib/brltty/libbrlttyxa2.so
%endif
%_man1dir/brltty.*
%_man1dir/eutp.1.*
%_man5dir/brltty.*
#%_datadir/metainfo/org.a11y.brltty.metainfo.xml
%doc LICENSE-LGPL
%doc Documents/ChangeLog Documents/TODO
%doc Documents/Manual-BRLTTY/
%doc doc/*

%if_with speech_dispatcher
%files speech-dispatcher
%doc Drivers/Speech/SpeechDispatcher/README
/%_lib/brltty/libbrlttyssd.so
%endif

%files xw
%doc Drivers/Braille/XWindow/README
%_x11sysconfdir/xsession.user.d/90xbrlapi
/%_lib/brltty/libbrlttybxw.so

%if_with at_spi1
%files at-spi
/%_lib/brltty/libbrlttyxas.so
%endif

%if_with at_spi2
%files at-spi2
/%_lib/brltty/libbrlttyxa2.so
%_datadir/gdm/greeter/autostart/xbrlapi.desktop
%endif

%files -n brlapi
%_bindir/vstp
%_bindir/xbrlapi
/%_lib/brltty/libbrlttybba.so
/%_lib/libbrlapi.so.*
%doc Drivers/Braille/XWindow/README
%doc Documents/Manual-BrlAPI/
%doc %_mandir/man1/xbrlapi.*
%doc %_mandir/man1/vstp.*

%files -n brlapi-devel
%_bindir/%name-config.sh
/%_lib/libbrlapi.so
%_includedir/brltty
%_includedir/brlapi*.h
%_pkgconfigdir/brltty.pc
%_man3dir/brlapi_*.3*
%doc Documents/BrlAPIref/BrlAPIref/

%if_with tcl
%files -n tcl-brlapi
%tcl_sitearch/brlapi-%api_ver
%endif

%if_with python3
%files -n python3-module-brlapi
%python3_sitelibdir/brlapi*.so
%python3_sitelibdir/Brlapi-%api_ver-*.egg-info
%endif

%files -n brlapi-java
%_jnidir/libbrlapi_java.so
%_javadir/brlapi.jar

%if_with ocaml
%files -n ocaml-brlapi
%prefix/%_lib/ocaml/brlapi/
#%prefix/%_lib/ocaml/stublibs/
%endif

%changelog
* Thu Apr 11 2024 Anton Midyukov <antohami@altlinux.org> 6.6-alt2
- Enable LTO
- Fix the Cython 3 crash (add patch from Fedora) (Closes: 49977)
- Convert License fields to SPDX format

* Sat Dec 09 2023 Anton Midyukov <antohami@altlinux.org> 6.6-alt1
- 6.6 (Closes: 48429)

* Thu Apr 27 2023 Sergey V Turchin <zerg@altlinux.org> 6.5-alt1.1
- NMU: don't require sudo (closes: 45900)
- NMU: disable LTO to fix compile

* Sun Jun 12 2022 Yuri N. Sedunov <aris@altlinux.org> 6.5-alt1
- 6.5

* Sun Jan 16 2022 Yuri N. Sedunov <aris@altlinux.org> 6.4-alt1
- 6.4

* Tue Jul 27 2021 Yuri N. Sedunov <aris@altlinux.org> 6.3-alt1
- 6.3
- disabled useless python2 support

* Mon Jan 13 2019 Anton Midyukov <antohami@altlinux.org> 5.6-alt3
- Convert to python3 latex-access.ctb
- Fixed PATH to brltty-systemd-wrapper in brltty@.service

* Mon Jul 02 2018 Yuri N. Sedunov <aris@altlinux.org> 5.6-alt2
- updated buildreqs

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.6-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Feb 12 2018 Yuri N. Sedunov <aris@altlinux.org> 5.6-alt1
- 5.6

* Mon Apr 24 2017 Yuri N. Sedunov <aris@altlinux.org> 5.5-alt1
- 5.5

* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 5.4-alt1
- 5.4

* Mon Apr 04 2016 Yuri N. Sedunov <aris@altlinux.org> 5.3.1-alt3
- removed /lib/udev/devices/* (ALT #29446)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.3.1-alt2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 5.3.1-alt2
- 5.3.1

* Fri Dec 18 2015 Yuri N. Sedunov <aris@altlinux.org> 5.3-alt1
- 5.3

* Fri May 15 2015 Yuri N. Sedunov <aris@altlinux.org> 5.2-alt1
- 5.2

* Tue May 21 2013 Dmitry V. Levin <ldv@altlinux.org> 4.5-alt3
- Fixed "find -perm" usage.

* Fri Apr 12 2013 Yuri N. Sedunov <aris@altlinux.org> 4.5-alt2
- huge spec cleanup
- new python3-module-brlapi subpackage

* Fri Apr 12 2013 Paul Wolneykien <manowar@altlinux.org> 4.5-alt1
- Fresh up to v4.5 with the help of cronbuild and update-source-functions.

* Mon Apr 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt3
- build with speech-dispatcher

* Sun Apr 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt2
- build with at-spi2 instead of at-spi1

* Sun Apr 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1
- new version

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 4.2-alt3
- fixed build (use system %%_jnidir)

* Thu Jan 12 2012 Michael Pozhidaev <msp@altlinux.ru> 4.2-alt2
- Added tables for Russian language

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2-alt1_4.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_4
- initial release by fcimport
- build w/o tcl bindings
