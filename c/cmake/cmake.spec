%define _unpackaged_files_terminate_build 1
%set_verify_elf_method unresolved=strict
%def_disable bootstrap
%if_disabled bootstrap
%def_enable gui
%def_enable docs
%def_disable jsoncpp_bootstrap
%endif
%def_without check
%add_optflags %optflags_shared
%define _cmake__builddir build

Name: cmake
Version: 3.29.1
Release: alt1

Summary: Cross-platform, open-source make system

License: BSD
Group: Development/Tools
Url: http://cmake.org/

# Source-url: https://gitlab.kitware.com/cmake/cmake/-/archive/v%version/cmake-v%version.tar.bz2
Source: %name-%version.tar

Source2: CMakeCache.txt
Patch1: alt-fallback-modules-dir.patch
Patch2: 696d16ae6c5214e314cfc7cb809c2e574bcff651.patch

%if_disabled bootstrap
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
%endif
BuildRequires(pre): rpm-build-xdg
BuildRequires: gcc-c++
BuildRequires: zlib-devel liblzma-devel bzlib-devel 
BuildRequires: libarchive-devel >= 3.3.3
BuildRequires: libcurl-devel
BuildRequires: libexpat-devel libxml2-devel
BuildRequires: libncurses-devel
BuildRequires: jsoncpp-devel >= 1.6.0
BuildRequires: doxygen graphviz zlib-devel
BuildRequires: librhash-devel
BuildRequires: libuv-devel >= 1.28.0
BuildRequires: shared-mime-info rpm-build-vim

%{?_enable_docs:BuildRequires: python3-module-sphinx-sphinx-build-symlink}
%{?_enable_gui:BuildRequires: qt5-base-devel}

%{?!_without_check:%{?!_disable_check:BuildRequires: /proc gcc-fortran java-devel cvs subversion mercurial git-core}}

Obsoletes: cpack < 2.4.5-alt3
Provides: cpack = %version-%release

Requires: %name-modules = %version-%release
# TODO: change cmake to rpm-build-cmake in all specs
Requires: rpm-macros-%name

%add_findreq_skiplist %_datadir/%name/Templates/cygwin-package.sh.in

%filter_from_requires /^gnustep-Backbone.*/d

%description
CMake is used to control the software compilation process using
simple platform and compiler independent configuration files.
CMake generates native makefiles and workspaces that can be
used in the compiler environment of your choice. CMake is quite
sophisticated: it is possible to support complex environments
requiring system configuration, pre-processor generation, code
generation, and template instantiation.


%package modules
Summary: Standard CMake modules
Group: Development/Tools
BuildArch: noarch

%description modules
CMake is used to control the software compilation process using
simple platform and compiler independent configuration files.

This package contains the standard modules from the CMake distribution.


%package -n ccmake
Summary: Curses interface for CMake
Group: Development/Tools
Requires: %name = %version-%release

%description -n ccmake
The "ccmake" executable is the CMake curses interface. Project
configuration settings may be specified interactively through this GUI.
Brief instructions are provided at the bottom of the terminal when the
program is running.


%package -n ctest
Summary: CMake test driver program
Group: Development/Tools
Requires: %name = %version-%release

%description -n ctest
The ctest executable is the CMake test driver program. CMake-generated
build trees created for projects that use the ENABLE_TESTING and
ADD_TEST commands have testing support. This program will run the tests
and report results.


%package gui
Summary: Qt interface for CMake
Group: Development/Tools
Requires: %name = %version-%release

%description gui
The "cmake-gui" executable is the CMake GUI.  Project configuration settings
may be specified interactively.  Brief instructions are provided at the
bottom of the window when the program is running.


%package doc
Summary: CMake docs
Group: Documentation
BuildArch: noarch

%description doc
This package contains CMake docs in DocBook, html and txt formats.


%package -n vim-plugin-%name
Summary: Vim plugins for CMake files
Group: Editors
BuildArch: noarch

