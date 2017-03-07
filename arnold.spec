# note: 20040104 release has heavily broken unix port
Summary:	Amstrad CPC Emulator
Summary(pl.UTF-8):	Emulator Amstrada CPC
Name:		arnold
Version:	0.20040104
Release:	0.1
License:	GPL v2+ (except ROMs)
Group:		Applications/Emulators
Source0:	http://arnold.emuunlim.com/download/arnsrc04012004.zip
# Source0-md5:	bf612e1bd535930f1c32c00811bc24dd
Patch0:		%{name}-build.patch
URL:		http://arnold.emuunlim.com/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Amstrad/Schneider CPC, Plus/CPC+ and VEB Mikroelektronik KC Compact
emulator.

The ROMs are (c) Copyright Amstrad plc and Locomotive Software Ltd,
distributed with this program with permission of Amstrad plc.

%description -l pl.UTF-8
Emulator Amstrada/Schneidera CPC, Plus/CPC+ oraz VEB Mikroelektronik
KC Compact.

Dołączone obrazy ROMów są objęte przez copyright Amstrad plc i
Locomotive Software Ltd, z tym programem są rozprowadzane za zgodą
Amstrad plc.

%prep
%setup -q -n %{name}
%patch0 -p1

%{__rm} src/configure

%build
cd src
%ifarch %{ix86} %{x8664} x32 alpha mipsel
CPPFLAGS="%{rpmcppflags} -DCPC_LSB_FIRST"
%endif
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install arnold $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc arnold_readme.txt file_id.diz readme.* whatsnew.*
%lang(es) %doc leeme.* novedades.linux
%attr(755,root,root) %{_bindir}/arnold
