\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{../class/IFSCreport}[IFSC]

\LoadClass[a4paper,10pt]{report}

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage[portuges,brazilian]{babel}
\RequirePackage[portuges,brazilian]{translator}
\RequirePackage{setspace}
\RequirePackage{amsmath}
%\RequirePackage{amssymb}
\RequirePackage{mathrsfs}
\RequirePackage{lastpage}
\RequirePackage{listings}
\RequirePackage{indentfirst}
\RequirePackage[skip=8pt plus1pt, indent=0pt]{parskip}
\RequirePackage[dvipsnames, xcdraw, table]{xcolor}
\RequirePackage{graphicx}
\RequirePackage{pdflscape}
\RequirePackage{epstopdf}
\RequirePackage{enumerate}
\RequirePackage{multirow}
\RequirePackage{fancyhdr}
\RequirePackage{sectsty}
\RequirePackage{colortbl}
\RequirePackage{diagbox} % substituto para \RequirePackage{slashbox}
\RequirePackage{tabularx}
\RequirePackage{mdframed}
%\RequirePackage[pdftex,pdfborder={0 0 0}]{hyperref}
\RequirePackage{ae}
\RequirePackage{pgfplots}
\RequirePackage{enumitem}
\RequirePackage{etoolbox}
\RequirePackage{subcaption}
\RequirePackage{biblatex}
\RequirePackage{booktabs}
\RequirePackage{xcolor}
%
\RequirePackage{lipsum}
%
\RequirePackage{tikz}
\usetikzlibrary{math}
\usetikzlibrary{tikzmark}
\usetikzlibrary{calendar}
%
\RequirePackage{fontspec}
\RequirePackage{fontawesome5}
\newfontfamily\monaco{JetBrains Mono NL medium}[NFSSFamily=Mono]
%
\RequirePackage[outputdir=../out, frozencache=false]{minted}
\usemintedstyle[custompython]{pycharm}
\usemintedstyle[text]{dracula}
%
\setminted{fontsize=\scriptsize}
\setminted[custompython]{fontfamily=Mono}
\definecolor{bg}{RGB}{30, 31, 34}
\definecolor{bg2}{HTML}{154360}
\definecolor{fg2}{HTML}{CCD1D1}
\setminted[custompython]{bgcolor=bg}
\setminted[text]{fontfamily=Mono}
\setminted[text]{bgcolor=bg2}
\renewcommand{\theFancyVerbLine}{\textcolor{darkgray}{\texttt{\fontsize{7}{8}\selectfont\arabic{FancyVerbLine}}}}
\setminted{numbersep=4pt}




%
\pgfdeclarelayer{back}
\pgfdeclarelayer{front}
\pgfsetlayers{back,main,front}









\AtBeginEnvironment[text]{minted}{\color{fg2}}
\BeforeBeginEnvironment{minted}{\vspace{-0.5em}}
\AfterEndEnvironment{minted}{\vspace{-3.0em}}



