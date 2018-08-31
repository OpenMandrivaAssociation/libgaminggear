#
# spec file for package libgaminggear
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define majorversion 0
%define libgaminggear       libgaminggear0
%define libgaminggearfx     libgaminggearfx0
%define libgaminggearwidget libgaminggearwidget0
%define libname %mklibname gaminggear %{major}
%define devname %mklibname gaminggear -d
Name:           libgaminggear
Version:        0.15.1
Release:        1
Summary:        Library for gaming input devices
License:        GPL-2.0 and CC-BY-3.0
Group:          System/Libraries
Url:            https://sourceforge.net/projects/libgaminggear/
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  cmake >= 2.6.4
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(sqlite3) >= 3.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A shared library initiated by the Roccat Linux driver project.

%package devel
Summary:        Development files for gaming input devices
Group:          System/Libraries
Requires:       %{libgaminggearfx} = %{version}
Requires:       %{libgaminggearwidget} = %{version}
Requires:       %{libgaminggear} = %{version}

%description devel
This package contains the header files, static libraries and
development documentation for libgaminggear. If you like to develop
programs using libgaminggear, you will need to install this package.

%package -n %{libgaminggear}
Summary:        Gaming input devices library - libgaminggear
Group:          System/Libraries

%description -n %{libgaminggear}
A shared library initiated by the Roccat Linux driver project.

This package holds libgaminggear.

%package -n %{libgaminggearfx}
Summary:        Gaming input devices library - libgaminggearfx
Group:          System/Libraries

%description -n %{libgaminggearfx}
A shared library initiated by the Roccat Linux driver project.

This package holds libgaminggearfx.

%package -n %{libgaminggearwidget}
Summary:        Gaming input devices library - libgaminggearwidget
Group:          System/Libraries

%description -n %{libgaminggearwidget}
A shared library initiated by the Roccat Linux driver project.

This package holds libgaminggearwidget.

#lang_package

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
cd build
%{__rm} -rf "%{buildroot}"
%{__make} -r %{?_smp_mflags} DESTDIR="%{buildroot}" install

%post   -n %{libgaminggear} -p /sbin/ldconfig
%postun -n %{libgaminggear} -p /sbin/ldconfig
%post   -n %{libgaminggearfx} -p /sbin/ldconfig
%postun -n %{libgaminggearfx} -p /sbin/ldconfig
%post   -n %{libgaminggearwidget} -p /sbin/ldconfig
%postun -n %{libgaminggearwidget} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README COPYING Changelog
%{_bindir}/gaminggearfxcontrol
%{_bindir}/gaminggearfxinfo
%{_datadir}/libgaminggear/

%files -n %{libgaminggear}
%defattr(-, root, root)
%doc README COPYING Changelog
%{_libdir}/libgaminggear.so.*
%{_datadir}/locale/*/LC_MESSAGES/libgaminggear.mo

%files -n %{libgaminggearfx}
%defattr(-, root, root)
%doc README COPYING Changelog
%{_libdir}/libgaminggearfx.so.*

%files -n %{libgaminggearwidget}
%defattr(-, root, root)
%doc README COPYING Changelog
%{_libdir}/libgaminggearwidget.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/gaminggear-0/
%{_libdir}/libgaminggear*.so
%{_datadir}/pkgconfig/gaminggear-%{majorversion}.pc
%{_datadir}/cmake/Modules/FindGAMINGGEAR%{majorversion}.cmake
