# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		3872237d397a82e6029247642d47561349e6a8cf
	%global commitdate	20230917
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	Lightweight and desktop independent task manager
Name:		lxtask
Version:	0.1.11
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/lxtask/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)

%description
Lightweight and desktop independent task manager.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man1/lxtask.1.*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	--enable-gtk3 \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name}

