%define _unpackaged_files_terminate_build 1

%define oname stone

%def_with check

Name:    python3-module-%oname
Version: 3.3.6
Release: alt1

Summary: The Official API Spec Language for Dropbox API V2
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/stone/
VCS:     https://github.com/dropbox/stone

BuildArch: noarch

Source:  %name-%version.tar
Patch:   stone-3.3.2-alt-drop-distutils.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-ply
BuildRequires: python3-module-six
%endif

%description
%summary

%prep
%setup
%patch -p1

# Don't use pytest-runner
sed -i '/pytest-runner/d' setup.py
# Python 3.11 compat https://github.com/dropbox/stone/issues/288
sed -i 's/getargspec/getfullargspec/' stone/frontend/ir_generator.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.rst
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Wed May 15 2024 Anton Vyatkin <toni@altlinux.org> 3.3.6-alt1
- New version 3.3.6.

* Tue May 14 2024 Anton Vyatkin <toni@altlinux.org> 3.3.5-alt1
- New version 3.3.5.

* Fri Mar 29 2024 Anton Vyatkin <toni@altlinux.org> 3.3.3-alt1
- New version 3.3.3.

* Thu Mar 28 2024 Anton Vyatkin <toni@altlinux.org> 3.3.2-alt1
- New version 3.3.2.

* Tue Jan 30 2024 Anton Vyatkin <toni@altlinux.org> 3.3.1-alt4
- Fixed FTBFS (replace deprecated imp).

* Thu Oct 12 2023 Anton Vyatkin <toni@altlinux.org> 3.3.1-alt3
- Dropped dependency on distutils.

* Thu Jun 08 2023 Anton Vyatkin <toni@altlinux.org> 3.3.1-alt2
- Fix FTBFS

* Mon Feb 13 2023 Anton Vyatkin <toni@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus
