%define _unpackaged_files_terminate_build 1
%define _localstatedir /var

Name: sanlock
Version: 3.9.2
Release: alt1
Summary: A shared storage lock manager

Group: System/Configuration/Other
License: GPLv2 and GPLv2+ and LGPLv2+
Url: https://pagure.io/sanlock

Source: %name-%version.tar
Patch1: %name-%version-%release.patch

Requires: lib%name = %version-%release

BuildRequires(pre): rpm-build-python3
BuildRequires: libblkid-devel libuuid-devel libaio-devel
BuildRequires: python3-devel python3(setuptools)

%description
The sanlock daemon manages leases for applications running on a cluster
of hosts with shared storage.

%package -n lib%name
Summary: A shared disk lock manager library
Group: System/Libraries

%description -n lib%name
The %name-lib package contains the runtime libraries for sanlock,
a shared storage lock manager.
Hosts connected to a common SAN can use this to synchronize their
access to the shared disks.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n python3-module-%name
Summary: Python bindings for the sanlock library
Group: Development/Python3

%description -n python3-module-%name
The %name-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the sanlock library.

%package -n fence-sanlock
Summary: Fence agent using sanlock and wdmd
Group: System/Configuration/Other
Requires: %name = %version-%release

%description -n fence-sanlock
The fence-sanlock package contains the fence agent and
daemon for using sanlock and wdmd as a cluster fence agent.

%package -n sanlk-reset
Summary: Host reset daemon and client using sanlock
Group: System/Configuration/Other
Requires: %name = %version-%release

%description -n sanlk-reset
The sanlk-reset package contains the reset daemon and client.
A cooperating host running the daemon can be reset by a host
running the client, so long as both maintain access to a
common sanlock lockspace.

%prep
%setup
%patch1 -p1

%build
# upstream does not require configure
# upstream does not support _smp_mflags
CFLAGS=$RPM_OPT_FLAGS make -C wdmd
CFLAGS=$RPM_OPT_FLAGS make -C src
CFLAGS=$RPM_OPT_FLAGS make -C python
CFLAGS=$RPM_OPT_FLAGS make -C fence_sanlock
CFLAGS=$RPM_OPT_FLAGS make -C reset

%install
make -C src \
        install LIBDIR=%_libdir \
        DESTDIR=%buildroot
make -C wdmd \
        install LIBDIR=%_libdir \
        DESTDIR=%buildroot
make -C python \
        install LIBDIR=%_libdir \
        DESTDIR=%buildroot
make -C fence_sanlock \
        install LIBDIR=%_libdir \
        DESTDIR=%buildroot
make -C reset \
        install LIBDIR=%_libdir \
        DESTDIR=%buildroot

install -D -m 0644 init.d/sanlock.service.native %buildroot%_unitdir/sanlock.service
install -D -m 0644 init.d/sanlock.tmpfile %buildroot%_tmpfilesdir/sanlock.conf
install -D -m 0755 init.d/sanlock %buildroot%_initddir/sanlock
install -D -m 0644 init.d/wdmd.service %buildroot%_unitdir/wdmd.service
install -D -m 0644 init.d/wdmd.tmpfile %buildroot%_tmpfilesdir/wdmd.conf
install -D -m 0644 init.d/wdmd.module %buildroot%_modulesloaddir/wdmd.conf
install -D -m 0755 init.d/wdmd %buildroot%_initddir/wdmd
install -D -m 0755 init.d/systemd-wdmd %buildroot/lib/systemd/systemd-wdmd
install -D -m 0644 init.d/fence_sanlockd.service %buildroot%_unitdir/fence_sanlockd.service
install -D -m 0644 init.d/fence_sanlockd.tmpfile %buildroot%_tmpfilesdir/fence_sanlockd.conf
install -D -m 0755 init.d/fence_sanlockd %buildroot%_initddir/fence_sanlockd
install -D -m 0644 init.d/sanlk-resetd.service %buildroot%_unitdir/sanlk-resetd.service
install -D -m 0755 init.d/sanlk-resetd %buildroot%_initddir/sanlk-resetd

install -D -m 0644 src/logrotate.sanlock \
        %buildroot/etc/logrotate.d/sanlock

