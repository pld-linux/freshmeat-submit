Summary:	Submit release information to freshmeat.net
Summary(pl):	Wysy³anie informacji o wydaniach na freshmeat.net
Name:		freshmeat-submit
Version:	1.6
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.catb.org/~esr/freshmeat-submit/%{name}-%{version}.tar.gz
# Source0-md5:	0c08186b4f0bd6d026c45c3028ed2ccc
URL:		http://www.catb.org/~esr/freshmeat-submit/
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
freshmeat-submit is a script that supports remote submission of
release updates to Freshmeat via its XML-RPC interface. It is intended
for use in project release scripts. It reads the metadata from an
RFC-2822-like message on standard input, possibly with overrides by
command-line switches.

%description -l pl
freshmeat-submit to skrypt wspomagaj±cy zdalne wysy³anie uaktualnieñ
informacji o wydaniach na Freshmeacie poprzez interfejs XML-RPC. Jest
przeznaczony do u¿ywania w skryptach u¿ywanych przy wydawaniu
projektów. Odczytuje metadane z wiadomo¶ci w stylu RFC-2822 ze
standardowego wej¶cia z mo¿liwymi przykryciami poprzez opcje z linii
poleceñ.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install freshmeat-submit $RPM_BUILD_ROOT%{_bindir}
install freshmeat-submit.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
