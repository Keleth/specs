%define IF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define IF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define IF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define IF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"
%define IF_ver_eq() %if "%(rpmvercmp '%1' '%2')" == "0"
%define IF_ver_not_gt() %if "%(rpmvercmp '%1' '%2')" <= "0"
%define IF_ver_not_gteq() %if "%(rpmvercmp '%1' '%2')" < "0"
%define IF_ver_not_lt() %if "%(rpmvercmp '%2' '%1')" <= "0"
%define IF_ver_not_lteq() %if "%(rpmvercmp '%2' '%1')" < "0"
%define IF_ver_not_eq() %if "%(rpmvercmp '%1' '%2')" != "0"
%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module qtwebengine
%ifarch %ix86
%set_verify_elf_method relaxed
%endif
%def_enable always_reducing_debuginfo
%ifarch %ix86
%def_disable no_sse2
%else
%def_disable no_sse2
%endif
%def_disable python3

%define ffmpeg_ver %{get_version libavformat-devel}
#define is_ffmpeg %([ -n "`rpmquery --qf '%%{SOURCERPM}' libavformat-devel 2>/dev/null | grep -e '^libav'`" ] && echo 0 || echo 1)
#IF_ver_gteq %ffmpeg_ver 6
%def_disable system_ffmpeg
#else
#def_enable system_ffmpeg
#endif

Name: qt5-webengine
Version: 5.15.16
Release: alt4

Group: System/Libraries
Summary: Qt5 - QtWebEngine components
Url: http://qt.io/
License: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
ExclusiveArch: %qt5_qtwebengine_arches

Source: %qt_module-everywhere-src-%version.tar
Source100: pako.min.js
Source101: d3.min.js
# upstream
Patch1: chromium-icu-74.patch
# FC
Patch4:  qtwebengine-opensource-src-5.15.0-fix-extractcflag.patch
Patch5:  qtwebengine-everywhere-src-5.15.5-no-icudtl-dat.patch
Patch6:  qtwebengine-everywhere-src-5.10.1-no-sse2.patch
Patch7:  qtwebengine-opensource-src-5.9.2-arm-fpu-fix.patch
Patch8: qtwebengine-everywhere-src-5.11.3-aarch64-new-stat.patch
Patch9: qtwebengine-opensource-src-5.15.5-webrtc-neon-detect.patch
Patch10: qtwebengine-skia-missing-includes.patch
Patch11: 0001-avcodec-x86-mathops-clip-constants-used-with-shift-i.patch
# SuSE
Patch30: chromium-non-void-return.patch
Patch31: armv6-ffmpeg-no-thumb.patch
Patch32: disable-gpu-when-using-nouveau-boo-1005323.diff
# Debian
Patch41: verbose-gn-bootstrap.patch
Patch42: sandbox-time64-syscalls.patch
Patch43: disable-catapult.patch
Patch44: python3.patch
Patch45: chromium-python3.patch
Patch46: python3.11.patch
Patch47: system-nspr-prtime.patch
Patch48: system-icu-utf.patch
Patch49: system-lcms2.patch
Patch50: system-openjpeg2.patch
# ALT
Patch101: alt-pepflashplayer.patch
Patch102: alt-fix-shrank-by-one-character.patch
Patch103: qtwebengine-everywhere-src-5.15.0-chromium-add-ppc64le-support.patch
Patch104: qtwebengine-everywhere-src-5.15.0-add-ppc64le-support.patch
Patch105: alt-openh264-x86-no-asm.patch
Patch106: qtwebengine-everywhere-src-5.12.6-alt-armh.patch
Patch107: alt-js-check-size.patch

