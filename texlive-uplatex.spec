Name:		texlive-uplatex
Version:	64072
Release:	1
Summary:	pLaTeX2e and miscellaneous macros for upTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uplatex
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uplatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uplatex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uplatex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides pLaTeX2e macros for upTeX by Takuji Tanaka.
This is a community edition syncing with platex. The bundle
depends on platex.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/uplatex
%{_texmfdistdir}/texmf-dist/tex/uplatex
%doc %{_texmfdistdir}/texmf-dist/doc/uplatex
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/uplatex.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/uplatex.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
