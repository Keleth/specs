%def_enable  ffmpeg
%def_enable  google_api_keys

%ifndef build_parallel_jobs
%global build_parallel_jobs %__nprocs
%endif

%global llvm_version 18.1

%set_verify_elf_method rpath=relaxed textrel=relaxed lfs=relaxed lint=relaxed
%add_debuginfo_skiplist %_libdir/* %_bindir/*

%define _unpackaged_files_terminate_build 1

# Leave this alone, please.
%global target out/Release

# Set up Google API keys, see http://www.chromium.org/developers/how-tos/api-keys .
# Note: these are for ALT Linux use ONLY. For your own distribution,
# please get your own set of keys.
%define api_key               AIzaSyAIIWz7zaCwYcUSe3ZaRPviXjMjkBP4-xY
%define default_client_id     1018394967181.apps.googleusercontent.com
%define default_client_secret h_PrTP1ymJu83YTLyz-E25nP

Name:           chromium
Version:        124.0.6367.207
Release:        alt1

Summary:        An open source web browser developed by Google
License:        BSD-3-Clause and LGPL-2.1+
Group:          Networking/WWW
Url:            https://www.chromium.org

# Get sources from https://chromium.woolyss.com/
Source0:        chromium.tar.zst

Source30:       master_preferences
Source31:       default_bookmarks.html
Source100:      chromium.sh
Source101:      chromium.desktop
Source102:      chromium.xml
Source200:      chromium.default

Provides:       chromium-browser = %version
Obsoletes:      chromium-browser < %version
Obsoletes:      chromium-stable <= %version

Provides:       webclient

Obsoletes:      chromium-password
Obsoletes:      chromium-kde
Obsoletes:      chromium-gnome
Obsoletes:      chromium-desktop-kde
Obsoletes:      chromium-desktop-gnome

ExclusiveArch: x86_64 aarch64

### Start Patches
Patch001: 0001-OPENSUSE-enables-reading-of-the-master-preference.patch
Patch002: 0002-ALT-Set-appropriate-desktop-file-name-for-default-br.patch
Patch003: 0003-DEBIAN-manpage-fixes.patch
Patch004: 0004-DEBIAN-add-ps-printing-capability-gtk2.patch
Patch005: 0005-ALT-Use-rpath-link-and-absolute-rpath.patch
Patch006: 0006-ALT-allow-to-override-clang-through-env-variables.patch
Patch007: 0007-ALT-Hack-to-avoid-build-error-with-clang7.patch
Patch008: 0008-FEDORA-bootstrap-with-python3.patch
Patch009: 0009-ALT-use-system-zlib.patch
Patch010: 0010-ALT-use-system-libdrm-library.patch
Patch011: 0011-DEBIAN-allow-building-against-system-libraries-even-.patch
Patch012: 0012-DEBIAN-use-system-zlib-library-instead-of-embedded-l.patch
Patch013: 0013-DEBIAN-use-system-opus-library-instead-of-embedded.patch
Patch014: 0014-DEBIAN-build-using-system-openjpeg.patch
Patch015: 0015-DEBIAN-use-system-jpeg-library.patch
Patch016: 0016-DEBIAN-use-system-libevent-library.patch
Patch017: 0017-DEBIAN-work-around-a-clang-bug-with-libstdc.patch
Patch018: 0018-Use-yandex-search-as-default.patch
Patch019: 0019-GENTOO-EnumTable-crash.patch
Patch020: 0020-ALT-Do-not-hardcode-flatbuffer-version.patch
Patch021: 0021-FEDORA-System-brotli.patch
Patch022: 0022-Revert-Use-aggregate-init-designed-initializers-more.patch
Patch023: 0023-Add-missing-headers.patch
Patch024: 0024-Disable-unsupported-compiler-flags.patch
Patch025: 0025-Fix-rust-clang-path.patch
Patch026: 0026-DEBIAN-remove-dependencies-on-third_party-catapult.patch
Patch027: 0027-Use-system-sysroot-for-rust.patch
Patch028: 0028-DEBIAN-work-around-incorrect-template-selection.patch
Patch029: 0029-nullptr_t-without-namespace-std.patch
Patch030: 0030-Fix-undefined-symbol-partition_alloc-internal-Intern.patch
Patch031: 0031-FEDORA-disable-screen-ai-service.patch
Patch032: 0032-FEDORA-libavif-deps.patch
Patch033: 0033-ALT-rename-std::powf.patch
Patch034: 0034-DEBIAN-uint-includes.patch
Patch035: 0035-DEBIAN-fps-optional.patch
Patch036: 0036-DEBIAN-span-optional.patch
Patch037: 0037-DEBIAN-webgpu-optional.patch
Patch038: 0038-DEBIAN-extractor-bitset.patch
Patch039: 0039-DEBIAN-atomic.patch
#Patch040: 0040-ALT-ninja-build1.12.patch
### End Patches

BuildRequires: /proc
BuildRequires: /dev/shm

BuildRequires:  bison
BuildRequires:  brotli
BuildRequires:  bzlib-devel
BuildRequires:  chrpath
BuildRequires:  elfutils
BuildRequires:  flex
BuildRequires:  glibc-kernheaders
BuildRequires:  gperf
BuildRequires:  libcups-devel
BuildRequires:  libdouble-conversion-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libstdc++-devel-static
BuildRequires:  ninja-build
BuildRequires:  node
BuildRequires:  nvidia-settings-devel
BuildRequires:  perl-Switch
BuildRequires:  pkg-config
BuildRequires:  usbids
BuildRequires:  xdg-utils
BuildRequires:  clang%{llvm_version}
BuildRequires:  clang%{llvm_version}-devel
BuildRequires:  llvm%{llvm_version}-devel
BuildRequires:  lld%{llvm_version}-devel
BuildRequires:  pkgconfig(absl_utility)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(cairo) >= 1.6
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(flatbuffers)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libhwy)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwoff2dec)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
%if_enabled ffmpeg
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(opus)
%endif

BuildRequires:  python3
BuildRequires:  python3(bs4)
BuildRequires:  python3(html5lib)
BuildRequires:  python3(markupsafe)
BuildRequires:  python3(ply)
BuildRequires:  python3(simplejson)

BuildRequires:  rust       >= 1.75.0-alt2
BuildRequires:  rust-cargo >= 1.75.0-alt2

# We do not build an internal version of libvulkan but we want to have it on the
# system.
#Requires: libvulkan1

Requires: libva
Requires: xdg-utils

%description
Chromium is an open-source browser project that aims to build a safer,
faster, and more stable way for all Internet users to experience the web.

%prep
%setup -q -n chromium
%autopatch -p1

sed -i \
        -e 's/"-ffile-compilation-dir=."//g' \
        -e 's/"-no-canonical-prefixes"//g' \
        -e 's/"-no-opaque-pointers",//g' \
        build/config/compiler/BUILD.gn

mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s %_bindir/node third_party/node/linux/node-linux-x64/bin/node

mkdir -p buildtools/third_party/eu-strip/bin
ln -sf %_bindir/eu-strip buildtools/third_party/eu-strip/bin/eu-strip

rm -f -- third_party/depot_tools/ninja
ln -s %_bindir/ninja third_party/depot_tools/ninja
ln -s %_bindir/python3 third_party/depot_tools/python


%build
export ALTWRAP_LLVM_VERSION="%llvm_version"
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
export RANLIB="llvm-ranlib"
export LLVM_PREFIX=`llvm-config --prefix`
export LLVM_LIBDIR=`llvm-config --libdir`
export CLANG_MAJVER=`echo %llvm_version | cut -d. -f1`
export CLANG_LIBDIR="$LLVM_LIBDIR/clang/$CLANG_MAJVER/lib"

bits=$(getconf LONG_BIT)

export PATH="$PWD/third_party/depot_tools:$PATH"
export CHROMIUM_RPATH="%_libdir/%name"

FLAGS=
FLAGS+=' -Wno-unknown-warning-option -Wno-deprecated-declarations'
FLAGS+=' -Wno-unused-command-line-argument -Wno-unused-but-set-variable'
FLAGS+=' -Wno-unused-result -Wno-unused-function -Wno-unused-variable'
FLAGS+=' -Wno-unused-const-variable -Wno-unneeded-internal-declaration'
FLAGS+=' -Wno-unknown-attributes'
FLAGS+=' -DUSE_SYSTEM_MINIZIP'

export CFLAGS="$FLAGS"
export CXXFLAGS="$FLAGS"

gn_arg=()
gn_arg+=( custom_toolchain=\"//build/toolchain/linux/unbundle:default\" )
gn_arg+=( host_toolchain=\"//build/toolchain/linux/unbundle:default\" )
gn_arg+=( is_official_build=true )
gn_arg+=( use_custom_libcxx=false )
gn_arg+=( use_sysroot=false )
gn_arg+=( use_gio=true )
gn_arg+=( use_glib=true )
gn_arg+=( use_libpci=true )
gn_arg+=( use_pulseaudio=true )
gn_arg+=( use_cups=true )
gn_arg+=( use_kerberos=true )
gn_arg+=( use_gold=false )
gn_arg+=( use_vaapi=true )
gn_arg+=( use_system_freetype=true )
gn_arg+=( use_system_harfbuzz=true )
gn_arg+=( use_system_lcms2=true )
gn_arg+=( use_system_libffi=true )
gn_arg+=( use_system_libdrm=true )
gn_arg+=( use_system_libjpeg=true )
gn_arg+=( use_system_libopenjpeg2=true )
gn_arg+=( use_system_libpng=true )
gn_arg+=( use_system_minigbm=true )
gn_arg+=( use_system_zlib=true )
gn_arg+=( use_bundled_weston=false )
gn_arg+=( use_xkbcommon=true )
gn_arg+=( use_icf=false )
gn_arg+=( enable_linux_installer=false )
gn_arg+=( optimize_webui=false )
gn_arg+=( link_pulseaudio=true )
gn_arg+=( enable_hangout_services_extension=true )
gn_arg+=( treat_warnings_as_errors=false )
gn_arg+=( fatal_linker_warnings=false )
gn_arg+=( system_libdir=\"%_lib\" )
gn_arg+=( enable_nocompile_tests=false )

# toolkit
gn_arg+=( use_qt=false )
gn_arg+=( use_gtk=true )
gn_arg+=( gtk_version=4 )

# ozone
gn_arg+=( use_ozone=true )
gn_arg+=( ozone_platform=\"x11\" )
gn_arg+=( ozone_platform_x11=true )
gn_arg+=( ozone_platform_wayland=true )
#gn_arg+=( angle_enable_gl=true )
#gn_arg+=( angle_enable_vulkan=true )

# ffmpeg
gn_arg+=( ffmpeg_branding=\"Chrome\" )
gn_arg+=( proprietary_codecs=true )

# Remove debug
gn_arg+=( is_debug=false )
gn_arg+=( dcheck_always_on=false )
gn_arg+=( dcheck_is_configurable=false )
gn_arg+=( symbol_level=0 )
gn_arg+=( blink_symbol_level=0 )
gn_arg+=( v8_symbol_level=0 )

gn_arg+=( enable_nacl=false )
gn_arg+=( is_component_ffmpeg=false )
gn_arg+=( is_component_build=false )
gn_arg+=( enable_widevine=true )

gn_arg+=( rtc_use_pipewire=true )
gn_arg+=( rtc_link_pipewire=true )

gn_arg+=( clang_base_path=\"$LLVM_PREFIX\" )
gn_arg+=( is_clang=true )
gn_arg+=( clang_use_chrome_plugins=false )
gn_arg+=( use_lld=true )
if [ "$bits" = 64 ]; then
    gn_arg+=( use_thin_lto=true )
    gn_arg+=( thin_lto_enable_optimizations=true )
else
    gn_arg+=( use_thin_lto=false )
    gn_arg+=( thin_lto_enable_optimizations=false )
fi
gn_arg+=( is_cfi=false )
gn_arg+=( use_cfi_icall=false )
gn_arg+=( chrome_pgo_phase=0 )

# use system rust
export RUSTC_BOOTSTRAP=1
gn_arg+=( rust_sysroot_absolute=\"$(rustc --print sysroot)\" )
gn_arg+=( rustc_version=\"$(rustc --version)\" )

%ifnarch x86_64
gn_arg+=( icu_use_data_file=false )
%endif

%ifnarch x86_64 aarch64
gn_arg+=( enable_vulkan=false )
%else
gn_arg+=( enable_vulkan=true )
%endif

%if_enabled google_api_keys
### From 2013 until early 2021, Google permitted distribution builds of
### Chromium to access Google APIs that added significant features to
### Chromium including, but not limited to, Sync and geolocation.
### As of March 15, 2021, any Chromium builds which pass client_id and/or
### client_secret during build will prevent end-users from signing into their
### Google account.
###
### I have removed the calls to "google_default_client_id"
### and "google_default_client_secret" to comply with their changes.
###
### We can still use the api key though. For now.
gn_arg+=( google_api_key=\"%api_key\" )

#gn_arg+=( google_default_client_id=\"%default_client_id\" )
#gn_arg+=( google_default_client_secret=\"%default_client_secret\" )
%endif

# Remove bundled libraries for which we will use the system copies.
.rpm/scripts/unbundle

tools/gn/bootstrap/bootstrap.py --gn-gen-args="${gn_arg[*]}" --build-path=%target
%target/gn --script-executable=%__python3 gen --args="${gn_arg[*]}" %target

n=%build_parallel_jobs
[ "$n" -lt 20 ] || n=20

for name in chrome chrome_sandbox chromedriver policy_templates; do
	export NINJA_STATUS="[$name %%f/%%t] "
	ninja -vvv -j "$n" -C %target $name
done


%install
mkdir -p -- \
	%buildroot/%_bindir \
	%buildroot/%_man1dir \
	%buildroot/%_libdir/%name \
	%buildroot/%_sysconfdir/%name \
#
install -m 755 %SOURCE100 %buildroot%_bindir/%name
install -m 644 %SOURCE200 %buildroot%_sysconfdir/%name/default

# add directories for policy management
mkdir -p %buildroot%_sysconfdir/%name/policies/managed
mkdir -p %buildroot%_sysconfdir/%name/policies/recommended

# compatibility symlink
ln -s %name %buildroot/%_bindir/chromium-browser

# manpage
.rpm/scripts/make-manpage.sh > %buildroot/%_man1dir/%name.1
ln -s %name.1  %buildroot/%_man1dir/chrome.1

pushd %target
cp -a chrome           %buildroot%_libdir/%name/%name
cp -a chrome_sandbox   %buildroot%_libdir/%name/chrome-sandbox
cp -a chrome_crashpad_handler %buildroot%_libdir/%name/chrome_crashpad_handler

for chromedriver in chromedriver chromedriver.unstripped; do
	[ ! -x $chromedriver ] || break
done

cp -a $chromedriver %buildroot%_libdir/%name/chromedriver
strip %buildroot%_libdir/%name/chromedriver

ln -s -- %_libdir/%name/chromedriver %buildroot/%_bindir/chromedriver

for f in *.bin *.so* *.pak swiftshader locales icudtl.dat MEIPreload vk_swiftshader_icd.json; do
	[ ! -e "$f" ] ||
		cp -at %buildroot%_libdir/%name -- "$f"
done
popd

# Remove garbage
find %buildroot%_libdir/%name -name '*.TOC' -delete
find %buildroot%_libdir/%name/locales -name '*.pak.info' -delete

# Icons
for size in 24 48 64 128 256; do
	install -Dm644 "chrome/app/theme/chromium/product_logo_$size.png" \
		"%buildroot/%_iconsdir/hicolor/${size}x${size}/apps/%name.png"
done
for size in 16 32; do
	install -Dm644 "chrome/app/theme/default_100_percent/chromium/product_logo_$size.png" \
		"%buildroot/%_iconsdir/hicolor/${size}x${size}/apps/%name.png"
done

# Desktop file
install -Dm0644 %SOURCE101 %buildroot/%_desktopdir/%name.desktop

mkdir -p -- %buildroot%_datadir/gnome-control-center/default-apps/
cp -a %SOURCE102 %buildroot%_datadir/gnome-control-center/default-apps/%name.xml

# link to browser plugin path.  Plugin patch doesn't work. Why?
mkdir -p -- %buildroot%_libdir/browser-plugins
ln -s -- %_libdir/browser-plugins %buildroot%_libdir/%name/plugins

# Install the master_preferences file
mkdir -p -- %buildroot%_sysconfdir/%name
install -m 0644 %SOURCE30 %buildroot%_sysconfdir/%name
install -m 0644 %SOURCE31 %buildroot%_sysconfdir/%name

# Set alternative to xbrowser
mkdir -p -- %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xbrowser	%_bindir/%name	50
%_bindir/x-www-browser	%_bindir/%name	50
EOF

(set +x;
	find %buildroot/%_libdir/%name -type f |
	while read f; do
		t="$(readlink -ev "$f")"

		file "$t" | grep -Fqs ELF || continue

		# Strip Chromium executables to disable debuginfo generation (became too huge)
		#strip -d "$t" ||:

		# Add real RPATH
		chrpath -r '%_libdir/%name' "$t" ||:
	done
)


%files
%doc AUTHORS LICENSE
%dir %_datadir/gnome-control-center/default-apps
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/policies
%dir %_sysconfdir/%name/policies/managed
%dir %_sysconfdir/%name/policies/recommended
%config %_sysconfdir/%name/*
%attr(4711,root,root) %_libdir/%name/chrome-sandbox
%_libdir/%name
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%_datadir/gnome-control-center/default-apps/*.xml
%_iconsdir/hicolor/*/apps/*.png
%_altdir/%name

%changelog
* Tue May 14 2024 Andrey Cherepanov <cas@altlinux.org> 124.0.6367.207-alt1
- New version (124.0.6367.207).
- Security fixes:
  + CVE-2024-4761: Out of bounds write in V8.

* Sun May 12 2024 Andrey Cherepanov <cas@altlinux.org> 124.0.6367.201-alt1
- New version (124.0.6367.201).
- Security fixes:
  + CVE-2024-4671: Use after free in Visuals.

* Thu May 09 2024 Andrey Cherepanov <cas@altlinux.org> 124.0.6367.155-alt1
- New version (124.0.6367.155).
- Security fixes:
  + CVE-2024-4558: Use after free in ANGLE.
  + CVE-2024-4559: Heap buffer overflow in WebAudio.
- Built using LLVM 18.1.

* Wed May 01 2024 Andrey Cherepanov <cas@altlinux.org> 124.0.6367.118-alt1
- New version (124.0.6367.118).
- Security fixes:
  + CVE-2024-4331: Use after free in Picture In Picture.
  + CVE-2024-4368: Use after free in Dawn.

* Thu Apr 25 2024 Andrey Cherepanov <cas@altlinux.org> 124.0.6367.78-alt1
- New version (124.0.6367.78).
- Security fixes:
  + CVE-2024-4058: Type Confusion in ANGLE.
  + CVE-2024-4059: Out of bounds read in V8 API.
  + CVE-2024-4060: Use after free in Dawn.

* Sat Apr 20 2024 Andrey Cherepanov <cas@altlinux.org> 124.0.6367.60-alt1
- New version (124.0.6367.60).
- Security fixes:
  + CVE-2024-3832: Object corruption in V8.
  + CVE-2024-3833: Object corruption in WebAssembly.
  + CVE-2024-3914: Use after free in V8.
  + CVE-2024-3834: Use after free in Downloads.
  + CVE-2024-3837: Use after free in QUIC.
  + CVE-2024-3838: Inappropriate implementation in Autofill.
  + CVE-2024-3839: Out of bounds read in Fonts.
  + CVE-2024-3840: Insufficient policy enforcement in Site Isolation.
  + CVE-2024-3841: Insufficient data validation in Browser Switcher.
  + CVE-2024-3843: Insufficient data validation in Downloads.
  + CVE-2024-3844: Inappropriate implementation in Extensions.
  + CVE-2024-3845: Inappropriate implementation in Network.
  + CVE-2024-3846: Inappropriate implementation in Prompts.
  + CVE-2024-3847: Insufficient policy enforcement in WebUI.

* Sat Apr 13 2024 Andrey Cherepanov <cas@altlinux.org> 123.0.6312.122-alt1
- New version (123.0.6312.122).
- Security fixes:
  + CVE-2024-3157: Out of bounds write in Compositing.
  + CVE-2024-3516: Heap buffer overflow in ANGLE.
  + CVE-2024-3515: Use after free in Dawn.
- Use vaapi flags from Fedora defaults.

* Wed Mar 27 2024 Andrey Cherepanov <cas@altlinux.org> 123.0.6312.86-alt1
- New version (123.0.6312.86).
- Security fixes:
  + CVE-2024-2883: Use after free in ANGLE.
  + CVE-2024-2885: Use after free in Daw.
  + CVE-2024-2886: Use after free in WebCodecs.
  + CVE-2024-2887: Type Confusion in WebAssembly.

* Thu Mar 21 2024 Alexey Gladkov <legion@altlinux.ru> 123.0.6312.58-alt1
- New version (123.0.6312.58).
- Security fixes:
  - CVE-2024-2173: Out of bounds memory access in V8.
  - CVE-2024-2174: Inappropriate implementation in V8.
  - CVE-2024-2176: Use after free in FedCM.
  - CVE-2024-2400: Use after free in Performance Manager.
  - CVE-2024-2625: Object lifecycle issue in V8.
  - CVE-2024-2626: Out of bounds read in Swiftshader.
  - CVE-2024-2627: Use after free in Canvas.
  - CVE-2024-2628: Inappropriate implementation in Downloads.
  - CVE-2024-2629: Incorrect security UI in iOS.
  - CVE-2024-2630: Inappropriate implementation in iOS.
  - CVE-2024-2631: Inappropriate implementation in iOS.

* Wed Feb 28 2024 Alexey Gladkov <legion@altlinux.ru> 122.0.6261.94-alt1
- New version (122.0.6261.94).
- Security fixes:
  - CVE-2024-1669: Out of bounds memory access in Blink.
  - CVE-2024-1670: Use after free in Mojo.
  - CVE-2024-1671: Inappropriate implementation in Site Isolation.
  - CVE-2024-1672: Inappropriate implementation in Content Security Policy.
  - CVE-2024-1673: Use after free in Accessibility.
  - CVE-2024-1674: Inappropriate implementation in Navigation.
  - CVE-2024-1675: Insufficient policy enforcement in Download.
  - CVE-2024-1676: Inappropriate implementation in Navigation.
  - CVE-2024-1938: Type Confusion in V8.
  - CVE-2024-1939: Type Confusion in V8.

* Thu Feb 08 2024 Alexey Gladkov <legion@altlinux.ru> 121.0.6167.160-alt1
- New version (121.0.6167.160).
- Security fixes:
  - CVE-2024-1283: Heap buffer overflow in Skia.
  - CVE-2024-1284: Use after free in Mojo.

* Thu Feb 08 2024 Alexey Gladkov <legion@altlinux.ru> 121.0.6167.139-alt1
- New version (121.0.6167.139).
- Security fixes:
  - CVE-2024-1059: Use after free in WebRTC.
  - CVE-2024-1060: Use after free in Canvas.
  - CVE-2024-1077: Use after free in Network.

* Wed Jan 24 2024 Alexey Gladkov <legion@altlinux.ru> 121.0.6167.85-alt1
- New version (121.0.6167.85).
- Security fixes:
  - CVE-2024-0804: Insufficient policy enforcement in iOS Security UI.
  - CVE-2024-0805: Inappropriate implementation in Downloads.
  - CVE-2024-0806: Use after free in Passwords.
  - CVE-2024-0807: Use after free in WebAudio.
  - CVE-2024-0808: Integer underflow in WebUI.
  - CVE-2024-0809: Inappropriate implementation in Autofill.
  - CVE-2024-0810: Insufficient policy enforcement in DevTools.
  - CVE-2024-0811: Inappropriate implementation in Extensions API.
  - CVE-2024-0812: Inappropriate implementation in Accessibility.
  - CVE-2024-0813: Use after free in Reading Mode.
  - CVE-2024-0814: Incorrect security UI in Payments.

* Mon Dec 18 2023 Alexey Gladkov <legion@altlinux.ru> 120.0.6099.109-alt2
- Bring back optimization flags.

* Sat Dec 16 2023 Alexey Gladkov <legion@altlinux.ru> 120.0.6099.109-alt1
- New version (120.0.6099.109).
- Security fixes:
  - CVE-2023-6702: Type Confusion in V8.
  - CVE-2023-6703: Use after free in Blink.
  - CVE-2023-6704: Use after free in libavif.
  - CVE-2023-6705: Use after free in WebRTC.
  - CVE-2023-6706: Use after free in FedCM.
  - CVE-2023-6707: Use after free in CSS.

* Thu Dec 07 2023 Alexey Gladkov <legion@altlinux.ru> 120.0.6099.71-alt1
- New version (120.0.6099.71).

* Thu Nov 16 2023 Alexey Gladkov <legion@altlinux.ru> 119.0.6045.159-alt1
- New version (119.0.6045.159).
- Security fixes:
  - CVE-2023-5997: Use after free in Garbage Collection.
  - CVE-2023-6112: Use after free in Navigation.

* Mon Nov 13 2023 Alexey Gladkov <legion@altlinux.ru> 119.0.6045.123-alt1
- New version (119.0.6045.123).
- Security fixes:
  - CVE-2023-5996: Use after free in WebAudio.

* Fri Nov 03 2023 Alexey Gladkov <legion@altlinux.ru> 119.0.6045.105-alt1
- New version (119.0.6045.105).
- Security fixes:
  - CVE-2023-5480: Inappropriate implementation in Payments.
  - CVE-2023-5482: Insufficient data validation in USB.
  - CVE-2023-5849: Integer overflow in USB.
  - CVE-2023-5850: Incorrect security UI in Downloads.
  - CVE-2023-5851: Inappropriate implementation in Downloads.
  - CVE-2023-5852: Use after free in Printing.
  - CVE-2023-5853: Incorrect security UI in Downloads.
  - CVE-2023-5854: Use after free in Profiles.
  - CVE-2023-5855: Use after free in Reading Mode.
  - CVE-2023-5856: Use after free in Side Panel.
  - CVE-2023-5857: Inappropriate implementation in Downloads.
  - CVE-2023-5858: Inappropriate implementation in WebApp Provider.
  - CVE-2023-5859: Incorrect security UI in Picture In Picture.
  - CVE-2023-5472: Use after free in Profiles.

* Mon Oct 16 2023 Alexey Gladkov <legion@altlinux.ru> 118.0.5993.70-alt1
- New version (118.0.5993.70).
- Security fixes:
  - CVE-2023-5218: Use after free in Site Isolation.
  - CVE-2023-5346: Type Confusion in V8.
  - CVE-2023-5473: Use after free in Cast.
  - CVE-2023-5474: Heap buffer overflow in PDF.
  - CVE-2023-5475: Inappropriate implementation in DevTools.
  - CVE-2023-5476: Use after free in Blink History.
  - CVE-2023-5477: Inappropriate implementation in Installer.
  - CVE-2023-5478: Inappropriate implementation in Autofill.
  - CVE-2023-5479: Inappropriate implementation in Extensions API.
  - CVE-2023-5481: Inappropriate implementation in Downloads.
  - CVE-2023-5483: Inappropriate implementation in Intents.
  - CVE-2023-5484: Inappropriate implementation in Navigation.
  - CVE-2023-5485: Inappropriate implementation in Autofill.
  - CVE-2023-5486: Inappropriate implementation in Input.
  - CVE-2023-5487: Inappropriate implementation in Fullscreen.

* Thu Sep 28 2023 Alexey Gladkov <legion@altlinux.ru> 117.0.5938.132-alt1
- New version (117.0.5938.132).
- Security fixes:
  - CVE-2023-5186: Use after free in Passwords.
  - CVE-2023-5187: Use after free in Extensions.
  - CVE-2023-5217: Heap buffer overflow in vp8 encoding in libvpx.

* Mon Sep 25 2023 Alexey Gladkov <legion@altlinux.ru> 117.0.5938.92-alt1
- New version (117.0.5938.92).

* Wed Sep 13 2023 Alexey Gladkov <legion@altlinux.ru> 117.0.5938.62-alt1
- New version (117.0.5938.62).
- Security fixes:
  - CVE-2023-4863: Heap buffer overflow in WebP.
  - CVE-2023-4900: Inappropriate implementation in Custom Tabs.
  - CVE-2023-4901: Inappropriate implementation in Prompts.
  - CVE-2023-4902: Inappropriate implementation in Input.
  - CVE-2023-4903: Inappropriate implementation in Custom Mobile Tabs.
  - CVE-2023-4904: Insufficient policy enforcement in Downloads.
  - CVE-2023-4905: Inappropriate implementation in Prompts.
  - CVE-2023-4906: Insufficient policy enforcement in Autofill.
  - CVE-2023-4907: Inappropriate implementation in Intents.
  - CVE-2023-4908: Inappropriate implementation in Picture in Picture.
  - CVE-2023-4909: Inappropriate implementation in Interstitials.

* Thu Aug 17 2023 Alexey Gladkov <legion@altlinux.ru> 116.0.5845.96-alt1
- New version (116.0.5845.96).
- Security fixes:
  - CVE-2023-2312: Use after free in Offline.
  - CVE-2023-4349: Use after free in Device Trust Connectors.
  - CVE-2023-4350: Inappropriate implementation in Fullscreen.
  - CVE-2023-4351: Use after free in Network.
  - CVE-2023-4352: Type Confusion in V8.
  - CVE-2023-4353: Heap buffer overflow in ANGLE.
  - CVE-2023-4354: Heap buffer overflow in Skia.
  - CVE-2023-4355: Out of bounds memory access in V8.
  - CVE-2023-4356: Use after free in Audio.
  - CVE-2023-4357: Insufficient validation of untrusted input in XML.
  - CVE-2023-4358: Use after free in DNS.
  - CVE-2023-4359: Inappropriate implementation in App Launcher.
  - CVE-2023-4360: Inappropriate implementation in Color.
  - CVE-2023-4361: Inappropriate implementation in Autofill.
  - CVE-2023-4362: Heap buffer overflow in Mojom IDL.
  - CVE-2023-4363: Inappropriate implementation in WebShare.
  - CVE-2023-4364: Inappropriate implementation in Permission Prompts.
  - CVE-2023-4365: Inappropriate implementation in Fullscreen.
  - CVE-2023-4366: Use after free in Extensions.
  - CVE-2023-4367: Insufficient policy enforcement in Extensions API.
  - CVE-2023-4368: Insufficient policy enforcement in Extensions API.

* Wed Jul 26 2023 Alexey Gladkov <legion@altlinux.ru> 115.0.5790.110-alt1
- New version (115.0.5790.110).

* Fri Jul 21 2023 Alexey Gladkov <legion@altlinux.ru> 115.0.5790.102-alt1
- New version (115.0.5790.102).

* Tue Jul 18 2023 Alexey Gladkov <legion@altlinux.ru> 114.0.5735.198-alt1
- New version (114.0.5735.198).
- Use LLVM16.
- Security fixes:
  - CVE-2023-3214: Use after free in Autofill payments.
  - CVE-2023-3215: Use after free in WebRTC.
  - CVE-2023-3216: Type Confusion in V8.
  - CVE-2023-3217: Use after free in WebXR.
  - CVE-2023-3420: Type Confusion in V8.
  - CVE-2023-3421: Use after free in Media.
  - CVE-2023-3422: Use after free in Guest View.

* Sat Jun 03 2023 Alexey Gladkov <legion@altlinux.ru> 114.0.5735.90-alt1
- New version (114.0.5735.90).
- Security fixes:
  - CVE-2023-2929: Out of bounds write in Swiftshader.
  - CVE-2023-2930: Use after free in Extensions.
  - CVE-2023-2931: Use after free in PDF.
  - CVE-2023-2932: Use after free in PDF.
  - CVE-2023-2933: Use after free in PDF.
  - CVE-2023-2934: Out of bounds memory access in Mojo.
  - CVE-2023-2935: Type Confusion in V8.
  - CVE-2023-2936: Type Confusion in V8.
  - CVE-2023-2937: Inappropriate implementation in Picture In Picture.
  - CVE-2023-2938: Inappropriate implementation in Picture In Picture.
  - CVE-2023-2939: Insufficient data validation in Installer.
  - CVE-2023-2940: Inappropriate implementation in Downloads.
  - CVE-2023-2941: Inappropriate implementation in Extensions API.

* Wed May 03 2023 Alexey Gladkov <legion@altlinux.ru> 113.0.5672.63-alt1
- New version (113.0.5672.63).
- Security fixes:
  - CVE-2023-2459: Inappropriate implementation in Prompts.
  - CVE-2023-2460: Insufficient validation of untrusted input in Extensions.
  - CVE-2023-2461: Use after free in OS Inputs.
  - CVE-2023-2462: Inappropriate implementation in Prompts.
  - CVE-2023-2463: Inappropriate implementation in Full Screen Mode.
  - CVE-2023-2464: Inappropriate implementation in PictureInPicture.
  - CVE-2023-2465: Inappropriate implementation in CORS.
  - CVE-2023-2466: Inappropriate implementation in Prompts.
  - CVE-2023-2467: Inappropriate implementation in Prompts.
  - CVE-2023-2468: Inappropriate implementation in PictureInPicture.

* Thu Apr 20 2023 Alexey Gladkov <legion@altlinux.ru> 112.0.5615.165-alt1
- New version (112.0.5615.165).
- Security fixes:
  - CVE-2023-1810: Heap buffer overflow in Visuals.
  - CVE-2023-1811: Use after free in Frames.
  - CVE-2023-1812: Out of bounds memory access in DOM Bindings.
  - CVE-2023-1813: Inappropriate implementation in Extensions.
  - CVE-2023-1814: Insufficient validation of untrusted input in Safe Browsing.
  - CVE-2023-1815: Use after free in Networking APIs.
  - CVE-2023-1816: Incorrect security UI in Picture In Picture.
  - CVE-2023-1817: Insufficient policy enforcement in Intents.
  - CVE-2023-1818: Use after free in Vulkan.
  - CVE-2023-1819: Out of bounds read in Accessibility.
  - CVE-2023-1820: Heap buffer overflow in Browser History.
  - CVE-2023-1821: Inappropriate implementation in WebShare.
  - CVE-2023-1822: Incorrect security UI in Navigation.
  - CVE-2023-1823: Inappropriate implementation in FedCM.
  - CVE-2023-2033: Type Confusion in V8.
  - CVE-2023-2133: Out of bounds memory access in Service Worker API.
  - CVE-2023-2134: Out of bounds memory access in Service Worker API.
  - CVE-2023-2135: Use after free in DevTools.
  - CVE-2023-2136: Integer overflow in Skia.
  - CVE-2023-2137: Heap buffer overflow in sqlite.

* Wed Mar 08 2023 Alexey Gladkov <legion@altlinux.ru> 111.0.5563.64-alt1
- New version (111.0.5563.64).
- Security fixes:
  - CVE-2023-1213: Use after free in Swiftshader.
  - CVE-2023-1214: Type Confusion in V8.
  - CVE-2023-1215: Type Confusion in CSS.
  - CVE-2023-1216: Use after free in DevTools.
  - CVE-2023-1217: Stack buffer overflow in Crash reporting.
  - CVE-2023-1218: Use after free in WebRTC.
  - CVE-2023-1219: Heap buffer overflow in Metrics.
  - CVE-2023-1220: Heap buffer overflow in UMA.
  - CVE-2023-1221: Insufficient policy enforcement in Extensions API.
  - CVE-2023-1222: Heap buffer overflow in Web Audio API.
  - CVE-2023-1223: Insufficient policy enforcement in Autofill.
  - CVE-2023-1224: Insufficient policy enforcement in Web Payments API.
  - CVE-2023-1225: Insufficient policy enforcement in Navigation.
  - CVE-2023-1226: Insufficient policy enforcement in Web Payments API.
  - CVE-2023-1227: Use after free in Core.
  - CVE-2023-1228: Insufficient policy enforcement in Intents.
  - CVE-2023-1229: Inappropriate implementation in Permission prompts.
  - CVE-2023-1230: Inappropriate implementation in WebApp Installs.
  - CVE-2023-1231: Inappropriate implementation in Autofill.
  - CVE-2023-1232: Insufficient policy enforcement in Resource Timing.
  - CVE-2023-1233: Insufficient policy enforcement in Resource Timing.
  - CVE-2023-1234: Inappropriate implementation in Intents.
  - CVE-2023-1235: Type Confusion in DevTools.
  - CVE-2023-1236: Inappropriate implementation in Internals.

* Wed Mar 01 2023 Alexey Gladkov <legion@altlinux.ru> 110.0.5481.177-alt2
- Bring back compiler optimizations (ALT#45454).

* Thu Feb 23 2023 Alexey Gladkov <legion@altlinux.ru> 110.0.5481.177-alt1
- New version (110.0.5481.177).
- Fix crach in autofill (ALT#45269).
- Security fixes:
  - CVE-2023-0927: Use after free in Web Payments API.
  - CVE-2023-0928: Use after free in SwiftShader.
  - CVE-2023-0929: Use after free in Vulkan.
  - CVE-2023-0930: Heap buffer overflow in Video.
  - CVE-2023-0931: Use after free in Video.
  - CVE-2023-0932: Use after free in WebRTC.
  - CVE-2023-0933: Integer overflow in PDF.
  - CVE-2023-0941: Use after free in Prompts.

* Thu Feb 09 2023 Alexey Gladkov <legion@altlinux.ru> 110.0.5481.77-alt1
- New version (110.0.5481.77).
- Upstream disallow to chromium build with system libwayland (crbug.com/1385736).
- Add more parameters to Yandex search url (ALT#45192).
- Security fixes:
  - CVE-2023-0696: Type Confusion in V8.
  - CVE-2023-0697: Inappropriate implementation in Full screen mode.
  - CVE-2023-0698: Out of bounds read in WebRTC.
  - CVE-2023-0699: Use after free in GPU.
  - CVE-2023-0700: Inappropriate implementation in Download.
  - CVE-2023-0701: Heap buffer overflow in WebUI.
  - CVE-2023-0702: Type Confusion in Data Transfer.
  - CVE-2023-0703: Type Confusion in DevTools.
  - CVE-2023-0704: Insufficient policy enforcement in DevTools.
  - CVE-2023-0705: Integer overflow in Core.

* Mon Jan 30 2023 Alexey Gladkov <legion@altlinux.ru> 109.0.5414.119-alt1
- New version (109.0.5414.119).
- Add a workaround to make the https_proxy environment variable work (ALT#44986).
- Security fixes:
  - CVE-2023-0471: Use after free in WebTransport.
  - CVE-2023-0472: Use after free in WebRTC.
  - CVE-2023-0473: Type Confusion in ServiceWorker API.
  - CVE-2023-0474: Use after free in GuestView.

* Thu Jan 12 2023 Alexey Gladkov <legion@altlinux.ru> 109.0.5414.74-alt1
- New version (109.0.5414.74).
- Security fixes:
  - CVE-2023-0128: Use after free in Overview Mode.
  - CVE-2023-0129: Heap buffer overflow in Network Service.
  - CVE-2023-0130: Inappropriate implementation in Fullscreen API.
  - CVE-2023-0131: Inappropriate implementation in iframe Sandbox.
  - CVE-2023-0132: Inappropriate implementation in Permission prompts.
  - CVE-2023-0133: Inappropriate implementation in Permission prompts.
  - CVE-2023-0134: Use after free in Cart.
  - CVE-2023-0135: Use after free in Cart.
  - CVE-2023-0136: Inappropriate implementation in Fullscreen API.
  - CVE-2023-0137: Heap buffer overflow in Platform Apps.
  - CVE-2023-0138: Heap buffer overflow in libphonenumber.
  - CVE-2023-0139: Insufficient validation of untrusted input in Downloads.
  - CVE-2023-0140: Inappropriate implementation in File System API.
  - CVE-2023-0141: Insufficient policy enforcement in CORS.

* Fri Dec 02 2022 Alexey Gladkov <legion@altlinux.ru> 108.0.5359.71-alt1
- New version (108.0.5359.71).
- Use LLVM 15.
- Security fixes:
  - CVE-2022-4174: Type Confusion in V8.
  - CVE-2022-4175: Use after free in Camera Capture.
  - CVE-2022-4176: Out of bounds write in Lacros Graphics.
  - CVE-2022-4177: Use after free in Extensions.
  - CVE-2022-4178: Use after free in Mojo.
  - CVE-2022-4179: Use after free in Audio.
  - CVE-2022-4180: Use after free in Mojo.
  - CVE-2022-4181: Use after free in Forms.
  - CVE-2022-4182: Inappropriate implementation in Fenced Frames.
  - CVE-2022-4183: Insufficient policy enforcement in Popup Blocker.
  - CVE-2022-4184: Insufficient policy enforcement in Autofill.
  - CVE-2022-4185: Inappropriate implementation in Navigation.
  - CVE-2022-4186: Insufficient validation of untrusted input in Downloads.
  - CVE-2022-4187: Insufficient policy enforcement in DevTools.
  - CVE-2022-4188: Insufficient validation of untrusted input in CORS.
  - CVE-2022-4189: Insufficient policy enforcement in DevTools.
  - CVE-2022-4190: Insufficient data validation in Directory.
  - CVE-2022-4191: Use after free in Sign-In.
  - CVE-2022-4192: Use after free in Live Caption.
  - CVE-2022-4193: Insufficient policy enforcement in File System API.
  - CVE-2022-4194: Use after free in Accessibility.
  - CVE-2022-4195: Insufficient policy enforcement in Safe Browsing.

* Fri Nov 18 2022 Alexey Gladkov <legion@altlinux.ru> 107.0.5304.110-alt1
- New version (107.0.5304.110).
- Security fixes:
  - CVE-2022-3885: Use after free in V8.
  - CVE-2022-3886: Use after free in Speech Recognition.
  - CVE-2022-3887: Use after free in Web Workers.
  - CVE-2022-3888: Use after free in WebCodecs.
  - CVE-2022-3889: Type Confusion in V8.
  - CVE-2022-3890: Heap buffer overflow in Crashpad.

* Tue Nov 01 2022 Alexey Gladkov <legion@altlinux.ru> 107.0.5304.87-alt1
- New version (107.0.5304.87).
- Security fixes:
  - CVE-2022-3723: Type Confusion in V8.
  - CVE-2022-3652: Type Confusion in V8.
  - CVE-2022-3653: Heap buffer overflow in Vulkan.
  - CVE-2022-3654: Use after free in Layout.
  - CVE-2022-3655: Heap buffer overflow in Media Galleries.
  - CVE-2022-3656: Insufficient data validation in File System.
  - CVE-2022-3657: Use after free in Extensions.
  - CVE-2022-3658: Use after free in Feedback service on Chrome OS.
  - CVE-2022-3659: Use after free in Accessibility.
  - CVE-2022-3660: Inappropriate implementation in Full screen mode.
  - CVE-2022-3661: Insufficient data validation in Extensions.

* Thu Oct 13 2022 Alexey Gladkov <legion@altlinux.ru> 106.0.5249.119-alt1
- New version (106.0.5249.119).
- Security fixes:
  - CVE-2022-3445: Use after free in Skia.
  - CVE-2022-3446: Heap buffer overflow in WebSQL.
  - CVE-2022-3447: Inappropriate implementation in Custom Tabs.
  - CVE-2022-3448: Use after free in Permissions API.
  - CVE-2022-3449: Use after free in Safe Browsing.
  - CVE-2022-3450: Use after free in Peer Connection.

* Mon Oct 10 2022 Alexey Gladkov <legion@altlinux.ru> 106.0.5249.103-alt1
- New version (106.0.5249.103).
- Security fixes:
  - CVE-2022-3370: Use after free in Custom Elements.
  - CVE-2022-3373: Out of bounds write in V8.

* Wed Sep 28 2022 Alexey Gladkov <legion@altlinux.ru> 106.0.5249.61-alt1
- New version (106.0.5249.61).
- Security fixes:
  - CVE-2022-3201: Insufficient validation of untrusted input in Developer Tools.
  - CVE-2022-3304: Use after free in CSS.
  - CVE-2022-3305: Use after free in Survey.
  - CVE-2022-3306: Use after free in Survey.
  - CVE-2022-3307: Use after free in Media.
  - CVE-2022-3308: Insufficient policy enforcement in Developer Tools.
  - CVE-2022-3309: Use after free in Assistant.
  - CVE-2022-3310: Insufficient policy enforcement in Custom Tabs.
  - CVE-2022-3311: Use after free in Import.
  - CVE-2022-3312: Insufficient validation of untrusted input in VPN.
  - CVE-2022-3313: Incorrect security UI in Full Screen.
  - CVE-2022-3314: Use after free in Logging.
  - CVE-2022-3315: Type confusion in Blink.
  - CVE-2022-3316: Insufficient validation of untrusted input in Safe Browsing.
  - CVE-2022-3317: Insufficient validation of untrusted input in Intents.
  - CVE-2022-3318: Use after free in ChromeOS Notifications.

* Mon Sep 05 2022 Alexey Gladkov <legion@altlinux.ru> 105.0.5195.102-alt1
- New version (105.0.5195.102).
- Security fixes:
  - CVE-2022-3075: Insufficient data validation in Mojo.

* Thu Sep 01 2022 Alexey Gladkov <legion@altlinux.ru> 105.0.5195.52-alt1
- New version (105.0.5195.52).
- Security fixes:
  - CVE-2022-3038: Use after free in Network Service.
  - CVE-2022-3039: Use after free in WebSQL.
  - CVE-2022-3040: Use after free in Layout.
  - CVE-2022-3041: Use after free in WebSQL.
  - CVE-2022-3042: Use after free in PhoneHub.
  - CVE-2022-3043: Heap buffer overflow in Screen Capture.
  - CVE-2022-3044: Inappropriate implementation in Site Isolation.
  - CVE-2022-3045: Insufficient validation of untrusted input in V8.
  - CVE-2022-3046: Use after free in Browser Tag.
  - CVE-2022-3047: Insufficient policy enforcement in Extensions API.
  - CVE-2022-3048: Inappropriate implementation in Chrome OS lockscreen.
  - CVE-2022-3049: Use after free in SplitScreen.
  - CVE-2022-3050: Heap buffer overflow in WebUI.
  - CVE-2022-3051: Heap buffer overflow in Exosphere.
  - CVE-2022-3052: Heap buffer overflow in Window Manager.
  - CVE-2022-3053: Inappropriate implementation in Pointer Lock.
  - CVE-2022-3054: Insufficient policy enforcement in DevTools.
  - CVE-2022-3055: Use after free in Passwords.
  - CVE-2022-3056: Insufficient policy enforcement in Content Security Policy.
  - CVE-2022-3057: Inappropriate implementation in iframe Sandbox.
  - CVE-2022-3058: Use after free in Sign-In Flow.
  - CVE-2022-3071: Use after free in Tab Strip.

* Sat Jun 25 2022 Alexey Gladkov <legion@altlinux.ru> 103.0.5060.53-alt1
- New version (103.0.5060.53).
- Security fixes:
  - CVE-2022-2156: Use after free in Base.
  - CVE-2022-2157: Use after free in Interest groups.
  - CVE-2022-2158: Type Confusion in V8.
  - CVE-2022-2160: Insufficient policy enforcement in DevTools.
  - CVE-2022-2161: Use after free in WebApp Provider.
  - CVE-2022-2162: Insufficient policy enforcement in File System API.
  - CVE-2022-2163: Use after free in Cast UI and Toolbar.
  - CVE-2022-2164: Inappropriate implementation in Extensions API.
  - CVE-2022-2165: Insufficient data validation in URL formatting.

* Wed Jun 01 2022 Alexey Gladkov <legion@altlinux.ru> 102.0.5005.61-alt2
- Handle kioslaverc config located in XDG_CONFIG_DIRS.

* Wed May 25 2022 Alexey Gladkov <legion@altlinux.ru> 102.0.5005.61-alt1
- New version (102.0.5005.61).
- Security fixes:
  - CVE-2022-1853: Use after free in Indexed DB.
  - CVE-2022-1854: Use after free in ANGLE.
  - CVE-2022-1855: Use after free in Messaging.
  - CVE-2022-1856: Use after free in User Education.
  - CVE-2022-1857: Insufficient policy enforcement in File System API.
  - CVE-2022-1858: Out of bounds read in DevTools.
  - CVE-2022-1859: Use after free in Performance Manager.
  - CVE-2022-1860: Use after free in UI Foundations.
  - CVE-2022-1861: Use after free in Sharing.
  - CVE-2022-1862: Inappropriate implementation in Extensions.
  - CVE-2022-1863: Use after free in Tab Groups.
  - CVE-2022-1864: Use after free in WebApp Installs.
  - CVE-2022-1865: Use after free in Bookmarks.
  - CVE-2022-1866: Use after free in Tablet Mode.
  - CVE-2022-1867: Insufficient validation of untrusted input in Data Transfer.
  - CVE-2022-1868: Inappropriate implementation in Extensions API.
  - CVE-2022-1869: Type Confusion in V8.
  - CVE-2022-1870: Use after free in App Service.
  - CVE-2022-1871: Insufficient policy enforcement in File System API.
  - CVE-2022-1872: Insufficient policy enforcement in Extensions API.
  - CVE-2022-1873: Insufficient policy enforcement in COOP.
  - CVE-2022-1874: Insufficient policy enforcement in Safe Browsing.
  - CVE-2022-1875: Inappropriate implementation in PDF.
  - CVE-2022-1876: Heap buffer overflow in DevTools.

* Wed May 11 2022 Alexey Gladkov <legion@altlinux.ru> 101.0.4951.41-alt2
- Disable use of client_id and client_secret (Google shut off API access).
- Use LLVM 13.

* Wed Apr 27 2022 Alexey Gladkov <legion@altlinux.ru> 101.0.4951.41-alt1
- New version (101.0.4951.41).
- Security fixes:
  - CVE-2022-1477: Use after free in Vulkan.
  - CVE-2022-1478: Use after free in SwiftShader.
  - CVE-2022-1479: Use after free in ANGLE.
  - CVE-2022-1480: Use after free in Device API.
  - CVE-2022-1481: Use after free in Sharing.
  - CVE-2022-1482: Inappropriate implementation in WebGL.
  - CVE-2022-1483: Heap buffer overflow in WebGPU.
  - CVE-2022-1484: Heap buffer overflow in Web UI Settings.
  - CVE-2022-1485: Use after free in File System API.
  - CVE-2022-1486: Type Confusion in V8.
  - CVE-2022-1487: Use after free in Ozone.
  - CVE-2022-1488: Inappropriate implementation in Extensions API.
  - CVE-2022-1489: Out of bounds memory access in UI Shelf.
  - CVE-2022-1490: Use after free in Browser Switcher.
  - CVE-2022-1491: Use after free in Bookmarks.
  - CVE-2022-1492: Insufficient data validation in Blink Editing.
  - CVE-2022-1493: Use after free in Dev Tools.
  - CVE-2022-1494: Insufficient data validation in Trusted Types.
  - CVE-2022-1495: Incorrect security UI in Downloads.
  - CVE-2022-1496: Use after free in File Manager.
  - CVE-2022-1497: Inappropriate implementation in Input.
  - CVE-2022-1498: Inappropriate implementation in HTML Parser.
  - CVE-2022-1499: Inappropriate implementation in WebAuthentication.
  - CVE-2022-1500: Insufficient data validation in Dev Tools.
  - CVE-2022-1501: Inappropriate implementation in iframe.

* Fri Apr 15 2022 Alexey Gladkov <legion@altlinux.ru> 100.0.4896.127-alt1
- New version (100.0.4896.127).
- Security fixes:
  - CVE-2022-1364: Type Confusion in V8.

* Wed Mar 30 2022 Alexey Gladkov <legion@altlinux.ru> 100.0.4896.60-alt1
- New version (100.0.4896.60) (ALT#42263).
- Security fixes:
  - CVE-2022-1125: Use after free in Portals.
  - CVE-2022-1127: Use after free in QR Code Generator.
  - CVE-2022-1128: Inappropriate implementation in Web Share API.
  - CVE-2022-1129: Inappropriate implementation in Full Screen Mode.
  - CVE-2022-1130: Insufficient validation of untrusted input in WebOTP.
  - CVE-2022-1131: Use after free in Cast UI.
  - CVE-2022-1132: Inappropriate implementation in Virtual Keyboard.
  - CVE-2022-1133: Use after free in WebRTC.
  - CVE-2022-1134: Type Confusion in V8.
  - CVE-2022-1135: Use after free in Shopping Cart.
  - CVE-2022-1136: Use after free in Tab Strip .
  - CVE-2022-1137: Inappropriate implementation in Extensions.
  - CVE-2022-1138: Inappropriate implementation in Web Cursor.
  - CVE-2022-1139: Inappropriate implementation in Background Fetch API.
  - CVE-2022-1141: Use after free in File Manager.
  - CVE-2022-1142: Heap buffer overflow in WebUI.
  - CVE-2022-1143: Heap buffer overflow in WebUI.
  - CVE-2022-1144: Use after free in WebUI.
  - CVE-2022-1145: Use after free in Extensions.
  - CVE-2022-1146: Inappropriate implementation in Resource Timing.

* Wed Mar 16 2022 Alexey Gladkov <legion@altlinux.ru> 99.0.4844.74-alt1
- New version (99.0.4844.74).
- Security fixes:
  - CVE-2022-0971: Use after free in Blink Layout.
  - CVE-2022-0972: Use after free in Extensions.
  - CVE-2022-0973: Use after free in Safe Browsing.
  - CVE-2022-0974: Use after free in Splitscreen.
  - CVE-2022-0975: Use after free in ANGLE.
  - CVE-2022-0976: Heap buffer overflow in GPU.
  - CVE-2022-0977: Use after free in Browser UI.
  - CVE-2022-0978: Use after free in ANGLE.
  - CVE-2022-0979: Use after free in Safe Browsing.
  - CVE-2022-0980: Use after free in New Tab Page.

* Thu Mar 03 2022 Alexey Gladkov <legion@altlinux.ru> 99.0.4844.51-alt1
- New version (99.0.4844.51).
- Security fixes:
  - CVE-2022-0789: Heap buffer overflow in ANGLE.
  - CVE-2022-0790: Use after free in Cast UI.
  - CVE-2022-0791: Use after free in Omnibox.
  - CVE-2022-0792: Out of bounds read in ANGLE.
  - CVE-2022-0793: Use after free in Views.
  - CVE-2022-0794: Use after free in WebShare.
  - CVE-2022-0795: Type Confusion in Blink Layout.
  - CVE-2022-0796: Use after free in Media.
  - CVE-2022-0797: Out of bounds memory access in Mojo.
  - CVE-2022-0798: Use after free in MediaStream.
  - CVE-2022-0799: Insufficient policy enforcement in Installer.
  - CVE-2022-0800: Heap buffer overflow in Cast UI.
  - CVE-2022-0801: Inappropriate implementation in HTML parser.
  - CVE-2022-0802: Inappropriate implementation in Full screen mode.
  - CVE-2022-0803: Inappropriate implementation in Permissions.
  - CVE-2022-0804: Inappropriate implementation in Full screen mode.
  - CVE-2022-0805: Use after free in Browser Switcher.
  - CVE-2022-0806: Data leak in Canvas.
  - CVE-2022-0807: Inappropriate implementation in Autofill.
  - CVE-2022-0808: Use after free in Chrome OS Shell.
  - CVE-2022-0809: Out of bounds memory access in WebXR.

* Wed Feb 16 2022 Alexey Gladkov <legion@altlinux.ru> 98.0.4758.102-alt1
- New version (98.0.4758.102) (ALT#41964).
- Security fixes:
  - CVE-2022-0603: Use after free in File Manager.
  - CVE-2022-0604: Heap buffer overflow in Tab Groups.
  - CVE-2022-0605: Use after free in Webstore API.
  - CVE-2022-0606: Use after free in ANGLE.
  - CVE-2022-0607: Use after free in GPU.
  - CVE-2022-0608: Integer overflow in Mojo.
  - CVE-2022-0609: Use after free in Animation.
  - CVE-2022-0610: Inappropriate implementation in Gamepad API.

* Fri Feb 04 2022 Alexey Gladkov <legion@altlinux.ru> 98.0.4758.80-alt1
- New version (98.0.4758.80).
- Build with python3.
- Security fixes:
  - CVE-2022-0452: Use after free in Safe Browsing.
  - CVE-2022-0453: Use after free in Reader Mode.
  - CVE-2022-0454: Heap buffer overflow in ANGLE.
  - CVE-2022-0455: Inappropriate implementation in Full Screen Mode.
  - CVE-2022-0456: Use after free in Web Search.
  - CVE-2022-0457: Type Confusion in V8.
  - CVE-2022-0458: Use after free in Thumbnail Tab Strip.
  - CVE-2022-0459: Use after free in Screen Capture.
  - CVE-2022-0460: Use after free in Window Dialog.
  - CVE-2022-0461: Policy bypass in COOP.
  - CVE-2022-0462: Inappropriate implementation in Scroll.
  - CVE-2022-0463: Use after free in Accessibility.
  - CVE-2022-0464: Use after free in Accessibility.
  - CVE-2022-0465: Use after free in Extensions.
  - CVE-2022-0466: Inappropriate implementation in Extensions Platform.
  - CVE-2022-0467: Inappropriate implementation in Pointer Lock.
  - CVE-2022-0468: Use after free in Payments.
  - CVE-2022-0469: Use after free in Cast.
  - CVE-2022-0470: Out of bounds memory access in V8.

* Tue Jan 25 2022 Alexey Gladkov <legion@altlinux.ru> 97.0.4692.99-alt1
- New version (97.0.4692.99).
- Security fixes:
  - CVE-2022-0289: Use after free in Safe browsing.
  - CVE-2022-0290: Use after free in Site isolation.
  - CVE-2022-0291: Inappropriate implementation in Storage.
  - CVE-2022-0292: Inappropriate implementation in Fenced Frames.
  - CVE-2022-0293: Use after free in Web packaging.
  - CVE-2022-0294: Inappropriate implementation in Push messaging.
  - CVE-2022-0295: Use after free in Omnibox.
  - CVE-2022-0296: Use after free in Printing.
  - CVE-2022-0297: Use after free in Vulkan.
  - CVE-2022-0298: Use after free in Scheduling.
  - CVE-2022-0300: Use after free in Text Input Method Editor.
  - CVE-2022-0301: Heap buffer overflow in DevTools.
  - CVE-2022-0302: Use after free in Omnibox.
  - CVE-2022-0304: Use after free in Bookmarks.
  - CVE-2022-0305: Inappropriate implementation in Service Worker API.
  - CVE-2022-0306: Heap buffer overflow in PDFium.
  - CVE-2022-0307: Use after free in Optimization Guide.
  - CVE-2022-0308: Use after free in Data Transfer.
  - CVE-2022-0309: Inappropriate implementation in Autofill.
  - CVE-2022-0310: Heap buffer overflow in Task Manager.
  - CVE-2022-0311: Heap buffer overflow in Task Manager.

* Wed Jan 05 2022 Alexey Gladkov <legion@altlinux.ru> 97.0.4692.71-alt1
- New version (97.0.4692.71).
- Security fixes:
  - CVE-2022-0096: Use after free in Storage.
  - CVE-2022-0097: Inappropriate implementation in DevTools.
  - CVE-2022-0098: Use after free in Screen Capture.
  - CVE-2022-0099: Use after free in Sign-in.
  - CVE-2022-0100: Heap buffer overflow in Media streams API.
  - CVE-2022-0101: Heap buffer overflow in Bookmarks.
  - CVE-2022-0102: Type Confusion in V8 .
  - CVE-2022-0103: Use after free in SwiftShader.
  - CVE-2022-0104: Heap buffer overflow in ANGLE.
  - CVE-2022-0105: Use after free in PDF.
  - CVE-2022-0106: Use after free in Autofill.
  - CVE-2022-0107: Use after free in File Manager API.
  - CVE-2022-0108: Inappropriate implementation in Navigation.
  - CVE-2022-0109: Inappropriate implementation in Autofill.
  - CVE-2022-0110: Incorrect security UI in Autofill.
  - CVE-2022-0111: Inappropriate implementation in Navigation.
  - CVE-2022-0112: Incorrect security UI in Browser UI.
  - CVE-2022-0113: Inappropriate implementation in Blink.
  - CVE-2022-0114: Out of bounds memory access in Web Serial.
  - CVE-2022-0115: Uninitialized Use in File API.
  - CVE-2022-0116: Inappropriate implementation in Compositing.
  - CVE-2022-0117: Policy bypass in Service Workers.
  - CVE-2022-0118: Inappropriate implementation in WebShare.
  - CVE-2022-0120: Inappropriate implementation in Passwords.

* Tue Dec 14 2021 Alexey Gladkov <legion@altlinux.ru> 96.0.4664.110-alt1
- New version (96.0.4664.110).
- Security fixes:
  - CVE-2021-4098: Insufficient data validation in Mojo.
  - CVE-2021-4099: Use after free in Swiftshader.
  - CVE-2021-4100: Object lifecycle issue in ANGLE.
  - CVE-2021-4101: Heap buffer overflow in Swiftshader.
  - CVE-2021-4102: Use after free in V8.

* Fri Nov 26 2021 Alexey Gladkov <legion@altlinux.ru> 96.0.4664.45-alt3
- Allow fallback to any GL implementation (ALT#41430).

* Tue Nov 23 2021 Andrey Cherepanov <cas@altlinux.org> 96.0.4664.45-alt2
- Apply upstream patches for fix window maximization in XFCE (ALT #41247).

* Tue Nov 16 2021 Alexey Gladkov <legion@altlinux.ru> 96.0.4664.45-alt1
- New version (96.0.4664.45).
- Security fixes:
  - CVE-2021-38005: Use after free in loader.
  - CVE-2021-38006: Use after free in storage foundation.
  - CVE-2021-38007: Type Confusion in V8.
  - CVE-2021-38008: Use after free in media.
  - CVE-2021-38009: Inappropriate implementation in cache.
  - CVE-2021-38010: Inappropriate implementation in service workers.
  - CVE-2021-38011: Use after free in storage foundation.
  - CVE-2021-38012: Type Confusion in V8.
  - CVE-2021-38013: Heap buffer overflow in fingerprint recognition.
  - CVE-2021-38014: Out of bounds write in Swiftshader.
  - CVE-2021-38015: Inappropriate implementation in input.
  - CVE-2021-38016: Insufficient policy enforcement in background fetch.
  - CVE-2021-38017: Insufficient policy enforcement in iframe sandbox.
  - CVE-2021-38018: Inappropriate implementation in navigation.
  - CVE-2021-38019: Insufficient policy enforcement in CORS.
  - CVE-2021-38020: Insufficient policy enforcement in contacts picker.
  - CVE-2021-38021: Inappropriate implementation in referrer.
  - CVE-2021-38022: Inappropriate implementation in WebAuthentication.

* Sat Nov 06 2021 Alexey Gladkov <legion@altlinux.ru> 95.0.4638.69-alt3
- Set zero insets on maximising the window (ALT#41247).

* Tue Nov 02 2021 Alexey Gladkov <legion@altlinux.ru> 95.0.4638.69-alt2
- New version (95.0.4638.69).
- Security fixes:
  - CVE-2021-37997: Use after free in Sign-In.
  - CVE-2021-37998: Use after free in Garbage Collection.
  - CVE-2021-37999: Insufficient data validation in New Tab Page.
  - CVE-2021-38000: Insufficient validation of untrusted input in Intents.
  - CVE-2021-38001: Type Confusion in V8.
  - CVE-2021-38002: Use after free in Web Transport.
  - CVE-2021-38003: Inappropriate implementation in V8.

* Mon Oct 25 2021 Alexey Gladkov <legion@altlinux.ru> 95.0.4638.54-alt2
- Audio process sandbox is disabled.

* Thu Oct 21 2021 Alexey Gladkov <legion@altlinux.ru> 95.0.4638.54-alt1
- New version (95.0.4638.54).
- Security fixes:
  - CVE-2021-37981: Heap buffer overflow in Skia.
  - CVE-2021-37982: Use after free in Incognito.
  - CVE-2021-37983: Use after free in Dev Tools.
  - CVE-2021-37984: Heap buffer overflow in PDFium.
  - CVE-2021-37985: Use after free in V8.
  - CVE-2021-37986: Heap buffer overflow in Settings.
  - CVE-2021-37987: Use after free in Network APIs.
  - CVE-2021-37988: Use after free in Profiles.
  - CVE-2021-37989: Inappropriate implementation in Blink.
  - CVE-2021-37990: Inappropriate implementation in WebView.
  - CVE-2021-37991: Race in V8.
  - CVE-2021-37992: Out of bounds read in WebAudio.
  - CVE-2021-37993: Use after free in PDF Accessibility.
  - CVE-2021-37994: Inappropriate implementation in iFrame Sandbox.
  - CVE-2021-37995: Inappropriate implementation in WebApp Installer.
  - CVE-2021-37996: Insufficient validation of untrusted input in Downloads.

* Wed Oct 13 2021 Alexey Gladkov <legion@altlinux.ru> 94.0.4606.81-alt2
- Fix build with glibc-2.34.

* Fri Oct 08 2021 Alexey Gladkov <legion@altlinux.ru> 94.0.4606.81-alt1
- New version (94.0.4606.81).
- Security fixes:
  - CVE-2021-37977: Use after free in Garbage Collection.
  - CVE-2021-37978: Heap buffer overflow in Blink.
  - CVE-2021-37979: Heap buffer overflow in WebRTC.
  - CVE-2021-37980: Inappropriate implementation in Sandbox.

* Fri Oct 01 2021 Alexey Gladkov <legion@altlinux.ru> 94.0.4606.71-alt1
- New version (94.0.4606.71).
- Security fixes:
  - CVE-2021-37974 : Use after free in Safe Browsing.
  - CVE-2021-37975 : Use after free in V8.
  - CVE-2021-37976 : Information leak in core.

* Thu Sep 23 2021 Alexey Gladkov <legion@altlinux.ru> 94.0.4606.54-alt1
- New version (94.0.4606.54).
- Security fixes:
  - CVE-2021-37956: Use after free in Offline use.
  - CVE-2021-37957 : Use after free in WebGPU.
  - CVE-2021-37958 : Inappropriate implementation in Navigation.
  - CVE-2021-37959 : Use after free in Task Manager.
  - CVE-2021-37960 : Inappropriate implementation in Blink graphics.
  - CVE-2021-37961 : Use after free in Tab Strip.
  - CVE-2021-37962 : Use after free in Performance Manager.
  - CVE-2021-37963 : Side-channel information leakage in DevTools.
  - CVE-2021-37964 : Inappropriate implementation in ChromeOS Networking.
  - CVE-2021-37965 : Inappropriate implementation in Background Fetch API.
  - CVE-2021-37966 : Inappropriate implementation in Compositing.
  - CVE-2021-37967 : Inappropriate implementation in Background Fetch API.
  - CVE-2021-37968 : Inappropriate implementation in Background Fetch API.
  - CVE-2021-37969 : Inappropriate implementation in Google Updater.
  - CVE-2021-37970 : Use after free in File System API.
  - CVE-2021-37971 : Incorrect security UI in Web Browser UI.
  - CVE-2021-37972 : Out of bounds read in libjpeg-turbo.

* Tue Sep 14 2021 Alexey Gladkov <legion@altlinux.ru> 93.0.4577.82-alt1
- New version (93.0.4577.82).
- Security fixes:
  - CVE-2021-30625: Use after free in Selection API.
  - CVE-2021-30626: Out of bounds memory access in ANGLE.
  - CVE-2021-30627: Type Confusion in Blink layout.
  - CVE-2021-30628: Stack buffer overflow in ANGLE.
  - CVE-2021-30629: Use after free in Permissions.
  - CVE-2021-30630: Inappropriate implementation in Blink .
  - CVE-2021-30631: Type Confusion in Blink layout.
  - CVE-2021-30632: Out of bounds write in V8.
  - CVE-2021-30633: Use after free in Indexed DB API.

* Wed Sep 01 2021 Alexey Gladkov <legion@altlinux.ru> 93.0.4577.63-alt1
- New version (93.0.4577.63).
- Use internal ffmpeg.
- Security fixes:
  - CVE-2021-30606: Use after free in Blink.
  - CVE-2021-30607: Use after free in Permissions.
  - CVE-2021-30608: Use after free in Web Share.
  - CVE-2021-30609: Use after free in Sign-In.
  - CVE-2021-30610: Use after free in Extensions API.
  - CVE-2021-30611: Use after free in WebRTC.
  - CVE-2021-30612: Use after free in WebRTC.
  - CVE-2021-30613: Use after free in Base internals.
  - CVE-2021-30614: Heap buffer overflow in TabStrip.
  - CVE-2021-30615: Cross-origin data leak in Navigation.
  - CVE-2021-30616: Use after free in Media.
  - CVE-2021-30617: Policy bypass in Blink.
  - CVE-2021-30618: Inappropriate implementation in DevTools.
  - CVE-2021-30619: UI Spoofing in Autofill.
  - CVE-2021-30620: Insufficient policy enforcement in Blink.
  - CVE-2021-30621: UI Spoofing in Autofill.
  - CVE-2021-30622: Use after free in WebApp Installs.
  - CVE-2021-30623: Use after free in Bookmarks.
  - CVE-2021-30624: Use after free in Autofill.

* Tue Aug 31 2021 Alexey Gladkov <legion@altlinux.ru> 92.0.4515.159-alt3
- Drop extra dependencies and remove own xdg-settings and xdg-mime.

* Tue Aug 24 2021 Alexey Gladkov <legion@altlinux.ru> 92.0.4515.159-alt2
- Enable pipewire support (ALT#40806).

* Sat Aug 21 2021 Alexey Gladkov <legion@altlinux.ru> 92.0.4515.159-alt1
- New version (92.0.4515.159).
- Security fixes:
  - CVE-2021-30598: Type Confusion in V8.
  - CVE-2021-30599: Type Confusion in V8.
  - CVE-2021-30600: Use after free in Printing.
  - CVE-2021-30601: Use after free in Extensions API.
  - CVE-2021-30602: Use after free in WebRTC.
  - CVE-2021-30603: Race in WebAudio.
  - CVE-2021-30604: Use after free in ANGLE.

* Wed Aug 11 2021 Alexey Gladkov <legion@altlinux.ru> 92.0.4515.131-alt1
- New version (92.0.4515.131).
- Use python3.
- Security fixes:
  - CVE-2021-30590: Heap buffer overflow in Bookmarks.
  - CVE-2021-30591: Use after free in File System API.
  - CVE-2021-30592: Out of bounds write in Tab Groups.
  - CVE-2021-30593: Out of bounds read in Tab Strip.
  - CVE-2021-30594: Use after free in Page Info UI.
  - CVE-2021-30596: Incorrect security UI in Navigation.
  - CVE-2021-30597: Use after free in Browser UI.

* Mon Jul 26 2021 Alexey Gladkov <legion@altlinux.ru> 92.0.4515.107-alt1
- New version (92.0.4515.107).
- Security fixes:
  - CVE-2021-30565: Out of bounds write in Tab Groups.
  - CVE-2021-30566: Stack buffer overflow in Printing.
  - CVE-2021-30567: Use after free in DevTools.
  - CVE-2021-30568: Heap buffer overflow in WebGL.
  - CVE-2021-30569: Use after free in sqlite.
  - CVE-2021-30571: Insufficient policy enforcement in DevTools.
  - CVE-2021-30572: Use after free in Autofill.
  - CVE-2021-30573: Use after free in GPU.
  - CVE-2021-30574: Use after free in protocol handling.
  - CVE-2021-30575: Out of bounds read in Autofill.
  - CVE-2021-30576: Use after free in DevTools.
  - CVE-2021-30577: Insufficient policy enforcement in Installer.
  - CVE-2021-30578: Uninitialized Use in Media.
  - CVE-2021-30579: Use after free in UI framework.
  - CVE-2021-30580: Insufficient policy enforcement in Android intents.
  - CVE-2021-30581: Use after free in DevTools.
  - CVE-2021-30582: Inappropriate implementation in Animation.
  - CVE-2021-30583: Insufficient policy enforcement in image handling on Windows.
  - CVE-2021-30584: Incorrect security UI in Downloads.
  - CVE-2021-30585: Use after free in sensor handling.
  - CVE-2021-30586: Use after free in dialog box handling on Windows.
  - CVE-2021-30587: Inappropriate implementation in Compositing on Windows.
  - CVE-2021-30588: Type Confusion in V8.
  - CVE-2021-30589: Insufficient validation of untrusted input in Sharing.

* Sat Jul 17 2021 Alexey Gladkov <legion@altlinux.ru> 91.0.4472.164-alt1
- New version (91.0.4472.164).
- Security fixes:
  - CVE-2021-30541: Use after free in V8.
  - CVE-2021-30559: Out of bounds write in ANGLE.
  - CVE-2021-30560: Use after free in Blink XSLT.
  - CVE-2021-30561: Type Confusion in V8.
  - CVE-2021-30562: Use after free in WebSerial.
  - CVE-2021-30563: Type Confusion in V8.
  - CVE-2021-30564: Heap buffer overflow in WebXR.

* Fri Jun 25 2021 Alexey Gladkov <legion@altlinux.ru> 91.0.4472.114-alt1
- New version (91.0.4472.114).
- Security fixes:
  - CVE-2021-30554: Use after free in WebGL.
  - CVE-2021-30555: Use after free in Sharing.
  - CVE-2021-30556: Use after free in WebAudio.
  - CVE-2021-30557: Use after free in TabGroups.

* Wed Jun 16 2021 Alexey Gladkov <legion@altlinux.ru> 91.0.4472.106-alt1
- New version (91.0.4472.106).

* Thu Jun 10 2021 Alexey Gladkov <legion@altlinux.ru> 91.0.4472.101-alt1
- New version (91.0.4472.101).
- Security fixes:
  - CVE-2021-30544: Use after free in BFCache.
  - CVE-2021-30545: Use after free in Extensions.
  - CVE-2021-30546: Use after free in Autofill.
  - CVE-2021-30547: Out of bounds write in ANGLE.
  - CVE-2021-30548: Use after free in Loader.
  - CVE-2021-30549: Use after free in Spell check.
  - CVE-2021-30550: Use after free in Accessibility.
  - CVE-2021-30551: Type Confusion in V8.
  - CVE-2021-30552: Use after free in Extensions.
  - CVE-2021-30553: Use after free in Network service.

* Fri May 28 2021 Alexey Gladkov <legion@altlinux.ru> 91.0.4472.77-alt1
- New version (91.0.4472.77).
- Security fixes:
  - CVE-2021-21212: Insufficient data validation in networking.
  - CVE-2021-30521: Heap buffer overflow in Autofill.
  - CVE-2021-30522: Use after free in WebAudio.
  - CVE-2021-30523: Use after free in WebRTC.
  - CVE-2021-30524: Use after free in TabStrip.
  - CVE-2021-30525: Use after free in TabGroups.
  - CVE-2021-30526: Out of bounds write in TabStrip.
  - CVE-2021-30527: Use after free in WebUI.
  - CVE-2021-30528: Use after free in WebAuthentication.
  - CVE-2021-30529: Use after free in Bookmarks.
  - CVE-2021-30530: Out of bounds memory access in WebAudio.
  - CVE-2021-30531: Insufficient policy enforcement in Content Security Policy.
  - CVE-2021-30532: Insufficient policy enforcement in Content Security Policy.
  - CVE-2021-30533: Insufficient policy enforcement in PopupBlocker.
  - CVE-2021-30534: Insufficient policy enforcement in iFrameSandbox.
  - CVE-2021-30535: Double free in ICU.
  - CVE-2021-30536: Out of bounds read in V8.
  - CVE-2021-30537: Insufficient policy enforcement in cookies.
  - CVE-2021-30538: Insufficient policy enforcement in content security policy.
  - CVE-2021-30539: Insufficient policy enforcement in content security policy.
  - CVE-2021-30540: Incorrect security UI in payments.

* Thu Apr 15 2021 Alexey Gladkov <legion@altlinux.ru> 90.0.4430.72-alt1
- New version (90.0.4430.72).
- Security fixes:
  - CVE-2021-21201: Use after free in permissions.
  - CVE-2021-21202: Use after free in extensions.
  - CVE-2021-21203: Use after free in Blink.
  - CVE-2021-21204: Use after free in Blink.
  - CVE-2021-21205: Insufficient policy enforcement in navigation.
  - CVE-2021-21207: Use after free in IndexedDB.
  - CVE-2021-21208: Insufficient data validation in QR scanner.
  - CVE-2021-21209: Inappropriate implementation in storage.
  - CVE-2021-21210: Inappropriate implementation in Network.
  - CVE-2021-21211: Inappropriate implementation in Navigation.
  - CVE-2021-21212: Incorrect security UI in Network Config UI.
  - CVE-2021-21213: Use after free in WebMIDI.
  - CVE-2021-21214: Use after free in Network API.
  - CVE-2021-21215: Inappropriate implementation in Autofill.
  - CVE-2021-21216: Inappropriate implementation in Autofill.
  - CVE-2021-21217: Uninitialized Use in PDFium.
  - CVE-2021-21218: Uninitialized Use in PDFium.
  - CVE-2021-21219: Uninitialized Use in PDFium.
  - CVE-2021-21221: Insufficient validation of untrusted input in Mojo.

* Thu Apr 08 2021 Alexey Gladkov <legion@altlinux.ru> 89.0.4389.114-alt1
- New version (89.0.4389.114).
- Security fixes:
  - CVE-2021-21194: Use after free in screen capture.
  - CVE-2021-21195: Use after free in V8.
  - CVE-2021-21196: Heap buffer overflow in TabStrip.
  - CVE-2021-21197: Heap buffer overflow in TabStrip.
  - CVE-2021-21198: Out of bounds read in IPC.
  - CVE-2021-21199: Use Use after free in Aura.

* Mon Mar 15 2021 Alexey Gladkov <legion@altlinux.ru> 89.0.4389.90-alt1
- New version (89.0.4389.90).
- Security fixes:
  - CVE-2021-21191: Use after free in WebRTC.
  - CVE-2021-21192: Heap buffer overflow in tab groups.
  - CVE-2021-21193: Use after free in Blink.

* Tue Mar 09 2021 Alexey Gladkov <legion@altlinux.ru> 89.0.4389.82-alt1
- New version (89.0.4389.82).
- Security fixes:
  - CVE-2020-27844: Heap buffer overflow in OpenJPEG.
  - CVE-2021-21159: Heap buffer overflow in TabStrip.
  - CVE-2021-21160: Heap buffer overflow in WebAudio.
  - CVE-2021-21161: Heap buffer overflow in TabStrip.
  - CVE-2021-21162: Use after free in WebRTC.
  - CVE-2021-21163: Insufficient data validation in Reader Mode.
  - CVE-2021-21164: Insufficient data validation in Chrome for iOS.
  - CVE-2021-21165: Object lifecycle issue in audio.
  - CVE-2021-21166: Object lifecycle issue in audio.
  - CVE-2021-21167: Use after free in bookmarks.
  - CVE-2021-21168: Insufficient policy enforcement in appcache.
  - CVE-2021-21169: Out of bounds memory access in V8.
  - CVE-2021-21170: Incorrect security UI in Loader.
  - CVE-2021-21171: Incorrect security UI in TabStrip and Navigation.
  - CVE-2021-21172: Insufficient policy enforcement in File System API.
  - CVE-2021-21173: Side-channel information leakage in Network Internals.
  - CVE-2021-21174: Inappropriate implementation in Referrer.
  - CVE-2021-21175: Inappropriate implementation in Site isolation.
  - CVE-2021-21176: Inappropriate implementation in full screen mode.
  - CVE-2021-21177: Insufficient policy enforcement in Autofill.
  - CVE-2021-21178: Inappropriate implementation in Compositing.
  - CVE-2021-21179: Use after free in Network Internals.
  - CVE-2021-21180: Use after free in tab search.
  - CVE-2021-21181: Side-channel information leakage in autofill.
  - CVE-2021-21182: Insufficient policy enforcement in navigations.
  - CVE-2021-21183: Inappropriate implementation in performance APIs.
  - CVE-2021-21184: Inappropriate implementation in performance APIs.
  - CVE-2021-21185: Insufficient policy enforcement in extensions.
  - CVE-2021-21186: Insufficient policy enforcement in QR scanning.
  - CVE-2021-21187: Insufficient data validation in URL formatting.
  - CVE-2021-21188: Use after free in Blink.
  - CVE-2021-21189: Insufficient policy enforcement in payments.
  - CVE-2021-21190: Uninitialized Use in PDFium.

* Sat Feb 06 2021 Alexey Gladkov <legion@altlinux.ru> 88.0.4324.150-alt1
- New version (88.0.4324.150).
- Security fixes:
  - CVE-2021-21148: Heap buffer overflow in V8.

* Wed Feb 03 2021 Alexey Gladkov <legion@altlinux.ru> 88.0.4324.146-alt1
- New version (88.0.4324.146).
- Security fixes:
  - CVE-2021-21142: Use after free in Payments .
  - CVE-2021-21143: Heap buffer overflow in Extensions.
  - CVE-2021-21144: Heap buffer overflow in Tab Groups.
  - CVE-2021-21145: Use after free in Fonts.
  - CVE-2021-21146: Use after free in Navigation.
  - CVE-2021-21147: Inappropriate implementation in Skia.

* Sun Jan 24 2021 Alexey Gladkov <legion@altlinux.ru> 88.0.4324.96-alt1
- New version (88.0.4324.96).
- Security fixes:
  - CVE-2020-16044: Use after free in WebRTC.
  - CVE-2021-21117: Insufficient policy enforcement in Cryptohome.
  - CVE-2021-21118: Insufficient data validation in V8.
  - CVE-2021-21119: Use after free in Media.
  - CVE-2021-21120: Use after free in WebSQL.
  - CVE-2021-21121: Use after free in Omnibox.
  - CVE-2021-21122: Use after free in Blink.
  - CVE-2021-21123: Insufficient data validation in File System API.
  - CVE-2021-21124: Potential user after free in Speech Recognizer.
  - CVE-2021-21125: Insufficient policy enforcement in File System API.
  - CVE-2021-21126: Insufficient policy enforcement in extensions.
  - CVE-2021-21127: Insufficient policy enforcement in extensions.
  - CVE-2021-21128: Heap buffer overflow in Blink.
  - CVE-2021-21129: Insufficient policy enforcement in File System API.
  - CVE-2021-21130: Insufficient policy enforcement in File System API.
  - CVE-2021-21131: Insufficient policy enforcement in File System API.
  - CVE-2021-21132: Inappropriate implementation in DevTools.
  - CVE-2021-21133: Insufficient policy enforcement in Downloads.
  - CVE-2021-21134: Incorrect security UI in Page Info.
  - CVE-2021-21135: Inappropriate implementation in Performance API.
  - CVE-2021-21136: Insufficient policy enforcement in WebView.
  - CVE-2021-21137: Inappropriate implementation in DevTools.
  - CVE-2021-21138: Use after free in DevTools.
  - CVE-2021-21139: Inappropriate implementation in iframe sandbox.
  - CVE-2021-21140: Uninitialized Use in USB.
  - CVE-2021-21141: Insufficient policy enforcement in File System API.

* Fri Jan 15 2021 Alexey Gladkov <legion@altlinux.ru> 87.0.4280.141-alt2
- Fix ServiceWorkerRegistrationObjectHost double free

* Fri Jan 08 2021 Alexey Gladkov <legion@altlinux.ru> 87.0.4280.141-alt1
- New version (87.0.4280.141).
- Security fixes:
  - CVE-2020-15995: Out of bounds write in V8.
  - CVE-2020-16043: Insufficient data validation in networking.
  - CVE-2021-21106: Use after free in autofill.
  - CVE-2021-21107: Use after free in drag and drop.
  - CVE-2021-21108: Use after free in media.
  - CVE-2021-21109: Use after free in payments.
  - CVE-2021-21110: Use after free in safe browsing.
  - CVE-2021-21111: Insufficient policy enforcement in WebUI.
  - CVE-2021-21112: Use after free in Blink.
  - CVE-2021-21113: Heap buffer overflow in Skia.
  - CVE-2021-21114: Use after free in audio.
  - CVE-2021-21115: Use after free in safe browsing.
  - CVE-2021-21116: Heap buffer overflow in audio.

* Sun Dec 20 2020 Alexey Gladkov <legion@altlinux.ru> 87.0.4280.88-alt1
- New version (87.0.4280.88).
- Security fixes:
  - CVE-2020-16037: Use after free in clipboard.
  - CVE-2020-16038: Use after free in media.
  - CVE-2020-16039: Use after free in extensions.
  - CVE-2020-16040: Insufficient data validation in V8.
  - CVE-2020-16041: Out of bounds read in networking.
  - CVE-2020-16042: Uninitialized Use in V8.

* Sat Nov 21 2020 Alexey Gladkov <legion@altlinux.ru> 87.0.4280.66-alt1
- New version (87.0.4280.66).
- Security fixes:
  - CVE-2019-8075: Insufficient data validation in Flash.
  - CVE-2020-16012: Side-channel information leakage in graphics.
  - CVE-2020-16014: Use after free in PPAPI.
  - CVE-2020-16015: Insufficient data validation in WASM.
  - CVE-2020-16018: Use after free in payments.
  - CVE-2020-16019: Inappropriate implementation in filesystem.
  - CVE-2020-16020: Inappropriate implementation in cryptohome.
  - CVE-2020-16021: Race in ImageBurner.
  - CVE-2020-16022: Insufficient policy enforcement in networking.
  - CVE-2020-16023: Use after free in WebCodecs.
  - CVE-2020-16024: Heap buffer overflow in UI.
  - CVE-2020-16025: Heap buffer overflow in clipboard.
  - CVE-2020-16026: Use after free in WebRTC.
  - CVE-2020-16027: Insufficient policy enforcement in developer tools.
  - CVE-2020-16028: Heap buffer overflow in WebRTC.
  - CVE-2020-16029: Inappropriate implementation in PDFium.
  - CVE-2020-16030: Insufficient data validation in Blink.
  - CVE-2020-16031: Incorrect security UI in tab preview.
  - CVE-2020-16032: Incorrect security UI in sharing.
  - CVE-2020-16033: Incorrect security UI in WebUSB.
  - CVE-2020-16034: Inappropriate implementation in WebRTC.
  - CVE-2020-16035: Insufficient data validation in cros-disks.
  - CVE-2020-16036: Inappropriate implementation in cookies.

* Sat Oct 24 2020 Alexey Gladkov <legion@altlinux.ru> 86.0.4240.111-alt1
- New version (86.0.4240.111).
- Enable vulkan support on x86/x86_64 platforms (thx Konstantin A. Lepikhov).
- Security fixes:
  - CVE-2020-15999: Heap buffer overflow in Freetype.
  - CVE-2020-16000: Inappropriate implementation in Blink.
  - CVE-2020-16001: Use after free in media.
  - CVE-2020-16002: Use after free in PDFium.
  - CVE-2020-16003: Use after free in printing.

* Sat Oct 10 2020 Alexey Gladkov <legion@altlinux.ru> 86.0.4240.75-alt1
- New version (86.0.4240.75).
- Security fixes:
  - CVE-2020-15967: Use after free in payments.
  - CVE-2020-15968: Use after free in Blink.
  - CVE-2020-15969: Use after free in WebRTC.
  - CVE-2020-15970: Use after free in NFC.
  - CVE-2020-15971: Use after free in printing.
  - CVE-2020-15972: Use after free in audio.
  - CVE-2020-15973: Insufficient policy enforcement in extensions.
  - CVE-2020-15974: Integer overflow in Blink.
  - CVE-2020-15975: Integer overflow in SwiftShader.
  - CVE-2020-15976: Use after free in WebXR.
  - CVE-2020-15977: Insufficient data validation in dialogs.
  - CVE-2020-15978: Insufficient data validation in navigation.
  - CVE-2020-15979: Inappropriate implementation in V8.
  - CVE-2020-15980: Insufficient policy enforcement in Intents.
  - CVE-2020-15981: Out of bounds read in audio.
  - CVE-2020-15982: Side-channel information leakage in cache.
  - CVE-2020-15983: Insufficient data validation in webUI.
  - CVE-2020-15984: Insufficient policy enforcement in Omnibox.
  - CVE-2020-15985: Inappropriate implementation in Blink.
  - CVE-2020-15986: Integer overflow in media.
  - CVE-2020-15987: Use after free in WebRTC.
  - CVE-2020-15988: Insufficient policy enforcement in downloads.
  - CVE-2020-15989: Uninitialized Use in PDFium.
  - CVE-2020-15990: Use after free in autofill.
  - CVE-2020-15991: Use after free in password manager.
  - CVE-2020-15992: Insufficient policy enforcement in networking.
  - CVE-2020-6557: Inappropriate implementation in networking.

* Mon Sep 07 2020 Alexey Gladkov <legion@altlinux.ru> 85.0.4183.83-alt2
- Drop third party VAAPI patch.

* Mon Aug 31 2020 Alexey Gladkov <legion@altlinux.ru> 85.0.4183.83-alt1
- New version (85.0.4183.83).
- Security fixes:
  - CVE-2020-6558: Insufficient policy enforcement in iOS.
  - CVE-2020-6559: Use after free in presentation API.
  - CVE-2020-6560: Insufficient policy enforcement in autofill.
  - CVE-2020-6561: Inappropriate implementation in Content Security Policy.
  - CVE-2020-6562: Insufficient policy enforcement in Blink.
  - CVE-2020-6563: Insufficient policy enforcement in intent handling.
  - CVE-2020-6564: Incorrect security UI in permissions.
  - CVE-2020-6565: Incorrect security UI in Omnibox.
  - CVE-2020-6566: Insufficient policy enforcement in media.
  - CVE-2020-6567: Insufficient validation of untrusted input in command line handling.
  - CVE-2020-6568: Insufficient policy enforcement in intent handling.
  - CVE-2020-6569: Integer overflow in WebUSB.
  - CVE-2020-6570: Side-channel information leakage in WebRTC.
  - CVE-2020-6571: Incorrect security UI in Omnibox.

* Tue Jul 28 2020 Alexey Gladkov <legion@altlinux.ru> 84.0.4147.105-alt1
- New version (84.0.4147.105).
- Security fixes:
  - CVE-2020-6532: Use after free in SCTP.
  - CVE-2020-6537: Type Confusion in V8.
  - CVE-2020-6538: Inappropriate implementation in WebView.
  - CVE-2020-6539: Use after free in CSS.
  - CVE-2020-6540: Heap buffer overflow in Skia.
  - CVE-2020-6541: Use after free in WebUSB.

* Wed Jul 15 2020 Alexey Gladkov <legion@altlinux.ru> 84.0.4147.89-alt1
- New version (84.0.4147.89).
- Fix compilation with system ffmpeg 4.3 (ALT#38716)
- Security fixes:
  - CVE-2020-6510: Heap buffer overflow in background fetch.
  - CVE-2020-6511: Side-channel information leakage in content security policy.
  - CVE-2020-6512: Type Confusion in V8.
  - CVE-2020-6513: Heap buffer overflow in PDFium.
  - CVE-2020-6514: Inappropriate implementation in WebRTC.
  - CVE-2020-6515: Use after free in tab strip.
  - CVE-2020-6516: Policy bypass in CORS.
  - CVE-2020-6517: Heap buffer overflow in history.
  - CVE-2020-6518: Use after free in developer tools.
  - CVE-2020-6519: Policy bypass in CSP.
  - CVE-2020-6520: Heap buffer overflow in Skia.
  - CVE-2020-6521: Side-channel information leakage in autofill.
  - CVE-2020-6522: Inappropriate implementation in external protocol handlers.
  - CVE-2020-6523: Out of bounds write in Skia.
  - CVE-2020-6524: Heap buffer overflow in WebAudio.
  - CVE-2020-6525: Heap buffer overflow in Skia.
  - CVE-2020-6526: Inappropriate implementation in iframe sandbox.
  - CVE-2020-6527: Insufficient policy enforcement in CSP.
  - CVE-2020-6528: Incorrect security UI in basic auth.
  - CVE-2020-6529: Inappropriate implementation in WebRTC.
  - CVE-2020-6530: Out of bounds memory access in developer tools.
  - CVE-2020-6531: Side-channel information leakage in scroll to text.
  - CVE-2020-6533: Type Confusion in V8.
  - CVE-2020-6534: Heap buffer overflow in WebRTC.
  - CVE-2020-6535: Insufficient data validation in WebUI.
  - CVE-2020-6536: Incorrect security UI in PWAs.

* Mon Jun 29 2020 Andrey Cherepanov <cas@altlinux.org> 83.0.4103.61-alt2
- Prevent ignored null byte warning in Flash plugin version detection.
- Add default parameters to system-wide variable $CHROMIUM_FLAGS.
- Use Chromium name in GenericName in desktop file (ALT #36815).
- Exclude armh from build.

* Thu May 21 2020 Alexey Gladkov <legion@altlinux.ru> 83.0.4103.61-alt1
- New version (83.0.4103.61).
- Security fixes:
  - CVE-2020-6465: Use after free in reader mode.
  - CVE-2020-6466: Use after free in media.
  - CVE-2020-6467: Use after free in WebRTC.
  - CVE-2020-6468: Type Confusion in V8.
  - CVE-2020-6469: Insufficient policy enforcement in developer tools.
  - CVE-2020-6470: Insufficient validation of untrusted input in clipboard.
  - CVE-2020-6471: Insufficient policy enforcement in developer tools.
  - CVE-2020-6472: Insufficient policy enforcement in developer tools.
  - CVE-2020-6473: Insufficient policy enforcement in Blink.
  - CVE-2020-6474: Use after free in Blink.
  - CVE-2020-6475: Incorrect security UI in full screen.
  - CVE-2020-6476: Insufficient policy enforcement in tab strip.
  - CVE-2020-6477: Inappropriate implementation in installer.
  - CVE-2020-6478: Inappropriate implementation in full screen.
  - CVE-2020-6479: Inappropriate implementation in sharing.
  - CVE-2020-6480: Insufficient policy enforcement in enterprise.
  - CVE-2020-6481: Insufficient policy enforcement in URL formatting.
  - CVE-2020-6482: Insufficient policy enforcement in developer tools.
  - CVE-2020-6483: Insufficient policy enforcement in payments.
  - CVE-2020-6484: Insufficient data validation in ChromeDriver.
  - CVE-2020-6485: Insufficient data validation in media router.
  - CVE-2020-6486: Insufficient policy enforcement in navigations.
  - CVE-2020-6487: Insufficient policy enforcement in downloads.
  - CVE-2020-6488: Insufficient policy enforcement in downloads.
  - CVE-2020-6489: Inappropriate implementation in developer tools.
  - CVE-2020-6490: Insufficient data validation in loader.
  - CVE-2020-6491: Incorrect security UI in site information.

* Wed May 13 2020 Alexey Gladkov <legion@altlinux.ru> 81.0.4044.138-alt1
- New version (81.0.4044.138).
- Security fixes:
  - CVE-2020-6464: Type Confusion in Blink.
  - CVE-2020-6831: Stack buffer overflow in SCTP.
  - CVE-2020-6461: Use after free in storage.
  - CVE-2020-6462: Use after free in task scheduling.
  - CVE-2020-6458: Out of bounds read and write in PDFium.
  - CVE-2020-6459: Use after free in payments.
  - CVE-2020-6460: Insufficient data validation in URL formatting.
  - CVE-2020-6463: Use after free in ANGLE.

* Thu Apr 16 2020 Alexey Gladkov <legion@altlinux.ru> 81.0.4044.113-alt1
- New version (81.0.4044.113).
- Security fixes:
  - CVE-2020-6457: Use after free in speech recognizer.

* Wed Apr 08 2020 Alexey Gladkov <legion@altlinux.ru> 81.0.4044.92-alt1
- New version (81.0.4044.92).
- Security fixes:
  - CVE-2020-6423: Use after free in audio.
  - CVE-2020-6430: Type Confusion in V8.
  - CVE-2020-6431: Insufficient policy enforcement in full screen.
  - CVE-2020-6432: Insufficient policy enforcement in navigations.
  - CVE-2020-6433: Insufficient policy enforcement in extensions.
  - CVE-2020-6434: Use after free in devtools.
  - CVE-2020-6435: Insufficient policy enforcement in extensions.
  - CVE-2020-6436: Use after free in window management.
  - CVE-2020-6437: Inappropriate implementation in WebView.
  - CVE-2020-6438: Insufficient policy enforcement in extensions.
  - CVE-2020-6439: Insufficient policy enforcement in navigations.
  - CVE-2020-6440: Inappropriate implementation in extensions.
  - CVE-2020-6441: Insufficient policy enforcement in omnibox.
  - CVE-2020-6442: Inappropriate implementation in cache.
  - CVE-2020-6443: Insufficient data validation in developer tools.
  - CVE-2020-6444: Uninitialized Use in WebRTC.
  - CVE-2020-6445: Insufficient policy enforcement in trusted types.
  - CVE-2020-6446: Insufficient policy enforcement in trusted types.
  - CVE-2020-6447: Inappropriate implementation in developer tools.
  - CVE-2020-6448: Use after free in V8.
  - CVE-2020-6454: Use after free in extensions.
  - CVE-2020-6455: Out of bounds read in WebSQL.
  - CVE-2020-6456: Insufficient validation of untrusted input in clipboard.

* Fri Mar 06 2020 Alexey Gladkov <legion@altlinux.ru> 80.0.3987.132-alt1
- New version (80.0.3987.132).
- Security fixes:
  - CVE-2019-18197: Multiple vulnerabilities in XML.
  - CVE-2019-19923: Out of bounds memory access in SQLite.
  - CVE-2019-19925: Multiple vulnerabilities in SQLite.
  - CVE-2019-19926: Inappropriate implementation in SQLite.
  - CVE-2020-6381: Integer overflow in JavaScript.
  - CVE-2020-6382: Type Confusion in JavaScript.
  - CVE-2020-6383: Type confusion in V8.
  - CVE-2020-6384: Use after free in WebAudio.
  - CVE-2020-6385: Insufficient policy enforcement in storage.
  - CVE-2020-6386: Use after free in speech.
  - CVE-2020-6387: Out of bounds write in WebRTC.
  - CVE-2020-6388: Out of bounds memory access in WebAudio.
  - CVE-2020-6389: Out of bounds write in WebRTC.
  - CVE-2020-6390: Out of bounds memory access in streams.
  - CVE-2020-6391: Insufficient validation of untrusted input in Blink.
  - CVE-2020-6392: Insufficient policy enforcement in extensions.
  - CVE-2020-6393: Insufficient policy enforcement in Blink.
  - CVE-2020-6394: Insufficient policy enforcement in Blink.
  - CVE-2020-6395: Out of bounds read in JavaScript.
  - CVE-2020-6396: Inappropriate implementation in Skia.
  - CVE-2020-6397: Incorrect security UI in sharing.
  - CVE-2020-6398: Uninitialized use in PDFium.
  - CVE-2020-6399: Insufficient policy enforcement in AppCache.
  - CVE-2020-6400: Inappropriate implementation in CORS.
  - CVE-2020-6401: Insufficient validation of untrusted input in Omnibox.
  - CVE-2020-6402: Insufficient policy enforcement in downloads.
  - CVE-2020-6403: Incorrect security UI in Omnibox.
  - CVE-2020-6404: Inappropriate implementation in Blink.
  - CVE-2020-6405: Out of bounds read in SQLite.
  - CVE-2020-6406: Use after free in audio.
  - CVE-2020-6407: Out of bounds memory access in streams.
  - CVE-2020-6408: Insufficient policy enforcement in CORS.
  - CVE-2020-6409: Inappropriate implementation in Omnibox.
  - CVE-2020-6410: Insufficient policy enforcement in navigation.
  - CVE-2020-6411: Insufficient validation of untrusted input in Omnibox.
  - CVE-2020-6412: Insufficient validation of untrusted input in Omnibox.
  - CVE-2020-6413: Inappropriate implementation in Blink.
  - CVE-2020-6414: Insufficient policy enforcement in Safe Browsing.
  - CVE-2020-6415: Inappropriate implementation in JavaScript.
  - CVE-2020-6416: Insufficient data validation in streams.
  - CVE-2020-6417: Inappropriate implementation in installer.
  - CVE-2020-6418: Type confusion in V8.
  - CVE-2020-6420: Insufficient policy enforcement in media.

* Mon Feb 03 2020 Alexey Gladkov <legion@altlinux.ru> 79.0.3945.130-alt1
- New version (79.0.3945.130).
- Security fixes:
  - CVE-2019-13767: Use after free in media picker.
  - CVE-2020-6377: Use after free in audio.
  - CVE-2020-6378: Use-after-free in speech recognizer.
  - CVE-2020-6379: Use-after-free in speech recognizer.
  - CVE-2020-6380: Extension message verification error.

* Mon Dec 16 2019 Alexey Gladkov <legion@altlinux.ru> 79.0.3945.79-alt1
- New version (79.0.3945.79).
- Security fixes:
  - CVE-2019-13725: Use after free in Bluetooth.
  - CVE-2019-13726: Heap buffer overflow in password manager.
  - CVE-2019-13727: Insufficient policy enforcement in WebSockets.
  - CVE-2019-13728: Out of bounds write in V8.
  - CVE-2019-13729: Use after free in WebSockets.
  - CVE-2019-13730: Type Confusion in V8.
  - CVE-2019-13732: Use after free in WebAudio.
  - CVE-2019-13734: Out of bounds write in SQLite.
  - CVE-2019-13735: Out of bounds write in V8.
  - CVE-2019-13736: Integer overflow in PDFium.
  - CVE-2019-13737: Insufficient policy enforcement in autocomplete.
  - CVE-2019-13738: Insufficient policy enforcement in navigation.
  - CVE-2019-13739: Incorrect security UI in Omnibox.
  - CVE-2019-13740: Incorrect security UI in sharing.
  - CVE-2019-13741: Insufficient validation of untrusted input in Blink.
  - CVE-2019-13742: Incorrect security UI in Omnibox.
  - CVE-2019-13743: Incorrect security UI in external protocol handling.
  - CVE-2019-13744: Insufficient policy enforcement in cookies.
  - CVE-2019-13745: Insufficient policy enforcement in audio.
  - CVE-2019-13746: Insufficient policy enforcement in Omnibox.
  - CVE-2019-13747: Uninitialized Use in rendering.
  - CVE-2019-13748: Insufficient policy enforcement in developer tools.
  - CVE-2019-13749: Incorrect security UI in Omnibox.
  - CVE-2019-13750: Insufficient data validation in SQLite.
  - CVE-2019-13751: Uninitialized Use in SQLite.
  - CVE-2019-13752: Out of bounds read in SQLite.
  - CVE-2019-13753: Out of bounds read in SQLite.
  - CVE-2019-13754: Insufficient policy enforcement in extensions.
  - CVE-2019-13755: Insufficient policy enforcement in extensions.
  - CVE-2019-13756: Incorrect security UI in printing.
  - CVE-2019-13757: Incorrect security UI in Omnibox.
  - CVE-2019-13758: Insufficient policy enforcement in navigation.
  - CVE-2019-13759: Incorrect security UI in interstitials.
  - CVE-2019-13761: Incorrect security UI in Omnibox.
  - CVE-2019-13762: Insufficient policy enforcement in downloads.
  - CVE-2019-13763: Insufficient policy enforcement in payments.
  - CVE-2019-13764: Type Confusion in V8.

* Mon Dec 02 2019 Alexey Gladkov <legion@altlinux.ru> 78.0.3904.108-alt1
- New version (78.0.3904.108).
- Security fixes:
  - CVE-2019-13723: Use-after-free in Bluetooth.
  - CVE-2019-13724: Out-of-bounds access in Bluetooth.

* Sat Nov 09 2019 Alexey Gladkov <legion@altlinux.ru> 78.0.3904.97-alt1
- New version (78.0.3904.97).
- Security fixes:
  - CVE-2019-13720: Use-after-free in audio.
  - CVE-2019-13721: Use-after-free in PDFium.

* Thu Oct 24 2019 Alexey Gladkov <legion@altlinux.ru> 78.0.3904.70-alt1
- New version (78.0.3904.70).
- Security fixes:
  - CVE-2019-13699: Use-after-free in media.
  - CVE-2019-13700: Buffer overrun in Blink.
  - CVE-2019-13701: URL spoof in navigation.
  - CVE-2019-13702: Privilege elevation in Installer.
  - CVE-2019-13703: URL bar spoofing.
  - CVE-2019-13704: CSP bypass.
  - CVE-2019-13705: Extension permission bypass.
  - CVE-2019-13706: Out-of-bounds read in PDFium.
  - CVE-2019-13707: File storage disclosure.
  - CVE-2019-13708: HTTP authentication spoof.
  - CVE-2019-13709: File download protection bypass.
  - CVE-2019-13710: File download protection bypass.
  - CVE-2019-13711: Cross-context information leak.
  - CVE-2019-13713: Cross-origin data leak.
  - CVE-2019-13714: CSS injection.
  - CVE-2019-13715: Address bar spoofing.
  - CVE-2019-13716: Service worker state error.
  - CVE-2019-13717: Notification obscured.
  - CVE-2019-13718: IDN spoof.
  - CVE-2019-13719: Notification obscured.
  - CVE-2019-15903: Buffer overflow in expat.

* Mon Oct 21 2019 Alexey Gladkov <legion@altlinux.ru> 77.0.3865.120-alt1
- New version (77.0.3865.120).
- Security fixes:
  - CVE-2019-13693: Use-after-free in IndexedDB.
  - CVE-2019-13694: Use-after-free in WebRTC.
  - CVE-2019-13695: Use-after-free in audio.
  - CVE-2019-13696: Use-after-free in V8.
  - CVE-2019-13697: Cross-origin size leak.

* Wed Sep 25 2019 Alexey Gladkov <legion@altlinux.ru> 77.0.3865.90-alt1
- New version (77.0.3865.90).
- Security fixes:
  - CVE-2019-13685: Use-after-free in UI.
  - CVE-2019-13686: Use-after-free in offline pages.
  - CVE-2019-13687: Use-after-free in media.
  - CVE-2019-13688: Use-after-free in media.

* Mon Sep 23 2019 Alexey Gladkov <legion@altlinux.ru> 77.0.3865.75-alt1
- New version (77.0.3865.75).
- Security fixes:
  - CVE-2019-13659: URL spoof.
  - CVE-2019-13660: Full screen notification overlap.
  - CVE-2019-13661: Full screen notification spoof.
  - CVE-2019-13662: CSP bypass.
  - CVE-2019-13663: IDN spoof.
  - CVE-2019-13664: CSRF bypass.
  - CVE-2019-13665: Multiple file download protection bypass.
  - CVE-2019-13666: Side channel using storage size estimate.
  - CVE-2019-13667: URI bar spoof when using external app URIs.
  - CVE-2019-13668: Global window leak via console.
  - CVE-2019-13669: HTTP authentication spoof.
  - CVE-2019-13670: V8 memory corruption in regex.
  - CVE-2019-13671: Dialog box fails to show origin.
  - CVE-2019-13673: Cross-origin information leak using devtools.
  - CVE-2019-13674: IDN spoofing.
  - CVE-2019-13675: Extensions can be disabled by trailing slash.
  - CVE-2019-13676: Google URI shown for certificate warning.
  - CVE-2019-13677: Chrome web store origin needs to be isolated.
  - CVE-2019-13678: Download dialog spoofing.
  - CVE-2019-13679: User gesture needed for printing.
  - CVE-2019-13680: IP address spoofing to servers.
  - CVE-2019-13681: Bypass on download restrictions.
  - CVE-2019-13682: Site isolation bypass.
  - CVE-2019-13683: Exceptions leaked by devtools.
  - CVE-2019-5870: Use-after-free in media.
  - CVE-2019-5871: Heap overflow in Skia.
  - CVE-2019-5872: Use-after-free in Mojo.
  - CVE-2019-5873: URL bar spoofing on iOS.
  - CVE-2019-5874: External URIs may trigger other browsers.
  - CVE-2019-5875: URL bar spoof via download redirect.
  - CVE-2019-5876: Use-after-free in media.
  - CVE-2019-5877: Out-of-bounds access in V8.
  - CVE-2019-5878: Use-after-free in V8.
  - CVE-2019-5879: Extensions can read some local files.
  - CVE-2019-5880: SameSite cookie bypass.
  - CVE-2019-5881: Arbitrary read in SwiftShader.

* Fri Aug 02 2019 Alexey Gladkov <legion@altlinux.ru> 76.0.3809.87-alt1
- New version (76.0.3809.87).
- Security fixes:
  - CVE-2019-5850: Use-after-free in offline page fetcher.
  - CVE-2019-5851: Use-after-poison in offline audio context.
  - CVE-2019-5852: Object leak of utility functions.
  - CVE-2019-5853: Memory corruption in regexp length check.
  - CVE-2019-5854: Integer overflow in PDFium text rendering.
  - CVE-2019-5855: Integer overflow in PDFium.
  - CVE-2019-5856: Insufficient checks on filesystem: URI permissions.
  - CVE-2019-5857: Comparison of -0 and null yields crash.
  - CVE-2019-5858: Insufficient filtering of Open URL service parameters.
  - CVE-2019-5859: res: URIs can load alternative browsers.
  - CVE-2019-5860: Use-after-free in PDFium.
  - CVE-2019-5861: Click location incorrectly checked.
  - CVE-2019-5862: AppCache not robust to compromised renderers.
  - CVE-2019-5863: Use-after-free in WebUSB on Windows.
  - CVE-2019-5864: Insufficient port filtering in CORS for extensions.
  - CVE-2019-5865: Site isolation bypass from compromised renderer.

* Fri May 03 2019 Alexey Gladkov <legion@altlinux.ru> 74.0.3729.131-alt1
- New version (74.0.3729.131).
- Security fixes:
  - CVE-2019-5805: Use after free in PDFium.
  - CVE-2019-5806: Integer overflow in Angle.
  - CVE-2019-5807: Memory corruption in V8.
  - CVE-2019-5808: Use after free in Blink.
  - CVE-2019-5809: Use after free in Blink.
  - CVE-2019-5810: User information disclosure in Autofill.
  - CVE-2019-5811: CORS bypass in Blink.
  - CVE-2019-5812: URL spoof in Omnibox on iOS.
  - CVE-2019-5813: Out of bounds read in V8.
  - CVE-2019-5814: CORS bypass in Blink.
  - CVE-2019-5815: Heap buffer overflow in Blink.
  - CVE-2019-5816: Exploit persistence extension on Android.
  - CVE-2019-5817: Heap buffer overflow in Angle on Windows.
  - CVE-2019-5818: Uninitialized value in media reader.
  - CVE-2019-5819: Incorrect escaping in developer tools.
  - CVE-2019-5820: Integer overflow in PDFium.
  - CVE-2019-5821: Integer overflow in PDFium.
  - CVE-2019-5822: CORS bypass in download manager.
  - CVE-2019-5823: Forced navigation from service worker.
  - CVE-2019-5824: Parameter passing error in media player.
  - CVE-2019-5825: Out-of-bounds write in V8
  - CVE-2019-5826: Use-after-free in IndexedDB
  - CVE-2019-5827: Out-of-bounds access in SQLite.

* Mon Mar 18 2019 Alexey Gladkov <legion@altlinux.ru> 73.0.3683.75-alt1
- New version (73.0.3683.75).
- Security fixes:
  - CVE-2019-5787: Use after free in Canvas.
  - CVE-2019-5788: Use after free in FileAPI.
  - CVE-2019-5789: Use after free in WebMIDI.
  - CVE-2019-5790: Heap buffer overflow in V8.
  - CVE-2019-5791: Type confusion in V8.
  - CVE-2019-5792: Integer overflow in PDFium.
  - CVE-2019-5793: Excessive permissions for private API in Extensions.
  - CVE-2019-5794: Security UI spoofing.
  - CVE-2019-5795: Integer overflow in PDFium.
  - CVE-2019-5796: Race condition in Extensions.
  - CVE-2019-5797: Race condition in DOMStorage.
  - CVE-2019-5798: Out of bounds read in Skia.
  - CVE-2019-5799: CSP bypass with blob URL.
  - CVE-2019-5800: CSP bypass with blob URL.
  - CVE-2019-5801: Incorrect Omnibox display on iOS.
  - CVE-2019-5802: Security UI spoofing.
  - CVE-2019-5803: CSP bypass with Javascript URLs'.
  - CVE-2019-5804: Command line command injection on Windows.

* Sun Mar 03 2019 Alexey Gladkov <legion@altlinux.ru> 72.0.3626.121-alt1
- New version (72.0.3626.121).

* Mon Feb 04 2019 Alexey Gladkov <legion@altlinux.ru> 72.0.3626.81-alt1
- New version (72.0.3626.81).
- Security fixes:
  - CVE-2019-5754: Inappropriate implementation in QUIC Networking.
  - CVE-2019-5755: Inappropriate implementation in V8.
  - CVE-2019-5756: Use after free in PDFium.
  - CVE-2019-5757: Type Confusion in SVG.
  - CVE-2019-5758: Use after free in Blink.
  - CVE-2019-5759: Use after free in HTML select elements.
  - CVE-2019-5760: Use after free in WebRTC.
  - CVE-2019-5761: Use after free in SwiftShader.
  - CVE-2019-5762: Use after free in PDFium.
  - CVE-2019-5763: Insufficient validation of untrusted input in V8.
  - CVE-2019-5764: Use after free in WebRTC.
  - CVE-2019-5765: Insufficient policy enforcement in the browser.
  - CVE-2019-5766: Insufficient policy enforcement in Canvas.
  - CVE-2019-5767: Incorrect security UI in WebAPKs.
  - CVE-2019-5768: Insufficient policy enforcement in DevTools.
  - CVE-2019-5769: Insufficient validation of untrusted input in Blink.
  - CVE-2019-5770: Heap buffer overflow in WebGL.
  - CVE-2019-5771: Heap buffer overflow in SwiftShader.
  - CVE-2019-5772: Use after free in PDFium.
  - CVE-2019-5773: Insufficient data validation in IndexedDB.
  - CVE-2019-5774: Insufficient validation of untrusted input in SafeBrowsing.
  - CVE-2019-5775: Insufficient policy enforcement in Omnibox.
  - CVE-2019-5776: Insufficient policy enforcement in Omnibox.
  - CVE-2019-5777: Insufficient policy enforcement in Omnibox.
  - CVE-2019-5778: Insufficient policy enforcement in Extensions.
  - CVE-2019-5779: Insufficient policy enforcement in ServiceWorker.
  - CVE-2019-5780: Insufficient policy enforcement.
  - CVE-2019-5781: Insufficient policy enforcement in Omnibox.
  - CVE-2019-5782: Inappropriate implementation in V8.
  - CVE-2019-5783: Insufficient validation of untrusted input in DevTools.

* Fri Dec 14 2018 Alexey Gladkov <legion@altlinux.ru> 71.0.3578.98-alt1
- New version (71.0.3578.98).
- Security fixes:
  - CVE-2018-17481: Use after free in PDFium.

* Wed Nov 07 2018 Alexey Gladkov <legion@altlinux.ru> 70.0.3538.77-alt1
- New version (70.0.3538.77).

* Mon Oct 22 2018 Alexey Gladkov <legion@altlinux.ru> 70.0.3538.67-alt1
- New version (70.0.3538.67).
- Security fixes:
  - CVE-2018-17462: Sandbox escape in AppCache.
  - CVE-2018-17463: Remote code execution in V8.
  - CVE to be assigned: Heap buffer overflow in Little CMS in PDFium.
  - CVE-2018-17464: URL spoof in Omnibox.
  - CVE-2018-17465: Use after free in V8.
  - CVE-2018-17466: Memory corruption in Angle.
  - CVE-2018-17467: URL spoof in Omnibox.
  - CVE-2018-17468: Cross-origin URL disclosure in Blink.
  - CVE-2018-17469: Heap buffer overflow in PDFium.
  - CVE-2018-17470: Memory corruption in GPU Internals.
  - CVE-2018-17471: Security UI occlusion in full screen mode.
  - CVE-2018-17472: iframe sandbox escape on iOS.
  - CVE-2018-17473: URL spoof in Omnibox.
  - CVE-2018-17474: Use after free in Blink.
  - CVE-2018-17475: URL spoof in Omnibox.
  - CVE-2018-17476: Security UI occlusion in full screen mode.
  - CVE-2018-5179: Lack of limits on update() in ServiceWorker.
  - CVE-2018-17477: UI spoof in Extensions.

* Thu Oct 11 2018 Alexey Gladkov <legion@altlinux.ru> 69.0.3497.100-alt1
- New version (69.0.3497.100).
- Add symlink /usr/bin/chromium -> chromium-browser.

* Wed Sep 05 2018 Alexey Gladkov <legion@altlinux.ru> 69.0.3497.81-alt1
- New version (69.0.3497.81).
- Security fixes:
  - CVE-2018-16065: Out of bounds write in V8.
  - CVE-2018-16066: Out of bounds read in Blink.
  - CVE-2018-16067: Out of bounds read in WebAudio.
  - CVE-2018-16068: Out of bounds write in Mojo.
  - CVE-2018-16069: Out of bounds read in SwiftShader.
  - CVE-2018-16070: Integer overflow in Skia.
  - CVE-2018-16071: Use after free in WebRTC.
  - CVE-2018-16072: Cross origin pixel leak in Chrome's interaction with Android's MediaPlayer.
  - CVE-2018-16073: Site Isolation bypass after tab restore.
  - CVE-2018-16074: Site Isolation bypass using Blob URLS.
  - CVE-2018-16075: Local file access in Blink.
  - CVE-2018-16076: Out of bounds read in PDFium.
  - CVE-2018-16077: Content security policy bypass in Blink.
  - CVE-2018-16078: Credit card information leak in Autofill.
  - CVE-2018-16079: URL spoof in permission dialogs.
  - CVE-2018-16080: URL spoof in full screen mode.
  - CVE-2018-16081: Local file access in DevTools.
  - CVE-2018-16082: Stack buffer overflow in SwiftShader.
  - CVE-2018-16083: Out of bounds read in WebRTC.
  - CVE-2018-16084: User confirmation bypass in external protocol handling.
  - CVE-2018-16085: Use after free in Memory Instrumentation.
  - Out of bounds read in Little-CMS.

* Wed Aug 08 2018 Alexey Gladkov <legion@altlinux.ru> 68.0.3440.84-alt1
- New version (68.0.3440.84).
- Security fixes:
  - CVE-2018-6153: Stack buffer overflow in Skia.
  - CVE-2018-6154: Heap buffer overflow in WebGL.
  - CVE-2018-6155: Use after free in WebRTC.
  - CVE-2018-6156: Heap buffer overflow in WebRTC.
  - CVE-2018-6157: Type confusion in WebRTC.
  - CVE-2018-6158: Use after free in Blink.
  - CVE-2018-6159: Same origin policy bypass in ServiceWorker.
  - CVE-2018-6160: URL spoof in Chrome on iOS.
  - CVE-2018-6161: Same origin policy bypass in WebAudio.
  - CVE-2018-6162: Heap buffer overflow in WebGL.
  - CVE-2018-6163: URL spoof in Omnibox.
  - CVE-2018-6164: Same origin policy bypass in ServiceWorker.
  - CVE-2018-6165: URL spoof in Omnibox.
  - CVE-2018-6166: URL spoof in Omnibox.
  - CVE-2018-6167: URL spoof in Omnibox.
  - CVE-2018-6168: CORS bypass in Blink.
  - CVE-2018-6169: Permissions bypass in extension installation .
  - CVE-2018-6170: Type confusion in PDFium.
  - CVE-2018-6171: Use after free in WebBluetooth.
  - CVE-2018-6172: URL spoof in Omnibox.
  - CVE-2018-6173: URL spoof in Omnibox.
  - CVE-2018-6174: Integer overflow in SwiftShader.
  - CVE-2018-6175: URL spoof in Omnibox.
  - CVE-2018-6176: Local user privilege escalation in Extensions.
  - CVE-2018-6177: Cross origin information leak in Blink.
  - CVE-2018-6178: UI spoof in Extensions.
  - CVE-2018-6179: Local file information leak in Extensions.
  - CVE-2018-6044: Request privilege escalation in Extensions .
  - CVE-2018-4117: Cross origin information leak in Blink.
  - CVE-2018-6150: Cross origin information disclosure in Service Workers.
  - CVE-2018-6151: Bad cast in DevTools.
  - CVE-2018-6152: Local file write in DevTools.

* Sun Jun 17 2018 Alexey Gladkov <legion@altlinux.ru> 67.0.3396.87-alt1
- New version (67.0.3396.87).
- Use ninja-build.
- Security fixes:
  - CVE-2018-6149: Out of bounds write in V8.
  - CVE-2018-6148: Incorrect handling of CSP header.
  - CVE-2018-6123: Use after free in Blink.
  - CVE-2018-6124: Type confusion in Blink.
  - CVE-2018-6125: Overly permissive policy in WebUSB.
  - CVE-2018-6126: Heap buffer overflow in Skia.
  - CVE-2018-6127: Use after free in indexedDB.
  - CVE-2018-6128: uXSS in Chrome on iOS.
  - CVE-2018-6129: Out of bounds memory access in WebRTC.
  - CVE-2018-6130: Out of bounds memory access in WebRTC.
  - CVE-2018-6131: Incorrect mutability protection in WebAssembly.
  - CVE-2018-6132: Use of uninitialized memory in WebRTC.
  - CVE-2018-6133: URL spoof in Omnibox.
  - CVE-2018-6134: Referrer Policy bypass in Blink.
  - CVE-2018-6135: UI spoofing in Blink.
  - CVE-2018-6136: Out of bounds memory access in V8.
  - CVE-2018-6137: Leak of visited status of page in Blink.
  - CVE-2018-6138: Overly permissive policy in Extensions.
  - CVE-2018-6139: Restrictions bypass in the debugger extension API.
  - CVE-2018-6140: Restrictions bypass in the debugger extension API.
  - CVE-2018-6141: Heap buffer overflow in Skia.
  - CVE-2018-6142: Out of bounds memory access in V8.
  - CVE-2018-6143: Out of bounds memory access in V8.
  - CVE-2018-6144: Out of bounds memory access in PDFium.
  - CVE-2018-6145: Incorrect escaping of MathML in Blink.
  - CVE-2018-6147: Password fields not taking advantage of OS protections in Views.

* Thu Apr 19 2018 Alexey Gladkov <legion@altlinux.ru> 66.0.3359.117-alt1
- New version (66.0.3359.117).
- Security fixes:
  - CVE-2018-6085: Use after free in Disk Cache.
  - CVE-2018-6086: Use after free in Disk Cache.
  - CVE-2018-6087: Use after free in WebAssembly.
  - CVE-2018-6088: Use after free in PDFium.
  - CVE-2018-6089: Same origin policy bypass in Service Worker.
  - CVE-2018-6090: Heap buffer overflow in Skia.
  - CVE-2018-6091: Incorrect handling of plug-ins by Service Worker.
  - CVE-2018-6092: Integer overflow in WebAssembly.
  - CVE-2018-6093: Same origin bypass in Service Worker.
  - CVE-2018-6094: Exploit hardening regression in Oilpan.
  - CVE-2018-6095: Lack of meaningful user interaction requirement before file upload.
  - CVE-2018-6096: Fullscreen UI spoof.
  - CVE-2018-6097: Fullscreen UI spoof.
  - CVE-2018-6098: URL spoof in Omnibox.
  - CVE-2018-6099: CORS bypass in ServiceWorker.
  - CVE-2018-6100: URL spoof in Omnibox.
  - CVE-2018-6101: Insufficient protection of remote debugging prototol in DevTools .
  - CVE-2018-6102: URL spoof in Omnibox.
  - CVE-2018-6103: UI spoof in Permissions.
  - CVE-2018-6104: URL spoof in Omnibox.
  - CVE-2018-6105: URL spoof in Omnibox.
  - CVE-2018-6106: Incorrect handling of promises in V8.
  - CVE-2018-6107: URL spoof in Omnibox.
  - CVE-2018-6108: URL spoof in Omnibox.
  - CVE-2018-6109: Incorrect handling of files by FileAPI.
  - CVE-2018-6110: Incorrect handling of plaintext files via file:// .
  - CVE-2018-6111: Heap-use-after-free in DevTools.
  - CVE-2018-6112: Incorrect URL handling in DevTools.
  - CVE-2018-6113: URL spoof in Navigation.
  - CVE-2018-6114: CSP bypass.
  - CVE-2018-6115: SmartScreen bypass in downloads.
  - CVE-2018-6116: Incorrect low memory handling in WebAssembly.
  - CVE-2018-6117: Confusing autofill settings.
  - CVE-2018-6084: Incorrect use of Distributed Objects in Google Software Updater on MacOS.

* Fri Mar 30 2018 Alexey Gladkov <legion@altlinux.ru> 65.0.3325.181-alt1
- New version (65.0.3325.181).

* Wed Mar 07 2018 Alexey Gladkov <legion@altlinux.ru> 65.0.3325.146-alt1
- New version (65.0.3325.146).
- Use clang.
- Security fixes:
  - CVE-2018-6058: Use after free in Flash.
  - CVE-2018-6059: Use after free in Flash.
  - CVE-2018-6060: Use after free in Blink.
  - CVE-2018-6061: Race condition in V8.
  - CVE-2018-6062: Heap buffer overflow in Skia.
  - CVE-2018-6057: Incorrect permissions on shared memory.
  - CVE-2018-6063: Incorrect permissions on shared memory.
  - CVE-2018-6064: Type confusion in V8.
  - CVE-2018-6065: Integer overflow in V8.
  - CVE-2018-6066: Same Origin Bypass via canvas.
  - CVE-2018-6067: Buffer overflow in Skia.
  - CVE-2018-6068: Object lifecycle issues in Chrome Custom Tab.
  - CVE-2018-6069: Stack buffer overflow in Skia.
  - CVE-2018-6070: CSP bypass through extensions.
  - CVE-2018-6071: Heap bufffer overflow in Skia.
  - CVE-2018-6072: Integer overflow in PDFium.
  - CVE-2018-6073: Heap bufffer overflow in WebGL.
  - CVE-2018-6074: Mark-of-the-Web bypass.
  - CVE-2018-6075: Overly permissive cross origin downloads.
  - CVE-2018-6076: Incorrect handling of URL fragment identifiers in Blink.
  - CVE-2018-6077: Timing attack using SVG filters.
  - CVE-2018-6078: URL Spoof in OmniBox.
  - CVE-2018-6079: Information disclosure via texture data in WebGL.
  - CVE-2018-6080: Information disclosure in IPC call.
  - CVE-2018-6081: XSS in interstitials.
  - CVE-2018-6082: Circumvention of port blocking.
  - CVE-2018-6083: Incorrect processing of AppManifests.

* Thu Jan 25 2018 Alexey Gladkov <legion@altlinux.ru> 64.0.3282.119-alt1
- New version (64.0.3282.119).
- Security fixes:
  - CVE-2018-6031: Use after free in PDFium.
  - CVE-2018-6032: Same origin bypass in Shared Worker.
  - CVE-2018-6033: Race when opening downloaded files.
  - CVE-2018-6034: Integer overflow in Blink.
  - CVE-2018-6035: Insufficient isolation of devtools from extensions.
  - CVE-2018-6036: Integer underflow in WebAssembly.
  - CVE-2018-6037: Insufficient user gesture requirements in autofill.
  - CVE-2018-6038: Heap buffer overflow in WebGL.
  - CVE-2018-6039: XSS in DevTools.
  - CVE-2018-6040: Content security policy bypass.
  - CVE-2018-6041: URL spoof in Navigation.
  - CVE-2018-6042: URL spoof in OmniBox.
  - CVE-2018-6043: Insufficient escaping with external URL handlers.
  - CVE-2018-6045: Insufficient isolation of devtools from extensions.
  - CVE-2018-6046: Insufficient isolation of devtools from extensions.
  - CVE-2018-6047: Cross origin URL leak in WebGL.
  - CVE-2018-6048: Referrer policy bypass in Blink.
  - CVE-2017-15420: URL spoofing in Omnibox.
  - CVE-2018-6049: UI spoof in Permissions.
  - CVE-2018-6050: URL spoof in OmniBox.
  - CVE-2018-6051: Referrer leak in XSS Auditor.
  - CVE-2018-6052: Incomplete no-referrer policy implementation.
  - CVE-2018-6053: Leak of page thumbnails in New Tab Page.
  - CVE-2018-6054: Use after free in WebUI.

* Fri Jan 05 2018 Alexey Gladkov <legion@altlinux.ru> 63.0.3239.132-alt1
- New version (63.0.3239.132).
- Build contains a number of bug fixes and security updates.

* Sat Dec 16 2017 Alexey Gladkov <legion@altlinux.ru> 63.0.3239.108-alt1
- New version (63.0.3239.108).
- Security fixes:
  - CVE-2017-15429: UXSS in V8.

* Mon Nov 13 2017 Alexey Gladkov <legion@altlinux.ru> 62.0.3202.89-alt1
- New version (62.0.3202.89).
- Security fixes:
  - CVE-2017-15398: Stack buffer overflow in QUIC.
  - CVE-2017-15399: Use after free in V8.

* Tue Oct 24 2017 Alexey Gladkov <legion@altlinux.ru> 62.0.3202.75-alt1
- New version (62.0.3202.75).
- Security fixes:
  - CVE-2017-5124: UXSS with MHTML.
  - CVE-2017-5125: Heap overflow in Skia.
  - CVE-2017-5126: Use after free in PDFium.
  - CVE-2017-5127: Use after free in PDFium.
  - CVE-2017-5128: Heap overflow in WebGL.
  - CVE-2017-5129: Use after free in WebAudio.
  - CVE-2017-5132: Incorrect stack manipulation in WebAssembly.
  - CVE-2017-5130: Heap overflow in libxml2.
  - CVE-2017-5131: Out of bounds write in Skia.
  - CVE-2017-5133: Out of bounds write in Skia.
  - CVE-2017-15386: UI spoofing in Blink.
  - CVE-2017-15387: Content security bypass.
  - CVE-2017-15388: Out of bounds read in Skia.
  - CVE-2017-15389: URL spoofing in OmniBox.
  - CVE-2017-15390: URL spoofing in OmniBox.
  - CVE-2017-15391: Extension limitation bypass in Extensions.
  - CVE-2017-15392: Incorrect registry key handling in PlatformIntegration.
  - CVE-2017-15393: Referrer leak in Devtools.
  - CVE-2017-15394: URL spoofing in extensions UI.
  - CVE-2017-15395: Null pointer dereference in ImageCapture.

* Tue Sep 26 2017 Alexey Gladkov <legion@altlinux.ru> 61.0.3163.100-alt1
- Security fixes:
  - CVE-2017-5121: Out-of-bounds access in V8. Reported by Jordan Rabet, Microsoft Offensive Security Research and Microsoft ChakraCore team on 2017-09-14
  - CVE-2017-5122: Out-of-bounds access in V8. Reported by Choongwoo Han of Naver Corporation on 2017-08-04

* Tue Sep 12 2017 Alexey Gladkov <legion@altlinux.ru> 61.0.3163.79-alt1
- New version (61.0.3163.79).
- Security fixes:
  - CVE-2017-5111: Use after free in PDFium. Reported by Luat Nguyen (@l4wio) of KeenLab, Tencent on 2017-06-27
  - CVE-2017-5112: Heap buffer overflow in WebGL. Reported by Tobias Klein (www.trapkit.de) on 2017-07-10
  - CVE-2017-5113: Heap buffer overflow in Skia. Reported by Anonymous on 2017-07-20
  - CVE-2017-5114: Memory lifecycle issue in PDFium. Reported by Ke Liu of Tencent's Xuanwu LAB on 2017-08-07
  - CVE-2017-5115: Type confusion in V8. Reported by Marco Giovannini on 2017-07-17
  - CVE-2017-5116: Type confusion in V8. Reported Guang Gong of Alpha Team, Qihoo 360 on 2017-08-28
  - CVE-2017-5117: Use of uninitialized value in Skia. Reported by Tobias Klein (www.trapkit.de) on 2017-07-04
  - CVE-2017-5118: Bypass of Content Security Policy in Blink. Reported by WenXu Wu of Tencent's Xuanwu Lab on 2017-07-24
  - CVE-2017-5119: Use of uninitialized value in Skia. Reported by Anonymous on 2017-05-22
  - CVE-2017-5120: Potential HTTPS downgrade during redirect navigation. Reported by Xiaoyin Liu (@general_nfs) on 2017-05-05

* Tue Aug 15 2017 Alexey Gladkov <legion@altlinux.ru> 60.0.3112.90-alt2
- Add missing libraries (ALT#33750).

* Mon Aug 14 2017 Alexey Gladkov <legion@altlinux.ru> 60.0.3112.90-alt1
- New version (60.0.3112.90).

* Tue Aug 01 2017 Alexey Gladkov <legion@altlinux.ru> 60.0.3112.78-alt1
- New version (60.0.3112.78).
- Security fixes:
  - CVE-2017-5091: Use after free in IndexedDB. Reported by Ned Williamson on 2017-06-02
  - CVE-2017-5092: Use after free in PPAPI. Reported by Yu Zhou, Yuan Deng of Ant-financial Light-Year Security Lab on 2017-06-15
  - CVE-2017-5093: UI spoofing in Blink. Reported by Luan Herrera on 2015-10-31
  - CVE-2017-5094: Type confusion in extensions. Reported by Anonymous on 2017-03-19
  - CVE-2017-5095: Out-of-bounds write in PDFium. Reported by Anonymous on 2017-06-13
  - CVE-2017-5096: User information leak via Android intents. Reported by Takeshi Terada on 2017-04-23
  - CVE-2017-5097: Out-of-bounds read in Skia. Reported by Anonymous on 2017-07-11
  - CVE-2017-5098: Use after free in V8. Reported by Jihoon Kim on 2017-07-11
  - CVE-2017-5099: Out-of-bounds write in PPAPI. Reported by Yuan Deng, Yu Zhou of Ant-financial Light-Year Security Lab on 2017-06-15
  - CVE-2017-5100: Use after free in Chrome Apps. Reported by Anonymous on 2017-05-04
  - CVE-2017-5101: URL spoofing in OmniBox. Reported by Luan Herrera on 2017-01-17
  - CVE-2017-5102: Uninitialized use in Skia. Reported by Anonymous on 2017-05-30
  - CVE-2017-5103: Uninitialized use in Skia. Reported by Anonymous on 2017-05-25
  - CVE-2017-5104: UI spoofing in browser. Reported by Khalil Zhani on 2017-06-02
  - CVE-2017-7000: Pointer disclosure in SQLite. Reported by Chaitin Security Research Lab (@ChaitinTech) working with Trend Micro's Zero Day Initiative
  - CVE-2017-5105: URL spoofing in OmniBox. Reported by Rayyan Bijoora on 2017-06-06
  - CVE-2017-5106: URL spoofing in OmniBox. Reported by Jack Zac on 2017-04-24
  - CVE-2017-5107: User information leak via SVG. Reported by David Kohlbrenner of UC San Diego on 2017-01-27
  - CVE-2017-5108: Type confusion in PDFium. Reported by Guang Gong of Alpha Team, Qihoo 360 on 2017-02-24
  - CVE-2017-5109: UI spoofing in browser. Reported by Jose Maria Acuna Morgado on 2017-04-11
  - CVE-2017-5110: UI spoofing in payments dialog. Reported by xisigr of Tencent's Xuanwu Lab on 2017-05-02

* Fri Jun 09 2017 Alexey Gladkov <legion@altlinux.ru> 59.0.3071.86-alt1
- New version (59.0.3071.86).
- Security fixes:
  - CVE-2017-5070: Type confusion in V8. Reported by Zhao Qixun(@S0rryMybad) of Qihoo 360 Vulcan Team on 2017-05-16
  - CVE-2017-5071: Out of bounds read in V8. Reported by Choongwoo Han on 2017-04-26
  - CVE-2017-5072: Address spoofing in Omnibox. Reported by Rayyan Bijoora on 2017-04-07
  - CVE-2017-5073: Use after free in print preview. Reported by Khalil Zhani on 2017-04-28
  - CVE-2017-5074: Use after free in Apps Bluetooth. Reported by anonymous on 2017-03-09
  - CVE-2017-5075: Information leak in CSP reporting. Reported by Emmanuel Gil Peyrot on 2017-01-05
  - CVE-2017-5086: Address spoofing in Omnibox. Reported by Rayyan Bijoora on 2017-05-16
  - CVE-2017-5076: Address spoofing in Omnibox. Reported by Samuel Erb on 2017-05-06
  - CVE-2017-5077: Heap buffer overflow in Skia. Reported by Sweetchip on 2017-04-28
  - CVE-2017-5078: Possible command injection in mailto handling. Reported by Jose Carlos Exposito Bueno on 2017-04-12
  - CVE-2017-5079: UI spoofing in Blink. Reported by Khalil Zhani on 2017-04-20
  - CVE-2017-5080: Use after free in credit card autofill. Reported by Khalil Zhani on 2017-04-05
  - CVE-2017-5081: Extension verification bypass. Reported by Andrey Kovalev (@L1kvID) Yandex Security Team on 2016-12-07
  - CVE-2017-5082: Insufficient hardening in credit card editor. Reported by Nightwatch Cybersecurity Research on 2017-05-11
  - CVE-2017-5083: UI spoofing in Blink. Reported by Khalil Zhani on 2017-04-24
  - CVE-2017-5085: Inappropriate javascript execution on WebUI pages. Reported by Zhiyang Zeng of Tencent security platform department on 2017-02-15

* Wed May 10 2017 Alexey Gladkov <legion@altlinux.ru> 58.0.3029.110-alt1
- New version (58.0.3029.110).

* Mon Mar 27 2017 Alexey Gladkov <legion@altlinux.ru> 57.0.2987.110-alt1
- New version (57.0.2987.110).
- Security fixes:
  - CVE-2017-5030: Memory corruption in V8. Credit to Brendon Tiszka
  - CVE-2017-5031: Use after free in ANGLE. Credit to Looben Yang
  - CVE-2017-5032: Out of bounds write in PDFium. Credit to Ashfaq Ansari - Project Srishti
  - CVE-2017-5029: Integer overflow in libxslt. Credit to Holger Fuhrmannek
  - CVE-2017-5034: Use after free in PDFium. Credit to Ke Liu of Tencent's Xuanwu LAB
  - CVE-2017-5035: Incorrect security UI in Omnibox. Credit to Enzo Aguado
  - CVE-2017-5036: Use after free in PDFium. Credit to Anonymous
  - CVE-2017-5037: Multiple out of bounds writes in ChunkDemuxer. Credit to Yongke Wang of Tencent's Xuanwu Lab (xlab.tencent.com)
  - CVE-2017-5039: Use after free in PDFium. Credit to jinmo123
  - CVE-2017-5040: Information disclosure in V8. Credit to Choongwoo Han
  - CVE-2017-5041: Address spoofing in Omnibox. Credit to Jordi Chancel
  - CVE-2017-5033: Bypass of Content Security Policy in Blink. Credit to Nicolai Grodum
  - CVE-2017-5042: Incorrect handling of cookies in Cast. Credit to Mike Ruddy
  - CVE-2017-5038: Use after free in GuestView. Credit to Anonymous
  - CVE-2017-5043: Use after free in GuestView. Credit to Anonymous
  - CVE-2017-5044: Heap overflow in Skia. Credit to Kushal Arvind Shah of Fortinet's FortiGuard Labs
  - CVE-2017-5045: Information disclosure in XSS Auditor. Credit to Dhaval Kapil (vampire)
  - CVE-2017-5046: Information disclosure in Blink. Credit to Masato Kinugawa

* Wed Feb 08 2017 Alexey Gladkov <legion@altlinux.ru> 56.0.2924.87-alt1
- New version (56.0.2924.87).
- Security fixes:
  - CVE-2017-5007: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2017-5006: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2017-5008: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2017-5010: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2017-5011: Unauthorised file access in Devtools. Credit to Khalil Zhani
  - CVE-2017-5009: Out of bounds memory access in WebRTC. Credit to Sean Stanek and Chip Bradford
  - CVE-2017-5012: Heap overflow in V8. Credit to Gergely Nagy (Tresorit)
  - CVE-2017-5013: Address spoofing in Omnibox. Credit to Haosheng Wang (@gnehsoah)
  - CVE-2017-5014: Heap overflow in Skia. Credit to sweetchip
  - CVE-2017-5015: Address spoofing in Omnibox. Credit to Armin Razmdjou
  - CVE-2017-5019: Use after free in Renderer. Credit to Wadih Matar
  - CVE-2017-5016: UI spoofing in Blink. Credit to Haosheng Wang (@gnehsoah)
  - CVE-2017-5017: Uninitialised memory access in webm video. Credit to Dan Berman
  - CVE-2017-5018: Universal XSS in chrome://apps. Credit to Rob Wu
  - CVE-2017-5020: Universal XSS in chrome://downloads. Credit to Rob Wu
  - CVE-2017-5021: Use after free in Extensions. Credit to Rob Wu
  - CVE-2017-5022: Bypass of Content Security Policy in Blink. Credit to  evi1m0#ly.com
  - CVE-2017-5023: Type confusion in metrics. Credit to the UK's National Cyber Security Centre (NCSC)
  - CVE-2017-5024: Heap overflow in FFmpeg. Credit to Paul Mehta
  - CVE-2017-5025: Heap overflow in FFmpeg. Credit to Paul Mehta
  - CVE-2017-5026: UI spoofing. Credit to Ronni Skansing
  - CVE-2017-5027: Bypass of Content Security Policy in Blink.

* Thu Dec 08 2016 Alexey Gladkov <legion@altlinux.ru> 55.0.2883.75-alt1
- New version (55.0.2883.75).
- Security fixes:
  - CVE-2016-9651: Private property access in V8. Credit to Guang Gong of Alpha Team Of Qihoo 360
  - CVE-2016-5208: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2016-5207: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2016-5206: Same-origin bypass in PDFium. Credit to Rob Wu (robwu.nl)
  - CVE-2016-5205: Universal XSS in Blink. Credit to Anonymous
  - CVE-2016-5204: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2016-5209: Out of bounds write in Blink. Credit to Giwan Go of STEALIEN
  - CVE-2016-5203: Use after free in PDFium. Credit to Anonymous
  - CVE-2016-5210: Out of bounds write in PDFium. Credit to Ke Liu of Tencent's Xuanwu LAB
  - CVE-2016-5212: Local file disclosure in DevTools. Credit to Khalil Zhani
  - CVE-2016-5211: Use after free in PDFium. Credit to Anonymous
  - CVE-2016-5213: Use after free in V8. Credit to Khalil Zhani
  - CVE-2016-5214: File download protection bypass. Credit to Jonathan Birch and MSVR
  - CVE-2016-5216: Use after free in PDFium. Credit to Anonymous
  - CVE-2016-5215: Use after free in Webaudio. Credit to Looben Yang
  - CVE-2016-5217: Use of unvalidated data in PDFium. Credit to Rob Wu (robwu.nl)
  - CVE-2016-5218: Address spoofing in Omnibox. Credit to Abdulrahman Alqabandi (@qab)
  - CVE-2016-5219: Use after free in V8. Credit to Rob Wu (robwu.nl)
  - CVE-2016-5221: Integer overflow in ANGLE. Credit to Tim Becker of ForAllSecure
  - CVE-2016-5220: Local file access in PDFium. Credit to Rob Wu (robwu.nl)
  - CVE-2016-5222: Address spoofing in Omnibox. Credit to xisigr of Tencent's Xuanwu Lab
  - CVE-2016-9650: CSP Referrer disclosure. Credit to Jakub Zoczek
  - CVE-2016-5223: Integer overflow in PDFium. Credit to Hwiwon Lee 
  - CVE-2016-5226: Limited XSS in Blink. Credit to Jun Kokatsu (@shhnjk)
  - CVE-2016-5225: CSP bypass in Blink. Credit to Scott Helme (@Scott_Helme, scotthelme.co.uk)
  - CVE-2016-5224: Same-origin bypass in SVG. Credit to Roeland Krak
  - CVE-2016-9652: Various fixes from internal audits, fuzzing and other initiatives

* Sun Oct 30 2016 Alexey Gladkov <legion@altlinux.ru> 54.0.2840.59-alt3
- Fix Requires.
- Add debuginfo.

* Tue Oct 25 2016 Alexey Gladkov <legion@altlinux.ru> 54.0.2840.59-alt2
- Rename chromium-stable to chromium.
- Enable VAAPI.

* Fri Oct 14 2016 Alexey Gladkov <legion@altlinux.ru> 54.0.2840.59-alt1
- New version (54.0.2840.59).
- Major spec-file changes.
- Many security fixes.

* Fri Mar 25 2016 Andrey Cherepanov <cas@altlinux.org> 49.0.2623.108-alt1
- New version
- Security fixes:
  - High CVE-2016-1647: Use-after-free in Navigation.
  - High CVE-2016-1648: Use-after-free in Extensions.
  - High CVE-2016-1649: Buffer overflow in libANGLE.

* Wed Mar 09 2016 Andrey Cherepanov <cas@altlinux.org> 49.0.2623.87-alt1
- New version
- Security fixes:
  - High CVE-2016-1643: Type confusion in Blink.
  - High CVE-2016-1644: Use-after-free in Blink.
  - High CVE-2016-1645: Out-of-bounds write in PDFium.

* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 49.0.2623.75-alt1
- New version
- Security fixes:
  - High CVE-2016-1630: Same-origin bypass in Blink.
  - High CVE-2016-1631: Same-origin bypass in Pepper Plugin.
  - High CVE-2016-1632: Bad cast in Extensions.
  - High CVE-2016-1633: Use-after-free in Blink.
  - High CVE-2016-1634: Use-after-free in Blink.
  - High CVE-2016-1635: Use-after-free in Blink.
  - High CVE-2016-1636: SRI Validation Bypass.
  - High CVE-2015-8126: Out-of-bounds access in libpng.
  - Medium CVE-2016-1637: Information Leak in Skia.
  - Medium CVE-2016-1638: WebAPI Bypass.
  - Medium CVE-2016-1639: Use-after-free in WebRTC.
  - Medium CVE-2016-1640: Origin confusion in Extensions UI.
  - Medium CVE-2016-1641: Use-after-free in Favicon.

* Fri Feb 19 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.116-alt1
- New version
- Security fixes:
  - Critical CVE-2016-1629: Same-origin bypass in Blink and Sandbox escape in Chrome.

* Wed Feb 17 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.109-alt2
- Require libv8-chromium-bin as separate package

* Mon Feb 15 2016 L.A. Kostis <lakostis@altlinux.ru> 48.0.2564.109-alt1.1
- Enabled WebRTC support on non-ARM platforms.
- Restored build of widevine (support of DRM-protected content playback).
- Added patches from Debian:
  + fix_building_widevinecdm_with_chromium.patch: If exterior-sourced 
    widevine library exists at run-time, use it.

* Wed Feb 10 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.109-alt1
- New version
- Security fixes:
  - High CVE-2016-1622: Same-origin bypass in Extensions.
  - High CVE-2016-1623: Same-origin bypass in DOM.
  - High CVE-2016-1624: Buffer overflow in Brotli.
  - Medium CVE-2016-1625: Navigation bypass in Chrome Instant.
  - Medium CVE-2016-1626: Out-of-bounds read in PDFium.

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.103-alt2
- Enable experimental VAAPI support (ALT #31772) (thanks L.A. Kostis
  for patch)

* Thu Feb 04 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.103-alt1
- New version

* Thu Jan 28 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.97-alt1
- New version

* Thu Jan 28 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.82-alt1
- New version
- Security fixes:
  - High CVE-2016-1613: Use-after-free in PDFium.
  - Medium CVE-2016-1614: Information leak in Blink.
  - Medium CVE-2016-1615: Origin confusion in Omnibox.
  - Medium CVE-2016-1616: URL Spoofing.
  - Medium CVE-2016-1617: History sniffing with HSTS and CSP.
  - Medium CVE-2016-1618: Weak random number generator in Blink.
  - Medium CVE-2016-1619: Out-of-bounds read in PDFium.

* Thu Jan 14 2016 Andrey Cherepanov <cas@altlinux.org> 47.0.2526.111-alt1
- New version

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 47.0.2526.106-alt1
- New version
- Security fix CVE-2015-6792: Fixes from internal audits and fuzzing
- Add missing requirements skipping by autoreq (ALT #31397)

* Wed Dec 09 2015 Andrey Cherepanov <cas@altlinux.org> 47.0.2526.80-alt1
- New version
- Security fixes:
  - High CVE-2015-6788: Type confusion in extensions.
  - High CVE-2015-6789: Use-after-free in Blink.
  - Medium CVE-2015-6790: Escaping issue in saved pages.

* Wed Dec 02 2015 Andrey Cherepanov <cas@altlinux.org> 47.0.2526.73-alt1
- New version
- Security fixes:
  - Critical CVE-2015-6765: Use-after-free in AppCache.
  - High CVE-2015-6766: Use-after-free in AppCache.
  - High CVE-2015-6767: Use-after-free in AppCache.
  - High CVE-2015-6768: Cross-origin bypass in DOM.
  - High CVE-2015-6769: Cross-origin bypass in core.
  - High CVE-2015-6770: Cross-origin bypass in DOM.
  - High CVE-2015-6771: Out of bounds access in v8.
  - High CVE-2015-6772: Cross-origin bypass in DOM.
  - High CVE-2015-6764: Out of bounds access in v8.
  - High CVE-2015-6773: Out of bounds access in Skia.
  - High CVE-2015-6774: Use-after-free in Extensions.
  - High CVE-2015-6775: Type confusion in PDFium.
  - High CVE-2015-6776: Out of bounds access in PDFium.
  - High CVE-2015-6777: Use-after-free in DOM.
  - Medium CVE-2015-6778: Out of bounds access in PDFium.
  - Medium CVE-2015-6779: Scheme bypass in PDFium.
  - Medium CVE-2015-6780: Use-after-free in Infobars.
  - Medium CVE-2015-6781: Integer overflow in Sfntly.
  - Medium CVE-2015-6782: Content spoofing in Omnibox.
  - Low CVE-2015-6784: Escaping issue in saved pages.
  - Low CVE-2015-6785: Wildcard matching issue in CSP.
  - Low CVE-2015-6786: Scheme bypass in CSP.
- Include libchromiumcontent (build disabled by default)

* Wed Nov 11 2015 Andrey Cherepanov <cas@altlinux.org> 46.0.2490.86-alt1
- New version
- Security fixes:
  - High CVE-2015-1302: Information leak in PDF viewer.

* Mon Nov 02 2015 Andrey Cherepanov <cas@altlinux.org> 46.0.2490.80-alt1
- New version

* Wed Oct 14 2015 Andrey Cherepanov <cas@altlinux.org> 46.0.2490.71-alt1
- New version
- Security fixes:
  - High CVE-2015-6755: Cross-origin bypass in Blink.
  - High CVE-2015-6756: Use-after-free in PDFium.
  - High CVE-2015-6757: Use-after-free in ServiceWorker.
  - High CVE-2015-6758: Bad-cast in PDFium.
  - Medium CVE-2015-6759: Information leakage in LocalStorage.
  - Medium CVE-2015-6760: Improper error handling in libANGLE.
  - Medium CVE-2015-6761: Memory corruption in FFMpeg.
  - Low CVE-2015-6762: CORS bypass via CSS fonts.

* Mon Sep 28 2015 Andrey Cherepanov <cas@altlinux.org> 45.0.2454.101-alt1
- New version
- Security fixes:
  - High CVE-2015-1303: Cross-origin bypass in DOM.
  - High CVE-2015-1304: Cross-origin bypass in V8.

* Wed Sep 23 2015 Andrey Cherepanov <cas@altlinux.org> 45.0.2454.99-alt1
- New version
- Strip binaries before install

* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 45.0.2454.93-alt1
- New version

* Wed Sep 02 2015 Andrey Cherepanov <cas@altlinux.org> 45.0.2454.85-alt1
- New version
- Security fixes:
  - High CVE-2015-1291: Cross-origin bypass in DOM.
  - High CVE-2015-1292: Cross-origin bypass in ServiceWorker.
  - High CVE-2015-1293: Cross-origin bypass in DOM.
  - High CVE-2015-1294: Use-after-free in Skia.
  - High CVE-2015-1295: Use-after-free in Printing.
  - High CVE-2015-1296: Character spoofing in omnibox.
  - Medium CVE-2015-1297: Permission scoping error in WebRequest.
  - Medium CVE-2015-1298: URL validation error in extensions.
  - Medium CVE-2015-1299: Use-after-free in Blink.
  - Medium CVE-2015-1300: Information leak in Blink.

* Wed Aug 26 2015 Andrey Cherepanov <cas@altlinux.org> 44.0.2403.157-alt1
- New version

* Wed Jul 15 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.134-alt1
- New version
- Critical update to Adobe Flash Player (18.0.0.209) and a fix for a
  full screen casting issue

* Wed Jul 08 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.132-alt1
- New version

* Mon Jun 29 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.130-alt1
- New version
- Security fixes:
  - High CVE-2015-1266: Scheme validation error in WebUI.
  - High CVE-2015-1268: Cross-origin bypass in Blink.
  - Medium CVE-2015-1267: Cross-origin bypass in Blink.
  - Medium CVE-2015-1269: Normalization error in HSTS/HPKP preload list.
- use more external shared libraries (especially libv8)

* Mon Jun 15 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.125-alt1
- New version
- Fixes:
  - Resolved browser font magnification/scaling issue
- Cannot package missing libpdf.so
- Add clearkeycdm component
- Disable build on i586 (because memory exhausted while linking)
- Disable automatic external extensions loading (see https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=786909)
  Also you can use --show-component-extension-options command line parameter
  to view all hidden extensions

* Thu Jun 04 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.81-alt1
- New version
- Fixes:
  - [490611] Fixed an issue where sometimes a blank page would print.
  - [478714] Icons not displaying properly on Linux.

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.65-alt1
- New version
- Security fixes:
  - High CVE-2015-1252: Sandbox escape in Chrome.
  - High CVE-2015-1253: Cross-origin bypass in DOM.
  - High CVE-2015-1254: Cross-origin bypass in Editing.
  - High CVE-2015-1255: Use-after-free in WebAudio.
  - High CVE-2015-1256: Use-after-free in SVG.
  - High CVE-2015-1251: Use-after-free in Speech.
  - Medium CVE-2015-1257: Container-overflow in SVG.
  - Medium CVE-2015-1258: Negative-size parameter in Libvpx.
  - Medium CVE-2015-1259: Uninitialized value in PDFium.
  - Medium CVE-2015-1260: Use-after-free in WebRTC.
  - Medium CVE-2015-1261: URL bar spoofing.
  - Medium CVE-2015-1262: Uninitialized value in Blink.
  - Low CVE-2015-1263: Insecure download of spellcheck dictionary.
  - Low CVE-2015-1264: Cross-site scripting in bookmarks.

* Tue May 19 2015 Andrey Cherepanov <cas@altlinux.org> 42.0.2311.152-alt1
- New version

* Wed Apr 29 2015 Andrey Cherepanov <cas@altlinux.org> 42.0.2311.135-alt1
- New version
- Security fixes:
  - High CVE-2015-1243: Use-after-free in DOM.

* Wed Apr 15 2015 Andrey Cherepanov <cas@altlinux.org> 42.0.2311.90-alt1
- New version
- Security fixes:
  - High CVE-2015-1235: Cross-origin-bypass in HTML parser.
  - Medium CVE-2015-1236: Cross-origin-bypass in Blink.
  - High CVE-2015-1237: Use-after-free in IPC.
  - High CVE-2015-1238: Out-of-bounds write in Skia.
  - Medium CVE-2015-1240: Out-of-bounds read in WebGL.
  - Medium CVE-2015-1241: Tap-Jacking.
  - High CVE-2015-1242: Type confusion in V8.
  - Medium CVE-2015-1244: HSTS bypass in WebSockets.
  - Medium CVE-2015-1245: Use-after-free in PDFium.
  - Medium CVE-2015-1246: Out-of-bounds read in Blink.
  - Medium CVE-2015-1247: Scheme issues in OpenSearch.
  - Medium CVE-2015-1248: SafeBrowsing bypass.


* Thu Apr 02 2015 Andrey Cherepanov <cas@altlinux.org> 41.0.2272.118-alt1
- New version
- Security fixes:
  - Critical CVE-2015-1233: A special thanks to Anonymous for a
    combination of V8, Gamepad and IPC bugs that can lead to remote
    code execution outside of the sandbox.
  - High CVE-2015-1234: Buffer overflow via race condition in GPU.

* Fri Mar 20 2015 Andrey Cherepanov <cas@altlinux.org> 41.0.2272.101-alt1
- New version
- Package all *.bin files

* Tue Mar 17 2015 Andrey Cherepanov <cas@altlinux.org> 41.0.2272.89-alt1
- New version

* Wed Mar 04 2015 Andrey Cherepanov <cas@altlinux.org> 41.0.2272.76-alt1
- New version
- Security fixes:
  - High CVE-2015-1212: Out-of-bounds write in media.
  - High CVE-2015-1213: Out-of-bounds write in skia filters.
  - High CVE-2015-1214: Out-of-bounds write in skia filters.
  - High CVE-2015-1215: Out-of-bounds write in skia filters.
  - High CVE-2015-1216: Use-after-free in v8 bindings.
  - High CVE-2015-1217: Type confusion in v8 bindings.
  - High CVE-2015-1218: Use-after-free in dom.
  - High CVE-2015-1219: Integer overflow in webgl.
  - High CVE-2015-1220: Use-after-free in gif decoder.
  - High CVE-2015-1221: Use-after-free in web databases.
  - High CVE-2015-1222: Use-after-free in service workers.
  - High CVE-2015-1223: Use-after-free in dom.
  - High CVE-2015-1230: Type confusion in v8.
  - Medium CVE-2015-1224: Out-of-bounds read in vpxdecoder.
  - Medium CVE-2015-1225: Out-of-bounds read in pdfium.
  - Medium CVE-2015-1226: Validation issue in debugger.
  - Medium CVE-2015-1227: Uninitialized value in blink.
  - Medium CVE-2015-1228: Uninitialized value in rendering.
  - Medium CVE-2015-1229: Cookie injection via proxies.

* Fri Feb 20 2015 Andrey Cherepanov <cas@altlinux.org> 40.0.2214.115-alt1
- New version

* Fri Feb 06 2015 Andrey Cherepanov <cas@altlinux.org> 40.0.2214.111-alt1
- New version
- Security fixes:
  - High CVE-2015-1211: Privilege escalation using service workers.

* Tue Jan 27 2015 Andrey Cherepanov <cas@altlinux.org> 40.0.2214.93-alt1
- New version

* Fri Jan 23 2015 Andrey Cherepanov <cas@altlinux.org> 40.0.2214.91-alt1
- New version
- Security fixes:
  - High CVE-2014-7923: Memory corruption in ICU.
  - High CVE-2014-7924: Use-after-free in IndexedDB.
  - High CVE-2014-7925: Use-after-free in WebAudio.
  - High CVE-2014-7926: Memory corruption in ICU.
  - High CVE-2014-7927: Memory corruption in V8.
  - High CVE-2014-7928: Memory corruption in V8.
  - High CVE-2014-7930: Use-after-free in DOM.
  - High CVE-2014-7931: Memory corruption in V8.
  - High CVE-2014-7929: Use-after-free in DOM.
  - High CVE-2014-7932: Use-after-free in DOM.
  - High CVE-2014-7933: Use-after-free in FFmpeg.
  - High CVE-2014-7934: Use-after-free in DOM.
  - High CVE-2014-7935: Use-after-free in Speech.
  - High CVE-2014-7936: Use-after-free in Views.
  - High CVE-2014-7937: Use-after-free in FFmpeg.
  - High CVE-2014-7938: Memory corruption in Fonts.
  - High CVE-2014-7939: Same-origin-bypass in V8.
  - Medium CVE-2014-7940: Uninitialized-value in ICU.
  - Medium CVE-2014-7941: Out-of-bounds read in UI.
  - Medium CVE-2014-7942: Uninitialized-value in Fonts.
  - Medium CVE-2014-7943: Out-of-bounds read in Skia.
  - Medium CVE-2014-7944: Out-of-bounds read in PDFium.
  - Medium CVE-2014-7945: Out-of-bounds read in PDFium.
  - Medium CVE-2014-7946: Out-of-bounds read in Fonts.
  - Medium CVE-2014-7947: Out-of-bounds read in PDFium.
  - Medium CVE-2014-7948: Caching error in AppCache.

* Wed Jan 14 2015 Andrey Cherepanov <cas@altlinux.org> 39.0.2171.99-alt1
- New version

* Wed Dec 10 2014 Andrey Cherepanov <cas@altlinux.org> 39.0.2171.95-alt1
- New version

* Tue Dec 09 2014 Andrey Cherepanov <cas@altlinux.org> 39.0.2171.71-alt1
- New version

* Fri Nov 21 2014 Andrey Cherepanov <cas@altlinux.org> 39.0.2171.65-alt1
- New version
- Security fixes:
  - High CVE-2014-7899: Address bar spoofing.
  - High CVE-2014-7900: Use-after-free in pdfium.
  - High CVE-2014-7901: Integer overflow in pdfium.
  - High CVE-2014-7902: Use-after-free in pdfium.
  - High CVE-2014-7903: Buffer overflow in pdfium.
  - High CVE-2014-7904: Buffer overflow in Skia.
  - High CVE-2014-7905: Flaw allowing navigation to intents that do not
    have the BROWSABLE category.
  - High CVE-2014-7906: Use-after-free in pepper plugins.
  - High CVE-2014-0574: Double-free in Flash.
  - High CVE-2014-7907: Use-after-free in blink.
  - High CVE-2014-7908: Integer overflow in media.
  - Medium CVE-2014-7909: Uninitialized memory read in Skia.
- Mark all files in /etc/chromium as config
- Strip Chromium executables to disable debuginfo generation (became too
  huge)

* Wed Nov 12 2014 Andrey Cherepanov <cas@altlinux.org> 38.0.2125.122-alt1
- New version

* Thu Nov 06 2014 Andrey Cherepanov <cas@altlinux.org> 38.0.2125.111-alt1
- New version
- Use sed insted of strings utility from binutils for detect PepperFlash
  plugin version
- Remove second tab in master preferences
- Replace default config

* Thu Oct 09 2014 Andrey Cherepanov <cas@altlinux.org> 38.0.2125.101-alt1
- New version
- Security fixes:
  - Critical CVE-2014-3188: A special thanks to Juri Aedla for a
    combination of V8 and IPC bugs that can lead to remote code
    execution outside of the sandbox.
  - High CVE-2014-3189: Out-of-bounds read in PDFium.
  - High CVE-2014-3190: Use-after-free in Events.
  - High CVE-2014-3191: Use-after-free in Rendering.
  - High CVE-2014-3192: Use-after-free in DOM.
  - High CVE-2014-3193: Type confusion in Session Management.
  - High CVE-2014-3194: Use-after-free in Web Workers.
  - Medium CVE-2014-3195: Information Leak in V8.
  - Medium CVE-2014-3197: Information Leak in XSS Auditor.
  - Medium CVE-2014-3198: Out-of-bounds read in PDFium.
  - Low CVE-2014-3199: Release Assert in V8 bindings.
- Replace chromium-support-ModeSwitch-key.patch by upstream version from
  commit 8585724

* Fri Sep 26 2014 Andrey Cherepanov <cas@altlinux.org> 37.0.2062.124-alt2
- New version
- Security fixes:
  - CVE-2014-1568: RSA signature malleability in NSS
- Fix path and version detection of PepperFlash

* Tue Sep 23 2014 Andrey Cherepanov <cas@altlinux.org> 37.0.2062.120-alt2
- Fix RightAlt behaviour. See https://code.google.com/p/chromium/issues/detail?id=377203
  for details
- Build PDF viewer plugin

* Thu Sep 18 2014 Andrey Cherepanov <cas@altlinux.org> 37.0.2062.120-alt1
- New version
- Security fixes:
  - High CVE-2014-3178: Use-after-free in rendering.
- Disable bundled binutils and gold

* Wed Aug 27 2014 Andrey Cherepanov <cas@altlinux.org> 37.0.2062.94-alt1
- New version
- Security fixes:
  - Critical CVE-2014-3176, CVE-2014-3177: A special reward to
    lokihardt@asrt for a combination of bugs in V8, IPC, sync, and
    extensions that can lead to remote code execution outside of the
    sandbox.
  - High CVE-2014-3168: Use-after-free in SVG.
  - High CVE-2014-3169: Use-after-free in DOM.
  - High CVE-2014-3170: Extension permission dialog spoofing.
  - High CVE-2014-3171: Use-after-free in bindings.
  - Medium CVE-2014-3172: Issue related to extension debugging.
  - Medium CVE-2014-3173: Uninitialized memory read in WebGL.
  - Medium CVE-2014-3174: Uninitialized memory read in Web Audio.

* Mon Aug 18 2014 Andrey Cherepanov <cas@altlinux.org> 36.0.1985.143-alt1
- New version
- Security fixes:
  - High CVE-2014-3165: Use-after-free in web sockets.
  - High CVE-2014-3166: Information disclosure in SPDY.

* Fri Jul 25 2014 Andrey Cherepanov <cas@altlinux.org> 36.0.1985.125-alt2
- Fix small user interface fonts (see https://code.google.com/p/chromium/issues/detail?id=375824)

* Thu Jul 17 2014 Andrey Cherepanov <cas@altlinux.org> 36.0.1985.125-alt1
- New version
- Security fixes:
  - Medium CVE-2014-3160: Same-Origin-Policy bypass in SVG.
- Fix wrong Russian translation (ALT #30182)
- Add flags to avoid memory exhaustion while linking on i586
- Use internal version of v8 library

* Mon Jul 14 2014 Andrey Cherepanov <cas@altlinux.org> 35.0.1916.153-alt1
- New version
- Security fixes:
  - High CVE-2014-3154: Use-after-free in filesystem api.
  - High CVE-2014-3155: Out-of-bounds read in SPDY.
  - Medium CVE-2014-3156: Buffer overflow in clipboard.
  - CVE-2014-3157: Heap overflow in media.

* Wed May 21 2014 Andrey Cherepanov <cas@altlinux.org> 35.0.1916.114-alt1
- New version
- Security fixes:
  - High CVE-2014-1743: Use-after-free in styles.
  - High CVE-2014-1744: Integer overflow in audio.
  - High CVE-2014-1745: Use-after-free in SVG.
  - Medium CVE-2014-1746: Out-of-bounds read in media filters.
  - Medium CVE-2014-1747: UXSS with local MHTML file.
  - Medium CVE-2014-1748: UI spoofing with scrollbar.

* Wed May 14 2014 Andrey Cherepanov <cas@altlinux.org> 34.0.1847.137-alt1
- New version
- Security fixes:
  - High CVE-2014-1740: Use-after-free in WebSockets.
  - High CVE-2014-1741: Integer overflow in DOM ranges.
  - High CVE-2014-1742: Use-after-free in editing.

* Fri May 02 2014 Andrey Cherepanov <cas@altlinux.org> 34.0.1847.132-alt2
- Add support for playing mp3 and mpeg4 (ALT #27863)
- Package icudtl.dat

* Wed Apr 30 2014 Andrey Cherepanov <cas@altlinux.org> 34.0.1847.132-alt1
- New version
- Security fixes:
  - High CVE-2014-1731: Type confusion in DOM.
  - Medium CVE-2014-1732: Use-after-free in Speech Recognition.
  - Medium CVE-2014-1733: Compiler bug in Seccomp-BPF.

* Tue Apr 15 2014 Andrey Cherepanov <cas@altlinux.org> 34.0.1847.116-alt1
- New version
- Security fixes:
  - High CVE-2014-1718: Integer overflow in compositor.
  - High CVE-2014-1719: Use-after-free in web workers.
  - High CVE-2014-1720: Use-after-free in DOM.
  - High CVE-2014-1722: Use-after-free in rendering.
  - High CVE-2014-1723: Url confusion with RTL characters.
  - High CVE-2014-1724: Use-after-free in speech.
  - Medium CVE-2014-1725: OOB read with window property.
  - Medium CVE-2014-1726: Local cross-origin bypass.
  - Medium CVE-2014-1727: Use-after-free in forms.
- Package depot-tools to correct build
- Do not show apps shortcut button on bookmark bar by default
- Switch build from make to ninja-build

* Tue Mar 18 2014 Andrey Cherepanov <cas@altlinux.org> 33.0.1750.152-alt1
- New version
- Security fixes:
  - High CVE-2014-1713: Use-after-free in Blink bindings
  - High CVE-2014-1705: Memory corruption in V8
  - High CVE-2014-1715: Directory traversal issue

* Wed Mar 12 2014 Andrey Cherepanov <cas@altlinux.org> 33.0.1750.149-alt1
- New version
- Security fixes:
  - High CVE-2014-1700: Use-after-free in speech.
  - High CVE-2014-1701: UXSS in events.
  - High CVE-2014-1702: Use-after-free in web database.

* Tue Mar 04 2014 Andrey Cherepanov <cas@altlinux.org> 33.0.1750.146-alt1
- New version
- Security fixes:
  - High CVE-2013-6663: Use-after-free in svg images.
  - High CVE-2013-6664: Use-after-free in speech recognition.
  - High CVE-2013-6665: Heap buffer overflow in software rendering.
  - Medium CVE-2013-6666: Chrome allows requests in flash header request.

* Fri Feb 21 2014 Andrey Cherepanov <cas@altlinux.org> 33.0.1750.117-alt1
- New version
- Security fixes:
  - High CVE-2013-6653: Use-after-free related to web contents.
  - High CVE-2013-6654: Bad cast in SVG.
  - High CVE-2013-6655: Use-after-free in layout.
  - High CVE-2013-6656: Information leak in XSS auditor.
  - Medium CVE-2013-6657: Information leak in XSS auditor.
  - Medium CVE-2013-6658: Use-after-free in layout.
  - Medium CVE-2013-6659: Issue with certificates validation in TLS handshake.
  - Low CVE-2013-6660: Information leak in drag and drop.
- Update patches from SUSE, Debian and Arch

* Tue Jan 28 2014 Andrey Cherepanov <cas@altlinux.org> 32.0.1700.102-alt1
- New version
- Security fixes:
  - High CVE-2013-6649: Use-after-free in SVG images.
- Fixes:
  - Mouse Pointer disappears after exiting full-screen mode. (317496)
  - Drag and drop files into Chrome may not work properly. (332579)
  - Quicktime Plugin crashes in Chrome. (308466)
  - Chrome becomes unresponsive. (335248)
  - Trackpad users may not be able to scroll horizontally. (332797)
  - Scrolling does not work in combo box. (334454)
  - Chrome does not work with all CSS minifiers such as whitespace
    around a media query's `and` keyword. (333035)

* Tue Jan 21 2014 Andrey Cherepanov <cas@altlinux.org> 32.0.1700.77-alt1
- New version
- Security fixes:
  - High CVE-2013-6646: Use-after-free in web workers.
  - High CVE-2013-6641: Use-after-free related to forms.
  - High CVE-2013-6643: Unprompted sync with an attacker's Google account.
  - Medium CVE-2013-6645 Use-after-free related to speech input elements.
- Set interpreter /bin/bash for main executable for correct ulimit call

* Thu Dec 05 2013 Andrey Cherepanov <cas@altlinux.org> 31.0.1650.63-alt1
- New version
- Security fixes:
  - Medium CVE-2013-6634: Session fixation in sync related to 302 redirects.
  - High CVE-2013-6635: Use-after-free in editing.
  - Medium CVE-2013-6636: Address bar spoofing related to modal dialogs.
- Increase default nproc limit from 1024 to 1536
- Remove SVN commit from release number

* Fri Nov 15 2013 Andrey Cherepanov <cas@altlinux.org> 31.0.1650.57-alt1.r235101
- New version
- Security fixes:
  - Critical CVE-2013-6632: Multiple memory corruption issues

* Wed Nov 13 2013 Andrey Cherepanov <cas@altlinux.org> 31.0.1650.48-alt1.r233213
- New version
- Security fixes:
  - Medium CVE-2013-6621: Use after free related to speech input elements.
  - High CVE-2013-6622: Use after free related to media elements.
  - High CVE-2013-6623: Out of bounds read in SVG.
  - High CVE-2013-6624: Use after free related to "id" attribute strings.
  - High CVE-2013-6625: Use after free in DOM ranges.
  - Low CVE-2013-6626: Address bar spoofing related to interstitial warnings.
  - High CVE-2013-6627: Out of bounds read in HTTP parsing.
  - Medium CVE-2013-6628: Issue with certificates not being checked during TLS renegotiation.

* Fri Oct 25 2013 Andrey Cherepanov <cas@altlinux.org> 30.0.1599.114-alt1.r229842
- New version
- Move chrome_sandbox to %%_libdir/chromium/chrome-sandbox

* Fri Oct 11 2013 Andrey Cherepanov <cas@altlinux.org> 30.0.1599.66-alt1.r225456
- New version
- Security fixes:
  - Medium CVE-2013-2906: Races in Web Audio.
  - Medium CVE-2013-2907: Out of bounds read in Window.prototype object.
  - Medium CVE-2013-2908: Address bar spoofing related to the "204 No Content" status code.
  - High CVE-2013-2909: Use after free in inline-block rendering.
  - Medium CVE-2013-2910: Use-after-free in Web Audio.
  - High CVE-2013-2911: Use-after-free in XSLT.
  - High CVE-2013-2912: Use-after-free in PPAPI.
  - High CVE-2013-2913: Use-after-free in XML document parsing.
  - Low CVE-2013-2915: Address bar spoofing via a malformed scheme.
  - High CVE-2013-2916: Address bar spoofing related to the "204 No Content" status code.
  - Medium CVE-2013-2917: Out of bounds read in Web Audio.
  - High CVE-2013-2918: Use-after-free in DOM.
  - High CVE-2013-2919: Memory corruption in V8.
  - Medium CVE-2013-2920: Out of bounds read in URL parsing.
  - High CVE-2013-2921: Use-after-free in resource loader.
  - High CVE-2013-2922: Use-after-free in template element.
  - CVE-2013-2923: Various fixes from internal audits, fuzzing and other initiatives.

* Wed Sep 25 2013 Andrey Cherepanov <cas@altlinux.org> 29.0.1547.76-alt2.r223446
- New version 29.0.1547.76

* Tue Sep 03 2013 Andrey Cherepanov <cas@altlinux.org> 29.0.1547.65-alt1.r220622
- New version 29.0.1547.62
- Security fixes:
  - High CVE-2013-2900: Incomplete path sanitization in file handling.
  - Low CVE-2013-2905: Information leak via overly broad permissions on
    shared memory files.
  - High CVE-2013-2901: Integer overflow in ANGLE.
  - High CVE-2013-2902: Use after free in XSLT.
  - High CVE-2013-2903: Use after free in media element.
  - High CVE-2013-2904: Use after free in document parsing.
- Improved Omnibox suggestions based on the recency of sites you have
  visited
- Ability to reset your profile back to its original state
- Many new apps and extensions APIs
- Lots of stability and performance improvements
- Fix an issue with printing from Google Docs applications
- Fix an issue with Sync

* Wed Jul 31 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 28.0.1500.95-alt2.r213514
- rebuild with versioned v8

* Wed Jul 31 2013 Andrey Cherepanov <cas@altlinux.org> 28.0.1500.95-alt1.r213514
- New version 28.0.1500.95
- Security fixes:
  - Medium CVE-2013-2881: Origin bypass in frame handling.
  - High CVE-2013-2883: Use-after-free in MutationObserver.
  - High CVE-2013-2884: Use-after-free in DOM.
  - High CVE-2013-2885: Use-after-free in input handling.

* Wed Jul 24 2013 Andrey Cherepanov <cas@altlinux.org> 28.0.1500.71-alt1.r209842
- New version 28.0.1500.71
- Security fixes:
  - High CVE-2013-2879: Confusion setting up sign-in and sync.
  - Medium CVE-2013-2868: Incorrect sync of NPAPI extension component.
  - Medium CVE-2013-2869: Out-of-bounds read in JPEG2000 handling.
  - Critical CVE-2013-2870: Use-after-free with network sockets.
  - Medium CVE-2013-2853: Man-in-the-middle attack against HTTP in SSL.
  - High CVE-2013-2871: Use-after-free in input handling.
  - High CVE-2013-2873: Use-after-free in resource loading.
  - Medium CVE-2013-2875: Out-of-bounds-read in SVG.
  - Medium CVE-2013-2876: Extensions permissions confusion with interstitials.
  - Low CVE-2013-2877: Out-of-bounds read in XML parsing.
  - None: Remove the "viewsource" attribute on iframes.
  - Medium CVE-2013-2878: Out-of-bounds read in text handling.
  - High CVE-2013-2880: Various fixes from internal audits, fuzzing and other initiatives

* Wed Jun 05 2013 Andrey Cherepanov <cas@altlinux.org> 27.0.1453.110-alt1.r202711
- New version 27.0.1453.110
- Security fixes:
  - Critical CVE-2013-2863: Memory corruption in SSL socket handling.
  - High CVE-2013-2856: Use-after-free in input handling.
  - High CVE-2013-2857: Use-after-free in image handling.
  - High CVE-2013-2858: Use-after-free in HTML5 Audio.
  - High CVE-2013-2859: Cross-origin namespace pollution.
  - High CVE-2013-2860: Use-after-free with workers accessing database APIs.
  - High CVE-2013-2861: Use-after-free with SVG.
  - High CVE-2013-2862: Memory corruption in Skia GPU handling.
  - High CVE-2013-2864: Bad free in PDF viewer.
  - High CVE-2013-2865: Various fixes from internal audits, fuzzing and other initiatives. 
  - Medium CVE-2013-2855: Memory corruption in dev tools API.

* Thu May 30 2013 Andrey Cherepanov <cas@altlinux.org> 27.0.1453.93-alt1.r200836
- New version 27.0.1453.93
- Security fixes:
  - High CVE-2013-2836: Various fixes from internal audits, fuzzing and
    other initiatives.
  - High CVE-2013-2837: Use-after-free in SVG.
  - High CVE-2013-2839: Bad cast in clipboard handling.
  - High CVE-2013-2840: Use-after-free in media loader.
  - High CVE-2013-2841: Use-after-free in Pepper resource handling.
  - High CVE-2013-2842: Use-after-free in widget handling.
  - High CVE-2013-2843: Use-after-free in speech handling.
  - High CVE-2013-2844: Use-after-free in style resolution.
  - High CVE-2013-2845: Memory safety issues in Web Audio.
  - High CVE-2013-2846: Use-after-free in media loader.
  - High CVE-2013-2847: Use-after-free race condition with workers.
  - Medium CVE-2013-2848: Possible data extraction with XSS Auditor.
  - Low CVE-2013-2849: Possible XSS with drag+drop or copy+paste.
- Web pages load 5%% faster on average
- New chrome.syncFileSystem API
- Improved ranking of predictions, improved spell correction, and
  numerous fundamental improvements for Omnibox predictions. Please see
  the Help Center for more information on our updated policies.

* Mon May 13 2013 Andrey Cherepanov <cas@altlinux.org> 26.0.1410.57-alt1.r191765
- New version 26.0.1410.57
- Security fixes:
  - High CVE-2013-0927: Unsafe config option loading in Pango.
- Requires new version speech-dispatcher

* Sun Mar 31 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt4.r187217
- Rebuild with libv8-3.15

* Wed Mar 27 2013 Andrey Cherepanov <cas@altlinux.org> 26.0.1410.43-alt1.r189671
- New version 26.0.1410.43
- Security fixes:
  - Medium CVE-2013-0926: Avoid pasting active tags in certain situations.
  - Low CVE-2013-0925: Avoid leaking URLs to extensions without the tabs permissions.
  - Low CVE-2013-0924: Check an extension's permissions API usage again file permissions.
  - Medium CVE-2013-0923: Memory safety issues in the USB Apps API.
  - Low CVE-2013-0922: Avoid HTTP basic auth brute force attempts.
  - High CVE-2013-0921: Ensure isolated web sites run in their own processes.
  - Medium CVE-2013-0920: Use-after-free in extension bookmarks API.
  - Medium CVE-2013-0919: Use-after-free with pop-up windows in extensions.
  - Low CVE-2013-0918: Do not navigate dev tools upon drag and drop.
  - Low CVE-2013-0917: Out-of-bounds read in URL loader.
  - High CVE-2013-0916: Use-after-free in Web Audio.

* Thu Mar 21 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt3.r187217
- Add note that the keys for Google API are only to be used for ALT Linux
- Fix run script if CHROMIUM_ULIMIT is not set in /etc/chromium/default

* Wed Mar 20 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt2.r187217
- Build with access to Google API

* Wed Mar 13 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt1.r187217
- New version 25.0.1364.172

* Mon Mar 11 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.160-alt1.r186726
- New version 25.0.1364.160
- Security fixes:
  - CVE-2013-0912: Type confusion in WebKit.
- Build with system libpng12 (old version)

* Wed Mar 06 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.152-alt1.r185281
- New version 25.0.1364.152
- Security fixes:
  - High CVE-2013-0902: Use-after-free in frame loader.
  - High CVE-2013-0903: Use-after-free in browser navigation handling.
  - High CVE-2013-0904: Memory corruption in Web Audio.
  - High CVE-2013-0905: Use-after-free with SVG animations.
  - High CVE-2013-0906: Memory corruption in Indexed DB.
  - Medium CVE-2013-0907: Race condition in media thread handling.
  - Medium CVE-2013-0908: Incorrect handling of bindings for extension processes.
  - Low CVE-2013-0909: Referer leakage with XSS Auditor.
  - Medium CVE-2013-0910: Mediate renderer -> browser plug-in loads more strictly.
  - High CVE-2013-0911: Possible path traversal in database handling.
- Use builtin libpng

* Fri Feb 22 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.97-alt1.r183676
- New version 25.0.1364.97
- Security fixes:
  - High CVE-2013-0879: Memory corruption with web audio node.
  - High CVE-2013-0880: Use-after-free in database handling.
  - Medium CVE-2013-0881: Bad read in Matroska handling.
  - High CVE-2013-0882: Bad memory access with excessive SVG parameters.
  - Medium CVE-2013-0883: Bad read in Skia.
  - Low CVE-2013-0884: Inappropriate load of NaCl.
  - Medium CVE-2013-0885: Too many API permissions granted to web store.
  - Low CVE-2013-0887: Developer tools process has too many permissions
    and places too much trust in the connected server.
  - Medium CVE-2013-0888: Out-of-bounds read in Skia.
  - Low CVE-2013-0889: Tighten user gesture check for dangerous file
    downloads.
  - High CVE-2013-0890: Memory safety issues across the IPC layer.
  - High CVE-2013-0891: Integer overflow in blob handling.
  - Medium CVE-2013-0892: Lower severity issues across the IPC layer.
  - Medium CVE-2013-0893: Race condition in media handling.
  - High CVE-2013-0894: Buffer overflow in vorbis decoding.
  - High CVE-2013-0895: Incorrect path handling in file copying.
  - High CVE-2013-0896: Memory management issues in plug-in message
    handling.
  - Low CVE-2013-0897: Off-by-one read in PDF.
  - High CVE-2013-0898: Use-after-free in URL handling.
  - Low CVE-2013-0899: Integer overflow in Opus handling.
  - Medium CVE-2013-0900: Race condition in ICU.

* Thu Jan 31 2013 Andrey Cherepanov <cas@altlinux.org> 24.0.1312.57-alt1.r178923
- New version 24.0.1312.57
- Remove revision number from tarball name

* Wed Jan 23 2013 Andrey Cherepanov <cas@altlinux.org> 24.0.1312.56-alt1.r177594
- New version 24.0.1312.56
- Security fixes:
  - High CVE-2013-0839: Use-after-free in canvas font handling.
  - Medium CVE-2013-0840: Missing URL validation when opening new windows.
  - High CVE-2013-0841: Unchecked array index in content blocking.
  - Medium CVE-2013-0842: Problems with NULL characters embedded in paths.

* Mon Jan 14 2013 Andrey Cherepanov <cas@altlinux.org> 24.0.1312.52-alt1.r175374
- New version 24.0.1312.52
- Security fixes:
  - High CVE-2012-5145: Use-after-free in SVG layout.
  - High CVE-2012-5146: Same origin policy bypass with malformed URL.
  - High CVE-2012-5147: Use-after-free in DOM handling.
  - Medium CVE-2012-5148: Missing filename sanitization in hyphenation support.
  - High CVE-2012-5149: Integer overflow in audio IPC handling.
  - High CVE-2012-5150: Use-after-free when seeking video.
  - High CVE-2012-5151: Integer overflow in PDF JavaScript.
  - Medium CVE-2012-5152: Out-of-bounds read when seeking video.
  - High CVE-2012-5156: Use-after-free in PDF fields.
  - Medium CVE-2012-5157: Out-of-bounds reads in PDF image handling.
  - High CVE-2013-0828: Bad cast in PDF root handling.
  - High CVE-2013-0829: Corruption of database metadata leading to incorrect file access.
  - Low CVE-2013-0831: Possible path traversal from extension process.
  - Medium CVE-2013-0832: Use-after-free with printing.
  - Medium CVE-2013-0833: Out-of-bounds read with printing.
  - Medium CVE-2013-0834: Out-of-bounds read with glyph handling.
  - Low CVE-2013-0835: Browser crash with geolocation.
  - Medium CVE-2013-0837: Crash in extension tab handling.
  - Low CVE-2013-0838: Tighten permissions on shared memory segments.
- Fixes:
  - Add new option CHROMIUM_ULIMIT in /etc/chromium/default for increase
    for example maximum number of open file descriptors ("-n 1024"
    is recommended for many opened tabs) if needed.

* Wed Dec 12 2012 Andrey Cherepanov <cas@altlinux.org> 23.0.1271.97-alt1.r171054
- New version 23.0.1271.97
- Security fixes:
  - High CVE-2012-5139: Use-after-free with visibility events.
  - High CVE-2012-5140: Use-after-free in URL loader.
  - Medium CVE-2012-5141: Limit Chromoting client plug-in instantiation.
  - Critical CVE-2012-5142: Crash in history navigation.
  - Medium CVE-2012-5143: Integer overflow in PPAPI image buffers.
  - High CVE-2012-5144: Stack corruption in AAC decoding.
- Fixes:
  - Some texts in a Website Settings popup are trimmed
  - <input> selection renders white text on white bg in apps
  - some plugins stopped working

* Fri Nov 30 2012 Andrey Cherepanov <cas@altlinux.org> 23.0.1271.95-alt1.r169798
- New version 23.0.1271.95
- Security fixes:
  - High CVE-2012-5138: Incorrect file path handling.
  - High CVE-2012-5137: Use-after-free in media source handling.
  - High CVE-2012-5133: Use-after-free in SVG filters.

* Thu Nov 08 2012 Andrey Cherepanov <cas@altlinux.org> 23.0.1271.64-alt1.r165196
- New version 23.0.1271.64
- Fixes:
  - High CVE-2012-5116: Use-after-free in SVG filter handling.
  - High CVE-2012-5121: Use-after-free in video layout.
  - High CVE-2012-5124: Memory corruption in texture handling.
  - Critical CVE-2012-5112: SVG use-after-free and IPC arbitrary file
    write.
  - High CVE-2012-2900: Crash in Skia text rendering.
  - Critical CVE-2012-5108: Race condition in audio device handling.
  - High CVE-2012-2896: Integer overflow in WebGL
  - High CVE-2012-2895: Out-of-bounds writes in PDF viewer.
  - High CVE-2012-2894: Crash in graphics context handling.
  - High CVE-2012-2893: Double free in XSL transforms.
  - High CVE-2012-2890: Use-after-free in PDF viewer.
  - High CVE-2012-2889: UXSS in frame handling.
  - High CVE-2012-2888: Use-after-free in SVG text references.
  - High CVE-2012-2887: Use-after-free in onclick handling.
  - High CVE-2012-2886: UXSS in v8 bindings.
  - High CVE-2012-2883: Out-of-bounds write in Skia.
  - High CVE-2012-2882: Wild pointer in OGG container handling.
  - High CVE-2012-2881: DOM tree corruption with plug-ins.
  - High CVE-2012-2878: Use-after-free in plug-in handling.
  - High CVE-2012-2876: Buffer overflow in SSE2 optimizations.
  - High CVE-2012-2874: Out-of-bounds write in Skia.
- Total move to system v8
- Use builtin icu-4.6 and patched zlib (see http://code.google.com/p/chromium/issues/detail?id=143623)

* Wed Oct 03 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt4.r154005
- Set flags for build on ARM
- Rebuild with new version of v8

* Tue Oct 02 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt3.r154005
- Enable video and audio support in HTML5

* Thu Sep 13 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt2.r154005
- Disable debug version and fix problem with Google accounts (ALT 27731)
- Build with system icu libraries
- Open blank initial tab and distribution start page
- Add ALT-specific initial bookmarks

* Fri Sep 07 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt1.r154005
- New version 21.0.1180.89
- Fixes:
  - Several Pepper Flash fixes (Issue 140577, 144107, 140498, 142479)
  - Microphone issues with tinychat.com (Issue: 143192)
  - Devtools regression with "save as" of edited source (issue: 141180)
  - Mini ninjas shaders fails (Issue: 142705)
  - Page randomly turns red/green gradient boxes (Issue: 110343)
  - Medium CVE-2012-2865: Out-of-bounds read in line breaking.
  - High CVE-2012-2866: Bad cast with run-ins.
  - Low CVE-2012-2867: Browser crash with SPDY.
  - Medium CVE-2012-2868: Race condition with workers and XHR.
  - High CVE-2012-2869: Avoid stale buffer in URL loading.
  - Low CVE-2012-2870: Lower severity memory management issues in XPath.
  - High CVE-2012-2871: Bad cast in XSL transforms.
  - Medium CVE-2012-2872: XSS in SSL interstitial.
- Export patches and flags from Debian
- Disable tcmalloc

* Fri Aug 24 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.81-alt1.r151980
- New version 21.0.1180.81
- Disable plugin installation
- Fix tcmalloc because glibc 2.16 removed the undocumented definition of
  'struct siginfo' from <bits/siginfo.h>

* Wed Aug 15 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt5.r139751
- Set appropriate desktop file name for default browser check

* Mon Aug 13 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt4.r139751
- Fix crash when displaying system print dialog on Linux
  (http://code.google.com/p/chromium/issues/detail?id=130095)
- Rename .desktop file and add localization strings

* Fri Aug 10 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt3.r139751
- Add missing file chrome_sandbox

* Thu Aug 09 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt2.r139751
- Rename DE specific packages and set appropriate requirement to wallet subsystem
- Set alternatives to chromium-kde and chromium-gnome
- Add default parameters support in /etc/chromium/default

* Wed Aug 08 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt1.r139751
- Build for Sisyphus version 21.0.1158.0 (import from SUSE)
- Rename to chromium