%description -n vim-plugin-%name
This package contains updated indent and syntax Vim plugins for CMake files.

%package -n bash-completion-%name
Summary: bash completion for CMake
Group: Shells
BuildArch: noarch

%description -n bash-completion-%name
bash completion for CMake

%prep
%setup
%patch1 -p1
%ifarch %e2k
# "Could NOT find OpenMP_C (missing: OpenMP_omp_LIBRARY OpenMP_pthread_LIBRARY)"
# cmake tries to scan the OpenMP example for libraries, which breaks the build
sed -i 's/if(CMAKE_${LANG}_VERBOSE_FLAG)/if(false) # &/' Modules/FindOpenMP.cmake
# workaround for SUNPro compiler also helps EDG
sed -i 's/__SUNPRO_CC/__EDG__/' Source/cmArgumentParserTypes.h
%endif

# use %_optlevel for any compiler
sed -i 's/ -O[23]/ -O%_optlevel/g' Modules/Compiler/*.cmake

# TODO: Source/cm_get_date.c:11:10: fatal error: ../Utilities/cmlibarchive/libarchive/archive_getdate.c:
# cmlibarchive
# remove bundled sources
rm -rv Utilities/{cmbzip2,cmcurl,cmexpat,cmliblzma,cmlibrhash,cmlibuv,cmnghttp2,cmvssetup,cmzlib,cmzstd}/
%if_disabled jsoncpp_bootstrap
rm -rv Utilities/cmjsoncpp/
%endif

%build
%if_enabled bootstrap
mkdir build
pushd build
install -m644 %SOURCE2 ./

CFLAGS="%optflags" CXXFLAGS="%optflags" ../bootstrap \
	--verbose \
	--parallel=%__nprocs \
	--system-libs \
	%{?_enable_gui:--qt-gui} \
	%{?_enable_docs:--sphinx-man --sphinx-html} \
	--prefix=%prefix \
	--datadir=/share/%name \
	--mandir=/share/man \
	--docdir=/share/doc/%name-%version \
	%{?_enable_jsoncpp_bootstrap:--no-system-jsoncpp} \
	%nil

export LD_LIBRARY_PATH=$PWD/Source:$PWD/Source/kwsys/:$PWD/Source/CursesDialog/form%{?_enable_jsoncpp_bootstrap::$PWD/Utilities/cmjsoncpp}
%make_build VERBOSE=1
popd
%else
# without bootstrap
%cmake \
    -DCMAKE_USE_SYSTEM_LIBRARY_CPPDAP=OFF \
    -DCMAKE_USE_SYSTEM_LIBRARIES=ON \
    -DCMAKE_DATA_DIR=share/%name \
    -DCMAKE_DOC_DIR=share/doc/%name-%version \
    -DCMAKE_MAN_DIR=share/man \
    %{?_enable_gui:-DBUILD_QtDialog=ON} \
    %{?_enable_docs:-DSPHINX_HTML=ON -DSPHINX_MAN=ON} \
    %nil
%cmake_build
%endif

%install
pushd build
%if_enabled bootstrap
export LD_LIBRARY_PATH=$PWD/Source:$PWD/Source/kwsys/:$PWD/Source/CursesDialog/form%{?_enable_jsoncpp_bootstrap::$PWD/Utilities/cmjsoncpp}
%else
# FIXME
subst 's|	bin/cmake|	$(CMAKE_COMMAND)|' Makefile
%endif
%makeinstall_std
popd

%if_enabled jsoncpp_bootstrap
cp build/Utilities/cmjsoncpp/libcmjsoncpp.so %buildroot%_libdir/
%endif

%if_with gui
for i in 32 128; do
    install -pD -m644 Source/QtDialog/CMakeSetup$i.png %buildroot%_iconsdir/hicolor/${i}x$i/apps/CMakeSetup.png
done
%endif

mkdir -p %buildroot{%vim_indent_dir,%vim_syntax_dir,%_sysconfdir/bash_completion.d}
install -m644 Auxiliary/vim/indent/%name.vim %buildroot%vim_indent_dir/%name.vim
install -m644 Auxiliary/vim/syntax/%name.vim %buildroot%vim_syntax_dir/%name.vim
rm -rf %buildroot%_datadir/%name/editors/vim

#mv -f %buildroot%_datadir/%name/completions %buildroot%_sysconfdir/bash_completion.d/%name
rm -vf %buildroot/usr/share/emacs/site-lisp/cmake-mode.el
# drop dump requires
rm -rfv %buildroot/%prefix/share/%name/Modules/Platform/AIX/

#install -p  build/Source/kwsys/libcmsys.so  %buildroot%_libdir/libcmsys.so
#install -p  build/Source/kwsys/libcmsys_c.so  %buildroot%_libdir/libcmsys_c.so

mkdir -p %buildroot%_libdir/cmake/

%check
%if_with check
# CTest.UpdateGIT fails, see #20884
unset GIT_DIR
unset GIT_INDEX_FILE
unset GIT_OBJECT_DIRECTORY
unset DISPLAY
pushd build
export LD_LIBRARY_PATH=%buildroot%_libdir
%make_build test ARGS="--output-on-failure -E 'CMake.FileDownload|CTestTestUpload'"
popd
%endif

%files
%_bindir/cmake
%_bindir/cpack
#_libdir/libCMakeLib.so
#_libdir/libCPackLib.so
#_libdir/libcmsys.so
#_libdir/libcmsys_c.so
%dir %_libdir/cmake/
%_datadir/%name/
%_aclocaldir/*
%if_enabled docs
%_man1dir/cmake*.*
%_man1dir/cpack.*
%_man7dir/*
%endif
%dir %_docdir/%name-%version/
#_docdir/%name-%version/ChangeLog.manual
%_docdir/%name-%version/Copyright.txt
%_docdir/%name-%version/cmsys/
%exclude %_datadir/%name/Modules/
%if_enabled jsoncpp_bootstrap
%_libdir/libcmjsoncpp.so
%endif

%files modules
%dir %_datadir/%name/
%_datadir/%name/Modules/


%files -n ccmake
%_bindir/ccmake
#_libdir/libcmForm.so
%if_enabled docs
%_man1dir/ccmake.*
%endif


%files -n ctest
%_bindir/ctest
#_libdir/libCTestLib.so
%if_enabled docs
%_man1dir/ctest.*
%endif


%if_enabled gui
%files gui
%_bindir/cmake-gui
%_desktopdir/cmake-gui.desktop
%_xdgmimedir/packages/cmakecache.xml
%_iconsdir/*/*/*/CMakeSetup.png
#_pixmapsdir/*
%endif


%if_enabled docs
%files doc
%dir %_docdir/%name-%version
#_docdir/%name-%version/ccmake.*
#_docdir/%name-%version/cmake*
#_docdir/%name-%version/cpack*
#_docdir/%name-%version/ctest.*
%_docdir/%name-%version/html
%_docdir/%name-%version/cmcppdap/
%endif


%files -n vim-plugin-%name
%vim_indent_dir/*
%vim_syntax_dir/*

%files -n bash-completion-%name
#%_sysconfdir/bash_completion.d/*
%_datadir/bash-completion/completions/*


%changelog
* Sat Apr 06 2024 Vitaly Lipatov <lav@altlinux.ru> 3.29.1-alt1
- new version 3.29.1 (with rpmrb script)
- build rpm-macros-cmake subpackage standalone

* Sun Mar 24 2024 Vitaly Lipatov <lav@altlinux.ru> 3.29.0-alt1
- new version 3.29.0
- spec: stop using nested if

* Sun Feb 18 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.28.3-alt1.1
- workaround for ICE on e2k

* Mon Feb 12 2024 Vitaly Lipatov <lav@altlinux.ru> 3.28.3-alt1
- new version (3.28.3) with rpmgs script
- add _cmakedir macro (ALT bug 49373)

* Thu Feb 01 2024 Vitaly Lipatov <lav@altlinux.ru> 3.28.2-alt1
- new version (3.28.2) with rpmgs script

* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 3.28.1-alt1
- new version (3.28.1) with rpmgs script

* Sat Oct 21 2023 Vitaly Lipatov <lav@altlinux.ru> 3.27.7-alt1
- new version

* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 3.27.6-alt1
- new version

* Thu Jul 27 2023 Vitaly Lipatov <lav@altlinux.ru> 3.27.1-alt1
- build 3.27.1 release, cleanup spec
- switch to build from a tarball

* Wed Apr 19 2023 Alexey Shabalin <shaba@altlinux.org> 3.23.2-alt3
- add ctest macro (ALT#45833)

* Wed Mar 29 2023 Michael Shigorin <mike@altlinux.org> 3.23.2-alt2
- cherry-picked upstream commit g28b1c5f to improve lcc 1.26 support on e2k

* Fri Oct 21 2022 Michael Shigorin <mike@altlinux.org> 3.23.2-alt1.2
- E2K: default to -O%%_optlevel instead of hardwired -O2

* Sat Jul 30 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.23.2-alt1.1
- fixed failure of finding OpenMP on e2k

* Tue Jun 07 2022 Vitaly Lipatov <lav@altlinux.ru> 3.23.2-alt1
- new version

* Wed Apr 13 2022 Vitaly Lipatov <lav@altlinux.ru> 3.23.1-alt1
- new version

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.23.0-alt1
- new version

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.22.2-alt1
- new version

* Fri Aug 27 2021 Vitaly Lipatov <lav@altlinux.ru> 3.21.2-alt1
- new version
- fix BR for bootstrap case (thanks, @iv)

* Thu Jul 29 2021 Vitaly Lipatov <lav@altlinux.ru> 3.21.1-alt1
- new version

* Sat Jul 24 2021 Vitaly Lipatov <lav@altlinux.ru> 3.21.0-alt3
- fix build

* Sat Jul 24 2021 Vitaly Lipatov <lav@altlinux.ru> 3.21.0-alt2
- add bootstrap switch and build via cmake by default
- add optflags_shared to optflags

* Fri Jul 23 2021 Vitaly Lipatov <lav@altlinux.ru> 3.21.0-alt1
- new version 3.21.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 3.20.5-alt1
- new version 3.20.5 (with rpmrb script)

* Fri Jun 04 2021 Arseny Maslennikov <arseny@altlinux.org> 3.19.7-alt4
- macros: honor NPROCS in addition to %%__nprocs. (fixes ALT bug 40153)

* Sat Apr 24 2021 Arseny Maslennikov <arseny@altlinux.org> 3.19.7-alt3
- macros: add a macro to allow cmake command name substitution
- macros: allow easy override of build artifact directory

* Fri Apr 23 2021 Vitaly Lipatov <lav@altlinux.ru> 3.19.7-alt2
- drop requires dump from cmake-modules
- build without bundled sources
- use python3-module-sphinx-sphinx-build-symlink instead of python-module-sphinx-devel

* Tue Mar 16 2021 Vitaly Lipatov <lav@altlinux.ru> 3.19.7-alt1
- new version 3.19.7 (with rpmrb script)

* Thu Feb 25 2021 Vitaly Lipatov <lav@altlinux.ru> 3.19.6-alt1
- new version 3.19.6 (with rpmrb script)

* Thu Jan 28 2021 Vitaly Lipatov <lav@altlinux.ru> 3.19.4-alt1
- new version 3.19.4 (with rpmrb script)

* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 3.19.3-alt1
- new version 3.19.3 (with rpmrb script)

* Tue Dec 01 2020 Vitaly Lipatov <lav@altlinux.ru> 3.19.1-alt1
- new version 3.19.1 (with rpmrb script)

* Wed Nov 18 2020 Vitaly Lipatov <lav@altlinux.ru> 3.18.5-alt1
- new version 3.18.5 (with rpmrb script)

* Tue Oct 06 2020 Vitaly Lipatov <lav@altlinux.ru> 3.18.4-alt1
- new version 3.18.4 (with rpmrb script)
- drop FindJNI.cmake patch (applied in upstream 3.18.4)

* Sat Sep 26 2020 Vitaly Lipatov <lav@altlinux.ru> 3.18.3-alt2
- add aarch64 dir support in FindJNI.cmake (ALT bug 38992)

* Tue Sep 22 2020 Vitaly Lipatov <lav@altlinux.ru> 3.18.3-alt1
- new version 3.18.3 (with rpmrb script)

* Fri Aug 21 2020 Vitaly Lipatov <lav@altlinux.ru> 3.18.2-alt1
- new version 3.18.2 (with rpmrb script)

* Thu Jul 30 2020 Vitaly Lipatov <lav@altlinux.ru> 3.18.1-alt1
- new version 3.18.1 (with rpmrb script)

* Wed Jul 15 2020 Vitaly Lipatov <lav@altlinux.ru> 3.18.0-alt1
- new version 3.18.0 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 3.17.3-alt1
- new version 3.17.3 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 3.17.2-alt1
- new version 3.17.2 (with rpmrb script)

* Sat Mar 21 2020 Vitaly Lipatov <lav@altlinux.ru> 3.17.0-alt1
- new version 3.17.0 (with rpmrb script)

* Thu Feb 06 2020 Vitaly Lipatov <lav@altlinux.ru> 3.16.4-alt1
- new version 3.16.4 (with rpmrb script)

* Wed Jan 29 2020 Vitaly Lipatov <lav@altlinux.ru> 3.16.3-alt2
- fix LIBDIR set in GNUInstallDirs

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 3.16.3-alt1
- new version 3.16.3 (with rpmrb script)

* Sun Oct 20 2019 Vitaly Lipatov <lav@altlinux.ru> 3.15.4-alt1
- new version 3.15.4 (with rpmrb script)

* Wed May 15 2019 Dmitry V. Levin <ldv@altlinux.org> 3.13.4-alt3
- NMU.
- macros: fixed bug in definitions of %%cmake and %%cmake_insource
  introduced in the previous release.

* Sat May 11 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.13.4-alt2
- macros: use %%_libsuff macro.
- spec: add knobs useful for bootstrap.

* Wed Feb 06 2019 Vitaly Lipatov <lav@altlinux.ru> 3.13.4-alt1
- new version 3.13.4 (with rpmrb script)
- treat "No source or binary directory provided" as warning (ALT bug 36051)

* Tue Feb 05 2019 Vitaly Lipatov <lav@altlinux.ru> 3.13.3-alt1
- new version 3.13.3 (with rpmrb script) (ALT bug 36041)

* Wed Dec 05 2018 Vitaly Lipatov <lav@altlinux.ru> 3.13.1-alt1
- Updated to upstream version 3.13.1 (ALT bug 35702)

* Thu Jul 19 2018 Grigory Ustinov <grenka@altlinux.org> 3.11.2-alt2
- Fixed FTBS (Add missing rpm-build-xdg).

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.2-alt1
- Updated to upstream version 3.11.2.

* Wed Feb 28 2018 Alexey Shabalin <shaba@altlinux.ru> 3.10.2-alt1
- 3.10.2
- backport support boost-1.66 from cmake-3.11.0-rc2

* Tue Oct 31 2017 Vitaly Lipatov <lav@altlinux.ru> 3.9.2-alt1
- autogen: Don't use AUTOMOC_MOC_OPTIONS in moc-predefs command (ALT bug 34055)

* Mon Oct 23 2017 Sergey V Turchin <zerg@altlinux.org> 3.9.2-alt0.4
- search old sharedir CMake directory too

* Thu Oct 19 2017 Igor Vlasenko <viy@altlinux.ru> 3.9.2-alt0.3
- NMU: set cmake sharedir to %%_datadir/ cmake, not CMake

* Wed Sep 13 2017 Alexey Shabalin <shaba@altlinux.org> 3.9.2-alt0.2
- Set optimization for RELEASE to ALTLinux default.
- FindBoost: Add version 1.65.1 (thx Roger Leigh).
- FindBoost: Add Boost 1.65 dependencies (thx Roger Leigh).
- FindBoost: Add option to prevent finding DEBUG/RELEASE Boost-libs (thx Deniz Bahadir).

* Tue Sep 12 2017 L.A. Kostis <lakostis@altlinux.ru> 3.9.2-alt0.1
- 3.9.2:
  + enable server mode by default.
  + update buildreq (added librhash and libuv).

* Fri Jan 20 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.6.3-alt0.2
- FindBoost.cmake: added support of boost 1.62 and 1.63.

* Tue Dec 13 2016 L.A. Kostis <lakostis@altlinux.ru> 3.6.3-alt0.1
- Updated to 3.6.3.
- .spec cleanup for new rpm.

* Sun Oct 23 2016 L.A. Kostis <lakostis@altlinux.ru> 3.6.2-alt0.2
- Added some patches from debian:
  - FindBoost_add_-lpthread_#563479.diff: Add -lpthread when using Boost::Thread.
  - qt_import_dir_variable.diff: FindQt4: define QT_IMPORTS_DIR variable 
    even if it is not present on the system.

* Sat Oct 22 2016 L.A. Kostis <lakostis@altlinux.ru> 3.6.2-alt0.1
- test build of 3.6.2.

* Mon Jun 13 2016 L.A. Kostis <lakostis@altlinux.ru> 3.4.3-alt0.1
- test build of 3.4.3.

* Wed Sep 02 2015 Sergey V Turchin <zerg@altlinux.org> 3.2.2-alt3.1
- remove variable dereference from FindPkgConfig

* Thu Jun  4 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 3.2.2-alt3
- rebuild with c++11 ABI

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.2-alt2
- Avoid requirement on gnustep-Backbone (ALT #30978)

* Sat Apr 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.2-alt1
- Version 3.2.2 (ALT #30677)

* Tue Nov 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.12.1-alt2
- Revert changes in cmake.macros and add new macros %%_cmake_skip_rpath -DCMAKE_SKIP_RPATH:BOOL=ON

* Thu Nov 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.12.1-alt1
- 2.8.12.1
- Added additional macros in cmake.macros (ALT#27879)
- Change in cmake.macros CMAKE_SKIP_RPATH to CMAKE_SKIP_INSTALL_RPATH
  look the discussion http://public.kitware.com/pipermail/cmake-developers/2012-February/003254.html

* Thu May 23 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.11-alt1
- 2.8.11

* Tue Mar 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.10.2-alt1
- 2.8.10.2

* Tue Nov 20 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.10.1-alt1
- 2.8.10.1

* Sat Oct 06 2012 Dmitry V. Levin <ldv@altlinux.org> 2.8.9-alt1.2
- Reverted previous change, it was a no longer needed workaround
  for make-3.82-alt4 quotation bug.

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.9-alt1.1
- Avoid tests with spaces in names of files and directories

* Sat Sep 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.9-alt1
- 2.8.9
- Add subpackage bash-completion-cmake

* Wed Jun 27 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.8-alt3
- Really fix FindPkgConfig.cmake regression (closes: #27499)

* Mon Jun 25 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.8-alt2
- Fix FindPkgConfig.cmake regression (closes: #27499)

* Sat Jun 23 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.8-alt1
- 2.8.8
- add %%cmake_build, %%cmake_install and %%cmakeinstall_std macros (closes: #24229)

* Tue Jan 24 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.7-alt1
- 2.8.7

* Sat Oct 08 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.6-alt1
- 2.8.6

* Sat Jul 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.5-alt1
- 2.8.5
- Disable test CTestTestUpload

* Sun Mar 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.4-alt1
- 2.8.4
- Update spec: add necessary LD_LIBRARY_PATH for build process (thanks real@)
- Remove build type and add flags for Fortran (thanks real@)

* Sat Jan 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.3-alt1
- 2.8.3

* Tue Jul 13 2010 Andrey Rahmatullin <wrar@altlinux.org> 2.8.2-alt1
- 2.8.2
- add/restore VCS tests by adding the necessary buildreqs
- add an additional #20884 workaround needed for new gear --commit

* Tue May 11 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.1-alt3
- fix %%cmake_insource (sin@, closes: #23459)

* Mon Mar 29 2010 Dmitry V. Levin <ldv@altlinux.org> 2.8.1-alt2
- Fixed and reenabled %%check.

* Sun Mar 28 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.1-alt1
- 2.8.1
- disable tests (CTestTestTimeout fails in hasher)

* Tue Nov 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.0-alt2
- move macros to the separate package according to the policy

* Mon Nov 16 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.0-alt1
- 2.8.0
- add %%cmake and %%cmake_insource macros (closes: #22209)

* Sat Jul 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.4-alt2
- add workarounds for buffer overflows

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Fri Mar 13 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.3-alt2
- package Vim plugins (closes: #19158)

* Fri Mar 06 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.3-alt1
- 2.6.3
- fix Group:
- cmake-doc: don't require cmake

* Thu Dec 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.2-alt3
- package docdir into the main package (repocop)

* Mon Nov 17 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.2-alt2
- remove update_*/clean_* invocations

