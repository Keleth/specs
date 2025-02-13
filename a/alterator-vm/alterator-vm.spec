Name: alterator-vm
Version: 0.4.41
Release: alt1

Summary: Alterator module for volume management
License: GPL
Group: System/Configuration/Other

Source0: %name.tar

BuildRequires: alterator >= 5.0 guile-devel >= 2.0 guile-evms >= 0.5

Requires: alterator >= 4.10-alt6
Requires: alterator-l10n >= 2.2-alt1
Requires: guile-evms >= 0.5-alt1
Conflicts: alterator-lookout < 1.5-alt1

%description
Alterator module for volume management

%prep
%setup -c

%build
make

%install
%makeinstall DESTDIR=%buildroot
install -pD -m0644 profile.scm %buildroot%_cachedir/alterator/vm-profile.scm

%files
%_alterator_datadir/steps/vm.desktop
%_alterator_datadir/images/vm
%_alterator_datadir/ui/vm
%_alterator_libdir/interfaces/guile/vm
%_alterator_libdir/interfaces/guile/backend/*
%_cachedir/alterator/vm-profile.scm

%changelog
* Tue May 14 2024 Oleg Solovyov <mcpain@altlinux.org> 0.4.41-alt1
- place after "pkg" step
- fail if not enough space for installation

* Fri Apr 05 2024 Oleg Solovyov <mcpain@altlinux.org> 0.4.40-alt1
- fix crash if LUKS partition is created on IMSM
- use new IMSM partition format

* Mon Apr 01 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 0.4.39-alt1
- add extra information when cleaning disks

* Wed Nov 22 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.38-alt1
- fix crash

* Tue Nov 21 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.37-alt1
- options: rewrite option querying by name (Fixes: 42029)

* Mon Nov 20 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.36-alt1
- Make "Create (Encrypted) Volume" buttons mutually exclusive (Closes: #45310)
- new operation: "Create Encrypted Volume" on disk wothout partition table (Closes: 28830)

* Fri Nov 03 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.35-alt1
- Double size for /boot/efi

* Thu Oct 19 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.34-alt1
- autoinstall: resolve conflict between vm-profile.scm and auto-appending /boot/efi

* Wed Oct 04 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.33-alt7
- new translations

* Tue Sep 26 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.33-alt6
- fix crash (Closes: #47701)

* Tue Aug 29 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.33-alt5
- sort partitions on IMSM volume by offset

* Fri Aug 25 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.33-alt4
- table: fix disappearing /dev/disk_luks regions

* Tue Aug 22 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.33-alt3
- more IMSM-related fixes:
  + fix crash when applying profine on IMSM
  + fix crash when applying profine on nvme
  + fix crash when trying to apply profile on IMSM-consumed disks

* Thu Jul 13 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.33-alt2
- rewrite details module
- imsm: allow volumes to be partitioned

* Thu Apr 06 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.32-alt2
- evms: ext2 plugin was renamed

* Wed Apr 05 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.32-alt1
- warn if /boot/efi is on RAID

* Tue Mar 07 2023 Slava Aseev <ptrnine@altlinux.org> 0.4.31-alt1
- introduce IMSM support

* Thu Jan 19 2023 Oleg Solovyov <mcpain@altlinux.org> 0.4.30-alt2
- new string from guile-evms

* Thu Dec 15 2022 Oleg Solovyov <mcpain@altlinux.org> 0.4.30-alt1
- remove vm.desktop from alterator modules

* Thu Jul 28 2022 Oleg Solovyov <mcpain@altlinux.org> 0.4.29-alt3
- fix regression of subvol autocreation

* Wed Jul 27 2022 Oleg Solovyov <mcpain@altlinux.org> 0.4.29-alt2
- fix crash if volume is not created (e.g. not enough space)

* Tue Jul 26 2022 Oleg Solovyov <mcpain@altlinux.org> 0.4.29-alt1
- New feature: autopartitioning with subvolumes

* Thu Jul 21 2022 Oleg Solovyov <mcpain@altlinux.org> 0.4.28-alt1
- Allow subvolume creating on LUKS'ed volumes

* Wed Jul 13 2022 Oleg Solovyov <mcpain@altlinux.org> 0.4.27-alt1
- Handle new BtrFS subvolume feature

* Wed May 04 2022 Oleg Solovyov <mcpain@altlinux.org> 0.4.26-alt1
- make sure that GRUB stage1.5 can be installed

* Mon Dec 27 2021 Oleg Solovyov <mcpain@altlinux.org> 0.4.25-alt1
- fix "Make Encrypted Volume" hiding

* Tue Sep 21 2021 Slava Aseev <ptrnine@altlinux.org> 0.4.24-alt1
- show popup-critical if multiple filesystems are assigned the same mountpoint

* Tue Sep 21 2021 Oleg Solovyov <mcpain@altlinux.org> 0.4.23-alt1
- choice: make dialog wider

* Thu Apr 22 2021 Oleg Solovyov <mcpain@altlinux.org> 0.4.22-alt1
- tree: fix partitions order if there are encryptred (Closes: #39896)

* Thu Apr 15 2021 Oleg Solovyov <mcpain@altlinux.org> 0.4.21-alt1
- EFI: show warning if there is no /boot/efi partition
- fix crash at specific conditions when going back and cancelling pending
  operations

* Tue Feb 02 2021 Oleg Solovyov <mcpain@altlinux.org> 0.4.20-alt1
- Fix disk grouping in case of multiple partitions on the same disk

* Tue Jan 19 2021 Oleg Solovyov <mcpain@altlinux.org> 0.4.19-alt1
- catch exception when restoring invalid value after backend error

* Fri Jan 15 2021 Oleg Solovyov <mcpain@altlinux.org> 0.4.18-alt1
- Forward exception message when getting options from backend

* Tue Nov 10 2020 Oleg Solovyov <mcpain@altlinux.org> 0.4.17-alt1
- Pending changes: fix LUKS partitions

* Fri Nov 06 2020 Oleg Solovyov <mcpain@altlinux.org> 0.4.16-alt1
- Pending changes: fix NVMe and mmcblk installations

* Thu Oct 01 2020 Oleg Solovyov <mcpain@altlinux.org> 0.4.15-alt1
- Show pending changes made by user/profile

* Tue Sep 22 2020 Oleg Solovyov <mcpain@altlinux.org> 0.4.14-alt1
- Fixed disk groups when there are no objects on disks

* Thu Aug 06 2020 Oleg Solovyov <mcpain@altlinux.org> 0.4.13-alt1
- Make possible to clear selected disks

* Fri Jun 19 2020 Oleg Solovyov <mcpain@altlinux.org> 0.4.12-alt1
- Don't encrypt last unencrypted disk
- Remove redundnant buttons when creating partition on already created LV

* Wed Feb 05 2020 Oleg Solovyov <mcpain@altlinux.org> 0.4.11-alt1
- Detect and show encrypted volumes on unpartitioned disks

* Mon Jan 20 2020 Slava Aseev <ptrnine@altlinux.org> 0.4.10-alt1
- Catch lvm2 VG shrink exception

* Thu Dec 12 2019 Slava Aseev <ptrnine@altlinux.org> 0.4.9-alt1
- Show "Unknown" for volumes with unknown fs

* Thu Nov 28 2019 Oleg Solovyov <mcpain@altlinux.org> 0.4.8-alt1
- Fixed crashing when handling insufficient space on disk using LVM profile
  (Closes: #37557)

* Wed Jul 17 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.7-alt1
- Fixed parentheses in default vm-profile.scm;
- Added support of PowerPC PReP partition on GPT;
- Changed profile to automatically create PReP partition on virtualized
  ppc64le systems.

* Tue Aug 28 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.6-alt1
- added lvm autoinstall support

* Tue Jul 31 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.5-alt3
- require guile >= 2.0 for build

* Tue Jan 16 2018 Paul Wolneykien <manowar@altlinux.org> 0.4.5-alt2
- Adapt for the E2K arch build.

* Wed Apr 19 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.5-alt1
- rebuilt with alterator 5.0

* Thu Nov 28 2013 Michael Shigorin <mike@altlinux.org> 0.4.4-alt1
- drop vista horror messages (but not expand and shrink!)

* Fri Mar 15 2013 Timur Aitov <timonbl4@altlinux.org> 0.4.3-alt1
- disable edit mount point for swap

* Mon Dec 24 2012 Timur Aitov <timonbl4@altlinux.org> 0.4.2-alt1
- use GPT when '/sys/firmware/efi/' exists (closes: 28161)
- create efi GPT partition in automatic mode (closes: 28162)

* Fri Nov 23 2012 Timur Aitov <timonbl4@altlinux.org> 0.4.1-alt21
- adapt for 'evms 2.5.5-alt27'

* Thu Nov 15 2012 Timur Aitov <timonbl4@altlinux.org> 0.4.1-alt20
- fixed create luks in raid/lvm
- fixed build tree with luks devices

* Wed Nov 07 2012 Timur Aitov <timonbl4@altlinux.org> 0.4.1-alt19
- added support for luks

* Wed Sep 07 2011 Timur Aitov <timonbl4@altlinux.org> 0.4.1-alt18
- fixed crushing on changing value in combobox (#25257)

* Fri Sep 02 2011 Timur Aitov <timonbl4@altlinux.org> 0.4.1-alt17
- create bios-boot GPT partition in automatic mode
- show information about installing GRUB on GPT

* Tue Aug 23 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt16
- Add translatable strings for newly supported file systems

* Mon Jul 07 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt15
- added support for raid10
- to-be-formatted indication for swap fixed

* Thu May 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt14
- recognize btrfs as allowed fsim

* Wed May 18 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt13
- Fix untranslatable strings (#23351)

* Tue Oct 19 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt12
- /vm/ortodox resurrected

* Mon Aug 10 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt11
- be more specific about possible data loss on removable disks

* Fri Aug  7 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt10
- fixed degraded raid removal, i hope (#20971)

* Mon Jun 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt9
- added GUID partition table support (#17753)

* Thu Jun 11 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt8
- allow more than one profile part with fuzzy size

* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt7
- added step file (inger@)

* Thu Apr 23 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt6
- do not offer fsims for swap partition (#19738)

* Mon Mar 30 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt4
- omit i18n stuff, use alterator-l10n from now

* Tue Mar 24 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt3
- workaround slider attribute order sensivity

* Wed Mar 11 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt2
- few more things w.r.t (#18311)
- translations updated

* Tue Mar 10 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- recovered ability to operate as an acc module (#18311)
- ask user to confirm/abandon uncommitted changes when stepping
  back from table (#18325)

* Wed Dec 10 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt2
- updated to recent alterator's core (inger@)

* Sun Dec  7 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt1
- updated for alterator's native backend scheme (inger@)
- support for power's PReP partition type

* Mon Aug 25 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt31
- help text updated (cas@) (#16760)

* Fri Jul 11 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt30
- fix crash when creating partition pointing to disk (#16340)

* Thu Jun 19 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt29
- sync'd with alterator's core

* Mon Jun 16 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt28
- fixed build with recent alterator

* Fri May 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt27
- obsolete alterator's `autoinstall' stuff removed

* Thu Apr 10 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt26
- replace volumes listbox in vm/blonde by ugly surrogate (#15119)

* Mon Apr  7 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt25
- do not propose to create fourth primary partition by default (#15081)
- translation in some popups fixed

* Fri Mar 28 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt24
- raid1/5 automatic placer now works (#14187)
- hide `next operation' pane on popup, when not applicable (#14685)
- another offloaded installer entry point added, /vm/lucky
- all installer entry points now have own urls [INCOMPATIBILITY]

* Wed Feb  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt23
- avoid to name specific distributions in help

* Wed Jan 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt22
- fixed build with recent alterator

* Wed Aug 15 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt21
- fixed autoinstall log generated by blonde.scm
- commented out tooltips, closes \#12240
- added /tmp/metadata directory for profile search paths
- uk.po updated (mike@)

* Mon Jul 16 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt20
- warn user on `clearall' when `next' clicked, closes \#12237 
- desktop entry added

* Mon Jul  9 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt19
- fix check for NTFS before resizing
- messages updated

* Tue Jul  3 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt18
- warn user before resizing NTFS partition, closes \#12176

* Wed Jun 27 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt17
- changed 'profile' names in vm/blonde 

* Mon Jun 11 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt16
- alternative offloaded /vm entry point added
- translations updated

* Sun May  6 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt15
- stick i18n everywhere, closes \#11708
- change `sure ?' popup type to question, closes \#11706
- be a bit more verbose when profile fails to apply

* Thu Apr 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt14
- ukrainian translation updated (Serhii Hlodin)

* Tue Apr 10 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt13
- workaround race when commiting slider value
- select freespace from given disk during op-segment-create
- popup geometry tweaked

* Mon Apr  9 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt12
- prefer raid1 over raid0 by default, closes \#11412

* Thu Apr  5 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt11
- allow ntfs resize

* Tue Apr  3 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt10
- added indication of required free space, semicloses \#11046
- disallow reset to empty value on renewal, closes \#11291
- replaced ugly [x] by icon, closes \#11265
- warn user early when `clearall' selected, closes \#11276
- various various for \#11292
- ukrainian translation, by Mike Shigorin & Wad Mashckoff

* Fri Mar 30 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt9
- skip first frame when looped back during install
- russian translation added

* Mon Mar 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt8
- removed apply/reset buttons when in instsaller mode
- warn user about postponed mkfs on existing volumes
- added indication for forced mkfs on volume
- do not autocreate volumes on segments of type raid/lvm
- show mount options, where applicable

* Fri Mar  9 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt7
- warn user, if pending changes exists, closes \#10631 & \#10811
- restrict acceptable fsims by partition type, closes \#11005
- update storage tree after reset, closes \#11030

* Thu Mar  1 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt6
- sync'd with browser idea about combo return value type

* Thu Feb 22 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt5
- ui redo, separate `volumes' table dropped
- autoplacer seems working
- do not try to resize ntfs volumes -- too slow
- do not care about bootable flag on partiotions
- 'linux raid autostart' partition type added

* Thu Feb  8 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt4
- incomplete logging for autoinstall fixed
- devices tree shown with size attributes now
- get rid of obsolete *box varians

* Fri Feb  2 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt3
- always show size in MBs during partition creation
- regression fix appeared in alt2

* Wed Jan 31 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt2
- made "/" bootable, if possible, warn user, if not #10722

* Thu Jan 18 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- ui improvements
- initial install profile support

* Fri Dec 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt2
- get rid of obsolete woo-read-names
- fix repetitive `options changed' in title
- fix not shown disks after unassigning partition table
- remove redundant mkfs op, when in installer mode
- hide `create partition table' op

* Tue Dec 19 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- ui: most recent operation chained
- ui: do not show inactive button actions
- ui: various various

* Tue Dec 12 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt11
- filter some uninterested/unambiguous options
- fix breakage with fifth primary
- be stricter on mountpoint assignement
- ui improved a bit

* Tue Dec  5 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt10
- activate volumes at startup, if any
- allow create raid/lvm vg iff free objects exists
- various ui fixes

* Wed Nov 29 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt9
- installer mode: assign mountpoint insterad of mount
- installer mode: back/next buttons pacified

* Mon Nov 27 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt8
- icons added

* Tue Nov 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt7
- distinguish between running under wizard vs standalone

* Mon Nov 20 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt6
- generate fstab-like file with newly created/assigned volumes

* Wed Nov  8 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt5
- autocommit acceptable objects during raid creation
- handle exceptions during task applying

* Wed Nov  8 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt4
- sync'd with alterator-2.9-alt0.13

* Tue Nov  7 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt3
- ui: avoid unneeded object selection
- ui: do not show empty objects/options boxes
- ui: handle exception from unsuccessful option value setting

* Tue Oct 31 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt2
- sync'd with alterator's core (2.9-alt0.11)

* Mon Oct 23 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- initial release
