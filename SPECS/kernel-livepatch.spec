%global package_speccommit 0e0e2e526b460d499edd786129446216e651d12e
%global package_srccommit v1.0.4

%global TO_VER_REL 4.19.19-8.0.33.xs8

Name: kernel-livepatch
Summary: Live patches for Linux
Version: 1.0.4
Release: 1%{?xsrel}%{?dist}

Group: System Environment/Kernel
License: GPLv2
Source0: kernel-livepatch-1.0.4.tar.gz

BuildRequires: kpatch-devel

# BuildRequires for each base
BuildRequires: kernel-lp-devel_4.19.19_8.0.32.xs8
# EndBuildRequires

# Provides for each live patch
Provides: livepatch(component/kernel/base/4.19.19-8.0.32.xs8/to/4.19.19-8.0.33.xs8/base-buildid/5de7b009ae6f0dee93f7d3f7041f9ef51502fdfb)
# EndProvides

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
* Mon Jan 15 2024 Alejandro Vallejo <alejandro.vallejo@cloud.com> - 1.0.4-1
- CA-387401: Add XSA-448 livepatch to release 8.0.32

* Wed Sep 13 2023 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.0.3-1
- CP-38520: Add Jira support to query released Kernel in last 6 months
- CA-378916: Drop hard-coded build dependencies
- CA-378916: Increase the length of module names to 55
- CA-378916: Run prepare-build script if it exists

* Wed Jul 20 2022 Ming Lu <ming.lu@citrix.com> - 1.0.1-1
- Initial release

* Mon Nov 29 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.0.0-1
- Initial packaging
