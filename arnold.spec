# note: 20040104 release is on DEVEL branch, but its unix port is heavily broken; stick to 20020127
Summary:	Amstrad CPC Emulator
Summary(pl.UTF-8):	Emulator Amstrada CPC
Name:		arnold
Version:	0.20020127
Release:	2
License:	GPL v2+ (except ROMs)
Group:		Applications/Emulators
Source0:	http://arnold.emuunlim.com/download/arnsrc27012002.zip
# Source0-md5:	a8ae9ce1aeeae6ba9a19083731811150
Patch0:		%{name}-romsdir.patch
Patch1:		%{name}-build.patch
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
%patch1 -p1

%{__rm} src/configure

%build
cd src
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/arnold,%{_bindir}}

cp -Rf roms $RPM_BUILD_ROOT%{_datadir}/arnold
install arnold $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc bugsetc.txt file_id.diz readme.* whatsnew.*
%attr(755,root,root) %{_bindir}/arnold
%{_datadir}/arnold
