%global tl_name thesis-ekf
%global tl_revision 77332

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.0
Release:	%{tl_revision}.1
Summary:	Thesis class for Eszterhazy Karoly Catholic University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thesis-ekf
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-ekf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-ekf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-ekf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides a LaTeX class for theses and dissertations at
Eszterhazy Karoly Catholic University (Eger, Hungary). The documentation
is written in Hungarian.

