%define git %nil

Name: ell
Version: 0.64
Release: alt1
Summary: Embedded Linux library
Group: System/Libraries
License: LGPLv2+
Url: https://01.org/ell
Source0: https://www.kernel.org/pub/linux/libs/%name/%name-%version.tar
Patch: %name-%version-%release.patch

%description
The Embedded Linux* Library (ELL) provides core, low-level functionality for
system daemons. It typically has no dependencies other than the Linux kernel, C
standard library, and libdl (for dynamic linking). While ELL is designed to be
efficient and compact enough for use on embedded Linux platforms, it is not
limited to resource-constrained systems.

%package -n lib%name
Summary: Embedded Linux library
Group: System/Libraries

%description -n lib%name
The Embedded Linux* Library (ELL) provides core, low-level functionality for
system daemons. It typically has no dependencies other than the Linux kernel, C
standard library, and libdl (for dynamic linking). While ELL is designed to be
efficient and compact enough for use on embedded Linux platforms, it is not
limited to resource-constrained systems.

%package -n lib%name-devel
Summary: Embedded Linux library development files
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Headers for developing against libell.

%prep
%setup

%build
%autoreconf
%configure
%make_build V=1

%install
%set_verify_elf_method unresolved=relaxed
%makeinstall

%files -n lib%name
%_libdir/libell.so.*
%doc AUTHORS README TODO ChangeLog COPYING

%files -n lib%name-devel
%_includedir/ell
%_libdir/libell.so
%_pkgconfigdir/ell.pc

%changelog
* Sat Apr 06 2024 L.A. Kostis <lakostis@altlinux.ru> 0.64-alt1
- 0.64.

* Thu Oct 26 2023 L.A. Kostis <lakostis@altlinux.ru> 0.59-alt1
- 0.59.

* Mon Jul 31 2023 L.A. Kostis <lakostis@altlinux.ru> 0.57-alt1
- 0.57.

* Fri Oct 21 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.53-alt1.1
- removed patch for Elbrus (no longer needed)

* Wed Oct 19 2022 L.A. Kostis <lakostis@altlinux.ru> 0.53-alt1
- 0.53.

* Sat Oct 30 2021 L.A. Kostis <lakostis@altlinux.ru> 0.44-alt1
- 0.44.

* Wed Jul 14 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.40-alt2
- added patch with workarounds for Elbrus compiler

* Fri Jun 11 2021 L.A. Kostis <lakostis@altlinux.ru> 0.40-alt1
- 0.40.

* Wed Aug 05 2020 L.A. Kostis <lakostis@altlinux.ru> 0.32-alt1
- 0.32.

* Sun Mar 15 2020 L.A. Kostis <lakostis@altlinux.ru> 0.28-alt1
- 0.28.

* Sat Mar 31 2018 L.A. Kostis <lakostis@altlinux.ru> 0.4-alt1.g1b8e643
- rebuild for ALTLinux.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 26 2017 Lubomir Rintel <lkundrak@v3.sk> - 0.2-2
- Renamed to libell to fix a naming conflict
- Addressed review issues (Igor Gnatenko, #1505237):
- Added BR gcc
- Made build verbose
- Moved pkgconfig file to devel subpackage
- Fixed license tag
- Dropped Group tag
- Packaged changelog

* Sun Oct 22 2017 Lubomir Rintel <lkundrak@v3.sk> - 0.2-1
- Initial packaging
