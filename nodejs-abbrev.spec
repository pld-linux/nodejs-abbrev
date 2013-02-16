%define		pkg	abbrev
Summary:	Abbreviation calculator for Node.js
Name:		nodejs-%{pkg}
Version:	1.0.4
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/abbrev-js
Source0:	http://registry.npmjs.org/abbrev/-/abbrev-%{version}.tgz
# Source0-md5:	85aa5087294a43d964af949deb0fca86
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
cp -pr lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