# Automatically added by buildreq on Sun Apr 03 2016
# optimized out: fontconfig fontconfig-devel gcc-c++ glib2-devel kf5-attica-devel kf5-kjs-devel libEGL-devel libGL-devel libX11-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXext-devel libXfixes-devel libXi-devel libXrandr-devel libXrender-devel libXtst-devel libfreetype-devel libgpg-error libharfbuzz-devel libharfbuzz-icu libicu-devel libnspr-devel libqt5-clucene libqt5-core libqt5-gui libqt5-help libqt5-network libqt5-positioning libqt5-qml libqt5-quick libqt5-sql libqt5-webchannel libqt5-widgets libstdc++-devel libxml2-devel pkg-config python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-multiprocessing python-modules-xml python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-phonon-devel qt5-tools qt5-webchannel-devel qt5-webkit-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-scrnsaverproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: git-core gperf kde5-akonadi-calendar-devel kde5-gpgmepp-devel kde5-kalarmcal-devel kde5-kblog-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-pimlibs-devel kde5-syndication-devel kf5-bluez-qt-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kplotting-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-kxmlrpcclient-devel kf5-libkscreen-devel kf5-modemmanager-qt-devel kf5-networkmanager-qt-devel kf5-solid-devel kf5-sonnet-devel kf5-threadweaver-devel libalsa-devel libcap-devel libdbus-devel libevent-devel libexpat-devel libjpeg-devel libminizip-devel libnss-devel libopus-devel libpci-devel libpng-devel libprotobuf-devel libpulseaudio-devel libre2-devel libsnappy-devel libsrtp-devel libvpx-devel libwebp-devel libxslt-devel ninja-build protobuf-compiler python-module-google python-module-simplejson python-modules-json python3-dev qt5-connectivity-devel qt5-multimedia-devel qt5-script-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-webengine-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel ruby ruby-stdlibs yasm
BuildRequires(pre): rpm-macros-qt5 rpm-macros-qt5-webengine qt5-tools
BuildRequires(pre): libavformat-devel
BuildRequires: libstdc++-devel-static
BuildRequires: libxkbcommon-devel
%if_enabled system_ffmpeg
BuildRequires: libavcodec-devel libavutil-devel libavformat-devel
%endif
BuildRequires: libvpx-devel libopus-devel pipewire-libs-devel
BuildRequires: /proc
BuildRequires: flex libicu-devel libEGL-devel
BuildRequires: libgio-devel libkrb5-devel
BuildRequires: git-core gperf libalsa-devel libcap-devel libdbus-devel libevent-devel libexpat-devel libjpeg-devel pkgconfig(libopenjp2) libminizip-devel libnss-devel
BuildRequires: libharfbuzz-devel fontconfig-devel
BuildRequires: libdrm-devel gyp libudev-devel libxml2-devel jsoncpp-devel liblcms2-devel
BuildRequires: libopus-devel libpci-devel libpng-devel libprotobuf-devel libpulseaudio-devel libre2-devel libsnappy-devel libsrtp2-devel
BuildRequires: libwebp-devel libxslt-devel ninja-build protobuf-compiler libva-devel libvdpau-devel
BuildRequires: node-yargs node-terser
%if_enabled python3
BuildRequires: python3-devel python3(six.moves)
%else
BuildRequires: python-devel python-modules-json
%endif
BuildRequires: qt5-connectivity-devel qt5-multimedia-devel qt5-script-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel
BuildRequires: qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel
BuildRequires: qt5-phonon-devel

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: qt5-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: %name-devel
%description devel-static
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-webengine
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common
Requires: libqt5-core = %_qt5_version
Requires: qt5-quickcontrols2
%description -n libqt5-webengine
%summary

%package -n libqt5-webenginecore
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common
Requires: libqt5-core = %_qt5_version
Requires: qt5-quickcontrols2
%description -n libqt5-webenginecore
%summary

%package -n libqt5-webenginewidgets
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common
Requires: libqt5-core = %_qt5_version
Requires: qt5-quickcontrols2
%description -n libqt5-webenginewidgets
%summary

%package -n libqt5-pdf
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common
Requires: libqt5-core = %_qt5_version
%description -n libqt5-pdf
%summary

%package -n libqt5-pdfwidgets
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common
Requires: libqt5-core = %_qt5_version
%description -n libqt5-pdfwidgets
%summary

%prep
%define icu_ver %{get_version libicu-devel}
%IF_ver_gteq %icu_ver 5.9
%def_enable system_icu
%else
%def_disable system_icu
%endif
%setup -n %qt_module-everywhere-src-%version
ln -s /usr/include/nspr src/3rdparty/chromium/nspr4
#
pushd src/3rdparty/chromium
%patch1 -p1
popd
%patch4 -p1
%patch5 -p1
%if_enabled no_sse2
%patch6 -p1
%endif
#%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
#
#%patch30 -p1
%patch31 -p1
%patch32 -p1
#
%patch41 -p1
%patch42 -p1
%patch43 -p1
%if_enabled python3
%patch44 -p1
%patch45 -p1
%patch46 -p1
%endif
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
#
%patch101 -p1
%patch102 -p1
%patch103 -p1
#%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1

