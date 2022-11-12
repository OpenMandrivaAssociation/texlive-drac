Name:		texlive-drac
Version:	15878
Release:	1
Summary:	Declare active character substitution, robustly
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/drac
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drac.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drac.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros \DeclareRobustActChar and
ReDeclareRobActChar. One uses \DeclareRobustActChar in the same
way one would use \DeclareRobustCommand; the macro \protects
the active character when it appears in a moving argument.
ReDeclareRobActChar redefines an active character previously
defined with \DeclareRobustActChar, in the same way that
\renewcommand works for ordinary commands.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
