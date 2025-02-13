%define oname scramp

%def_with check

Name:    python3-module-%oname
Version: 1.4.5
Release: alt1

Summary: Python implementation of the SCRAM protocol
License: MIT-0
Group:   Development/Python3
URL:     https://pypi.org/project/scramp/
VCS:     https://github.com/tlocke/scramp

Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-asn1crypto
BuildRequires: python3-module-passlib
BuildRequires: python3-module-pytest-mock
%endif

%description
%summary.

%prep
%setup -n %oname-%version

sed -i '/dynamic = /d' pyproject.toml
sed -i '9a version = "%version"' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Sun Apr 14 2024 Anton Vyatkin <toni@altlinux.org> 1.4.5-alt1
- New version 1.4.5.

* Fri Mar 24 2023 Anton Vyatkin <toni@altlinux.org> 1.4.4-alt1
- Initial build for Sisyphus