# delete all "toolprefix = " lines from build/toolchain/linux/BUILD.gn, as we
# never cross-compile in native Fedora RPMs, fixes ARM and aarch64 FTBFS
sed -i -e '/toolprefix = /d' -e 's/\${toolprefix}//g' \
  src/3rdparty/chromium/build/toolchain/linux/BUILD.gn
# http://bugzilla.redhat.com/1337585
# can't just delete, but we'll overwrite with system headers to be on the safe side
cp -bv /usr/include/re2/*.h src/3rdparty/chromium/third_party/re2/src/re2/
# add compile flags
sed -i 's|"-fPIC"|"-DPIC","-fPIC"|' src/3rdparty/chromium/build/config/compiler/BUILD.gn
sed -i 's|"-fPIC"|"-DPIC","-fPIC"|' src/3rdparty/chromium/third_party/*/BUILD.gn

%if_enabled always_reducing_debuginfo
sed -i -e 's/symbol_level=2/symbol_level=1/g' src/buildtools/config/common.pri
%endif
%ifnarch x86_64
# most arches run out of memory with full debuginfo, so use -g1 on non-x86_64
sed -i -e 's/symbol_level=2/symbol_level=1/g' src/buildtools/config/common.pri
%endif
sed -i -e 's/symbol_level=[[:digit:]]/symbol_level=0/g' src/buildtools/config/common.pri


# redefine _FORTIFY_SOURCE
for f in \
    src/3rdparty/chromium/build/config/compiler/BUILD.gn \
    src/3rdparty/chromium/third_party/minigbm/src/common.mk
do
    sed -i 's|_FORTIFY_SOURCE=[[:digit:]]|_FORTIFY_SOURCE=1|g' $f
done

# install missing files
for f in \
    src/3rdparty/chromium/third_party/devtools-frontend/src/front_end/third_party/lighthouse/lighthouse-dt-bundle.js \
    src/3rdparty/chromium/third_party/devtools-frontend/src/front_end/third_party/lighthouse/report-assets/report-generator.js \
    src/3rdparty/chromium/third_party/devtools-frontend/src/front_end/diff/diff_match_patch.js \
    src/3rdparty/chromium/third_party/devtools-frontend/src/front_end/third_party/acorn/package/dist/acorn.js \
    src/3rdparty/chromium/third_party/catapult/common/py_vulcanize/third_party/rjsmin/bench/jsmin.py \
    src/3rdparty/chromium/third_party/web-animations-js/sources/web-animations-next-lite.min.js
do mkdir -p `dirname $f`; touch $f; done
mkdir -p src/3rdparty/chromium/third_party/catapult/tracing/third_party/pako/
install -m 0644 %SOURCE100 src/3rdparty/chromium/third_party/catapult/tracing/third_party/pako/
mkdir -p src/3rdparty/chromium/third_party/catapult/tracing/third_party/d3/
install -m 0644 %SOURCE101 src/3rdparty/chromium/third_party/catapult/tracing/third_party/d3/
pushd src/3rdparty/chromium/third_party/jstemplate
    cat util.js jsevalcontext.js jstemplate.js exports.js >jstemplate_compiled.js
popd

# generate qtwebengine-3rdparty.qdoc, it is missing from the tarball
pushd src/3rdparty
%if_enabled python3
%__python3 \
%else
%__python \
%endif
  chromium/tools/licenses.py \
  --file-template ../../tools/about_credits.tmpl \
  --entry-template ../../tools/about_credits_entry.tmpl \
  credits >../webengine/doc/src/qtwebengine-3rdparty.qdoc
popd

# copy the Chromium license so it is installed with the appropriate name
cp -p src/3rdparty/chromium/LICENSE LICENSE.Chromium

# fix find system ninja
mkdir -p bin
ln -s %_bindir/ninja-build bin/ninja
# fix find system python
%if_enabled python3
ln -s %__python3 bin/python
%else
ln -s %__python bin/python
%endif

syncqt.pl-qt5  -version %version

%build
ulimit -n $(ulimit -Hn) ||:
%add_optflags %optflags_shared -Wno-error=return-type
export PATH=$PWD/bin:$PATH
%if_enabled no_sse2
# workaround against linking
mkdir -p %_target_platform/lib
ln -s ../src/core/Release/lib/libv8.so %_target_platform/lib/libv8.so
%endif
NUM_PROCS="%__nprocs"
cat /proc/meminfo | grep ^Mem
cat /sys/fs/cgroup/user.slice/user-${UID}.slice/memory.max ||:
cat /sys/fs/cgroup/user.slice/user-${UID}.slice/memory.high ||:
ulimit -a | grep mem
MEM_PER_PROC=10000000
MAX_MEM=`grep ^MemTotal: /proc/meminfo | sed -e 's|^\(.*\)[[:space:]].*|\1|' -e 's|.*[[:space:]]||'`
#NUM_PROCS="$(($MAX_MEM / $MEM_PER_PROC))"
[ "$NUM_PROCS" -ge 2  ] || NUM_PROCS=2
[ "$NUM_PROCS" -le 16  ] || NUM_PROCS=16

