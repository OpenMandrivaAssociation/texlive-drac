# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/drac
# catalog-date 2008-08-17 11:40:59 +0200
# catalog-license lppl
# catalog-version 1
Name:		texlive-drac
Version:	1
Release:	1
Summary:	Declare active character substitution, robustly
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/drac
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drac.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drac.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides macros \DeclareRobustActChar and
ReDeclareRobActChar. One uses \DeclareRobustActChar in the same
way one would use \DeclareRobustCommand; the macro \protects
the active character when it appears in a moving argument.
ReDeclareRobActChar redefines an active character previously
defined with \DeclareRobustActChar, in the same way that
\renewcommand works for ordinary commands.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/drac/drac.sty
%doc %{_texmfdistdir}/doc/latex/drac/drac-fr.pdf
%doc %{_texmfdistdir}/doc/latex/drac/drac.pdf
#- source
%doc %{_texmfdistdir}/source/latex/drac/LISEZMOI
%doc %{_texmfdistdir}/source/latex/drac/Makefile
%doc %{_texmfdistdir}/source/latex/drac/README
%doc %{_texmfdistdir}/source/latex/drac/drac-en.dtx
%doc %{_texmfdistdir}/source/latex/drac/drac-fr.dtx
%doc %{_texmfdistdir}/source/latex/drac/drac.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
