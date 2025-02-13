Name:    kiosk-mate-profiles
Version: 0.8
Release: alt1

Summary: profiles for mate desktop for kiosk mode
License: MIT
Group:   Other
Url:     https://git.altlinux.org/people/nbr/packages/kiosk-mate-profiles.git

Packager: "Denis Medvedev" <nbr@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

%description
A set of profiles for mate desktop for kiosk locking of desktop.

%prep
%setup

%install
mkdir -p %buildroot/%_sysconfdir/kiosk/profiles
install -Dm 0644 profiles/*  %buildroot/%_sysconfdir/kiosk/profiles

%files
%doc README
%_sysconfdir/kiosk/profiles/*

%changelog
* Fri Apr 26 2024 "Denis Medvedev" <nbr@altlinux.org> 0.8-alt1
Initial release