export NPROCS=$NUM_PROCS
export STRIP=strip
export NINJAFLAGS="-v -j $NUM_PROCS"
export NINJA_PATH=%_bindir/ninja-build
OPTFLAGS="%optflags"
%if_enabled always_reducing_debuginfo
export OPTFLAGS=`echo "$OPTFLAGS" | sed -e 's/ -g / -g1 /g'`
%endif
%ifnarch x86_64
# most arches run out of memory with full debuginfo, so use -g1 on non-x86_64
export OPTFLAGS=`echo "$OPTFLAGS" | sed -e 's/ -g / -g1 /g'`
%endif
export RPM_OPT_FLAGS="$OPTFLAGS"
export CFLAGS="$OPTFLAGS" CXXFLAGS="$OPTFLAGS"

mkdir -p %_target_platform
pushd %_target_platform
#    CONFIG+=" webcore_debug v8base_debug" \
%_qt5_qmake \
    QMAKE_CFLAGS="$CFLAGS" \
    QMAKE_CXXFLAGS="$CXXFLAGS" \
    QMAKE_LFLAGS+="-Wl,--no-keep-memory -Wl,--hash-size=31 -Wl,--reduce-memory-overheads" \
%ifarch %ix86
    QMAKE_LFLAGS+=-Wl,-z,notext \
%endif
    QMAKE_EXTRA_ARGS+="-proprietary-codecs -feature-webengine-system-libvpx -feature-webengine-system-openjpeg2" \
    QMAKE_EXTRA_ARGS+="-webengine-jumbo-build 0 -system-opus -system-webp -webengine-kerberos" \
%if_enabled system_icu
    QMAKE_EXTRA_ARGS+="-system-webengine-icu" \
%endif
%if_enabled system_ffmpeg
    QMAKE_EXTRA_ARGS+="-system-webengine-ffmpeg" \
    QMAKE_EXTRA_ARGS+="-webengine-webrtc-pipewire" \
%endif
    ..
#(while true; do date; sleep 7m; done) &
%make_build -Onone
%if %qdoc_found
export QT_HASH_SEED=0
%make docs
%endif
popd

%install
%install_qt5 -C %_target_platform
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs -C %_target_platform ||:
%endif

%if_disabled system_icu
install -m 0644 \
    src/3rdparty/chromium/third_party/icu/common/icudtl.dat \
    %buildroot/%_qt5_datadir/resources/
%endif

# fix cmake dependencies
%IF_ver_not_eq %_qt5_version %version
sed -i -e \
  "s|%version[[:space:]][[:space:]]*\${_Qt5WebEngine\(.*_FIND_VERSION_EXACT\)|%_qt5_version \${_Qt5WebEngine\1|" \
  %buildroot/%_libdir/cmake/Qt5WebEngine*/Qt5WebEngine*Config.cmake
%endif

# find translations
echo "%%defattr(644,root,root,755)" >translations_list.lang
find %buildroot/%_qt5_translationdir/qtwebengine_locales -type f -name \*.pak | \
while read t
do
    lang_file=`basename $t`
    lang_name=`echo "$lang_file" | sed -e 's|\.pak$||' -e 's|-|_|'`
    if echo $lang_name | grep -q ^en
    then
	echo "%%_qt5_translationdir/qtwebengine_locales/$lang_file" >>translations_list.lang
    else
	echo "%%lang($lang_name) %%_qt5_translationdir/qtwebengine_locales/$lang_file" >>translations_list.lang
    fi
done