* Sat Sep 27 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sun Aug 03 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.1-alt1
- 2.6.1
- fix .desktop file according to desktop-file-validate
- move CMakeSetup.png from _pixmapsdir to _niconsdir
- make -doc subpackage noarch and split noarch -modules subpackage

* Sun May 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.0-alt1
- 2.6.0
- package html and txt docs separately

* Sat Feb 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Mon Jul 23 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.7-alt1
- 2.4.7

* Fri Mar 30 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.6-alt2
- rebuild with libcurl.so.4

* Sat Jan 13 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.6-alt1
- 2.4.6

* Wed Jan 03 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt4
- build in separate dir
- use optflags

* Wed Jan 03 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt3
- merge cpack package into cmake, since it is required by (almost?)
  all cmake builds (#10577)

* Sun Dec 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt2
- remove globbing of /usr/lib/qt-3* from FindQt3.cmake, which caused
  incorrect buildreq output for projects using FIND_PACKAGE(Qt3)

* Sat Dec 09 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt1
- 2.4.5
- fix x86_64 build (damir@)

* Sun Dec 03 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt0.2
- separate packages for ccmake, cpack and ctest

* Sat Dec 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt0.1
- 2.4.5 RC4
- fix search for libxmlrpc

* Thu Nov 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Wed Aug 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.3-alt2
- build with system libs
- build bundled libs as shared
- invoke make test

* Thu Aug 03 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.3-alt1
- new version

* Thu Jul 13 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt0.1
- new version 2.4.2 (with rpmrb script) (fix bug #9776)

* Tue May 09 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt0.1
- new version (2.4.1)

* Wed Jan 25 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt0.1
- new version
- fix rpath using

* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version

* Sun Feb 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- first release for ALT Linux Sisyphus

* Tue Nov 23 2004 Gaetan LEHMANN <gaetan.lehmann@jouy.inra.fr> 2.0.5-1mdk
- 2.0.5

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.6.7-2mdk
- Rebuild

* Thu Jul 17 2003 Austin Acton <aacton@yorku.ca> 1.6.7-1mdk
- 1.6.7

* Thu Jan 9 2003 Austin Acton <aacton@yorku.ca> 1.4.7-1mdk
- initial package
