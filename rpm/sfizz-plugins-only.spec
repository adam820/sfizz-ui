%global debug_package %{nil}
%global source_date_epoch_from_changelog 1

Name:      sfizz-ui
Version:   1.2.3
Release:   3.1
License:   BSD-2-Clause
Group:     Productivity/Multimedia/Sound/Players
Summary:   Sampler plugins for SFZ instruments
Url:       https://github.com/sfztools/sfizz-ui
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: git gcc gcc-c++ cmake

BuildRequires: abseil-cpp-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel libxcb-devel xcb-util-devel xcb-util-cursor-devel xcb-util-keysyms-devel libxkbcommon-devel libxkbcommon-x11-devel fontconfig-devel cairo-devel pango-devel
BuildRequires: freetype-devel

# disable LTO to work around static library problems
%define _lto_cflags %{nil}

%description
Sfizz is a musical sampler, available as LV2 and VST plugins for musicians

%package -n lv2-sfizz-ui
Summary: Sfizz musical sampler LV2 plugin for SFZ instruments

%package -n sfizz-ui-vst3
Summary: Sfizz musical sampler VST3 plugin for SFZ instruments

%description -n lv2-sfizz-ui
Sfizz is a musical sampler, available as LV2 plugin for musicians

%description -n sfizz-ui-vst3
Sfizz is a musical sampler, available as VST3 plugin for musicians

%prep
%setup -q -n sfizz-ui-%{version}

%build
%cmake  -DENABLE_LTO=ON \
        -DSFIZZ_JACK=OFF \
        -DSFIZZ_RENDER=OFF \
        -DPLUGIN_PUREDATA=OFF \
        -DLV2_PLUGIN_INSTALL_DIR=%{_libdir}/lv2 \
        -DPLUGIN_LV2=ON -DPLUGIN_VST3=ON \
        -DSFIZZ_USE_SNDFILE=OFF \
        -DSFIZZ_USE_SYSTEM_ABSEIL=ON \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_CXX_STANDARD=17 .
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/usr/lib64/vst3/sfizz.vst3
mv -v %{buildroot}/usr/lib/vst3/sfizz.vst3 %{buildroot}/usr/lib64/vst3/sfizz.vst3

rm -f %{buildroot}/usr/lib64/libsfizz.so*
rm -f %{buildroot}/usr/lib64/pkgconfig/sfizz.pc
rm -rf %{buildroot}/usr/lib/.build-id
rm -rf %{buildroot}/usr/lib/debug
rm -rf %{buildroot}/usr/include

#%files
%files -n lv2-sfizz-ui
%dir %{_libdir}/lv2/sfizz.lv2
%{_libdir}/lv2/sfizz.lv2/*

%files -n sfizz-ui-vst3
%dir %{_libdir}/vst3/sfizz.vst3
%{_libdir}/vst3/sfizz.vst3/*

%clean
rm -rf %{buildroot}

%changelog
* Tue Oct 07 2025 Adam D <1794794+adam820@users.noreply.github.com> - 1.2.3-1
- Adapt spec and build plugins only for F42 COPR
* Wed May 24 2023 Paul Ferrand <paul@ferrand.cc> - 1.2.3-1
- New version
* Wed May 24 2023 redtide <redtide@sfz.tools> - 1.2.1-1
- New version
* Tue Oct 26 2021 Paul Ferrand <paul@ferrand.cc> - 1.1.0-1
- New version
* Fri Apr 16 2021 Jean Pierre Cimalando <jp-dev@inbox.ru> - 12345678-1
- Build from the stable release channel
