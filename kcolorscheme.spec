#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kcolorscheme
Version  : 6.5.0
Release  : 12
URL      : https://download.kde.org/stable/frameworks/6.5/kcolorscheme-6.5.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.5/kcolorscheme-6.5.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.5/kcolorscheme-6.5.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kcolorscheme-data = %{version}-%{release}
Requires: kcolorscheme-lib = %{version}-%{release}
Requires: kcolorscheme-license = %{version}-%{release}
Requires: kcolorscheme-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KColorScheme
Classes to read and interact with KColorScheme

%package data
Summary: data components for the kcolorscheme package.
Group: Data

%description data
data components for the kcolorscheme package.


%package dev
Summary: dev components for the kcolorscheme package.
Group: Development
Requires: kcolorscheme-lib = %{version}-%{release}
Requires: kcolorscheme-data = %{version}-%{release}
Provides: kcolorscheme-devel = %{version}-%{release}
Requires: kcolorscheme = %{version}-%{release}

%description dev
dev components for the kcolorscheme package.


%package lib
Summary: lib components for the kcolorscheme package.
Group: Libraries
Requires: kcolorscheme-data = %{version}-%{release}
Requires: kcolorscheme-license = %{version}-%{release}

%description lib
lib components for the kcolorscheme package.


%package license
Summary: license components for the kcolorscheme package.
Group: Default

%description license
license components for the kcolorscheme package.


%package locales
Summary: locales components for the kcolorscheme package.
Group: Default

%description locales
locales components for the kcolorscheme package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kcolorscheme-6.5.0
cd %{_builddir}/kcolorscheme-6.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723220936
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723220936
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcolorscheme
cp %{_builddir}/kcolorscheme-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kcolorscheme/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/kcolorscheme-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcolorscheme/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kcolorscheme-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcolorscheme/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98 || :
cp %{_builddir}/kcolorscheme-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kcolorscheme/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/kcolorscheme-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kcolorscheme/0b71159e19bef95069e18d17296291916e89b5cd || :
cp %{_builddir}/kcolorscheme-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kcolorscheme/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kcolorscheme-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kcolorscheme/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kcolorscheme-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kcolorscheme/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcolorscheme6

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kcolorscheme.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KColorScheme/KColorScheme
/usr/include/KF6/KColorScheme/KColorSchemeManager
/usr/include/KF6/KColorScheme/KColorSchemeModel
/usr/include/KF6/KColorScheme/KStatefulBrush
/usr/include/KF6/KColorScheme/kcolorscheme.h
/usr/include/KF6/KColorScheme/kcolorscheme_export.h
/usr/include/KF6/KColorScheme/kcolorscheme_version.h
/usr/include/KF6/KColorScheme/kcolorschememanager.h
/usr/include/KF6/KColorScheme/kcolorschememodel.h
/usr/include/KF6/KColorScheme/kstatefulbrush.h
/usr/lib64/cmake/KF6ColorScheme/KF6ColorSchemeConfig.cmake
/usr/lib64/cmake/KF6ColorScheme/KF6ColorSchemeConfigVersion.cmake
/usr/lib64/cmake/KF6ColorScheme/KF6ColorSchemeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6ColorScheme/KF6ColorSchemeTargets.cmake
/usr/lib64/libKF6ColorScheme.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF6ColorScheme.so.6
/usr/lib64/libKF6ColorScheme.so.6.5.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcolorscheme/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/kcolorscheme/0b71159e19bef95069e18d17296291916e89b5cd
/usr/share/package-licenses/kcolorscheme/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
/usr/share/package-licenses/kcolorscheme/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kcolorscheme/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcolorscheme/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kcolorscheme/fa05e58320cb7c64786b26396f4b992579a628bc

%files locales -f kcolorscheme6.lang
%defattr(-,root,root,-)

