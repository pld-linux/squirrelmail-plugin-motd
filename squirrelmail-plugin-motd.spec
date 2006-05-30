%define		_plugin	motd
%define		mversion	1.0.3
Summary:	Plugin that allows MOTD on login page
Summary(pl):	Wtyczka pozwalaj±ca umie¶ciæ MOTD na stronie logowania
Name:		squirrelmail-plugin-%{_plugin}
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}.%{version}-%{mversion}.tar.gz
# Source0-md5:	d76f2f5282dfc4a4c90dc28326d92b4b
Patch0:		%{name}-ri_once.patch
URL:		http://www.squirrelmail.org/
Requires:	squirrelmail >= 1.4.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}

%description
This plugin will allow you to place a "Message of the Day" on the
loginscreen.

%description -l pl
Ta wtyczka pozwoli Ci zamie¶ciæ "Wiadomo¶æ Dnia" ("Message of the
Day") na stronie logowania.

%prep
%setup -q -n %{_plugin}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

install *.php $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_plugindir}
%{_plugindir}/*.php
