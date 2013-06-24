%define		module	github3
Summary:	Github API v3 library for Python
Name:		python-%{module}
Version:	0.5
Release:	1
License:	ISC
Group:		Development/Languages/Python
Source0:	https://github.com/copitux/python-github3/tarball/%{version}/%{name}-%{version}.tgz
# Source0-md5:	2978ebf0ef709e436eb34f6c3a9e9a7c
URL:		https://github.com/copitux/python-github3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
Requires:	python-requests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pygithub3 is a wrapper to the Github API v3, written in Python.

It has been developed with extensibility in mind, because the API is
in a beta state, trying to achieve a very loosly coupled software.

It should be very easy to extend to support new requests and
resources, because each of them are managed by itself.

%prep
%setup -qc
mv *-%{module}-*/* .

%build
ver=$(%{__python} -c "import  pygithub3; print pygithub3.__version__")
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
%doc AUTHORS.rst README.rst LICENSE requirements/base.txt docs
%{py_sitescriptdir}/pygithub3
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pygithub3-%{version}-*.egg-info
%endif
