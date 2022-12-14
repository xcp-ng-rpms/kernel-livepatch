%global package_speccommit 07888cf92e2205d9b0bd987e12ae7e464741f915
%global package_srccommit v1.0.1

%global TO_VER_REL 4.19.19-8.0.19

Name: kernel-livepatch
Summary: Live patches for Linux
Version: 1.0.1
Release: 1%{?xsrel}%{?dist}

Group: System Environment/Kernel
License: GPLv2
Source0: kernel-livepatch-1.0.1.tar.gz

BuildRequires: kpatch-devel
BuildRequires: bc
BuildRequires: bison
BuildRequires: flex
BuildRequires: elfutils

# BuildRequires for each base
# END

%description
Contains live patches to be applied against various Linux versions.


%prep
%autosetup -p1


%build
./build-livepatches %{TO_VER_REL}


%install
install -d -m 755 "%{buildroot}/usr/lib/kernel-livepatch"

if ls out/* > /dev/null 2>&1; then
    for lp in out/*/*.ko; do
        chmod 755 "${lp}"
        ln -sf "$(basename ${lp})" "$(dirname ${lp})/livepatch.ko"
    done

    mv out/* "%{buildroot}/usr/lib/kernel-livepatch"
fi


%files
%defattr(-,root,root)
%{_usr}/lib/kernel-livepatch


%changelog
* Wed Jul 20 2022 Ming Lu <ming.lu@citrix.com> - 1.0.1-1
- Initial release

* Mon Nov 29 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.0.0-1
- Initial packaging
