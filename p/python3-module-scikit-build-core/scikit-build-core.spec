%define oname scikit-build-core
%define pypi_name scikit_build_core

%def_with check

Name:    python3-module-%oname
Version: 0.9.4
Release: alt1

Summary: A next generation Python CMake adaptor and Python API for plugins

License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/scikit-build-core
VCS:     https://github.com/scikit-build/scikit-build-core

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pybind11-devel
BuildRequires: python3-module-pytest
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-build
BuildRequires: python3-module-cattrs
BuildRequires: python3-module-fastjsonschema
BuildRequires: python3-module-numpy
BuildRequires: python3-module-wheel
# for fixture 'fp'
BuildRequires: python3-module-pytest-subprocess
%endif

Source: %name-%version.tar
Patch: scikit-build-core-offline-wheelhouse.patch

BuildArch: noarch

%description
%summary

%prep
%setup
%patch -p1
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -m "not network"

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 0.9.4-alt1
- Automatically updated to 0.9.4.

* Fri May 17 2024 Grigory Ustinov <grenka@altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus.
