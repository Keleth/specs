%define soname 1

Name: roct-thunk-interface
Version: 6.0.0
Release: alt0.2
License: MIT
Summary: AMD user-mode API interfaces used to interact with the ROCk driver
Url: https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface
Group: System/Libraries

Source: %name-%version.tar
Patch: libhsakmt-add-extra-symbols.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libnuma-devel libdrm-devel

%description
User-mode API interfaces used to interact with the ROCk driver.

%package -n libhsakmt%{soname}
Summary: Thunk libraries for AMD KFD
Group: System/Libraries
Provides: hsakmt-roct = %EVR

%description -n libhsakmt%{soname}
This package includes the libhsakmt (Thunk) libraries for AMD KFD.

%package -n hsakmt-rocm-devel
Summary: Development headers for AMD KFD thunk libraries
Group: Development/C

%description -n hsakmt-rocm-devel
Development headers for AMD KFD thunk libraries.

%prep
%setup
%patch -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=on
%cmake_build

%install
%cmake_install

%files -n libhsakmt%{soname}
%doc README.md LICENSE.md
%_libdir/libhsakmt.so.%{soname}*

%files -n hsakmt-rocm-devel
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/cmake/hsakmt
%_libdir/libhsakmt.so

%changelog
* Sun Dec 24 2023 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.2
- Update extra-symbols.patch (add hsaKmtGetAMDGPUDeviceHandle).

* Sat Dec 23 2023 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.1
- rocm-6.0.0.

* Mon Nov 06 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.1-alt0.1
- rocm-5.7.1.

* Wed Sep 20 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.0-alt0.2
- Add missing symbols used by -runtime library.

* Tue Sep 19 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.0-alt0.1
- rocm-5.7.0.

* Wed Aug 30 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.1-alt0.1
- rocm-5.6.1 (no code change, just version bump).

* Mon Jul 03 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.1
- rocm-5.6.0.

* Sun May 28 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.1
- rocm-5.5.1.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.
