\ProvidesClass{../class/slide}

\LoadClass[aspectratio=43]{beamer}



\usefonttheme[onlytext]{structurebold}

\renewcommand{\mathfamilydefault}{\rmdefault}


\RequirePackage{amsmath, tikz, pythontex, color, graphicx, epstopdf, animate, ifthen, colortbl, xcolor, calc, pgfplots, hyperref, amssymb, stmaryrd, wasysym, textcomp}
\RequirePackage[brazil]{babel}

\RequirePackage[skip=8pt plus1pt, indent=0pt]{parskip}
\RequirePackage[outputdir=../out, frozencache=false]{minted}
\usetikzlibrary{calc}
\usetikzlibrary{math}
\usetikzlibrary{backgrounds}
\usetikzlibrary{patterns}
\usetikzlibrary{patterns.meta}



\usemintedstyle[custompython]{pycharm}   % registrar style executando ./setup/register_style.py
%\usemintedstyle[python]{nord-darker}



% Define theme options %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\DeclareOption{dark}{
    \definecolor{background}{HTML}{2D2B24}
    \definecolor{textcolor}{HTML}{F4E3C3}
    \definecolor{primary}{HTML}{89C53F}
    \definecolor{secondary}{RGB}{234, 32, 38}
    \definecolor{codebackground}{RGB}{34, 32, 30}
    \definecolor{codetextcolor}{HTML}{BCBEC4}
    \renewcommand{\logo}{../class/figs/logo_ifsc}
}
\DeclareOption{light}{
    \definecolor{background}{HTML}{FFFEF9}
    \definecolor{textcolor}{HTML}{2D2B24}
    \definecolor{primary}{RGB}{47, 158, 64}
    \definecolor{secondary}{RGB}{205, 23, 30}
    \definecolor{codebackground}{RGB}{30, 31, 34}
    \definecolor{codetextcolor}{HTML}{BCBEC4}
    \renewcommand{\logo}{../class/figs/logo_ifsc_oficial}
}
\ExecuteOptions{dark} % Set default option
\ProcessOptions\relax % Process options
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\setminted{
    bgcolor=codebackground,
    fontsize=\scriptsize,
    framesep=3pt,
    rulecolor=codetextcolor,
    autogobble=true
}



\RequirePackage{tcolorbox}
\tcbset{
    colframe=codebackground,
    colback=codebackground,
    boxsep=0em,
    arc=3pt,
    left=2pt, right=2pt, top=2pt, bottom=2pt
}

\RequirePackage{fontspec}
\setmonofont{JetBrains Mono NL medium}












% Aplicar cores ao tema
\setbeamercolor{background canvas}{bg=background}
\setbeamercolor{normal text}{fg=textcolor}
\setbeamercolor{frametitle}{fg=primary, bg=background}
\setbeamercolor{title}{fg=primary}
\setbeamercolor{itemize item}{fg=primary}
\setbeamercolor{alerted text}{fg=primary}

\setbeamertemplate{navigation symbols}{}



% Templates do Beamer
\setbeamertemplate{frametitle}[default][center]


\setbeamerfont{frametitle}{size=\huge}
\setbeamerfont{title}{size=\huge}
\setbeamerfont{author}{size=\normalfont}
\setbeamerfont{institute}{size=\small}
\setbeamerfont{date}{size=\small}
\setbeamerfont{subtitle}{size=\large}
%\setbeamerfont{normalfont}{size=\Huge}
%\setbeamerfont{normal text}{size=\Huge}

\renewcommand{\normalsize}{\fontsize{12pt}{14pt}\selectfont}
\setlength{\parskip}{6pt} % Define o espaçamento entre parágrafos
\setlength{\parindent}{0pt} % Remove o recuo da primeira linha
\setbeamertemplate{itemize/enumerate body begin}{\noindent}

\RequirePackage{enumitem}



\RequirePackage{pifont}
\setlist[itemize]{itemsep=0.5em, topsep=0pt, parsep=0pt, label={\ding{224}}}
%\setlist[itemize]{itemsep=0.5em, topsep=0pt, parsep=0pt, label={\ding{70}}}

%\RequirePackage{fdsymbol}
%\setlist[itemize]{itemsep=0pt, topsep=0pt, parsep=0pt, label={$\smallblackdiamond$}}
%\RequirePackage{fourier}
%\setlist[itemize]{itemsep=0pt, topsep=0pt, parsep=0pt, label={\starredbullet}}


\setbeamercovered{again covered={\opaqueness<1->{75}}}
%\setbeamercovered{dynamic}


\definecolor{pagenumber}{RGB}{90, 90, 90}

% Personalizar o rodapé
% Personalizar o rodapé com logo e numeração
\addtobeamertemplate{footline}{%
        \raggedright
        \hspace{2pt}\includegraphics[height=1cm]{\logo}
        \hfill
        \color{pagenumber}\insertframenumber/\inserttotalframenumber\hspace{2pt}
        \vspace{2pt}
}





% Comandos personalizados
\newcommand{\splitframe}[2]{%
  \begin{columns}
    \begin{column}{0.5\linewidth}
        \vspace{-0.7em}#1
    \end{column}
    \begin{column}{0.5\linewidth}
        \vspace{-0.7em}#2
    \end{column}
  \end{columns}
}





%\newenvironment{\pythoncode}{%não funciona
%\begin{tcolorbox}
%\begin{minted}{python}
%}{%
%\end{minted}
%\end{tcolorbox}
%}





\AtBeginEnvironment[text]{minted}{\color{codetextcolor}}
%\BeforeBeginEnvironment{minted}{\vspace{-0.5em}}
%\AfterEndEnvironment{minted}{\vspace{-3.0em}}





% Apply the theme in the document
%\AtBeginDocument{
%  \pagecolor{\themeBackground}
%  \color{\themeText}
%}


\newcommand{\nonumberfootnote}[1]{%
    \let\svthefootnote\thefootnote
    \let\thefootnote\relax
    \footnotetext{#1}%
    \let\thefootnote\svthefootnote
}
