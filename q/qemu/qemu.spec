# vim: set ft=spec
# vim600: set fdm=marker:

# {{{ macros define
%define _unpackaged_files_terminate_build 1
# Disable LTO
# qos-test fails when built with LTO and gcc-12
# https://gitlab.com/qemu-project/qemu/-/issues/1186
%def_disable lto
%if_disabled lto
%global optflags_lto %nil
%endif

%def_disable edk2_cross

%def_enable user_static

%def_enable sdl
%def_enable curses
%def_enable vnc
%def_enable vnc_sasl
%def_enable vnc_jpeg
%def_enable png
%def_enable xkbcommon
%def_disable vde
%def_enable alsa
%def_enable pulseaudio
%def_enable pipewire
%def_enable oss
%def_disable jack
%def_disable sndio
%def_enable capstone
%def_enable aio
%def_enable io_uring
%def_enable install_blobs
%def_enable smartcard
%def_enable libusb
%def_enable usb_redir
%def_enable vhost_crypto
%def_enable vhost_net
%def_enable bpf
%def_enable opengl
%def_enable guest_agent
%def_enable tools
%def_enable spice
%def_enable libiscsi
%ifarch %ix86 %arm %mips32 ppc riscv64
%def_disable rbd
%def_disable glusterfs
%else
%def_enable rbd
%def_enable glusterfs
%endif
%def_enable vitastor
%def_enable libnfs
%def_enable zstd
%def_enable seccomp
%def_enable gtk
%def_enable gtk_clipboard
%def_enable gnutls
%def_disable nettle
%def_disable gcrypt
%def_enable selinux
%def_enable virglrenderer
%def_enable tpm
%def_enable libssh
%def_enable live_block_migration
%def_enable replication
%ifnarch %arm %ix86 %mips32
%def_enable numa
%else
%def_disable numa
%endif
%ifnarch %arm %ix86 %mips32 loongarch64
%def_enable libpmem
%else
%def_disable libpmem
%endif
%def_enable replication
%def_enable rdma
%def_enable lzo
%def_enable snappy
%def_enable bzip2
%def_disable lzfse
%def_disable xen
%def_enable mpath
%def_enable blkio
%def_enable libudev
%def_enable libdaxctl
%def_enable fuse
%def_disable brlapi
%def_disable af_xdp

%define power64 ppc64 ppc64p7 ppc64le
%define mips32 mips mipsel mipsr6 mipsr6el
%define mips64 mips64 mips64el mips64r6 mips64r6el
%define mips_arch %mips32 %mips64

%ifarch %ix86
%global kvm_package system-x86
%def_enable qemu_kvm
%endif
%ifarch x86_64
%global kvm_package system-x86
%def_enable qemu_kvm
%endif
%ifarch %power64
%global kvm_package   system-ppc
%def_enable qemu_kvm
%endif
%ifarch s390x
%global kvm_package   system-s390x
%endif
%ifarch armh
%global kvm_package   system-arm
%def_enable qemu_kvm
%endif
%ifarch aarch64
%global kvm_package   system-aarch64
%def_enable qemu_kvm
%endif
%ifarch riscv64
%global kvm_package   system-riscv
%def_enable qemu_kvm
%endif
%ifarch loongarch64
%global kvm_package   system-loongarch
%def_enable qemu_kvm
%endif
%ifarch %mips_arch
%global kvm_package   system-mips
%endif

%def_enable have_kvm

%define audio_drv_list %{?_enable_oss:oss} %{?_enable_alsa:alsa} %{?_enable_sdl:sdl} %{?_enable_pulseaudio:pa} %{?_enable_pipewire:pipewire} %{?_enable_jack:jack} %{?_enable_sndio:sndio} dbus
%define block_drv_list curl dmg %{?_enable_glusterfs:gluster} %{?_enable_libiscsi:iscsi} %{?_enable_libnfs:nfs} %{?_enable_rbd:rbd} %{?_enable_libssh:ssh} %{?_enable_blkio:blkio} %{?_enable_vitastor:vitastor}
%define ui_list %{?_enable_gtk:gtk} %{?_enable_curses:curses} %{?_enable_sdl:sdl} %{?_enable_opengl:opengl} dbus
%define ui_spice_list %{?_enable_spice:app core}
%define device_usb_list redirect %{?_enable_smartcard:smartcard} host
%define device_display_list virtio-gpu-pci %{?_enable_virglrenderer:virtio-gpu virtio-gpu-gl virtio-gpu-pci-gl virtio-vga-gl} virtio-vga %{?_enable_spice:qxl}
%define qemu_arches aarch64 alpha arm avr cris hppa loongarch m68k microblaze mips nios2 or1k ppc riscv rx s390x sh4 sparc tricore x86 xtensa

%global _group vmusers
%global rulenum 90
%global _libexecdir /usr/libexec
%global _localstatedir /var
%global firmwaredirs "%_datadir/qemu:%_datadir/seabios:%_datadir/seavgabios:%_datadir/ipxe:%_datadir/ipxe.efi"

# }}}

Name: qemu
Version: 8.2.3
Release: alt1

Summary: QEMU CPU Emulator
License: BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group: Emulators
Url: https://www.qemu.org
# git://git.qemu.org/qemu.git
Source0: %name-%version.tar
Source100: keycodemapdb.tar
Source101: berkeley-testfloat-3.tar
Source102: berkeley-softfloat-3.tar
# qemu-kvm back compat wrapper
Source5: qemu-kvm.sh
# guest agent service
Source8: qemu-guest-agent.rules
Source9: qemu-guest-agent.service
Source10: qemu-guest-agent.init
Source11: qemu-ga.sysconfig
# /etc/qemu/bridge.conf
Source12: bridge.conf

Patch: qemu-alt.patch