\newcounter{mymark}
\newcommand{\MarkMe}[5][]{\stepcounter{mymark}%
\tikzmark{mark-\number\value{mymark}}%

\begin{tikzpicture}[overlay,remember picture]
    \def\pv##1{\pgfkeysvalueof{/tikz/my mark/##1}}
    \draw[/tikz/my mark/arrow,line width=\pv{line width},yellow!50!red,shorten >=\pv{halo},
    shorten <=\pv{halo}]
    ([yshift=2pt]pic cs:mark-\number\value{mymark})
    --++ (#3,#4) node[#2, /tikz/my mark/mark node,align=center]{#5};
  \end{tikzpicture}}
\tikzset{my mark/.cd,
mark node/.style={fill=yellow!30,draw},
line width/.initial=0.6pt,
halo/.initial=0pt,
arrow/.style={latex-}}




\definecolor{code_bg}{rgb}{0.98, 0.98, 0.9}
\definecolor{console_bg}{rgb}{0.92, 0.95, 0.95}


%cusmom colors
\definecolor{mygreen}{RGB}{28,172,0}
\definecolor{c_keywords}{RGB}{170,55,241}
\definecolor{c_strings}{RGB}{170,55,241}
\definecolor{c_numbers}{rgb}{0.5,0.5,0.5}
\definecolor{c_backgrount}{rgb}{0.98,0.98,0.9}
\definecolor{c_comments}{rgb}{0.0,0.4,0.0}


%layout da página  (https://en.wikibooks.org/wiki/LaTeX/Page_Layout)
\setlength{\evensidemargin} {0mm}    %3
\setlength{\topmargin}      {15mm}   %4
\setlength{\headheight}     {9mm}   %5
\setlength{\headsep}        {6mm}    %6
\setlength{\textheight}     {245mm}  %7
\setlength{\textwidth}      {142mm}  %8
\setlength{\marginparsep}   {0mm}    %9
\setlength{\marginparwidth} {0mm}    %10
\setlength{\footskip}       {15mm}   %11
\setlength{\marginparpush}  {0mm}    %12
\setlength{\hoffset}        {-15mm}  %13
\setlength{\voffset}        {-1in}   %14
\setlength{\paperwidth}     {200mm}  %15
\setlength{\paperheight}    {297mm}  %16



% campos e comandos para capa, cabeçalho e rodapé
\newcommand{\thetitle}{\@title}
\newcommand{\theauthor}{\@author}

\newcommand{\@email}{}            \newcommand{\email}[1]{\renewcommand{\@email}{#1}}          \newcommand{\theemail}{\@email}

\newcommand{\@subject}{}            \newcommand{\subject}[1]{\renewcommand{\@subject}{#1}}          \newcommand{\thesubject}{\@subject}
%\newcommand{\@course}{}             \newcommand{\course}[1]{\renewcommand{\@course}{#1}}            \newcommand{\thecourse}{\@course}
\newcommand{\@subtitle}{}          \newcommand{\subtitle}[1]{\renewcommand{\@subtitle}{#1}}         \newcommand{\thesubtitle}{\@subtitle}
\newcommand{\@shorttitle}{}         \newcommand{\shorttitle}[1]{\renewcommand{\@shorttitle}{#1}}
%\newcommand{\@course}{}             \newcommand{\course}[1]{\renewcommand{\@course}{#1}}            \newcommand{\thecourse}{\@course}

\newcommand{\@cabecalho}{}          \newcommand{\cabecalho}[1]{\renewcommand{\@cabecalho}{#1}}
\renewcommand{\maketitle}{\capa}    \newcommand{\eq}[1]{(\ref{#1})}

\newcommand{\noteA}{\MarkMe{\posA}{\xA}{\yA}{\txtA}}
\newcommand{\posA}{}
\newcommand{\xA}{}
\newcommand{\yA}{}
\newcommand{\txtA}{}
\newcommand{\setNoteA}[4][right]{\renewcommand{\posA}{#1}\renewcommand{\xA}{#2} \renewcommand{\yA}{#3} \renewcommand{\txtA}{#4}}

\newcommand{\noteB}{\MarkMe{\posB}{\xB}{\yB}{\txtB}}
\newcommand{\posB}{}
\newcommand{\xB}{}
\newcommand{\yB}{}
\newcommand{\txtB}{}
\newcommand{\setNoteB}[4][right]{\renewcommand{\posB}{#1}\renewcommand{\xB}{#2} \renewcommand{\yB}{#3} \renewcommand{\txtB}{#4}}

\newcommand{\noteC}{\MarkMe{\posC}{\xC}{\yC}{\txtC}}
\newcommand{\posC}{}
\newcommand{\xC}{}
\newcommand{\yC}{}
\newcommand{\txtC}{}
\newcommand{\setNoteC}[4][right]{\renewcommand{\posC}{#1}\renewcommand{\xC}{#2} \renewcommand{\yC}{#3} \renewcommand{\txtC}{#4}}

\newcommand{\noteD}{\MarkMe{\posD}{\xD}{\yD}{\txtD}}
\newcommand{\posD}{}
\newcommand{\xD}{}
\newcommand{\yD}{}
\newcommand{\txtD}{}
\newcommand{\setNoteD}[4][right]{\renewcommand{\posD}{#1}\renewcommand{\xD}{#2} \renewcommand{\yD}{#3} \renewcommand{\txtD}{#4}}

\newcommand{\noteE}{\MarkMe{\posE}{\xE}{\yE}{\txtE}}
\newcommand{\posE}{}
\newcommand{\xE}{}
\newcommand{\yE}{}
\newcommand{\txtE}{}
\newcommand{\setNoteE}[4][right]{\renewcommand{\posE}{#1}\renewcommand{\xE}{#2} \renewcommand{\yE}{#3} \renewcommand{\txtE}{#4}}

\newcommand{\noteF}{\MarkMe{\posF}{\xF}{\yF}{\txtF}}
\newcommand{\posF}{}
\newcommand{\xF}{}
\newcommand{\yF}{}
\newcommand{\txtF}{}
\newcommand{\setNoteF}[4][right]{\renewcommand{\posF}{#1}\renewcommand{\xF}{#2} \renewcommand{\yF}{#3} \renewcommand{\txtF}{#4}}

\newcommand{\noteG}{\MarkMe{\posG}{\xG}{\yG}{\txtG}}
\newcommand{\posG}{}
\newcommand{\xG}{}
\newcommand{\yG}{}
\newcommand{\txtG}{}
\newcommand{\setNoteG}[4][right]{\renewcommand{\posG}{#1}\renewcommand{\xG}{#2} \renewcommand{\yG}{#3} \renewcommand{\txtG}{#4}}


% refs
\newcommand{\figr}[1]{Figura~\ref{#1}}
\newcommand{\tabr}[1]{Tabela~\ref{#1}}
\newcommand{\secr}[1]{Se\c{c}\~ao~\ref{#1}}
\newcommand{\eqr}[1]{(\ref{#1})}

% math
\renewcommand{\Re}{\operatorname{Re}}
\renewcommand{\Im}{\operatorname{Im}}


\newcommand{\inlcode}[1]{\texttt{\color{blue!65!green}\lstinline{#1}}}
\newcommand{\inlstr}[1]{\texttt{\color{blue!40!green}\lstinline{\'#1\'}}}
\newcommand{\inlkey}[1]{\texttt{\color{blue!40!green}\lstinline{\'#1\'}}}

%%
%seção
\sectionfont{\sectionrule{0ex}{0pt}{-1ex}{0.0pt}}
\makeatletter \def\@seccntformat#1{\csname the#1\endcsname:\quad}




%cabeçalho e rodapé
%\renewcommand{\headrulewidth}{.5pt}
%\renewcommand{\footrulewidth}{.5pt}
%\lhead{\includegraphics[scale=0.24]{../class/figs/ifsc}\\ \noindent\rule[2ex]{\linewidth}{.50pt}}
\lhead{\includegraphics[scale=0.16]{../class/figs/logo_cabecalho} \noindent\rule[2ex]{\linewidth}{.50pt}}
\chead{}
\rhead{
    \begin{minipage}{0.80\textwidth} \small
        \begin{flushleft}
            \@cabecalho
        \end{flushleft}
    \end{minipage}\\ \vspace{1.2mm}
}

%\lfoot{\footnotesize{T\'itulo: \@shorttitle \\ Autor: \theauthor}}
%\cfoot{}
%\rfoot{\footnotesize{ \ \@date \\ P\'agina \thepage  \ de  \pageref{LastPage}}}

\lfoot{}
\rfoot{}
\cfoot{\thepage}

\renewcommand{\headrulewidth}{0pt}




\newcommand\HUGE{\@setfontsize\Huge{30}{35}}



\cabecalho{
    \textsc{Grupo de Pesquisa em Eletrônica de Potência e Acionamentos Industriais} \\
    \textsc{Instituto Federal de Educação, Ciência e Tecnologia de Santa Catarina} \\
    \textsc{Campus Florianópolis --- Departamento Acadêmico de Eletrotécnica}
}
\newcommand{\capa}{
    \textbf{\thispagestyle{empty}}
    \begin{center}
%        \includegraphics[scale=.5]{../class/figs/gepai} \\
        \vspace{-5mm}
        \HUGE\textbf{\@title} \\
        \vspace{3mm}
        \LARGE\textbf{\@subtitle} \\
        \vfill
        \includegraphics[scale=1.0]{../class/figs/logo_capa} \\
        \vfill


    \large\textbf{\@subject} \\
    \vspace{7mm}
    \large\textbf{Autor: \@author} \\ \texttt{\@email} \\
    \vspace{15mm}
    \includegraphics[scale=.4]{../class/figs/logo_ifsc} \\
    \vspace{-5mm}
    \end{center}
    \newpage
    \pagestyle{fancy}
    }

\newcommand\unnumberedchapter[1]{%
  \chapter*{#1}%
  \addcontentsline{toc}{chapter}{#1}}

\setstretch{1.2}

%\setcounter{footnote}{1}

