%define pypi_name pyasyncore

Name: python3-module-%pypi_name
Version: 1.0.4
Release: alt1

Summary: Make asyncore available for Python 3.12 onwards

License: Python-2.0.1
Group: Development/Python3
Url: https://pypi.org/project/pyasyncore

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
This package contains the asyncore module as found in Python versions
prior to 3.12. It is provided so that existing code relying on import
asyncore is able to continue being used without significant
refactoring.

%prep
%setup
# these should not be executable
chmod ugo-x README.md LICENSE

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md
%python3_sitelibdir/asyncore
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Apr 16 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.4-alt1
- Build new version.

* Tue Nov 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
