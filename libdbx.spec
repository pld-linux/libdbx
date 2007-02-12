Summary:	Tools for conversion of Outlook Express files to mailbox format
Summary(pl.UTF-8):   Narzędzia do konwersji plików Outlook Expressa do formatu mailbox
Name:		libdbx
Version:	1.0.3
Release:	1
License:	GPL
Group:		Applications/Files
Source0:	http://dl.sourceforge.net/ol2mbox/%{name}_%{version}.tgz
# Source0-md5:	fa169c99d5245c836f017badf392529d
URL:		http://sourceforge.net/projects/ol2mbox/
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides tools for the conversion of Outlook Express data
files to standard mailbox format.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do konwersji plików z danymi Outlook
Expressa do standardowego formatu skrzynek (mailbox).

%package devel
Summary:	libdbx development files
Summary(pl.UTF-8):   Pliki programistyczne libdbx
Group:		Development/Libraries
# doesn't require base

%description devel
libdbx development files (header and object files).

%description devel -l pl.UTF-8
Pliki programistyczne libdbx (pliki nagłówkowe i obiektowe).

%prep
%setup -q -n %{name}_%{version}

%build
# makefile would need rewrite
%{__cc} %{rpmcflags} -c libdbx.c timeconv.c readdbx.c readoe.c
%{__cxx} %{rpmcflags} -c libdbx++.cpp

%{__cc} %{rpmldflags} -o readdbx readdbx.o libdbx.o timeconv.o
%{__cc} %{rpmldflags} -o readoe readoe.o libdbx.o timeconv.o 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install readdbx readoe $RPM_BUILD_ROOT%{_bindir}
install libdbx.o libdbx++.o $RPM_BUILD_ROOT%{_libdir}
install libdbx.h libdbx++.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%doc FILE-FORMAT README.libdbx*
%{_libdir}/*.o
%{_includedir}/*.h
