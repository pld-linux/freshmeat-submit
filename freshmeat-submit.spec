%include	/usr/lib/rpm/macros.python
Summary:	Submit release information to freshmeat.net
Name:		freshmeat-submit
Version:	1.4
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.catb.org/~esr/freshmeat-submit/%{name}-%{version}.tar.gz
# Source0-md5:	ab45def4807f8ee8da9d877eb3175f90
BuildRequires:	rpm-pythonprov
Requires:	python
URL:		http://www.catb.org/~esr/freshmeat-submit/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
freshmeat-submit is a script that supports remote submission of
release updates to Freshmeat via its XML-RPC interface. It is intended
for use in project release scripts. It reads the metadata from an
RFC-2822-like message on standard input, possibly with overrides by
command-line switches.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
rm -rf "$RPM_BUILD_ROOT"
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install freshmeat-submit $RPM_BUILD_ROOT%{_bindir}
install freshmeat-submit.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