install -D -m 0644 init.d/sanlock.sysconfig \
        %buildroot/etc/sysconfig/sanlock

install -D -m 0644 init.d/wdmd.sysconfig \
        %buildroot/etc/sysconfig/wdmd

install -Dd -m 0755 %buildroot/etc/wdmd.d

%pre
groupadd -r -f %name >/dev/null 2>&1 ||:
useradd -r -d -M /run/%name -s /bin/false -c "sanlock user" -g %name -G disk %name >/dev/null 2>&1 ||:

%post
%post_service wdmd
%post_service sanlock

%preun
%preun_service wdmd
%preun_service sanlock

%post -n fence-sanlock
%post_service fence_sanlockd

%preun -n fence-sanlock
%preun_service fence_sanlockd

%post -n sanlk-reset
%post_service sanlk-resetd

%preun -n sanlk-reset
%preun_service sanlk-resetd

%files
%_unitdir/sanlock.service
%_tmpfilesdir/sanlock.conf
%_unitdir/wdmd.service
/lib/systemd/systemd-wdmd
%_tmpfilesdir/wdmd.conf
%_modulesloaddir/wdmd.conf
%_initddir/sanlock
%_initddir/wdmd
%_sbindir/sanlock
%_sbindir/wdmd
%dir /etc/wdmd.d
%_man8dir/wdmd*
%_man8dir/sanlock*
%config(noreplace) %_sysconfdir/logrotate.d/sanlock
%config(noreplace) %_sysconfdir/sysconfig/sanlock
%config(noreplace) %_sysconfdir/sysconfig/wdmd

%files -n lib%name
%_libdir/libsanlock.so.*
%_libdir/libsanlock_client.so.*
%_libdir/libwdmd.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n python3-module-%name
%python3_sitelibdir/*

%files -n fence-sanlock
%_unitdir/fence_sanlockd.service
%_tmpfilesdir/fence_sanlockd.conf
%_initddir/fence_sanlockd
%_sbindir/fence_sanlock
%_sbindir/fence_sanlockd
%_man8dir/fence_sanlock*

%files -n sanlk-reset
%_sbindir/sanlk-reset
%_sbindir/sanlk-resetd
%_initddir/sanlk-resetd
%_unitdir/sanlk-resetd.service
%_man8dir/sanlk-reset*

%changelog
* Fri May 03 2024 Alexey Shabalin <shaba@altlinux.org> 3.9.2-alt1
- 3.9.2

* Mon Jan 15 2024 Alexey Shabalin <shaba@altlinux.org> 3.9.0-alt1
- 3.9.0

* Fri Nov 03 2023 Alexey Shabalin <shaba@altlinux.org> 3.8.5-alt2
- Fixed wdmd.service unit
- Not package dir in /run because is a tmpfs

* Thu Nov 03 2022 Alexey Shabalin <shaba@altlinux.org> 3.8.5-alt1
- 3.8.5

* Mon Aug 23 2021 Alexey Shabalin <shaba@altlinux.org> 3.8.4-alt1
- 3.8.4

* Wed Nov 25 2020 Alexey Shabalin <shaba@altlinux.org> 3.8.2-alt1
- 3.8.2

* Sat May 16 2020 Alexey Shabalin <shaba@altlinux.org> 3.8.1-alt1
- 3.8.1

* Sun Mar 08 2020 Alexey Shabalin <shaba@altlinux.org> 3.8.0-alt2
- package native systemd units

* Thu Jul 11 2019 Alexey Shabalin <shaba@altlinux.org> 3.8.0-alt1
- 3.8.0
- switch to python3

* Fri Apr 26 2019 Alexey Shabalin <shaba@altlinux.org> 3.7.1-alt1
- 3.7.1

* Wed Apr 03 2019 Alexey Shabalin <shaba@altlinux.org> 3.7.0-alt1
- 3.7.0

* Tue Jan 09 2018 Alexey Shabalin <shaba@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Fri Jun 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Tue Jun 30 2015 Alexey Shabalin <shaba@altlinux.ru> 3.2.4-alt1
- 3.2.4

* Wed Sep 24 2014 Alexey Shabalin <shaba@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Fri Jan 31 2014 Alexey Shabalin <shaba@altlinux.ru> 3.1.0-alt1
- initial build
