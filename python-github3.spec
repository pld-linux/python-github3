%define 	module	github3
Summary:	Github API v3 library for Python
Name:		python-%{module}
Version:	0.0.11
Release:	1
License:	New BSD License
Group:		Development/Languages/Python
Source0:	https://github.com/ChristopherMacGown/python-github3/tarball/master/%{name}.tgz
# Source0-md5:	a0e539279d0169ecd163c8adf0bcb144
URL:		https://github.com/ChristopherMacGown/python-github3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python library to take advantage of the new API. It is still
in development and the interfaces may (read: will) change but is full
featured enough now to be used for most tasks of the new API.

%prep
%setup -qc
mv *-%{module}-*/* .

%build
ver=$(awk -F"'" '/version/{print $2}' setup.py)
test "$ver" = %{version}

%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HACKING
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/python_%{module}-*.egg-info
%endif