%set_verify_elf_method fhs=relaxed
%add_verify_elf_skiplist %_datadir/%name/*
%add_findreq_skiplist %_datadir/%name/*

Requires: %name-system = %EVR
Requires: %name-user = %EVR

# for tests
BuildRequires: /dev/kvm

BuildRequires(pre): rpm-build-python3
BuildRequires: meson >= 0.63.0
BuildRequires: glibc-devel-static zlib-devel-static glib2-devel-static libpcre2-devel-static libattr-devel-static libdw-devel-static
BuildRequires: glib2-devel >= 2.56 libgio-devel
BuildRequires: libdw-devel
BuildRequires: makeinfo perl-devel python3-module-sphinx python3-module-sphinx_rtd_theme
BuildRequires: libcap-ng-devel
BuildRequires: libxfs-devel
BuildRequires: zlib-devel libcurl-devel >= 7.29.0 libpci-devel glibc-kernheaders
BuildRequires: ipxe-roms-qemu >= 1:20161208-alt1.git26050fd seavgabios seabios >= 1.7.4-alt2 libfdt-devel >= 1.5.0.0.20.2431 qboot
BuildRequires: libpixman-devel >= 0.21.8
BuildRequires: libkeyutils-devel
%{?_enable_af_xdp:BuildRequires: libxdp-devel >= 1.4.0}
BuildRequires: python3-devel >= 3.8
BuildRequires: flex
%ifarch riscv64
BuildRequires: libatomic-devel-static
%endif
%{?_enable_sdl:BuildRequires: libSDL2-devel libSDL2_image-devel}
%{?_enable_curses:BuildRequires: libncursesw-devel}
%{?_enable_alsa:BuildRequires: libalsa-devel}
%{?_enable_pulseaudio:BuildRequires: libpulseaudio-devel}
%{?_enable_pipewire:BuildRequires: pkgconfig(libpipewire-0.3) >= 0.3.60}
%{?_enable_jack:BuildRequires: libjack-devel jack-audio-connection-kit}
%{?_enable_sndio:BuildRequires: libsndio-devel}
%{?_enable_capstone:BuildRequires: libcapstone-devel}
%{?_enable_vnc_sasl:BuildRequires: libsasl2-devel}
%{?_enable_vnc_jpeg:BuildRequires: libjpeg-devel}
%{?_enable_png:BuildRequires: libpng-devel >= 1.6.34}
%{?_enable_xkbcommon:BuildRequires: libxkbcommon-devel xkeyboard-config-devel}
%{?_enable_vde:BuildRequires: libvde-devel}
%{?_enable_aio:BuildRequires: libaio-devel}
%{?_enable_io_uring:BuildRequires: liburing-devel >= 0.3}
%{?_enable_bpf:BuildRequires: libbpf-devel}
%{?_enable_spice:BuildRequires: libspice-server-devel >= 0.14.0 spice-protocol >= 0.14.0}
BuildRequires: libuuid-devel
%{?_enable_smartcard:BuildRequires: libcacard-devel >= 2.5.1}
%{?_enable_usb_redir:BuildRequires: libusbredir-devel >= 0.5}
%{?_enable_opengl:BuildRequires: libepoxy-devel libgbm-devel}
%{?_enable_guest_agent:BuildRequires: glib2-devel >= 2.38}
%{?_enable_rbd:BuildRequires: ceph-devel >= 1.12.0}
%{?_enable_vitastor:BuildRequires: libvitastor-devel}
%{?_enable_libiscsi:BuildRequires: libiscsi-devel >= 1.9.0}
%{?_enable_libnfs:BuildRequires: libnfs-devel >= 1.9.3}
%{?_enable_zstd:BuildRequires: libzstd-devel >= 1.4.0}
%{?_enable_seccomp:BuildRequires: libseccomp-devel >= 2.3.0}
%{?_enable_glusterfs:BuildRequires: pkgconfig(glusterfs-api)}
%{?_enable_gtk:BuildRequires: libgtk+3-devel >= 3.22.0 pkgconfig(vte-2.91)}
%{?_enable_gnutls:BuildRequires: libgnutls-devel >= 3.5.18}
%{?_enable_nettle:BuildRequires: libnettle-devel >= 3.4}
%{?_enable_gcrypt:BuildRequires: libgcrypt-devel >= 1.8.0}
%{?_enable_selinux:BuildRequires: libselinux-devel}
BuildRequires: libpam-devel
BuildRequires: libtasn1-devel
BuildRequires: libslirp-devel >= 4.1.0
%{?_enable_virglrenderer:BuildRequires: pkgconfig(virglrenderer)}
%{?_enable_libssh:BuildRequires: libssh-devel >= 0.8.7}
%{?_enable_libusb:BuildRequires: libusb-devel >= 1.0.13}
%{?_enable_rdma:BuildRequires: rdma-core-devel}
%{?_enable_numa:BuildRequires: libnuma-devel}
%{?_enable_lzo:BuildRequires: liblzo2-devel}
%{?_enable_snappy:BuildRequires: libsnappy-devel}
%{?_enable_bzip2:BuildRequires: bzlib-devel}
%{?_enable_lzfse:BuildRequires: liblzfse-devel}
%{?_enable_xen:BuildRequires: libxen-devel}
%{?_enable_mpath:BuildRequires: libudev-devel libmultipath-devel}
%{?_enable_blkio:BuildRequires: libblkio-devel}
%{?_enable_libpmem:BuildRequires: libpmem-devel}
%{?_enable_libudev:BuildRequires: libudev-devel}
%{?_enable_libdaxctl:BuildRequires: libdaxctl-devel}
%{?_enable_fuse:BuildRequires: libfuse3-devel}
# used by some linux user impls
BuildRequires: libdrm-devel

%global requires_all_modules \
Requires: %name-block-curl \
Requires: %name-block-dmg  \
%{?_enable_glusterfs:Requires: %name-block-gluster} \
%{?_enable_libiscsi:Requires: %name-block-iscsi} \
%{?_enable_libnfs:Requires: %name-block-nfs}     \
%{?_enable_rbd:Requires: %name-block-rbd}        \
%{?_enable_vitasor:Requires: %name-block-vitasor} \
%{?_enable_libssh:Requires: %name-block-ssh}     \
%{?_enable_alsa:Requires: %name-audio-alsa}      \
%{?_enable_oss:Requires: %name-audio-oss}        \
%{?_enable_pipewire:Requires: %name-audio-pipewire}  \
%{?_enable_pulseaudio:Requires: %name-audio-pa}  \
%{?_enable_jack:Requires: %name-audio-jack}      \
%{?_enable_sndio:Requires: %name-audio-sndio}    \
%{?_enable_sdl:Requires: %name-audio-sdl}        \
%{?_enable_spice:Requires: %name-audio-spice}    \
%{?_enable_curses:Requires: %name-ui-curses}     \
%{?_enable_spice:Requires: %name-ui-spice-app}   \
%{?_enable_spice:Requires: %name-ui-spice-core}  \
%{?_enable_spice:Requires: %name-device-display-qxl} \
Requires: %name-device-display-virtio-gpu-pci    \
Requires: %name-device-display-virtio-vga        \
%{?_enable_virglrenderer:Requires: %name-device-display-virtio-gpu} \
%{?_enable_virglrenderer:Requires: %name-device-display-virtio-gpu-gl}  \
%{?_enable_virglrenderer:Requires: %name-device-display-virtio-gpu-pci-gl} \
%{?_enable_virglrenderer:Requires: %name-device-display-virtio-vga-gl}  \
%{?_enable_virglrenderer:Requires: %name-device-display-vhost-user-gpu} \
%{?_enable_brlapi:Requires: %name-char-baum} \
%{?_enable_spice:Requires: %name-char-spice} \
Requires: %name-device-usb-host \
Requires: %name-device-usb-redirect \
%{?_enable_smartcard:Requires: %name-device-usb-smartcard}

##%%{?_enable_opengl:Requires: %%name-ui-opengl} \
##%%{?_enable_opengl:Requires: %%name-ui-egl-headless} \
##%%{?_enable_gtk:Requires: %%name-ui-gtk}       \
##%%{?_enable_sdl:Requires: %%name-ui-sdl}

%description
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.  QEMU has two operating modes:

* Full system emulation.  In this mode, QEMU emulates a full system
  (for example a PC), including a processor and various peripherials.
  It can be used to launch different Operating Systems without rebooting
  the PC or to debug system code.

* User mode emulation.  In this mode, QEMU can launch Linux processes
  compiled for one CPU on another CPU.  It can be used to launch the
  Wine Windows API emulator or to ease cross-compilation and
  cross-debugging.

As QEMU requires no host kernel patches to run, it is very safe and easy
to use.

%package common
Summary: QEMU CPU Emulator - common files
Group: Emulators
Requires(pre): shadow-utils sysvinit-utils
Requires: %name-img = %EVR
Requires: ipxe-roms-qemu

%description common
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.
This package contains common files for qemu.

%package system
Summary: QEMU CPU Emulator - full system emulation
Group: Emulators
BuildArch: noarch
Requires: %name-common = %EVR
Requires: %name-tools = %EVR
%{?_enable_mpath:Requires: %name-pr-helper = %EVR}
Conflicts: %name-img < %EVR
%{expand:%(for i in %qemu_arches; do echo Requires: %%name-system-$i ; done)}

%description system
Full system emulation.  In this mode, QEMU emulates a full system
(for example a PC), including a processor and various peripherials.
It can be used to launch different Operating Systems without rebooting
the PC or to debug system code.

%if_enabled have_kvm
%package kvm
Summary: QEMU metapackage for KVM support
Group: Emulators
Requires: qemu-%kvm_package = %EVR
Requires: qemu-kvm-core = %EVR

%description kvm
This is a meta-package that provides a qemu-system-<arch> package for native
architectures where kvm can be enabled. For example, in an x86 system, this
will install qemu-system-x86

%package kvm-core
Summary: QEMU metapackage for KVM support
Group: Emulators
Requires: qemu-%kvm_package-core = %EVR

%description kvm-core
This is a meta-package that provides a qemu-system-<arch>-core package
for native architectures where kvm can be enabled. For example, in an
x86 system, this will install qemu-system-x86-core
%endif

%package user
Summary: QEMU CPU Emulator - user mode emulation
Group: Emulators
Requires: %name-common = %EVR
%{expand:%(for i in %qemu_arches; do echo Requires: %%name-user-$i ; done)}

%description user
User mode emulation.  In this mode, QEMU can launch Linux processes
compiled for one CPU on another CPU.  It can be used to launch the
Wine Windows API emulator or to ease cross-compilation and
cross-debugging.

%package user-binfmt
Summary: QEMU user mode emulation of qemu targets
Group: Emulators
Requires: %name-user = %EVR
# qemu-user-binfmt + qemu-user-static both provide binfmt rules
Conflicts: %name-user-static-binfmt
Conflicts: %name-user < 2.10.1-alt1
%{expand:%(for i in %qemu_arches; do echo Requires: %%name-user-binfmt-$i ; done)}

%description user-binfmt
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the user mode emulation of qemu targets

%package user-static
Summary: QEMU user mode emulation of qemu targets static build
Group: Emulators
Requires: %name-aux = %EVR
%{expand:%(for i in %qemu_arches; do echo Requires: %%name-user-static-$i ; done)}

%description user-static
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the user mode emulation of qemu targets built as
static binaries

%package user-static-binfmt
Summary: QEMU user mode emulation of qemu targets static build
Group: Emulators
Requires: %name-user-static
Conflicts: %name-user-binfmt
Conflicts: %name-user < 2.10.1-alt1
Provides: %name-user-binfmt_misc = %EVR
Obsoletes: %name-user-binfmt_misc < %EVR
%{expand:%(for i in %qemu_arches; do echo Requires: %%name-user-static-binfmt-$i ; done)}

%description user-static-binfmt
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the user mode emulation of qemu targets

%global do_package_user() \
%%package %%{1}-%%{2} \
Summary: QEMU CPU Emulator - %%{1}-%%{2} mode emulation \
Group: Emulators \
%%{?3} %%{?4} \
%%{?5} %%{?6} \
%%description %%{1}-%%{2} \
User mode emulation.  In this mode, QEMU can launch Linux processes \
compiled for one CPU on another CPU. \
%%files %%{1}-%%{2} -f %%{1}-%%{2}.list

%{expand:%(for i in %qemu_arches hexagon; do echo %%do_package_user user $i Requires: qemu-common; done)}
%{expand:%(for i in %qemu_arches hexagon; do echo %%do_package_user user-binfmt $i Requires: qemu-user-$i Conflicts: qemu-user-static-binfmt-$i; done)}

%if_enabled user_static
%{expand:%(for i in %qemu_arches hexagon; do echo %%do_package_user user-static $i; done)}
%{expand:%(for i in %qemu_arches hexagon; do echo %%do_package_user user-static-binfmt $i Requires: qemu-user-static-$i Conflicts: qemu-user-binfmt-$i; done)}
%endif

%package img
Summary: QEMU command line tool for manipulating disk images
Group: Emulators
Provides: qemu-kvm-img = %EVR
Obsoletes: qemu-kvm-img < %EVR
Requires: %name-aux = %EVR

%description img
This package provides a command line tool for manipulating disk images

%package tools
Summary: Tools for QEMU
Group: Emulators
Requires: %name-img = %EVR
Requires: %name-aux = %EVR
Conflicts: %name-system < 2.11.0-alt2

%description tools
This package contains various QEMU related tools, including a bridge helper,
a virtfs helper.

%package pr-helper
Summary: qemu-pr-helper utility for %name
Group: Emulators

%description pr-helper
This package provides the qemu-pr-helper utility that is required for certain
SCSI features.

%package tests
Summary: tests for the %name package
Group: Emulators
Requires: %name = %EVR

%define testsdir %_libdir/%name/tests-src
%add_python3_path %testsdir

%description tests
The %name-tests rpm contains tests that can be used to verify
the functionality of the installed %name package

Install this package if you want access to the avocado_qemu
tests, or qemu-iotests.

%global do_package_block() \
%%package block-%%{1} \
Summary: QEMU %%{1} block driver \
Group: Emulators \
Requires: %%name-common = %%EVR \
\
%%description block-%%{1} \
This package provides the additional %%{1} block driver for QEMU. \
\
%%files block-%%{1} \
%%_libdir/qemu/block-%%{1}*.so

%{expand:%(for i in %block_drv_list; do echo %%do_package_block $i; done)}

%global do_package_audio() \
%%package audio-%%{1} \
Summary: QEMU %%{1} audio driver \
Group: Emulators \
Requires: %%name-common = %%EVR \
\
%%description audio-%%{1} \
This package provides the additional %%{1} audio driver for QEMU. \
\
%%files audio-%%{1} \
%%_libdir/qemu/audio-%%{1}.so

%{expand:%(for i in %audio_drv_list spice; do echo %%do_package_audio $i; done)}

%global do_package_ui() \
%%package ui-%%{1} \
Summary: QEMU %%{1} UI driver \
Group: Emulators \
Requires: %%name-common = %%EVR \
%%if "%%{1}" == "gtk" \
Requires: %%name-ui-opengl \
%%endif \
%%if "%%{1}" == "sdl" \
Requires: %%name-ui-opengl \
%%endif \
\
%%description ui-%%{1} \
This package provides the additional %%{1} UI for QEMU. \
\
%%files ui-%%{1} \
%%_libdir/qemu/ui-%%{1}.so

%{expand:%(for i in %ui_list; do echo %%do_package_ui $i; done)}

%global do_package_ui_spice() \
%%package ui-spice-%%{1} \
Summary: QEMU spice-%%{1} UI driver \
Group: Emulators \
Requires: %%name-common = %%EVR \
%%if "%%{1}" == "core" \
Requires: %%name-ui-opengl \
%%endif \
%%if "%%{1}" == "app" \
Requires: %%name-ui-spice-core \
Requires: %%name-char-spice \
%%endif \
\
%%description ui-spice-%%{1} \
This package provides the additional %%{1} UI for QEMU. \
\
%%files ui-spice-%%{1} \
%%_libdir/qemu/ui-spice-%%{1}.so

%{expand:%(for i in %ui_spice_list; do echo %%do_package_ui_spice $i; done)}

%package ui-egl-headless
Summary: QEMU EGL headless driver
Group: Emulators
Requires: %name-common = %EVR
Requires: %name-ui-opengl = %EVR

%description ui-egl-headless
This package provides the additional egl-headless UI for QEMU.

%package device-display-vhost-user-gpu
Group: Emulators
Summary: QEMU vhost-user-gpu display device
Requires: %name-common = %EVR

%description device-display-vhost-user-gpu
This package provides the vhost-user-gpu display device for QEMU.

%package device-display-virtio-gpu-ccw
Group: Emulators
Summary: QEMU virtio-gpu-ccw display device
Requires: %name-common = %EVR

%description device-display-virtio-gpu-ccw
This package provides the virtio-gpu-ccw display device for QEMU.

%global do_package_device_display() \
%%package device-display-%%{1} \
Summary: QEMU display-%%{1} device \
Group: Emulators \
Requires: %%name-common = %%EVR \
%%if "%%{1}" == "qxl" \
Requires: %%name-ui-spice-core \
%%endif \
\
%%description device-display-%%{1} \
This package provides the additional device display-%%{1} for QEMU. \
\
%%files device-display-%%{1} \
%%_libdir/qemu/hw-display-%%{1}.so

%{expand:%(for i in %device_display_list; do echo %%do_package_device_display $i; done)}

%global do_package_device_usb() \
%%package device-usb-%%{1} \
Summary: QEMU usb-%%{1} device \
Group: Emulators \
Requires: %%name-common = %%EVR \
\
%%description device-usb-%%{1} \
This package provides the additional device usb-%%{1} for QEMU. \
\
%%files device-usb-%%{1} \
%%_libdir/qemu/hw-usb-%%{1}.so

%{expand:%(for i in %device_usb_list; do echo %%do_package_device_usb $i; done)}

%package char-baum
Summary: QEMU Baum chardev driver
Group: Emulators
Requires: %name-common = %EVR

%description char-baum
This package provides the Baum chardev driver for QEMU.

%package char-spice
Summary: QEMU spice chardev driver
Group: Emulators
Requires: %name-common = %EVR
Requires: %name-ui-spice-core = %EVR

%description char-spice
This package provides the spice chardev driver for QEMU.

%package guest-agent
Summary: QEMU guest agent
Group: Emulators
Requires: %name-aux = %EVR

%description guest-agent
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides an agent to run inside guests, which communicates
with the host over a virtio-serial channel named "org.qemu.guest_agent.0"

This package does not need to be installed on the host OS.

%package doc
Summary: User documentation for %name
Group: Documentation
BuildArch: noarch
Requires: %name-aux = %EVR

%description doc
User documentation for %name

%package aux
Summary: QEMU auxiliary package
Group: Emulators
BuildArch: noarch

%description aux
QEMU is a generic and open source processor emulator which achieves
good emulation speed by using dynamic translation.

This is an auxiliary package.

%global do_package_system() \
%%package system-%%{1} \
Summary: QEMU system emulator for %%{1} \
Group: Emulators \
Requires: %%name-system-%%{1}-core \
%%requires_all_modules \
%%ifnarch %%arm %%ix86 %%mips32 \
Requires: vhostuser-backend(fs) \
%%endif \
%%description system-%%{1} \
This package provides the system emulator for %%{1}. \
%%files system-%%{1} \
\
%%package system-%%{1}-core \
Summary: QEMU system emulator for %%{1} \
Group: Emulators \
Requires: %%name-common \
Conflicts: %%name-system < 2.10.1-alt1 \
\
%%if "%%{1}" == "x86" \
Requires: seabios seavgabios edk2-ovmf libseccomp qboot \
%%endif \
%%if "%%{1}" == "aarch64" \
Requires: edk2-aarch64 \
%%endif \
%%if "%%{1}" == "ppc" \
Requires: seavgabios \
%%endif \
\
%%description system-%%{1}-core \
This package provides the system emulator for %%{1}. \
%%files system-%%{1}-core \
\
%%if "%%{1}" == "x86" \
%%_bindir/qemu-system-i386 \
%%_man1dir/qemu-system-i386.1* \
%%_libdir/%%name/accel-tcg-i386.so \
%%_libdir/%%name/accel-tcg-x86_64.so \
%%_datadir/%%name/bios* \
%%_datadir/%%name/linuxboot* \
%%_datadir/%%name/multiboot.bin \
%%_datadir/%%name/multiboot_dma.bin \
%%_datadir/%%name/kvmvapic.bin \
%%_datadir/%%name/pvh.bin \
%%endif \
\
%%if "%%{1}" == "alpha" \
%%_datadir/%%name/palcode-clipper \
%%endif \
\
%%if "%%{1}" == "arm" \
%%_datadir/%%name/npcm7xx_bootrom.bin \
%%endif \
\
%%if "%%{1}" == "hppa" \
%%_datadir/%%name/hppa-firmware.img \
%%endif \
\
%%if "%%{1}" == "microblaze" \
%%_datadir/%%name/petalogix*.dtb \
%%endif \
\
%%if "%%{1}" == "s390x" \
%%_datadir/%%name/s390-*.img \
%%endif \
\
%%if "%%{1}" == "sparc" \
%%_datadir/%%name/QEMU* \
%%_datadir/%%name/openbios-sparc* \
%%endif \
\
%%if "%%{1}" == "ppc" \
%%_datadir/%%name/bamboo.dtb \
%%_datadir/%%name/canyonlands.dtb \
%%_datadir/%%name/qemu_vga.ndrv \
%%_datadir/%%name/skiboot.lid \
%%_datadir/%%name/u-boot* \
%%_datadir/%%name/openbios-ppc \
%%_datadir/%%name/slof.bin \
%%_datadir/%%name/vof*.bin \
%%endif \
\
%%if "%%{1}" == "riscv" \
%%_datadir/%%name/opensbi* \
%%endif \
\
%%_bindir/qemu-system-%%{1}* \
%%_man1dir/qemu-system-%%{1}*

%{expand:%(for i in %qemu_arches; do echo %%do_package_system $i; done)}

%prep
%setup
mkdir -p subprojects/{keycodemapdb,berkeley-testfloat-3,berkeley-softfloat-3}
tar -xf %SOURCE100 -C subprojects/keycodemapdb --strip-components 1
tar -xf %SOURCE101 -C subprojects/berkeley-testfloat-3 --strip-components 1
tar -xf %SOURCE102 -C subprojects/berkeley-softfloat-3 --strip-components 1
cp -a subprojects/packagefiles/berkeley-testfloat-3/* subprojects/berkeley-testfloat-3/
cp -a subprojects/packagefiles/berkeley-softfloat-3/* subprojects/berkeley-softfloat-3/

%patch -p1

%build
run_configure() {
# non-GNU configure
../configure \
	--disable-download \
	--prefix=%prefix \
	--sysconfdir=%_sysconfdir \
	--libdir=%_libdir \
	--mandir=%_mandir \
	--libexecdir=%_libexecdir \
	--localstatedir=%_localstatedir \
	--extra-cflags="%optflags" \
	--with-pkgversion=%name-%version-%release \
	--disable-werror \
	--disable-debug-tcg \
	--disable-sparse \
	--disable-strip \
	%{?_enable_lto:--enable-lto} \
	--firmwarepath="%firmwaredirs" \
	 "$@"
}

%if_enabled user_static
mkdir build-static
pushd build-static
# non-GNU configure
run_configure \
	--static \
	--enable-user \
	--enable-linux-user \
	--enable-attr \
	--enable-tcg \
	--extra-ldflags="-Wl,-Ttext-segment=0x60000000" \
	--audio-drv-list="" \
	--disable-af-xdp \
	--disable-alsa \
	--disable-fdt \
	--disable-auth-pam \
	--disable-avx2 \
	--disable-avx512f \
	--disable-avx512bw \
	--disable-install-blobs \
	--disable-blkio \
	--disable-bochs \
	--disable-bpf \
	--disable-brlapi \
	--disable-bsd-user \
	--disable-bzip2 \
	--disable-cap-ng \
	--disable-capstone \
	--disable-cloop \
	--disable-cocoa \
	--disable-colo-proxy \
	--disable-coreaudio \
	--disable-crypto-afalg \
	--disable-curl \
	--disable-curses \
	--disable-dbus-display \
	--disable-debug-graph-lock \
	--disable-debug-info \
	--disable-debug-mutex \
	--disable-debug-tcg \
	--disable-dmg \
	--disable-docs \
	--disable-download \
	--disable-dsound \
	--disable-fuse \
	--disable-gcrypt \
	--disable-gio \
	--disable-gtk \
	--disable-gettext \
	--disable-glusterfs \
	--disable-gnutls \
	--disable-gtk \
	--disable-gtk-clipboard \
	--disable-guest-agent \
	--disable-guest-agent-msi \
	--disable-hv-balloon \
	--disable-hvf \
	--disable-iconv \
	--disable-jack \
	--disable-sndio \
	--disable-keyring \
	--disable-libkeyutils \
	--disable-kvm \
	--disable-l2tpv3 \
	--disable-libdaxctl \
	--disable-libiscsi \
	--disable-libnfs \
	--disable-libpmem \
	--disable-libssh \
	--disable-libudev \
	--disable-libusb \
	--disable-linux-aio \
	--disable-linux-io-uring \
	--disable-live-block-migration \
	--disable-replication \
	--disable-lzfse \
	--disable-lzo \
	--disable-membarrier \
	--disable-modules \
	--disable-mpath \
	--disable-netmap \
	--disable-nettle \
	--disable-numa \
	--disable-nvmm \
	--disable-opengl \
	--disable-oss \
	--disable-pa \
	--disable-parallels \
	--disable-pie \
	--disable-pipewire \
	--disable-pixman \
	--disable-plugins \
	--disable-pvrdma \
	--disable-qcow1 \
	--disable-qed \
	--disable-qom-cast-debug \
	--disable-rbd \
	--disable-vitastor \
	--disable-rdma \
	--disable-relocatable \
	--disable-replication \
	--disable-rutabaga-gfx \
	--disable-rng-none \
	--disable-sdl \
	--disable-sdl-image \
	--disable-seccomp \
	--disable-selinux \
	--disable-slirp \
	--disable-slirp-smbd \
	--disable-smartcard \
	--disable-snappy \
	--disable-sparse \
	--disable-spice \
	--disable-spice-protocol \
	--disable-system \
	--disable-tools \
	--disable-tpm \
	--disable-tsan \
	--disable-u2f \
	--disable-usb-redir \
	--disable-vpc \
	--disable-vde \
	--disable-vdi \
	--disable-vfio-user-server \
	--disable-vhdx \
	--disable-vhost-crypto \
	--disable-vhost-kernel \
	--disable-vhost-net \
	--disable-vhost-user \
	--disable-vhost-vdpa \
	--disable-virglrenderer \
	--disable-virtfs \
	--disable-vnc \
	--disable-vnc-jpeg \
	--disable-png \
	--disable-vnc-sasl \
	--disable-vte \
	--disable-vvfat \
	--disable-whpx \
	--disable-xen \
	--disable-xen-pci-passthrough \
	--disable-xkbcommon \
	--disable-zstd \
	--disable-fuse \
	--disable-libvduse \
	--without-default-devices

# Please do not touch this
sed -i "/cpu_get_model/ {
N
N
/return / s,any,cortex-a8,
}" ../linux-user/arm/target_elf.h

%make_build 

%if_with arm
mv qemu-arm qemu-armh

sed -i '/return / s,cortex-a8,cortex-a53,' ../linux-user/arm/target_elf.h
%make_build
mv qemu-arm qemu-aarch64

exit 0

sed -i '/return / s,cortex-a53,any,' ../linux-user/arm/target_elf.h
%make_build
%endif

popd
%endif

%ifarch loongarch64
# XXX: until glibc-kernheaders is updated from 6.7, we need a workaround:
pushd linux-headers
ln -s asm-loongarch asm
popd
%endif

# Build for non-static qemu-*
mkdir build-dynamic
pushd build-dynamic
# non-GNU configure
run_configure \
	--enable-system \
	--enable-kvm \
	--enable-user \
	--enable-linux-user \
	--enable-pie \
	--enable-modules \
	%{?_enable_sdl:--enable-sdl} \
	%{?_disable_curses:--disable-curses} \
	--enable-dbus-display \
	%{subst_enable vnc} \
	%{?_enable_gtk:--enable-gtk --enable-vte} \
	%{?_enable_gtk_clipboard:--enable-gtk-clipboard} \
	%{?_disable_vnc_tls:--disable-vnc-tls} \
	%{?_disable_vnc_sasl:--disable-vnc-sasl} \
	%{?_disable_vnc_jpeg:--disable-vnc-jpeg} \
	%{subst_enable png} \
	%{?_disable_xkbcommon:--disable-xkbcommon} \
	%{?_disable_vde:--disable-vde} \
	%{?_disable_aio:--disable-linux-aio} \
	%{?_disable_io_uring:--disable-linux-io-uring} \
	%{?_disable_install_blobs: --disable-install-blobs} \
	%{subst_enable spice} \
	%{subst_enable brlapi} \
	--enable-curl \
	%{subst_enable virglrenderer} \
	%{subst_enable tpm} \
	%{subst_enable bpf} \
	--enable-fdt=system \
	%{subst_enable xen} \
	%{?_enable_vhost_crypto:--enable-vhost-crypto} \
	%{?_enable_vhost_net:--enable-vhost-net} \
	--enable-slirp \
	%{subst_enable smartcard} \
	%{subst_enable libusb} \
	%{?_enable_usb_redir:--enable-usb-redir} \
	%{subst_enable opengl} \
	%{subst_enable zstd} \
	%{subst_enable seccomp} \
	%{subst_enable libiscsi} \
	%{subst_enable rbd} \
	%{subst_enable vitastor} \
	%{subst_enable libnfs} \
	%{subst_enable glusterfs} \
	%{subst_enable libssh} \
	%{?_enable_live_block_migration:--enable-live-block-migration} \
	%{subst_enable replication} \
	%{subst_enable rdma} \
	%{subst_enable gnutls} \
	%{subst_enable nettle} \
	%{subst_enable gcrypt} \
	%{subst_enable selinux} \
	%{subst_enable numa} \
	--enable-malloc-trim \
	%{subst_enable replication} \
	%{subst_enable lzo} \
	%{subst_enable snappy} \
	%{subst_enable bzip2} \
	%{subst_enable lzfse} \
	%{?_disable_guest_agent:--disable-guest-agent} \
	%{subst_enable tools} \
	%{subst_enable libpmem} \
	%{subst_enable blkio} \
	%{subst_enable libdaxctl} \
	%{subst_enable fuse} \
	--enable-vhdx \
	--enable-vpc \
	--enable-vmdk \
	--enable-xkbcommon \
	--disable-xen

%make_build
popd

%install
%define docdir %_docdir/%name-%version

%if_enabled user_static
pushd build-static
%makeinstall_std
# Rename all QEMU user emulators to have a -static suffix
for src in %buildroot%_bindir/qemu-*
do
  mv $src $src.static
done

for f in %buildroot%_bindir/qemu-*.static; do
    [ -f "$f" ]
    symlink="${f%%.static}-static"
    ln -sfr "$f" "$symlink"
done
popd
%endif

pushd build-dynamic
%makeinstall_std
popd
mv %buildroot%_docdir/qemu %buildroot%docdir
install -D -p -m0644 -t %buildroot%docdir README.rst COPYING COPYING.LIB LICENSE
for emu in %buildroot%_bindir/qemu-system-*; do
    ln -sf qemu.1.xz %buildroot%_man1dir/$(basename $emu).1.xz
done

%if_enabled qemu_kvm
install -m 0755 %SOURCE5 %buildroot%_bindir/qemu-kvm
ln -r -s %buildroot%_bindir/qemu-kvm %buildroot%_bindir/kvm
ln -r -s %buildroot%_bindir/qemu-kvm %buildroot%_bindir/qemu
ln -sf qemu.1.xz %buildroot%_man1dir/qemu-kvm.1.xz
%endif

rm -f %buildroot%_bindir/check-*
rm -f %buildroot%_sysconfdir/udev/rules.d/*

# Install qemu-guest-agent service and udev rules
install -D -m 0644 %SOURCE8 %buildroot%_udevrulesdir/%rulenum-%name-guest-agent.rules
install -D -m 0644 %SOURCE9 %buildroot%_unitdir/%name-guest-agent.service
install -D -m 0755 %SOURCE10 %buildroot%_initdir/%name-guest-agent
install -D -m 0644 %SOURCE11 %buildroot%_sysconfdir/sysconfig/qemu-ga
mkdir -p %buildroot%_sysconfdir/%name/fsfreeze-hook.d
install -D -m 0755 scripts/qemu-guest-agent/fsfreeze-hook %buildroot%_sysconfdir/%name/
install -D -m 0644 scripts/qemu-guest-agent/fsfreeze-hook.d/*.sample %buildroot%_sysconfdir/%name/fsfreeze-hook.d/
mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/qga-fsfreeze-hook.log

# Install qemu-pr-helper service
install -m 0644 contrib/systemd/qemu-pr-helper.service %buildroot%_unitdir/qemu-pr-helper.service
install -m 0644 contrib/systemd/qemu-pr-helper.socket %buildroot%_unitdir/qemu-pr-helper.socket
# Install rules to use the bridge helper with libvirt's virbr0
install -m 0644 %SOURCE12 %buildroot%_sysconfdir/%name

%if_enabled vnc_sasl
install -D -p -m 0644 qemu.sasl %buildroot%_sysconfdir/sasl2/%name.conf
%endif

install -m 0644 scripts/dump-guest-memory.py %buildroot%_datadir/%name

# Install simpletrace
install -m 0755 scripts/simpletrace.py %buildroot%_datadir/%name/simpletrace.py
mkdir -p %buildroot%_datadir/%name/tracetool
install -m 0644 -t %buildroot%_datadir/%name/tracetool scripts/tracetool/*.py
mkdir -p %buildroot%_datadir/%name/tracetool/backend
install -m 0644 -t %buildroot%_datadir/%name/tracetool/backend scripts/tracetool/backend/*.py
mkdir -p %buildroot%_datadir/%name/tracetool/format
install -m 0644 -t %buildroot%_datadir/%name/tracetool/format scripts/tracetool/format/*.py


# TODO: add tests subpackage
# Create new directories and put them all under tests-src
#mkdir -p %buildroot%testsdir/python
#mkdir -p %buildroot%testsdir/tests
#mkdir -p %buildroot%testsdir/tests/avocado
#mkdir -p %buildroot%testsdir/tests/qemu-iotests
#mkdir -p %buildroot%testsdir/scripts/qmp

# Install avocado_qemu tests
#cp -R tests/avocado/* %buildroot%testsdir/tests/avocado/

# Install qemu.py and qmp/ scripts required to run avocado_qemu tests
#cp -R python/qemu %buildroot%testsdir/python
#cp -R scripts/qmp/* %buildroot%testsdir/scripts/qmp
#install -p -m 0755 tests/Makefile.include %buildroot%testsdir/tests/

# Install qemu-iotests
#cp -R tests/qemu-iotests/* %buildroot%testsdir/tests/qemu-iotests/

%find_lang %name

# todo: build new openbios and SLOF
# Provided by package openbios
#rm -f %buildroot%_datadir/%name/openbios*
# Provided by package SLOF
#rm -f %buildroot%_datadir/%name/slof.bin
# Provided by package ipxe
rm -f %buildroot%_datadir/%name/pxe*rom
rm -f %buildroot%_datadir/%name/efi*rom
# Provided by package seavgabios
rm -f %buildroot%_datadir/%name/vgabios*bin
# Provided by package seabios
rm -f %buildroot%_datadir/%name/bios.bin
rm -f %buildroot%_datadir/%name/bios-256k.bin
rm -f %buildroot%_datadir/%name/bios-microvm.bin
# Provided by package qboot
rm -f %buildroot%_datadir/%name/qboot.rom
# Provided by package edk2
rm -f %buildroot%_datadir/%name/edk2-*
rm -f %buildroot%_datadir/%name/firmware/*

rm -f %buildroot%_datadir/%name/qemu-nsis.bmp
rm -rf %buildroot%_includedir
# the pxe ipxe images will be symlinks to the images on
# /usr/share/ipxe, as QEMU doesn't know how to look
# for other paths, yet.

for rom in e1000 ne2k_pci pcnet rtl8139 virtio eepro100 e1000e vmxnet3 ; do
  ln -r -s %buildroot%_datadir/ipxe/pxe-${rom}.rom %buildroot%_datadir/%name/pxe-${rom}.rom
  ln -r -s %buildroot%_datadir/ipxe.efi/efi-${rom}.rom %buildroot%_datadir/%name/efi-${rom}.rom
done

for bios in vgabios vgabios-cirrus vgabios-qxl vgabios-stdvga vgabios-vmware vgabios-virtio vgabios-ramfb vgabios-bochs-display vgabios-ati ; do
  ln -r -s %buildroot%_datadir/seavgabios/${bios}.bin %buildroot%_datadir/%name/${bios}.bin
done

ln -r -s %buildroot%_datadir/seabios/{bios,bios-256k,bios-microvm}.bin %buildroot%_datadir/%name/
ln -r -s %buildroot%_datadir/qboot/bios.bin %buildroot%_datadir/%name/qboot.rom

mkdir -p %buildroot%_binfmtdir
./scripts/qemu-binfmt-conf.sh --systemd ALL --exportdir %buildroot%_binfmtdir --qemu-path %_bindir

# Drop qemu-mipsn32*.conf -- see https://bugzilla.altlinux.org/39619
rm -rf %buildroot%_binfmtdir/*mipsn32*

for f in %buildroot%_binfmtdir/*.conf; do
    [ -f "$f" ]
    dynamic="${f%%.conf}-dynamic.conf"
    mv "$f" "$dynamic"
%if_enabled user_static
    static="${f%%.conf}-static.conf"
    sed 's/:$/.static:F/' < "$dynamic" > "$static"
%endif
done

# files list
for i in %qemu_arches hexagon; do
    find %buildroot%_bindir/qemu-$i* \
        -type f \( ! -name "*static" ! -name "*-system-*" \) |
        sed -e 's#%{buildroot}##' |
        sort -u > user-$i.list

    find %buildroot%_binfmtdir/qemu-$i* \
        -type f \( -name "*dynamic.conf" \) |
        sed -e 's#%{buildroot}##' |
        sort -u > user-binfmt-$i.list

%if_enabled user_static
    find %buildroot%_bindir/qemu-$i* \
        \( -name "*static" \) |
        sed -e 's#%{buildroot}##' |
        sort -u > user-static-$i.list

    find %buildroot%_binfmtdir/qemu-$i* \
        -type f \( -name "*static.conf" \) |
        sed -e 's#%{buildroot}##' |
        sort -u > user-static-binfmt-$i.list

%endif
done

echo "%_bindir/qemu-i386" >> user-x86.list
echo "%_bindir/qemu-i386.static" >> user-static-x86.list
echo "%_bindir/qemu-i386-static" >> user-static-x86.list

%ifnarch %ix86 x86_64
echo "%_binfmtdir/qemu-i386-dynamic.conf" >> user-binfmt-x86.list
echo "%_binfmtdir/qemu-i386-static.conf" >> user-static-binfmt-x86.list
echo "%_binfmtdir/qemu-i486-dynamic.conf" >> user-binfmt-x86.list
echo "%_binfmtdir/qemu-i486-static.conf" >> user-static-binfmt-x86.list
%endif

%check

%define archs_skip_tests ppc64le
#%%define archs_skip_tests ""

%ifarch %archs_skip_tests
exit 0
%endif

pushd build-dynamic
%make_build V=1 check
popd

%pre common
%_sbindir/groupadd -r -f %_group
%files

%files aux
%dir %_sysconfdir/%name
%dir %docdir/
%docdir/LICENSE

%files common
%dir %_datadir/%name
%_desktopdir/qemu.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/%name/keymaps
%_datadir/%name/*.rom
%_datadir/%name/vgabios*.bin
%dir %_datadir/%name/firmware
%_man1dir/%name.1*
%if_enabled vnc_sasl
%config(noreplace) %_sysconfdir/sasl2/%name.conf
%endif
%_man7dir/qemu-block-drivers.*
%_man7dir/qemu-ga-ref.*
%_man7dir/qemu-qmp-ref.*
%_man7dir/qemu-cpu-models.*

%config(noreplace) %_sysconfdir/%name/bridge.conf
%attr(4710,root,vmusers) %_libexecdir/qemu-bridge-helper

%dir %_datadir/qemu/vhost-user

%_libexecdir/virtfs-proxy-helper
%_man1dir/virtfs-proxy-helper.*

%files system -f %name.lang
%if_enabled have_kvm
%files kvm
%files kvm-core
%if_enabled qemu_kvm
%_bindir/qemu
%_bindir/qemu-kvm
%_bindir/kvm
%_man1dir/qemu-kvm.1*
%endif
%endif

%files user
%files user-binfmt
%if_enabled user_static
%files user-static
%files user-static-binfmt
%endif

%files img
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-nbd
%_man1dir/qemu-img.1*
%_man8dir/qemu-nbd.8*
%_bindir/qemu-storage-daemon
%_man1dir/qemu-storage-daemon.*
%_man7dir/qemu-storage-daemon-qmp-ref.*

%if_enabled mpath
%files -n qemu-pr-helper
%_bindir/qemu-pr-helper
%_unitdir/qemu-pr-helper.service
%_unitdir/qemu-pr-helper.socket
%_man8dir/qemu-pr-helper.*
%endif

%files tools
%_bindir/elf2dmp
%_bindir/qemu-edid
%_bindir/qemu-keymap
%_datadir/%name/dump-guest-memory.*
%_datadir/%name/simpletrace.*
%_datadir/%name/tracetool
%_datadir/%name/trace-events-all

%files tests
#%testsdir
%_libdir/%name/accel-qtest-*.so

%if_enabled opengl
%files ui-egl-headless
%_libdir/qemu/ui-egl-headless.so
%endif

%if_enabled brlapi
%files char-baum
%_libdir/qemu/chardev-baum.so
%endif

%if_enabled spice
%files char-spice
%_libdir/qemu/chardev-spice.so
%endif

%files device-display-virtio-gpu-ccw
%_libdir/qemu/hw-s390x-virtio-gpu-ccw.so

%if_enabled virglrenderer
%files device-display-vhost-user-gpu
%_libexecdir/vhost-user-gpu
%_datadir/%name/vhost-user/50-qemu-gpu.json
%endif

%files guest-agent
%_bindir/qemu-ga
%_man8dir/qemu-ga.8*
%_udevrulesdir/%rulenum-%name-guest-agent.rules
%_unitdir/%name-guest-agent.service
%_initdir/%name-guest-agent
%config(noreplace) %_sysconfdir/sysconfig/qemu-ga
%_sysconfdir/%name/fsfreeze-hook
%dir %_sysconfdir/%name/fsfreeze-hook.d
%config(noreplace) %_sysconfdir/%name/fsfreeze-hook.d/*
%ghost %_logdir/qga-fsfreeze-hook.log

%files doc
%docdir/
%exclude %docdir/LICENSE

%changelog
* Tue May 07 2024 Alexey Shabalin <shaba@altlinux.org> 8.2.3-alt1
- 8.2.3 (Fixes:  CVE-2024-3446, CVE-2024-3447, CVE-2024-3567).

* Fri May 03 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 8.2.2-alt4
- LoongArch: load UEFI via pflash (like other architectures do).

* Fri Apr 19 2024 Alexey Shabalin <shaba@altlinux.org> 8.2.2-alt3
- Revert use --disable-pie on ix86 only.

* Tue Apr 16 2024 Alexey Shabalin <shaba@altlinux.org> 8.2.2-alt2
- Revert "linux-user: Adjust brk for load_bias" (see QEMU#1913)
- use --disable-pie on ix86 only

* Mon Apr 08 2024 Alexey Shabalin <shaba@altlinux.org> 8.2.2-alt1
- 8.2.2.
- backkport patches (Fixes:  CVE-2024-26327, CVE-2024-26328).

* Mon Mar 04 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 8.2.1-alt2
- LoongArch KVM support from https://github.com/loongson/qemu.git,
  branch kvm-loongarch, commit 432f4cf89493f2a1ac144018224e7d1b4fbc31a4.
- qemu-user: fixed running 32-bit x86 binaries on hosts with a page
  size > 4KB (such as LoongArch, ppc64*)
- spec:
  + LoongArch: work around old glibc-kernheaders (thanks iv@)
  + LoongArch: pmem is not supported [yet]

* Sun Mar 03 2024 Alexey Shabalin <shaba@altlinux.org> 8.2.1-alt1
- 8.2.1.
- backkport patches (Fixes: CVE-2023-0330, CVE-2023-6683).

* Fri Dec 29 2023 Alexey Shabalin <shaba@altlinux.org> 8.2.0-alt1
- 8.2.0 (Fixes: CVE-2023-3255, CVE-2023-3019, CVE-2021-3527, CVE-2023-6693).

* Mon Dec 04 2023 Alexey Shabalin <shaba@altlinux.org> 8.1.3-alt1
- 8.1.3 (Fixes: CVE-2023-1544).
- update vitastor block driver to vitastor-v1.3.1.

* Fri Nov 03 2023 Alexey Shabalin <shaba@altlinux.org> 8.1.2-alt2
- update vitastor block driver to vitastor/hotfix-1.1.0.

* Wed Oct 18 2023 Alexey Shabalin <shaba@altlinux.org> 8.1.2-alt1
- 8.1.2 (Fixes: CVE-2023-42467).

* Wed Aug 23 2023 Alexey Shabalin <shaba@altlinux.org> 8.1.0-alt1
- 8.1.0.

* Mon Aug 21 2023 Alexey Shabalin <shaba@altlinux.org> 8.0.4-alt1
- 8.0.4 (Fixes: CVE-2023-3255, CVE-2023-3354, CVE-2023-3180).
- Backport fix oob memory read in fdp events log (Fixes: CVE-2023-4135).

* Fri Jul 28 2023 Alexey Shabalin <shaba@altlinux.org> 8.0.3-alt1
- 8.0.3 (Fixes: CVE-2023-3301, CVE-2023-2861, CVE-2023-0330)
- Disabled support glusterfs for 32-bit arches and riscv64.

* Tue May 23 2023 Alexey Shabalin <shaba@altlinux.org> 8.0.0-alt3
- Add BR: /dev/kvm for tests.

* Fri Apr 28 2023 Alexey Shabalin <shaba@altlinux.org> 8.0.0-alt2
- Build with libpmem support.
- Build with libblkio support.

* Mon Apr 24 2023 Alexey Shabalin <shaba@altlinux.org> 8.0.0-alt1
- 8.0.0 (Fixes: CVE-2022-1050, CVE-2021-20203)
- Add vitastor support (https://vitastor.io).
- Drop udev rules and control for /dev/kvm.

* Tue Jan 10 2023 Alexey Shabalin <shaba@altlinux.org> 7.2.0-alt3
- Build with enable-replication.
- Allow build with sndio.
- Build with enable-gtk-clipboard.
- Fixed run make check. Disable check for ppc64le.

* Sun Jan 08 2023 Vitaly Chikunov <vt@altlinux.org> 7.2.0-alt2
- Temporary workaround 'Could not install MSR_CORE_THREAD_COUNT handler'
  kernel bug when KVM is used on i586.

* Fri Dec 16 2022 Alexey Shabalin <shaba@altlinux.org> 7.2.0-alt1
- 7.2.0 (Fixes: CVE-2022-4144, CVE-2022-3165, CVE-2021-3638).
- Revert "Add the Kunpeng-920 CPU model."

* Mon Nov 14 2022 Alexey Shabalin <shaba@altlinux.org> 7.1.0-alt1
- 7.1.0 (Fixes: CVE-2020-14394, CVE-2022-0216).

* Sat Nov 05 2022 Ivan A. Melnikov <iv@altlinux.org> 7.0.0-alt2
- fix FTBFS: switch to libpcre2 as glib2 did
  (see also: altbug #44217)
- explicitly disable LTO for older GCC versions
- experimental build on riscv64

* Tue Jun 07 2022 Alexey Shabalin <shaba@altlinux.org> 7.0.0-alt1
- 7.0.0.
- Split out qemu-virtiofsd subpackage.
- Backport patches from upstream for fix virtio-scsi.
- Fixes for the following security vulnerabilities:
  + CVE-2021-3507 hw/block/fdc: Prevent end-of-track overrun
  + CVE-2021-4206 ui/cursor: fix integer overflow in cursor_alloc
  + CVE-2021-4207 display/qxl-render: fix race condition in qxl_cursor
  + CVE-2021-3611 hw/audio/intel-hda: Restrict DMA engine to memories
  + CVE-2022-26353 virtio-net: fix map leaking on error during receive
  + CVE-2022-26354 vhost-vsock: detach the virqueue element in case of error
  + CVE-2021-3929 hw/nvme: fix

* Thu Jun 02 2022 Alexey Shabalin <shaba@altlinux.org> 6.2.0-alt3
- Fixed /usr/bin/qemu-kvm script (ALT #42713)

* Thu Feb 24 2022 Alexey Shabalin <shaba@altlinux.org> 6.2.0-alt2
- Fixes for the following security vulnerabilities:
  + CVE-2022-0358 virtiofsd: Drop membership of all supplementary groups
  + CVE-2021-4158 acpi: validate hotplug selector on access
  + CVE-2021-3929: hw/nvme: fix
- 9pfs: Fix segfault in do_readdir_many caused by struct dirent overread

* Fri Dec 17 2021 Alexey Shabalin <shaba@altlinux.org> 6.2.0-alt1
- 6.2.0.
- Fixes for the following security vulnerabilities:
  + CVE-2021-20203 vmxnet3: validate configuration values during activate
  + CVE-2021-3947 hw/nvme: fix buffer overrun in nvme_changed_nslist
  + CVE-2021-20196 Null Pointer Failure in fdctrl_read() in hw/block/fdc.c

* Mon Nov 15 2021 Alexey Shabalin <shaba@altlinux.org> 6.1.0-alt2
- Backport patches from upstream:
  + qemu-sockets: fix unix socket path copy (again)
  + tests: tcg: Fix PVH test with binutils 2.36+
  + qxl: fix pre-save logic
  + ebpf: only include in system emulators
  + virtio-net: fix use after unmap/free for sg (Fixes: CVE-2021-3748)
  + e1000: fix tx re-entrancy problem (CVE-2021-20257)
  + Fix virtio-net-pci* "vectors" compat
  + hw/scsi/scsi-disk: MODE_PAGE_ALLS not allowed in MODE SELECT commands
    (Fixes: CVE-2021-3930)

* Thu Sep 02 2021 Alexey Shabalin <shaba@altlinux.org> 6.1.0-alt1
- 6.1.0.
- Enabled build with bpf support.
- Disabled build with nettle support.
- Added subpackages:
  + device-display-virtio-gpu-gl
  + device-display-virtio-gpu-pci-gl
  + device-display-virtio-vga-gl
  + device-display-vhost-user-gpu
  + device-usb-host
- Split out qemu-pr-helper subpackage.
- Moved qemu-storage-daemon from qemu-tools to qemu-img subpackage.
- Moved virtfs-proxy-helper, qemu-bridge-helper, virtiofsd
  from tools to common subpackage.
- Fixes for the following security vulnerabilities:
  + CVE-2021-3582
  + CVE-2021-3607
  + CVE-2021-3608
  + CVE-2021-3545
  + CVE-2021-3544
  + CVE-2021-3546
  + CVE-2021-3527
  + CVE-2021-3713

* Fri May 28 2021 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt2
- Update udev rules and control facilities.

* Tue May 04 2021 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt1
- 6.0.0
- Fixes for the following security vulnerabilities:
  + CVE-2020-17380
  + CVE-2020-25085
  + CVE-2020-35517
  + CVE-2020-29443
  + CVE-2021-3392
  + CVE-2021-3409
  + CVE-2021-3416
  + CVE-2021-20181
  + CVE-2021-20263
  + CVE-2021-20221
- Build with fuse.
- Fixed execute fsfreeze hook (ALT #37000).

* Mon Apr 12 2021 Ivan A. Melnikov <iv@altlinux.org> 5.2.0-alt5
- Move qemu-user-static text segment to 0x60000000 (ALT #39178)
- Drop qemu-aux dependency from qemu-user-static (ALT #39815)
- Drop qemu-mipsn32*.conf from binfmt config packages (ALT #39619)

* Mon Feb 01 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.2.0-alt4
- Add the Kunpeng-920 CPU model.

* Sun Jan 17 2021 Alexey Shabalin <shaba@altlinux.org> 5.2.0-alt3
- Switch bios-microvm.bin from qboot to seabios
- Package /usr/share/qemu/firmware dir
- Define firmware path as --firmwarepath for configure

* Thu Jan 14 2021 Ivan A. Melnikov <iv@altlinux.org> 5.2.0-alt2
- fix elf loading in qemu-user (altbug #39141)
- restore special CPU selection for ARM qemu-user-static

* Tue Dec 15 2020 Alexey Shabalin <shaba@altlinux.org> 5.2.0-alt1
- 5.2.0 (Fixes: CVE-2020-14364)
- Drop ivshmem-tools package
- Drop lm32 and unicore32 arches
- Add new packages:
  + qemu-audio-spice
  + qemu-char-spice
  + qemu-display-virtio-gpu-pci
  + qemu-display-virtio-vga
  + qemu-display-virtio-gpu
  + qemu-ui-spice-core
  + qemu-ui-opengl
  + qemu-ui-egl-headless

* Thu Aug 13 2020 Alexey Shabalin <shaba@altlinux.org> 5.1.0-alt1
- 5.1.0 (Fixes: CVE-2020-13253, CVE-2020-13754, CVE-2020-10761, CVE-2020-13800, CVE-2020-10717)

* Thu Apr 30 2020 Alexey Shabalin <shaba@altlinux.org> 5.0.0-alt1
- 5.0.0 (Fixes: VE-2018-12617, CVE-2020-1711)
- drop bluez support
- build emulator for RX

* Sun Apr  5 2020 Nikita Ermakov <arei@altlinux.org> 4.2.0-alt3
- Fix FP context saving in RISC-V target.

* Thu Feb 27 2020 Alexey Shabalin <shaba@altlinux.org> 4.2.0-alt2
- Arithmetic error in EDID generation fixed (boyarsh@)

* Mon Dec 16 2019 Alexey Shabalin <shaba@altlinux.org> 4.2.0-alt1
- 4.2.0

* Mon Dec 09 2019 Alexey Shabalin <shaba@altlinux.org> 4.1.1-alt1
- 4.1.1

* Fri Aug 16 2019 Alexey Shabalin <shaba@altlinux.org> 4.1.0-alt1
- 4.1.0

* Thu Aug 15 2019 Alexey Shabalin <shaba@altlinux.org> 4.0.0-alt5
- change back suffix .static for binaries in user-static package

* Sun Aug 11 2019 Alexey Shabalin <shaba@altlinux.org> 4.0.0-alt4
- change suffix from .static to -static for binaries in user-static package (ALT #37083)

* Fri Aug 09 2019 Nikita Ermakov <arei@altlinux.org> 4.0.0-alt3
- fix to handle variably sized SIOCGSTAMP with new kernels.

* Mon Jun 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.0-alt2
- qemu-kvm: fixed armh and aarch64 support.
- Added ppc* architectures support.
- Updated BR: libfdt-devel minimal version.

* Fri May 31 2019 Alexey Shabalin <shaba@altlinux.org> 4.0.0-alt1
- 4.0.0
- define md-clear CPUID bit
  (fixes: CVE-2018-12126, CVE-2018-12127, CVE-2018-12130, CVE-2019-11091)

* Fri Feb 22 2019 Alexey Shabalin <shaba@altlinux.org> 3.1.0-alt2
- disable support ceph on 32-bit arch

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 3.1.0-alt1
- 3.1.0

* Tue Dec 11 2018 Ilfat Aminov <aminov@altlinux.org> 3.0.0-alt4
- Enable OpenGL support

* Tue Nov 20 2018 Lenar Shakirov <snejok@altlinux.ru> 3.0.0-alt3
- qemu-kvm.sh fixed on i?86 systems

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt2
- disable vde support

* Wed Aug 15 2018 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Jul 11 2018 Alexey Shabalin <shaba@altlinux.ru> 2.12.0-alt2
- rebuilt against libnfs.so.12
- set arch for qemu-kvm,qemu-user-binfmt,qemu-user-static-binfmt packages

* Fri Apr 27 2018 Alexey Shabalin <shaba@altlinux.ru> 2.12.0-alt1
- 2.12.0
- use python3 for build
- generate binfmt configs with qemu-binfmt-conf.sh
- build all supported arch targets (riscv too)
- new packages:
  + qemu-audio-alsa
  + qemu-audio-oss
  + qemu-audio-pa
  + qemu-audio-sdl
  + qemu-ui-curses
  + qemu-ui-gtk
  + qemu-ui-sdl

* Fri Feb 16 2018 Alexey Shabalin <shaba@altlinux.ru> 2.11.1-alt1
- 2.11.1
- This update contains new functionality needed to enable mitigations
  for Spectre/Meltdown (CVE-2017-5715)
- fixes for potential host DoS attacks via VGA devices (CVE-2018-5683)
  and VNC clients (CVE-2017-15124)
- revert define MAX_RESERVED_VA for arm

* Wed Jan 31 2018 Alexey Shabalin <shaba@altlinux.ru> 2.11.0-alt2
- backport patch for fix configure test memfd
- add support fsfreeze-hook for qemu guest agent
- move helpers from system to tools package

* Wed Dec 20 2017 Alexey Shabalin <shaba@altlinux.ru> 2.11.0-alt1
- 2.11.0

* Thu Nov 02 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.10.1-alt3
- Enabled support of *attr syscalls in qemu-user static binaries.

* Fri Oct 13 2017 Alexey Shabalin <shaba@altlinux.ru> 2.10.1-alt2
- fixed qemu-kvm for armh and aarch64 (sbolshakov@)
- disable numa for armh (sbolshakov@)

* Tue Oct 10 2017 Alexey Shabalin <shaba@altlinux.ru> 2.10.1-alt1
- 2.10.1
- package arm flavour, with defaults to aarch64
- build without tcmalloc
- split system package to arch subpackages
- build block transports as modules and package to separated packages
- build with OpenRisc32,NIOS2,Xtensa emulator
- rename package qemu-user-binfmt_misc to qemu-user-static
- add qemu-user-binfmt and qemu-user-static-binfmt packages with configs in /lib/binfmt.d

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 2.10.0-alt1
- 2.10.0
- build with SDL2

* Wed Jun 28 2017 Yuri N. Sedunov <aris@altlinux.org> 2.9.0-alt1.1
- rebuild against libnfs.so.11

* Fri Apr 21 2017 Alexey Shabalin <shaba@altlinux.ru> 2.9.0-alt1
- 2.9.0

* Wed Dec 21 2016 Alexey Shabalin <shaba@altlinux.ru> 2.8.0-alt1
- 2.8.0
- enable xen support

* Sat Oct 01 2016 Alexey Shabalin <shaba@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Tue Sep 06 2016 Alexey Shabalin <shaba@altlinux.ru> 2.6.1-alt1
- 2.6.1
- fixed CVE-2016-4439,CVE-2016-4441,CVE-2016-4952

* Fri May 13 2016 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0
- fixed CVE-2015-8558,CVE-2015-8619,CVE-2016-1981,CVE-2016-3710,CVE-2016-3712
- move virtfs-proxy-helper and qemu-bridge-helper to from qemu-img to qemu-system
- ignore test failures for check
- add vhost-net manage to control
- disable xen support

* Tue Apr 12 2016 Denis Medvedev <nbr@altlinux.org> 2.5.0-alt2
- Fixed linking.

* Fri Dec 18 2015 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0
- add tilegx arch
- build with jemalloc support
- libcacard is now a standalone project
- build with virgl support
- build with seccomp support
- add ivshmem-tools package
- add qemu-guest-agent sysv script

* Thu Nov 05 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Fri Oct 02 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0.1-alt1
- 2.4.0.1
- build without gtk3 ui

* Thu Jun 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt5
- Fixes a crash during image compression (RH#1214855)

* Wed Jun 24 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt4
- add requires edk2-ovmf

* Mon Jun 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt3
- add aarch64-softmmu to target_list_system
- fixed CVE-2015-4037, CVE-2015-3209

* Thu May 14 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt2
- fixed CVE-2015-3456

* Tue Apr 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0
- build with ceph, xfsctl, libnfs, glusterfs support

* Tue Dec 16 2014 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Sep 30 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Thu Sep 11 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Mon Aug 04 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt2
- fixed migration from older versions (ALT#30033)
- fixed build on arm

* Fri Apr 18 2014 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0
- build aarch64-linux-user
- enable support libusb (ALT#29981)
- add condition for libnfs, but disable (need libnfs package)
- enable quorum support
- enable xen support
- enable lzo and snappy support
- enable build with cris,microblaze,sh4 build
- add binfmt config

* Tue Dec 10 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt3
- rebuild with new libiscsi

* Mon Dec 02 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt2
- fixed %%post and %%preun common package

* Thu Nov 28 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Fri Oct 11 2013 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1 (fixed CVE-2013-4344)
- drop qemu-kvm service

* Fri Aug 16 2013 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0
- build with rdma support

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt2
- switch from vgabios to seavgabios

* Mon Jul 29 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2
- fixed CVE-2013-2231

* Thu Jul 04 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Tue May 21 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- build with libssh2
- build with tpm
- build with gtk3 ui

* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Apr 16 2013 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1.1
- Fix test (FC patch)

* Mon Feb 18 2013 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Dec 24 2012 Ivan Ovcherenko <asdus@altlinux.org> 1.2.0-alt3
- Rebuild with Flattened Device Tree support.

* Fri Nov 02 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt2
- Introduced -aux subpackage, updated interpackage dependencies.

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.1
- Rebuilt with libpng15

* Mon Sep 10 2012 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Aug 30 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt5
- Use upstreamed version of the getdents emulation fix,
  to ease further merges.

* Fri Aug 17 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt4
- Fixed emulation of getdents.

* Thu Aug 09 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt3
- binfmt_misc: package two arm flavours, with defaults to armv5 and armv7

* Wed Jul 25 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt2
- reverted make check

* Fri Jul 20 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- git snapshot of stable-1.1 branch (b7093f294c330c4db789c077dac9d8611e4f8ee0)
- add systemd unit files
- split qemu-guest agent package

* Mon Mar 05 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.1-alt2
- change arm defaults to convenient values

* Thu Mar 01 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1
- enable libiscsi support

* Fri Dec 02 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0
- add usb-redir support
- enable spice for i686
- enable compile alpha

* Thu Oct 13 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1
- 0.15.1

* Thu Aug 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.0-alt1
- 0.15.0
- disable compile alpha
- enable compile s390x, lm32, unicore32
- enable smartcard support
- enable compile guest agent

* Mon May 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt4
- enable pulseaudio support

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt3
- enable SDL support
- disable pulseaudio support

* Fri Feb 25 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt2
- add udev rules,control rules, init script for load kvm kernel module (import from qemu-kvm package)
- drop alternatives for qemu-img
- add doc subpackage
- move man and locales to common subpackage
- use roms and bioses from another packages: vgabios,seabios,gpxe-roms-qemu
- disable SDL support

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0 release

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt0.rc0
- 0.14.0-rc0

* Wed Jan 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.13.50-alt1
- snapshot 5677903453
- add alternatives for qemu-system-%ix86
- add img subpackage, add alternatives for qemu-img and other
- cleanup attr
- add spice support for x86_64 only
- add libalsa-devel to buildreq for alsa support
- add vnc-jpeg and vnc-png support
- add adlib and hda soundcards
- build without esound support
- add libpci-devel to buildreq
- fix bluez buildreq
- drop non devel library from buildreq
- install config for sasl
- fix install /etc/qemu/*.conf
- qemu-common package as noarch

* Thu Jan 14 2010 Kirill A. Shutemov <kas@altlinux.org> 0.12.1-alt1
- v0.12.1-31-g49a3aaa
- Fix NULL pointer dereference on handling -chardev socket

* Mon Dec 14 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.92-alt1
- v0.12.0-rc2-3-g910628f
- UUID support enabled

* Sat Sep 19 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt6
- Fix building binfmt_misc binaries

* Sat Sep 19 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt5
- v0.11.0-rc0-867-gdbf9580
- Do not set uname for linux-user targets
- Use %%check section for tests

* Tue Sep 08 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt4
- v0.11.0-rc0-799-g2637c75
- Compile alpha, m68k, mips and sparc support by default
- Enable Linux AIO
- Enalbe unit tests
- Review configure options
- Update URL
- Update PIE patches

* Tue Sep 01 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt3
- Disable IO thread to fix KVM support

* Tue Sep 01 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt2
- fix building on x86_64

* Fri Aug 21 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt1
- updated to v0.11.0-rc0-564-g757506d
  + no KQEMU support any more
  + fixes CVE-2008-0928 (ALT #20010)
  + keyboard works fine without -k (ALT #15774)
  + framebuffer works fine with -kernel (ALT #11324)
- build linux-user targets as PIE and drop link hack
- enable KVM support
- enable curl support
- enable IO thread
- enable VNC SASL support
- enable bluez support

* Thu Feb 19 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt11
- svn 20090219
- add hack to implement CLONE_CHILD_CLEARTID
- enable more audio drivers and cards
- enable curses support
- enable vde support
- enable VNC TLS support

* Sun Dec 14 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt10
- svn 20081214
  + no need in gcc3 any more
- fixes for mmap() related code

* Mon Oct 13 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt9
- svn 20081013
- fix mmap(), mremap() and shmat() syscalls on 64-bit host with
  32-bit targets

* Fri Oct 10 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt8
- rename binaries in package qemu-user-binfmt_misc back to *.static
  to make them compatible with hasher

* Fri Oct 10 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt7
- svn 20081010
  + some changes merged to upstream
- enable/disable binfmt_misc support at compile time
- fix and cleanup system v ipc syscalls
- fix getdents* syscalls
- fix fstatat64()/newfstatat() syscalls
- implement readahead() syscall
- revert some legacy changes

* Sun Sep 14 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt6
- Fix building with glibc-kernheaders-2.6.27-alt1

* Mon Sep 08 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt5
- svn 20080908
- Implement futimesat() syscall
- binfmt-misc-friendly:
  + Use auxv to find out binary file descriptor
- ioctl:
  + Implement ioctls MTIOCTOP, MTIOCGET and MTIOCPOS

* Sun Aug 31 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt4
- 0.9.1 + svn 20080831
- Add option -binfmt-misc-friendly to user emulators

* Fri Aug 29 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt3
- fix building on i586
- implement fstatat64() syscall

* Sat Aug 23 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt2
- 0.9.1 + svn 20080829
  + CVE-2008-2004
  + Brand new "Tiny Code Generator" by Fabrice Bellard
  + A lot of changes
- Review all changes and patches cleanup
- fix vfork(2) implementation
- Build only x86, arm and ppc architectures by default

* Tue Jan 29 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt1.cvs20080127
- 0.9.1 + cvs 20080127
- fix-syscalls--iovec
  + do not stop iovec conversion on iov_base == NULL if iov_len is 0
- fix-signals
  + do not show message on uncaught target signal

* Sun Nov 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20071124-alt15
- cvs 20071124
- fix-syscalls--getgroups:
  + getgroups: return total number of supplementary group IDs for the
    process if size == 0

* Sat Nov 24 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20071123-alt14
- cvs 20071123
- fix-cpu-copy:
  + Handle cpu_model in copy_cpu()

* Mon Nov 19 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20071119-alt13
- cvs 20071119
- Branch based git repo
- Fix execve syscall
- Build all targets
- adlib: include missed header
- Cleanup configure options
- Drop obsoleted/unsupported patches:
  + qemu-0.6.2-alt-hdtrans.patch
  + qemu-0.7.0-sigaltstackhack.patch
  + qemu-0.9.0-alt-alpha_syscall_nr.patch
  + qemu-0.9.0-alt-arm_syscall_nr.patch
  + qemu-0.9.0-alt-i386_syscall_nr.patch
  + qemu-0.9.0-alt-m68k_syscall_nr.patch
  + qemu-0.9.0-alt-ppc64_syscall_nr.patch
  + qemu-0.9.0-alt-ppc_syscall_nr.patch
  + qemu-0.9.0-alt-qvm86.patch
  + qemu-0.9.0-alt-sh4_syscall_nr.patch
  + qemu-0.9.0-alt-sparc64_syscall_nr.patch
  + qemu-0.9.0-alt-sparc_syscall_nr.patch
  + qemu-0.9.0-alt-syscall_cleanup.patch
  + qemu-0.9.0-disk-scsi.patch
  + qemu-0.9.0-vmware_vga-fix.patch

* Thu Oct 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070917-alt12
- cvs 20070917
- Added qemu-0.9.0-alt-shm.patch
  + Add shm* syscalls
- Sync patches with new version
- Update qemu-0.9.0-security.patch
  + part of fix is in the upsteam
- qemu-0.9.0-alt-alpha_syscall_nr.patch, qemu-0.9.0-alt-ppc64_syscall_nr.patch
  + sync syscall numbers with kernel
- Drop qemu-0.9.0-alt-statfs.patch
  + fixed in upstream

* Fri Aug 24 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070607-alt11
- qemu-arm: uname -m => armv4l/armv4b
- fix path(): return NULL if NULL passed

* Fri Jun 08 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070607-alt10
- cvs 20070607
- qemu-0.8.2-nptl.patch -> qemu-0.9.0-nptl.patch, qemu-0.9.0-disk-scsi.patch:
  + rejection fix
- Drop qemu-0.9.0-alt-mips_syscall_nr.patch
  + in the upstream now
- Update qemu-0.9.0-alt-sem.patch and qemu-0.9.0-alt-sem.patch
  + part of this patches is in the upstream now

* Mon May 21 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070420-alt9
- Added qemu-0.9.0-alt-getgroups.patch
  + trivial fix
- Moved qemu-0.9.0-sem.patch -> qemu-0.9.0-alt-sem.patch:
  + Fix do_semctl
  + Added standalone syscalls semget, semop, semctl
- Moved qemu-0.9.0-msgop.patch -> qemu-0.9.0-alt-sem.patch
  + Added standalone syscalls msg*
- Dropped qemu-0.9.0-efault.patch

* Tue Apr 03 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070420-alt8
- cvs 20070420
- Added qemu-0.9.0-security.patch:
  + CVE-2007-1320, CVE-2007-1321, CVE-2007-1322, CVE-2007-1323, CVE-2007-1366
- Added qemu-0.9.0-sb16-fix.patch:
  + Fix infinite loop in the SB16 driver
- Disable building alpha emulation due build error
- Update qemu-0.8.2-nptl.patch
  + Fix cpu_env list corruption by disabling CLONE_VM when doing CLONE_VFORK.
    This is a hack to avoid segfault on vfork.
- Added qemu-0.9.0-nptl-update.patch:
  + implemented/fixed several nptl-related syscalls
  + Fix build on i586
- Added qemu-0.9.0-vmware_vga-fix.patch:
  + Disable -vmwarevga acceleration code for now (missing range checks)
- Fix bug #11363
  + rename qemu to qemu-system-i386
  + add symlink qemu to qemu-system-%%_target_os
- Added qemu-0.8.2-deb-tls-ld.patch
  + Fix segfault of user mode qemu on ix86
- Updated qemu-0.9.0-alt-path.patch
  + content of emulation dir can change
  + some refactoring
- Added qemu-0.9.0-alt-arm-eabi-pread-pwrite.patch:
  + pread and pwrite syscall fix for ARM EABI guest
- Added qemu-0.9.0-alt-statfs.patch
  + fix statfs syscall bug
- Updated qemu-0.9.0-alt-i386-user-fix.patch
  + fix qemu-i386 on x86 host
- Update qemu-0.8.2-alt-qvm86.patch -> qemu-0.9.0-alt-qvm86.patch:
  + rejection fexed
- Updated qemu-0.9.0-disk-scsi.patch
  + rejection fixed
- Update qemu-0.9.0-alt-syscall_cleanup.patch:
  + rejection fixed

* Sun Mar 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070324-alt7
- cvs 20070324
- Sync syscall numbers with linux-2.6.21-rc4
- Update linux-user/syscall.c:
  + build fix
  + cleaup
- Dropped Debian's patches
- Added qemu-0.9.0-alt-i386-user-fix.patch:
  + fix SIGSEGV in qemu-i386 (by Sergey Vlasov aka vsu@)
- Added qemu-0.9.0-efault.patch:
  + fix returning EFAULT from syscalls
- Added qemu-0.9.0-msgop.patch:
  + fix msg* syscalls
- Added qemu-0.9.0-sem.patch:
  + fix sem* syscalls
- Dropped qemu-0.9.0-alt-fcntl64-fix.patch:
  + in upstream now

* Tue Mar 20 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070320-alt6
- cvs 20070320
- Dropped 43_arm_cpustate.patch,
  qemu-0.9.0-alt-syscall-getsockname-fix.patch,
  qemu-0.9.0-alt-syscalls-clock.patch,
  qemu-0.9.0-alt-syscalls-recv-and-recvfrom-fix.patch:
  + fixed in upstream now
- Updated qemu-0.9.0-alt-makefile.patch, qemu-0.9.0-disk-scsi.patch:
  + fix rejections
- Updated qemu-0.9.0-alt-fcntl64-fix.patch:
  + pass host flag to fcntl instead target flag
- Renamed qemu-0.8.2-alt-path.patch -> qemu-0.9.0-alt-path.patch
- Updated qemu-0.9.0-alt-path.patch:
  + fix memory leak by caching
- Spec cleap

* Fri Mar 09 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070304-alt5
- fix fcntl64 syscal: used TARGET_F_*64 instead F_*64
- cdrom name fixed
- option -disk scsi,type=cdrom fixed (bug #11010)

* Sun Mar 04 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070304-alt4
- cvs snapshot
- fix order of ide devices(bug #11004)
- drop mdk patches
- user gcc 3.4 for building(bug #11006)
- fix sigfault
- spec cleanup

* Thu Mar 01 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt3
- cdrom option fixed(bug #10971)
- syscall clock_gettime rewritten
- syscall clock_getres added
- syscalls getsockname, recv and recvfrom fixed

* Wed Feb 28 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt2
- scsi disk support added

* Thu Feb 15 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt1
- lock_user_string used for mount syscall

* Wed Feb 07 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt0.3
- requires fixed
- docs is in package qemu-common now
- description and summary fixed
- alsa enabled
- spec cleanup

* Wed Feb 07 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt0.2
- mandriva patches updated
- fix realpath() crash again (by vsu@)

* Tue Feb 06 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt0.1
- 0.9.0
- separate into four packages: qemu, softmmu, user, user-static
- spec cleanup
- patches updated

* Mon Feb 05 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.8.2-alt1.2
- fix crash with -fstack-protector due to wrong realpath() usage
- patches reorganized, debian patches added
- qemu-0.8.2-alt-path.patch fixed
- qemu-arm: uname -m => armv5l/armv5b
- qemu-0.8.2-alt-mmap.patch added
- support msg* and sem* syscalls
- name for static version: qemu-<arch>.static

* Thu Dec 14 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.8.2-alt1.1
- build static version of qemu-arm
- patches for qemu-arm and other linux mode emulators

* Wed Aug 23 2006 Alexey Tourbin <at@altlinux.ru> 0.8.2-alt1
- 0.8.0 -> 0.8.2
- sync madriva patches 0.8.2-1mdv2007.0
- removed kernel-source-kqemu from here, which should be packaged
  separately because of its non-free status
- added support for /dev/qvm86

* Wed Dec 21 2005 Kachalov Anton <mouse@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Tue Sep 20 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.2-alt1
- 0.7.2
- Updated Kqemu to 0.7.2

* Thu Aug 04 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.1-alt1
- 0.7.1
- Updated:
  * Kqemu to 0.7.1-1
  * GTK support

* Thu Jun 23 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt2
- Added:
  * GTK support (-use-gtk option)
  * Distribution permission from Fabrice Bellard to Kqemu

* Fri Apr 29 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt1
- 0.7.0
- Kqemu support

* Mon Nov 29 2004 Kachalov Anton <mouse@altlinux.ru> 0.6.2-alt1
- Snapshot of 23-28 Nov 2004
- LARGE disk fix (actual for NT4, win2k, winXP)

* Fri Nov 26 2004 Kachalov Anton <mouse@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Sun Oct 17 2004 Alexey Tourbin <at@altlinux.ru> 0.6.0-alt1
- initial revision
