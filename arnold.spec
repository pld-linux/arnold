Summary:	Amstrad CPC Emulator
Summary(pl):	Emulator Amstrada CPC
Name:		arnold
Version:	0.20020127
Release:	0.9
License:	GPL
Group:		Applications
Source0:	http://arnold.emuunlim.com/download/arnsrc27012002.zip
#Source0-md5:	a8ae9ce1aeeae6ba9a19083731811150
Patch0:		%{name}-romsdir.patch
BuildRequires:	SDL-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Empty

%description -l pl
Empty

%prep
%setup -q -n arnold
%patch0 -p1

%build
cd src
chmod a+x configure
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/arnold
install -d $RPM_BUILD_ROOT%{_bindir}
cp -Rf roms $RPM_BUILD_ROOT%{_datadir}/arnold
install arnold $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%doc readme.linux
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/arnold
%dir %{_datadir}/arnold/roms
%dir %{_datadir}/arnold/roms/*
%attr(644,root,root) %{_datadir}/arnold/roms/*/*