%files common -f translations_list.lang
%doc LICENSE.* LICENSE*EXCEPT*
%dir %_qt5_translationdir/qtwebengine_locales/
%dir %_qt5_datadir/resources/
%_qt5_datadir/resources/qtwebengine*.pak
%if_disabled system_icu
%_qt5_datadir/resources/*icu*
%endif

%files -n libqt5-webengine
%_qt5_libdir/libQt?WebEngine.so.*
%_qt5_qmldir/QtWebEngine/
%files -n libqt5-webenginecore
%_qt5_libdir/libQt?WebEngineCore.so.*
%if_enabled no_sse2
%_qt5_libdir/qtwebengine/
%endif
%_qt5_libexecdir/QtWebEngineProcess
%files -n libqt5-webenginewidgets
%_qt5_libdir/libQt?WebEngineWidgets.so.*
%files -n libqt5-pdf
%_qt5_libdir/libQt?Pdf.so.*
%_qt5_plugindir/imageformats/libqpdf.so
%_qt5_qmldir/QtQuick/Pdf/
%files -n libqt5-pdfwidgets
%_qt5_libdir/libQt?PdfWidgets.so.*

%files doc
%if %qdoc_found
%_qt5_docdir/*
%endif
%_qt5_examplesdir/*

%files devel
%_bindir/qwebengine_convert_dict*
%_qt5_bindir/qwebengine_convert_dict*
#
%_qt5_plugindir/designer/libqwebengineview.so
%_qt5_headerdir/QtWebEngine/
%_qt5_headerdir/QtWebEngineCore/
%_qt5_headerdir/QtWebEngineWidgets/
%_qt5_headerdir/QtPdf/
%_qt5_headerdir/QtPdfWidgets/
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/qt_*.pri

%changelog
* Fri Apr 12 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.16-alt4
- always use internal ffmpeg

* Fri Apr 12 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.16-alt3
- update build requires

* Mon Jan 22 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.16-alt2
- build with python2

* Wed Jan 10 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.16-alt1
- new version

* Thu Nov 23 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.15-alt2
- fix to build with icu-74

* Mon Sep 11 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.15-alt1
- new version

* Mon Jul 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.14-alt1
- new version

* Thu Apr 27 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.13-alt2
- fix to build with new icu

* Thu Mar 23 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.13-alt1
- new version

* Wed Jan 18 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.12-alt1
- new version

* Mon Oct 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.11-alt1
- new version

* Wed Jul 06 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.10-alt1
- new version

* Wed Jul 06 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.9-alt2
- add workaround agains build system open descriptors limit

* Mon Apr 18 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.9-alt1
- new version

* Thu Jan 20 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.8-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt1
- new version

* Wed Oct 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.6-alt3
- add fix against glibc-2.34

* Thu Sep 23 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.6-alt2
- don't apply harfbuzz patches with old harfbuzz

* Wed Sep 22 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.6-alt1
- new version

* Wed Sep 22 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt6
- fix to build with new harfbuz

* Fri Aug 20 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt1
- new version

* Fri Aug 20 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt4
- fix debug output when build (thanks iv@alt)

* Tue Jun 29 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt3
- fix compile

* Wed Jun 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt2
- fix to build with icu-69

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt1
- new version

* Thu Sep 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt1
- new version

* Wed Jul 29 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt2
- build with restored ppc64le support (thanks glebfm@alt)

* Wed Jul 29 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.15.0-alt0.ppc64le
- Restored ppc64le support.

* Fri Jul 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Fri Jul 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt2
- tune build for p9

* Mon Jun 22 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt1
- new version

* Thu Apr 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Thu Apr 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.12.7-alt2
- fix build on armh arch

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Mon Oct 21 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt2
- build internal chromium with additional codecs

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Thu Jun 27 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.12.4-alt2
- Added ppc64le support (tnx for patches to Timothy Pearson and
  Shawn Anastasio).

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Tue Mar 19 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt2
- update chromium

* Mon Mar 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Wed Feb 27 2019 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt3
- update build requires

* Tue Feb 12 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.11.3-alt2
- Added ExclusiveArch: %%qt5_qtwebengine_arches (to disable build
  on architectures webengine does't support).

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Wed Oct 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt2
- rebuild with new icu

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1
- new version

* Thu Sep 06 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt4
- rebuild with new libevent

* Tue Aug 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt3
- rebuild with new Qt

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt2
- rebuild with new icu

* Tue Jun 19 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1
- new version

* Mon Jun 18 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.10.1-alt3
- rebuild with new Qt

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.10.1-alt2
- rebuild with new Qt
- sync FC patches

* Fri Feb 16 2018 Sergey V Turchin <zerg@altlinux.org> 5.10.1-alt1.1
- don't use old system icu

* Wed Feb 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.10.1-alt1
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt2
- fix cmake dependencies

* Wed Jan 31 2018 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1
- new version

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Apr 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt2
- fix find flash plugin
- properly package translations

* Tue Mar 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- initial build
