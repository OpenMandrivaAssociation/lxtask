Summary:	Lightweight and desktop independent task manager
Name:		lxtask
Version:	0.1.4
Release:	9
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
Patch0:	lxtask-0.1.4-automake_113.patch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)

%description
Lightweight and desktop independent task manager.

%prep
%setup -q
%autopatch -p1
./autogen.sh

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop

