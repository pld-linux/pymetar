Summary:	pymetar downloads the weather reports.
Summary(pl.UTF-8):	pymetar jest biblioteką ściągającą raporty pogody.
Name:		pymetar
Version:	0.13
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.schwarzvogel.de/pkgs/%{name}-%{version}.tar.gz
# Source0-md5:	84b6737b101daf5647a60d0d93d7783a
URL:		http://www.schwarzvogel.de/software-pymetar.shtml
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library downloads the weather report for a given station ID (get yours here), decodes it and provides easy access to all the data found in the report.


%prep
%setup -q
find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS TODO
%attr(755,root,root) %{_bindir}/weather.py
%{py_sitescriptdir}/pymetar-*egg-info
%{py_sitescriptdir}/pymetar.py[co]
