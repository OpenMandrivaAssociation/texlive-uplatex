%global tl_name uplatex
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	pLaTeX2e and miscellaneous macros for upTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/uplatex
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uplatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uplatex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uplatex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(babel)
Requires:	texlive(cm)
Requires:	texlive(firstaid)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(l3backend)
Requires:	texlive(l3backend-dev)
Requires:	texlive(l3kernel)
Requires:	texlive(l3kernel-dev)
Requires:	texlive(latex)
Requires:	texlive(latex-base-dev)
Requires:	texlive(latex-firstaid-dev)
Requires:	texlive(latex-fonts)
Requires:	texlive(platex)
Requires:	texlive(tex-ini-files)
Requires:	texlive(unicode-data)
Requires:	texlive(uplatex.bin)
Requires:	texlive(uptex)
Requires:	texlive(uptex-fonts)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides pLaTeX2e macros for upTeX by Takuji Tanaka. This is
a community edition syncing with platex. The bundle depends on platex.

