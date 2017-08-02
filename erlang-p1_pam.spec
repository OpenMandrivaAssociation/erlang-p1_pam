%global srcname p1_pam
# The Fedora Erlang convention is to avoid separating the debug symbols:
# https://fedoraproject.org/wiki/User:Peter/Erlang_Packaging_Guidelines
%global debug_package %{nil}


Name:       erlang-%{srcname}
Version:    1.0.0
Release:    %mkrel 1
Group:      Development/Erlang
Summary:    Library for ejabberd for PAM authentication support
License:    GPLv2
URL:        https://github.com/processone/epam/
Source0:    https://github.com/processone/epam/archive/%{version}.tar.gz

BuildRequires: erlang-rebar
BuildRequires: erlang-rpm-macros
BuildRequires: pam-devel

Requires: erlang-erts


%description
An Erlang library for ejabberd that helps with PAM authentication.


%prep
%autosetup -n epam-%{version}


%build
%rebar_compile


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/bin

install -pm644 ebin/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin
install -pm755 priv/bin/epam $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/bin/


%files
%license COPYING
%doc README.md
%{_erllibdir}/%{srcname}-%{version}


%changelog
* Fri May 06 2016 neoclust <neoclust> 1.0.0-1.mga6
+ Revision: 1009911
- imported package erlang-p1_pam

