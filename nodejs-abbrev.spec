%define		pkg	abbrev
Summary:	Abbreviation calculator for Node.js
Name:		nodejs-%{pkg}
Version:	1.0.5
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/abbrev/-/abbrev-%{version}.tgz
# Source0-md5:	73e04446fa70cacc5536e5cb7d83ccb0
URL:		https://github.com/isaacs/abbrev-js
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calculate the set of unique abbreviations for a given set of strings.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
