# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       x10iii-cam-button

# >> macros
# << macros
%define theme sailfish-default

Summary:    Toggle XPeria 10III Cameras
Version:    0.3.2
Release:    0
Group:      Applications
License:    ASL 2.0
BuildArch:  noarch
URL:        https://github.com/nephros/x10iii-cam-button
Source0:    %{name}-%{version}.tar.gz
Source100:  x10iii-cam-button.yaml
Requires:   droid-system-pdx213
Requires:   sailfish-version >= 4.4.0
Requires:   /usr/bin/pkill
Requires:   /bin/sed
Requires(preun): systemd
Requires(post): systemd
Requires(postun): systemd
BuildRequires:  qml-rpm-macros
BuildRequires:  qt5-qmake
BuildRequires:  qt5-qttools-linguist
BuildRequires:  sailfish-svg2png
BuildRequires:  systemd

%description
Adds a Top Menu switch to toggle triple cameras on Xperia 10 III.

Tapping that will modify a vendor config file and kill the camera service,
after which Camera apps will gain access to all three cameras.

Note that enabling triple cameras DISABLES the front (selfie) camera (and the other way around).

You should only toggle the button while any applications using the camera
are STOPPED. I.e. close camera apps, and anything else like video chats
etc.

Also this will ONLY install on X10III devices, and they MUST be running SFOS 4.4 or later!
%if "%{?vendor}" == "chum"
PackageName: X10III Triple Camera Toggle
Type: desktop-application
DeveloperName: nephros
Categories:
  - System
  - Settings
Custom:
  Repo: %{url}
Icon: https://sailfishos.org/content/sailfishos-docs//sailfish-content-graphics-default/latest/images/icon-cover-camera.svg
Screenshots:
       - %{url}/raw/master/Screenshot_001.png
       - %{url}/raw/master/Screenshot_002.png
       - %{url}/raw/master/Screenshot_003.png
Url:
  Homepage: %{url}
  Help: https://docs.sailfishos.org/Support/Help_Articles/Camera/#multiple-cameras-of-xperia-10-iii
  Bugtracker: %{url}/issues
  Donation: https://openrepos.net/donate
%endif


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# mangle version info
sed -i -e "s/@@UNRELEASED@@/%{version}-%{release}/" %{buildroot}%{_datadir}/jolla-settings/pages/%{name}/EnableSwitch.qml
# << install post

%preun
# >> preun
if [ $1 == 0 ]; then #uninstall
systemctl stop org.nephros.sailfish.x10iiicamera.service
fi
# << preun

%post
# >> post
systemctl daemon-reload ||:
# << post

%postun
# >> postun
if [ $1 == 0 ]; then #uninstall
systemctl daemon-reload
fi
# << postun

%files
%defattr(-,root,root,-)
%{_unitdir}/org.nephros.sailfish.x10iiicamera.service
%{_datadir}/jolla-settings/entries/%{name}.json
%{_datadir}/jolla-settings/pages/%{name}/EnableSwitch.qml
%{_datadir}/translations/*.qm
%{_datadir}/themes/%{theme}/meegotouch/z*/icons/*.png
# >> files
# << files
