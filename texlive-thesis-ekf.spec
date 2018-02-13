Name:		texlive-thesis-ekf
Version:	2.2
Release:	1
Summary:	Thesis class for Eszterhazy Karoly College
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thesis-ekf
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-ekf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-ekf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-ekf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The distribution contains the files to generate the thesis
class, only.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/thesis-ekf
%doc %{_texmfdistdir}/doc/latex/thesis-ekf
#- source
%doc %{_texmfdistdir}/source/latex/thesis-ekf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
