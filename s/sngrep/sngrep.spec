Name: sngrep
Version: 1.8.1
Release: alt1

Summary: sngrep is a tool for displaying SIP calls message flows from terminal

License: GPLv2+
Group: Networking/Other
Url: https://github.com/irontec/sngrep

Source: %name-%version.tar

Patch0: %name-%version-alt.patch

BuildRequires: libncurses-devel libpcap libgnutls-devel libpcap-devel libpcre2-devel libgcrypt-devel libncursesw-devel libssl-devel

%description
sngrep is a tool for displaying SIP calls message flows from terminal.
It supports live capture to display realtime SIP packets and can also be used
as PCAP viewer.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure \
           --enable-eep \
           --with-pcre2 \
           --with-openssl \
           --enable-unicode \
           --enable-ipv6 \

%make_build

%install
%makeinstall_std

%files
%_sysconfdir/sngreprc
%_bindir/sngrep
%_man8dir/sngrep.8*

%changelog
* Tue Apr 09 2024 Ilya Demyanov <turbid@altlinux.org> 1.8.1-alt1
- new upstream version

* Thu Dec 21 2023 Ilya Demyanov <turbid@altlinux.org> 1.8.0-alt1
- new upstream version

* Wed Apr 05 2023 Ilya Demyanov <turbid@altlinux.org> 1.7.0-alt1
- new upstream version

* Fri Jan 27 2023 Ilya Demyanov <turbid@altlinux.org> 1.6.0-alt1
- new upstream version
- migrate to pcre2

* Fri Aug 28 2020 Bolshedvorsky Evgeny <jenya@altlinux.org> 1.4.7-alt1
- added support for ipv6,unicode

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt2
- NMU: remove %ubt from release

* Wed Apr 12 2017 Evgeny Bolshedvorsky <jenya@altlinux.org> 1.4.2-alt1%ubt
- added ubt

* Mon Apr 10 2017 Evgeny Bolshedvorsky <jenya@altlinux.org> 1.4.2-alt1
- initial build
