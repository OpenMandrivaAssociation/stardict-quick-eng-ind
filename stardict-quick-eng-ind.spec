%define	version	2.4.2
%define release %mkrel 7
%define dict_format_version	2.4.2

Summary:	English -> Indonesian *Quick dictionary for StarDict 2
Name:		stardict-quick-eng-ind
Version:	%{version}
Release:	%{release}
License:	Distributable
Group:		Databases
URL:		http://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-quick_eng-ind-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
English -> Indonesian *Quick dictionary in StarDict 2 format.
*Quick is an open source translation application. For more info, visit

http://www.futureware.at/.

%prep
%setup -q -n stardict-quick_eng-ind-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stardict/dic
install -m 0644 * $RPM_BUILD_ROOT%{_datadir}/stardict/dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*


