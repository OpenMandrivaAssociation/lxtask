Summary:	Lightweight and desktop independent task manager
Name:		lxtask
Version:	0.1.10
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
#Patch0:	lxtask-0.1.4-automake_113.patch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)

%description
Lightweight and desktop independent task manager.

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man1/lxtask.1.*
