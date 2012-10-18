%define		packname	ROC

Summary:	Utilities for ROC, with uarray focus
Name:		R-%{packname}
Version:	1.34.0
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	f316540fd92c5700b726630235b8359e
URL:		http://www.bioconductor.org/packages/release/bioc/html/ROC.html
BuildRequires:	R-Biobase
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-Biobase
Requires:	R
Requires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for ROC, with uarray focus.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/%{packname}.so
