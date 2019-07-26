%bcond_without check

Name:          sbsigntools
Version:       0.9.2
Release:       2%{?dist}
Summary:       Signing utility for UEFI secure boot
License:       GPLv3+
URL:           https://build.opensuse.org/package/show/home:jejb1:UEFI/sbsigntools
# upstream tarballs don't include bundled ccan
# run sbsigntools-mktarball.sh
Source0:       %{name}-%{version}.tar.xz
Source1:       %{name}-mktarball.sh
# don't fetch ccan or run git from autogen.sh, already done by mktarball.sh
Patch0:        %{name}-no-git.patch
# add Fedora gnu-efi path and link statically against libefi.a/libgnuefi.a
Patch1:        %{name}-gnuefi.patch
# same as gnu-efi
ExclusiveArch: x86_64 aarch64 %{arm} %{ix86}
BuildRequires: automake
BuildRequires: binutils-devel
BuildRequires: gcc
BuildRequires: gnu-efi-devel >= 3.0.8-3
BuildRequires: help2man
BuildRequires: libuuid-devel
%if %{with check}
BuildRequires: openssl
%endif
BuildRequires: openssl-devel
Provides: bundled(ccan-array_size)
Provides: bundled(ccan-build_assert)
Provides: bundled(ccan-endian)
Provides: bundled(ccan-read_write_all)
Provides: bundled(ccan-talloc)

%description
Tools to add signatures to EFI binaries and Drivers.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%if %{with check}
%check
make check
%endif

%files
%license COPYING LICENSE.GPLv3 lib/ccan/licenses/*
%doc AUTHORS ChangeLog
%{_bindir}/sbattach
%{_bindir}/sbkeysync
%{_bindir}/sbsiglist
%{_bindir}/sbsign
%{_bindir}/sbvarsign
%{_bindir}/sbverify
%{_mandir}/man1/sbattach.1.*
%{_mandir}/man1/sbsiglist.1.*
%{_mandir}/man1/sbsign.1.*
%{_mandir}/man1/sbvarsign.1.*
%{_mandir}/man1/sbverify.1.*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Dominik Mierzejewski <dominik@greysector.net> - 0.9.2-1
- update to 0.9.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Dominik Mierzejewski <dominik@greysector.net> - 0.9.1-3
- fix paths to gnu-efi (work around #1608293)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Dominik Mierzejewski <dominik@greysector.net> - 0.9.1-1
- update to 0.9.1
- add Fedora gnu-efi libs location to search path
- link tests statically against gnu-efi libs, there are no shared versions

* Mon Sep  4 2017 Dominik Mierzejewski <dominik@greysector.net> - 0.8-1
- initial build
