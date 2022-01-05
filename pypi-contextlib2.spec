#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-contextlib2
Version  : 21.6.0
Release  : 76
URL      : https://files.pythonhosted.org/packages/c7/13/37ea7805ae3057992e96ecb1cffa2fa35c2ef4498543b846f90dd2348d8f/contextlib2-21.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c7/13/37ea7805ae3057992e96ecb1cffa2fa35c2ef4498543b846f90dd2348d8f/contextlib2-21.6.0.tar.gz
Summary  : Backports and enhancements for the contextlib module
Group    : Development/Tools
License  : Python-2.0
Requires: pypi-contextlib2-license = %{version}-%{release}
Requires: pypi-contextlib2-python = %{version}-%{release}
Requires: pypi-contextlib2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: contextlib2
Provides: contextlib2-python
Provides: contextlib2-python3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://jazzband.co/static/img/badge.svg
:target: https://jazzband.co/
:alt: Jazzband

%package license
Summary: license components for the pypi-contextlib2 package.
Group: Default

%description license
license components for the pypi-contextlib2 package.


%package python
Summary: python components for the pypi-contextlib2 package.
Group: Default
Requires: pypi-contextlib2-python3 = %{version}-%{release}

%description python
python components for the pypi-contextlib2 package.


%package python3
Summary: python3 components for the pypi-contextlib2 package.
Group: Default
Requires: python3-core
Provides: pypi(contextlib2)

%description python3
python3 components for the pypi-contextlib2 package.


%prep
%setup -q -n contextlib2-21.6.0
cd %{_builddir}/contextlib2-21.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641424852
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-contextlib2
cp %{_builddir}/contextlib2-21.6.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-contextlib2/f71a7d6eae28b232379541a2b0a020cd48259b84
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-contextlib2/f71a7d6eae28b232379541a2b0a020cd48259b84

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
