Name:    SDL2_pango
Version: 2.1.5
Release: alt2

Summary: SDL2 port of SDL_Pango

License: LGPL-2.1
Group:   System/Libraries
Url:     https://github.com/markuskimius/SDL2_Pango

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar

BuildRequires: libSDL2-devel
BuildRequires: libpango-devel

%description
SDL2_Pango is a library for graphically rendering
internationalized and tagged text in SDL2 using TrueType fonts.

%package -n lib%name
Summary: SDL2 port of SDL_Pango
Group: System/Libraries

%description -n lib%name
SDL2_Pango is a library for graphically rendering
internationalized and tagged text in SDL2 using TrueType fonts.

%package -n lib%name-devel
Summary: Development files for SDL2_pango
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files for SDL2_pango.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files -n lib%name
%doc COPYING AUTHORS ChangeLog NEWS README
%_libdir/*.so.4*

%files -n lib%name-devel
%doc docs/html/*
%_includedir/SDL2_Pango.h
%_libdir/pkgconfig/SDL2_Pango.pc
%_libdir/*.so

%changelog
* Thu Apr 04 2024 Grigory Ustinov <grenka@altlinux.org> 2.1.5-alt2
- Renamed package to be similar with others.

* Tue Apr 02 2024 Grigory Ustinov <grenka@altlinux.org> 2.1.5-alt1
- Initial build for Sisyphus.
