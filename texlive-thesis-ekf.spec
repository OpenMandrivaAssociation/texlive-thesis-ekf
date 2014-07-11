# revision 34208
# category Package
# catalog-ctan /macros/latex/contrib/thesis-ekf
# catalog-date 2014-05-22 00:39:42 +0200
# catalog-license lppl1.2
# catalog-version 1.0
Name:		texlive-thesis-ekf
Version:	1.0
Release:	2
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
%{_texmfdistdir}/tex/latex/thesis-ekf/thesis-ekf.cls
%doc %{_texmfdistdir}/doc/latex/thesis-ekf/README
%doc %{_texmfdistdir}/doc/latex/thesis-ekf/images/ekf-logo1.png
%doc %{_texmfdistdir}/doc/latex/thesis-ekf/images/ekf-logo2.pdf
%doc %{_texmfdistdir}/doc/latex/thesis-ekf/magyar.ldf
%doc %{_texmfdistdir}/doc/latex/thesis-ekf/szakdolgozat1.pdf
%doc %{_texmfdistdir}/doc/latex/thesis-ekf/szakdolgozat1.tex
%doc %{_texmfdistdir}/doc/latex/thesis-ekf/szakdolgozat2.pdf
%doc %{_texmfdistdir}/doc/latex/thesis-ekf/szakdolgozat2.tex
%doc %{_texmfdistdir}/doc/latex/thesis-ekf/thesis-ekf.pdf
#- source
%doc %{_texmfdistdir}/source/latex/thesis-ekf/thesis-ekf.dtx
%doc %{_texmfdistdir}/source/latex/thesis-ekf/thesis-ekf.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
