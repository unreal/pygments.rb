# -*- coding: utf-8 -*-
"""
    pygments.lexers._mapping
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer mapping defintions. This file is generated by itself. Everytime
    you change something on a builtin lexer defintion, run this script from
    the lexers folder to update it.

    Do not alter the LEXERS dictionary by hand.

    :copyright: Copyright 2006-2013 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

LEXERS = {
    'ABAPLexer': ('pygments.lexers.other', 'ABAP', ('abap',), ('*.abap',), ('text/x-abap',)),
    'ActionScript3Lexer': ('pygments.lexers.web', 'ActionScript 3', ('as3', 'actionscript3'), ('*.as',), ('application/x-actionscript', 'text/x-actionscript', 'text/actionscript')),
    'ActionScriptLexer': ('pygments.lexers.web', 'ActionScript', ('as', 'actionscript'), ('*.as',), ('application/x-actionscript3', 'text/x-actionscript3', 'text/actionscript3')),
    'AdaLexer': ('pygments.lexers.compiled', 'Ada', ('ada', 'ada95ada2005'), ('*.adb', '*.ads', '*.ada'), ('text/x-ada',)),
    'AgdaLexer': ('pygments.lexers.functional', 'Agda', ('agda',), ('*.agda',), ('text/x-agda',)),
    'AntlrActionScriptLexer': ('pygments.lexers.parsers', 'ANTLR With ActionScript Target', ('antlr-as', 'antlr-actionscript'), ('*.G', '*.g'), ()),
    'AntlrCSharpLexer': ('pygments.lexers.parsers', 'ANTLR With C# Target', ('antlr-csharp', 'antlr-c#'), ('*.G', '*.g'), ()),
    'AntlrCppLexer': ('pygments.lexers.parsers', 'ANTLR With CPP Target', ('antlr-cpp',), ('*.G', '*.g'), ()),
    'AntlrJavaLexer': ('pygments.lexers.parsers', 'ANTLR With Java Target', ('antlr-java',), ('*.G', '*.g'), ()),
    'AntlrLexer': ('pygments.lexers.parsers', 'ANTLR', ('antlr',), (), ()),
    'AntlrObjectiveCLexer': ('pygments.lexers.parsers', 'ANTLR With ObjectiveC Target', ('antlr-objc',), ('*.G', '*.g'), ()),
    'AntlrPerlLexer': ('pygments.lexers.parsers', 'ANTLR With Perl Target', ('antlr-perl',), ('*.G', '*.g'), ()),
    'AntlrPythonLexer': ('pygments.lexers.parsers', 'ANTLR With Python Target', ('antlr-python',), ('*.G', '*.g'), ()),
    'AntlrRubyLexer': ('pygments.lexers.parsers', 'ANTLR With Ruby Target', ('antlr-ruby', 'antlr-rb'), ('*.G', '*.g'), ()),
    'ApacheConfLexer': ('pygments.lexers.text', 'ApacheConf', ('apacheconf', 'aconf', 'apache'), ('.htaccess', 'apache.conf', 'apache2.conf'), ('text/x-apacheconf',)),
    'AppleScriptLexer': ('pygments.lexers.other', 'AppleScript', ('applescript',), ('*.applescript',), ()),
    'AspectJLexer': ('pygments.lexers.jvm', 'AspectJ', ('aspectj',), ('*.aj',), ('text/x-aspectj',)),
    'AsymptoteLexer': ('pygments.lexers.other', 'Asymptote', ('asy', 'asymptote'), ('*.asy',), ('text/x-asymptote',)),
    'AugeasLexer': ('pygments.lexers.github', 'Augeas', ('augeas',), ('*.aug',), ()),
    'AutoItLexer': ('pygments.lexers.other', 'AutoIt', ('autoit', 'Autoit'), ('*.au3',), ('text/x-autoit',)),
    'AutohotkeyLexer': ('pygments.lexers.other', 'autohotkey', ('ahk', 'autohotkey'), ('*.ahk', '*.ahkl'), ('text/x-autohotkey',)),
    'AwkLexer': ('pygments.lexers.other', 'Awk', ('awk', 'gawk', 'mawk', 'nawk'), ('*.awk',), ('application/x-awk',)),
    'BBCodeLexer': ('pygments.lexers.text', 'BBCode', ('bbcode',), (), ('text/x-bbcode',)),
    'BaseMakefileLexer': ('pygments.lexers.text', 'Base Makefile', ('basemake',), (), ()),
    'BashLexer': ('pygments.lexers.shell', 'Bash', ('bash', 'sh', 'ksh'), ('*.sh', '*.ksh', '*.bash', '*.ebuild', '*.eclass', '.bashrc', 'bashrc', '.bash_*', 'bash_*'), ('application/x-sh', 'application/x-shellscript')),
    'BashSessionLexer': ('pygments.lexers.shell', 'Bash Session', ('console',), ('*.sh-session',), ('application/x-shell-session',)),
    'BatchLexer': ('pygments.lexers.shell', 'Batchfile', ('bat', 'dosbatch', 'winbatch'), ('*.bat', '*.cmd'), ('application/x-dos-batch',)),
    'BefungeLexer': ('pygments.lexers.other', 'Befunge', ('befunge',), ('*.befunge',), ('application/x-befunge',)),
    'BlitzBasicLexer': ('pygments.lexers.compiled', 'BlitzBasic', ('blitzbasic', 'b3d', 'bplus'), ('*.bb', '*.decls'), ('text/x-bb',)),
    'BlitzMaxLexer': ('pygments.lexers.compiled', 'BlitzMax', ('blitzmax', 'bmax'), ('*.bmx',), ('text/x-bmx',)),
    'BooLexer': ('pygments.lexers.dotnet', 'Boo', ('boo',), ('*.boo',), ('text/x-boo',)),
    'BrainfuckLexer': ('pygments.lexers.other', 'Brainfuck', ('brainfuck', 'bf'), ('*.bf', '*.b'), ('application/x-brainfuck',)),
    'BroLexer': ('pygments.lexers.other', 'Bro', ('bro',), ('*.bro',), ()),
    'BugsLexer': ('pygments.lexers.math', 'BUGS', ('bugs', 'winbugs', 'openbugs'), ('*.bug',), ()),
    'CLexer': ('pygments.lexers.compiled', 'C', ('c',), ('*.c', '*.h', '*.idc'), ('text/x-chdr', 'text/x-csrc')),
    'CMakeLexer': ('pygments.lexers.text', 'CMake', ('cmake',), ('*.cmake', 'CMakeLists.txt'), ('text/x-cmake',)),
    'CObjdumpLexer': ('pygments.lexers.asm', 'c-objdump', ('c-objdump',), ('*.c-objdump',), ('text/x-c-objdump',)),
    'CSharpAspxLexer': ('pygments.lexers.dotnet', 'aspx-cs', ('aspx-cs',), ('*.aspx', '*.asax', '*.ascx', '*.ashx', '*.asmx', '*.axd'), ()),
    'CSharpLexer': ('pygments.lexers.dotnet', 'C#', ('csharp', 'c#'), ('*.cs',), ('text/x-csharp',)),
    'Ca65Lexer': ('pygments.lexers.asm', 'ca65', ('ca65',), ('*.s',), ()),
    'CbmBasicV2Lexer': ('pygments.lexers.other', 'CBM BASIC V2', ('cbmbas',), ('*.bas',), ()),
    'CeylonLexer': ('pygments.lexers.jvm', 'Ceylon', ('ceylon',), ('*.ceylon',), ('text/x-ceylon',)),
    'Cfengine3Lexer': ('pygments.lexers.other', 'CFEngine3', ('cfengine3', 'cf3'), ('*.cf',), ()),
    'CheetahHtmlLexer': ('pygments.lexers.templates', 'HTML+Cheetah', ('html+cheetah', 'html+spitfire', 'htmlcheetah'), (), ('text/html+cheetah', 'text/html+spitfire')),
    'CheetahJavascriptLexer': ('pygments.lexers.templates', 'JavaScript+Cheetah', ('js+cheetah', 'javascript+cheetah', 'js+spitfire', 'javascript+spitfire'), (), ('application/x-javascript+cheetah', 'text/x-javascript+cheetah', 'text/javascript+cheetah', 'application/x-javascript+spitfire', 'text/x-javascript+spitfire', 'text/javascript+spitfire')),
    'CheetahLexer': ('pygments.lexers.templates', 'Cheetah', ('cheetah', 'spitfire'), ('*.tmpl', '*.spt'), ('application/x-cheetah', 'application/x-spitfire')),
    'CheetahXmlLexer': ('pygments.lexers.templates', 'XML+Cheetah', ('xml+cheetah', 'xml+spitfire'), (), ('application/xml+cheetah', 'application/xml+spitfire')),
    'ClayLexer': ('pygments.lexers.compiled', 'Clay', ('clay',), ('*.clay',), ('text/x-clay',)),
    'ClojureLexer': ('pygments.lexers.jvm', 'Clojure', ('clojure', 'clj'), ('*.clj',), ('text/x-clojure', 'application/x-clojure')),
    'CobolFreeformatLexer': ('pygments.lexers.compiled', 'COBOLFree', ('cobolfree',), ('*.cbl', '*.CBL'), ()),
    'CobolLexer': ('pygments.lexers.compiled', 'COBOL', ('cobol',), ('*.cob', '*.COB', '*.cpy', '*.CPY'), ('text/x-cobol',)),
    'CoffeeScriptLexer': ('pygments.lexers.web', 'CoffeeScript', ('coffee-script', 'coffeescript', 'coffee'), ('*.coffee',), ('text/coffeescript',)),
    'ColdfusionHtmlLexer': ('pygments.lexers.templates', 'Coldfusion HTML', ('cfm',), ('*.cfm', '*.cfml', '*.cfc'), ('application/x-coldfusion',)),
    'ColdfusionLexer': ('pygments.lexers.templates', 'cfstatement', ('cfs',), (), ()),
    'CommonLispLexer': ('pygments.lexers.functional', 'Common Lisp', ('common-lisp', 'cl', 'lisp'), ('*.cl', '*.lisp', '*.el'), ('text/x-common-lisp',)),
    'CoqLexer': ('pygments.lexers.functional', 'Coq', ('coq',), ('*.v',), ('text/x-coq',)),
    'CppLexer': ('pygments.lexers.compiled', 'C++', ('cpp', 'c++'), ('*.cpp', '*.hpp', '*.c++', '*.h++', '*.cc', '*.hh', '*.cxx', '*.hxx', '*.C', '*.H', '*.cp', '*.CPP'), ('text/x-c++hdr', 'text/x-c++src')),
    'CppObjdumpLexer': ('pygments.lexers.asm', 'cpp-objdump', ('cpp-objdump', 'c++-objdumb', 'cxx-objdump'), ('*.cpp-objdump', '*.c++-objdump', '*.cxx-objdump'), ('text/x-cpp-objdump',)),
    'CrocLexer': ('pygments.lexers.agile', 'Croc', ('croc',), ('*.croc',), ('text/x-crocsrc',)),
    'CssDjangoLexer': ('pygments.lexers.templates', 'CSS+Django/Jinja', ('css+django', 'css+jinja'), (), ('text/css+django', 'text/css+jinja')),
    'CssErbLexer': ('pygments.lexers.templates', 'CSS+Ruby', ('css+erb', 'css+ruby'), (), ('text/css+ruby',)),
    'CssGenshiLexer': ('pygments.lexers.templates', 'CSS+Genshi Text', ('css+genshitext', 'css+genshi'), (), ('text/css+genshi',)),
    'CssLexer': ('pygments.lexers.web', 'CSS', ('css',), ('*.css',), ('text/css',)),
    'CssPhpLexer': ('pygments.lexers.templates', 'CSS+PHP', ('css+php',), (), ('text/css+php',)),
    'CssSmartyLexer': ('pygments.lexers.templates', 'CSS+Smarty', ('css+smarty',), (), ('text/css+smarty',)),
    'CudaLexer': ('pygments.lexers.compiled', 'CUDA', ('cuda', 'cu'), ('*.cu', '*.cuh'), ('text/x-cuda',)),
    'CythonLexer': ('pygments.lexers.compiled', 'Cython', ('cython', 'pyx', 'pyrex'), ('*.pyx', '*.pxd', '*.pxi'), ('text/x-cython', 'application/x-cython')),
    'DLexer': ('pygments.lexers.compiled', 'D', ('d',), ('*.d', '*.di'), ('text/x-dsrc',)),
    'DObjdumpLexer': ('pygments.lexers.asm', 'd-objdump', ('d-objdump',), ('*.d-objdump',), ('text/x-d-objdump',)),
    'DarcsPatchLexer': ('pygments.lexers.text', 'Darcs Patch', ('dpatch',), ('*.dpatch', '*.darcspatch'), ()),
    'DartLexer': ('pygments.lexers.web', 'Dart', ('dart',), ('*.dart',), ('text/x-dart',)),
    'Dasm16Lexer': ('pygments.lexers.github', 'dasm16', ('DASM16',), ('*.dasm16', '*.dasm'), ('text/x-dasm16',)),
    'DebianControlLexer': ('pygments.lexers.text', 'Debian Control file', ('control', 'debcontrol'), ('control',), ()),
    'DelphiLexer': ('pygments.lexers.compiled', 'Delphi', ('delphi', 'pas', 'pascal', 'objectpascal'), ('*.pas',), ('text/x-pascal',)),
    'DgLexer': ('pygments.lexers.agile', 'dg', ('dg',), ('*.dg',), ('text/x-dg',)),
    'DiffLexer': ('pygments.lexers.text', 'Diff', ('diff', 'udiff'), ('*.diff', '*.patch'), ('text/x-diff', 'text/x-patch')),
    'DjangoLexer': ('pygments.lexers.templates', 'Django/Jinja', ('django', 'jinja'), (), ('application/x-django-templating', 'application/x-jinja')),
    'DtdLexer': ('pygments.lexers.web', 'DTD', ('dtd',), ('*.dtd',), ('application/xml-dtd',)),
    'DuelLexer': ('pygments.lexers.web', 'Duel', ('duel', 'Duel Engine', 'Duel View', 'JBST', 'jbst', 'JsonML+BST'), ('*.duel', '*.jbst'), ('text/x-duel', 'text/x-jbst')),
    'DylanConsoleLexer': ('pygments.lexers.compiled', 'Dylan session', ('dylan-console', 'dylan-repl'), ('*.dylan-console',), ('text/x-dylan-console',)),
    'DylanLexer': ('pygments.lexers.compiled', 'Dylan', ('dylan',), ('*.dylan', '*.dyl', '*.intr'), ('text/x-dylan',)),
    'DylanLidLexer': ('pygments.lexers.compiled', 'DylanLID', ('dylan-lid', 'lid'), ('*.lid', '*.hdp'), ('text/x-dylan-lid',)),
    'ECLLexer': ('pygments.lexers.other', 'ECL', ('ecl',), ('*.ecl',), ('application/x-ecl',)),
    'ECLexer': ('pygments.lexers.compiled', 'eC', ('ec',), ('*.ec', '*.eh'), ('text/x-echdr', 'text/x-ecsrc')),
    'EbnfLexer': ('pygments.lexers.text', 'EBNF', ('ebnf',), ('*.ebnf',), ('text/x-ebnf',)),
    'ElixirConsoleLexer': ('pygments.lexers.functional', 'Elixir iex session', ('iex',), (), ('text/x-elixir-shellsession',)),
    'ElixirLexer': ('pygments.lexers.functional', 'Elixir', ('elixir', 'ex', 'exs'), ('*.ex', '*.exs'), ('text/x-elixir',)),
    'ErbLexer': ('pygments.lexers.templates', 'ERB', ('erb',), (), ('application/x-ruby-templating',)),
    'ErlangLexer': ('pygments.lexers.functional', 'Erlang', ('erlang',), ('*.erl', '*.hrl', '*.es', '*.escript'), ('text/x-erlang',)),
    'ErlangShellLexer': ('pygments.lexers.functional', 'Erlang erl session', ('erl',), ('*.erl-sh',), ('text/x-erl-shellsession',)),
    'EvoqueHtmlLexer': ('pygments.lexers.templates', 'HTML+Evoque', ('html+evoque',), ('*.html',), ('text/html+evoque',)),
    'EvoqueLexer': ('pygments.lexers.templates', 'Evoque', ('evoque',), ('*.evoque',), ('application/x-evoque',)),
    'EvoqueXmlLexer': ('pygments.lexers.templates', 'XML+Evoque', ('xml+evoque',), ('*.xml',), ('application/xml+evoque',)),
    'FSharpLexer': ('pygments.lexers.dotnet', 'FSharp', ('fsharp',), ('*.fs', '*.fsi'), ('text/x-fsharp',)),
    'FactorLexer': ('pygments.lexers.agile', 'Factor', ('factor',), ('*.factor',), ('text/x-factor',)),
    'FancyLexer': ('pygments.lexers.agile', 'Fancy', ('fancy', 'fy'), ('*.fy', '*.fancypack'), ('text/x-fancysrc',)),
    'FantomLexer': ('pygments.lexers.compiled', 'Fantom', ('fan',), ('*.fan',), ('application/x-fantom',)),
    'FelixLexer': ('pygments.lexers.compiled', 'Felix', ('felix', 'flx'), ('*.flx', '*.flxh'), ('text/x-felix',)),
    'FortranLexer': ('pygments.lexers.compiled', 'Fortran', ('fortran',), ('*.f', '*.f90', '*.F', '*.F90'), ('text/x-fortran',)),
    'FoxProLexer': ('pygments.lexers.foxpro', 'FoxPro', ('Clipper', 'XBase'), ('*.PRG', '*.prg'), ()),
    'GLShaderLexer': ('pygments.lexers.compiled', 'GLSL', ('glsl',), ('*.vert', '*.frag', '*.geo'), ('text/x-glslsrc',)),
    'GasLexer': ('pygments.lexers.asm', 'GAS', ('gas', 'asm'), ('*.s', '*.S'), ('text/x-gas',)),
    'GenshiLexer': ('pygments.lexers.templates', 'Genshi', ('genshi', 'kid', 'xml+genshi', 'xml+kid'), ('*.kid',), ('application/x-genshi', 'application/x-kid')),
    'GenshiTextLexer': ('pygments.lexers.templates', 'Genshi Text', ('genshitext',), (), ('application/x-genshi-text', 'text/x-genshi')),
    'GettextLexer': ('pygments.lexers.text', 'Gettext Catalog', ('pot', 'po'), ('*.pot', '*.po'), ('application/x-gettext', 'text/x-gettext', 'text/gettext')),
    'GherkinLexer': ('pygments.lexers.other', 'Gherkin', ('Cucumber', 'cucumber', 'Gherkin', 'gherkin'), ('*.feature',), ('text/x-gherkin',)),
    'GnuplotLexer': ('pygments.lexers.other', 'Gnuplot', ('gnuplot',), ('*.plot', '*.plt'), ('text/x-gnuplot',)),
    'GoLexer': ('pygments.lexers.compiled', 'Go', ('go',), ('*.go',), ('text/x-gosrc',)),
    'GoodDataCLLexer': ('pygments.lexers.other', 'GoodData-CL', ('gooddata-cl',), ('*.gdc',), ('text/x-gooddata-cl',)),
    'GosuLexer': ('pygments.lexers.jvm', 'Gosu', ('gosu',), ('*.gs', '*.gsx', '*.gsp', '*.vark'), ('text/x-gosu',)),
    'GosuTemplateLexer': ('pygments.lexers.jvm', 'Gosu Template', ('gst',), ('*.gst',), ('text/x-gosu-template',)),
    'GroffLexer': ('pygments.lexers.text', 'Groff', ('groff', 'nroff', 'man'), ('*.[1234567]', '*.man'), ('application/x-troff', 'text/troff')),
    'GroovyLexer': ('pygments.lexers.jvm', 'Groovy', ('groovy',), ('*.groovy',), ('text/x-groovy',)),
    'HamlLexer': ('pygments.lexers.web', 'Haml', ('haml', 'HAML'), ('*.haml',), ('text/x-haml',)),
    'HaskellLexer': ('pygments.lexers.functional', 'Haskell', ('haskell', 'hs'), ('*.hs',), ('text/x-haskell',)),
    'HaxeLexer': ('pygments.lexers.web', 'Haxe', ('hx', 'Haxe', 'haxe', 'haXe', 'hxsl'), ('*.hx', '*.hxsl'), ('text/haxe', 'text/x-haxe', 'text/x-hx')),
    'HtmlDjangoLexer': ('pygments.lexers.templates', 'HTML+Django/Jinja', ('html+django', 'html+jinja', 'htmldjango'), (), ('text/html+django', 'text/html+jinja')),
    'HtmlGenshiLexer': ('pygments.lexers.templates', 'HTML+Genshi', ('html+genshi', 'html+kid'), (), ('text/html+genshi',)),
    'HtmlLexer': ('pygments.lexers.web', 'HTML', ('html',), ('*.html', '*.htm', '*.xhtml', '*.xslt'), ('text/html', 'application/xhtml+xml')),
    'HtmlPhpLexer': ('pygments.lexers.templates', 'HTML+PHP', ('html+php',), ('*.phtml',), ('application/x-php', 'application/x-httpd-php', 'application/x-httpd-php3', 'application/x-httpd-php4', 'application/x-httpd-php5')),
    'HtmlSmartyLexer': ('pygments.lexers.templates', 'HTML+Smarty', ('html+smarty',), (), ('text/html+smarty',)),
    'HttpLexer': ('pygments.lexers.text', 'HTTP', ('http',), (), ()),
    'HxmlLexer': ('pygments.lexers.text', 'Hxml', ('haxeml', 'hxml'), ('*.hxml',), ()),
    'HybrisLexer': ('pygments.lexers.other', 'Hybris', ('hybris', 'hy'), ('*.hy', '*.hyb'), ('text/x-hybris', 'application/x-hybris')),
    'IDLLexer': ('pygments.lexers.math', 'IDL', ('idl',), ('*.pro',), ('text/idl',)),
    'IgorLexer': ('pygments.lexers.math', 'Igor', ('igor', 'igorpro'), ('*.ipf',), ('text/ipf',)),
    'IniLexer': ('pygments.lexers.text', 'INI', ('ini', 'cfg', 'dosini'), ('*.ini', '*.cfg'), ('text/x-ini',)),
    'IoLexer': ('pygments.lexers.agile', 'Io', ('io',), ('*.io',), ('text/x-iosrc',)),
    'IokeLexer': ('pygments.lexers.jvm', 'Ioke', ('ioke', 'ik'), ('*.ik',), ('text/x-iokesrc',)),
    'IrcLogsLexer': ('pygments.lexers.text', 'IRC logs', ('irc',), ('*.weechatlog',), ('text/x-irclog',)),
    'JadeLexer': ('pygments.lexers.web', 'Jade', ('jade', 'JADE'), ('*.jade',), ('text/x-jade',)),
    'JagsLexer': ('pygments.lexers.math', 'JAGS', ('jags',), ('*.jag', '*.bug'), ()),
    'JavaLexer': ('pygments.lexers.jvm', 'Java', ('java',), ('*.java',), ('text/x-java',)),
    'JavascriptDjangoLexer': ('pygments.lexers.templates', 'JavaScript+Django/Jinja', ('js+django', 'javascript+django', 'js+jinja', 'javascript+jinja'), (), ('application/x-javascript+django', 'application/x-javascript+jinja', 'text/x-javascript+django', 'text/x-javascript+jinja', 'text/javascript+django', 'text/javascript+jinja')),
    'JavascriptErbLexer': ('pygments.lexers.templates', 'JavaScript+Ruby', ('js+erb', 'javascript+erb', 'js+ruby', 'javascript+ruby'), (), ('application/x-javascript+ruby', 'text/x-javascript+ruby', 'text/javascript+ruby')),
    'JavascriptGenshiLexer': ('pygments.lexers.templates', 'JavaScript+Genshi Text', ('js+genshitext', 'js+genshi', 'javascript+genshitext', 'javascript+genshi'), (), ('application/x-javascript+genshi', 'text/x-javascript+genshi', 'text/javascript+genshi')),
    'JavascriptLexer': ('pygments.lexers.web', 'JavaScript', ('js', 'javascript'), ('*.js',), ('application/javascript', 'application/x-javascript', 'text/x-javascript', 'text/javascript')),
    'JavascriptPhpLexer': ('pygments.lexers.templates', 'JavaScript+PHP', ('js+php', 'javascript+php'), (), ('application/x-javascript+php', 'text/x-javascript+php', 'text/javascript+php')),
    'JavascriptSmartyLexer': ('pygments.lexers.templates', 'JavaScript+Smarty', ('js+smarty', 'javascript+smarty'), (), ('application/x-javascript+smarty', 'text/x-javascript+smarty', 'text/javascript+smarty')),
    'JsonLexer': ('pygments.lexers.web', 'JSON', ('json',), ('*.json',), ('application/json',)),
    'JspLexer': ('pygments.lexers.templates', 'Java Server Page', ('jsp',), ('*.jsp',), ('application/x-jsp',)),
    'JuliaConsoleLexer': ('pygments.lexers.math', 'Julia console', ('jlcon',), (), ()),
    'JuliaLexer': ('pygments.lexers.math', 'Julia', ('julia', 'jl'), ('*.jl',), ('text/x-julia', 'application/x-julia')),
    'KconfigLexer': ('pygments.lexers.other', 'Kconfig', ('kconfig', 'menuconfig', 'linux-config', 'kernel-config'), ('Kconfig', '*Config.in*', 'external.in*', 'standard-modules.in'), ('text/x-kconfig',)),
    'KokaLexer': ('pygments.lexers.functional', 'Koka', ('koka',), ('*.kk', '*.kki'), ('text/x-koka',)),
    'KotlinLexer': ('pygments.lexers.jvm', 'Kotlin', ('kotlin',), ('*.kt',), ('text/x-kotlin',)),
    'LassoCssLexer': ('pygments.lexers.templates', 'CSS+Lasso', ('css+lasso',), (), ('text/css+lasso',)),
    'LassoHtmlLexer': ('pygments.lexers.templates', 'HTML+Lasso', ('html+lasso',), (), ('text/html+lasso', 'application/x-httpd-lasso', 'application/x-httpd-lasso[89]')),
    'LassoJavascriptLexer': ('pygments.lexers.templates', 'JavaScript+Lasso', ('js+lasso', 'javascript+lasso'), (), ('application/x-javascript+lasso', 'text/x-javascript+lasso', 'text/javascript+lasso')),
    'LassoLexer': ('pygments.lexers.web', 'Lasso', ('lasso', 'lassoscript'), ('*.lasso', '*.lasso[89]'), ('text/x-lasso',)),
    'LassoXmlLexer': ('pygments.lexers.templates', 'XML+Lasso', ('xml+lasso',), (), ('application/xml+lasso',)),
    'LighttpdConfLexer': ('pygments.lexers.text', 'Lighttpd configuration file', ('lighty', 'lighttpd'), (), ('text/x-lighttpd-conf',)),
    'LiterateAgdaLexer': ('pygments.lexers.functional', 'Literate Agda', ('lagda', 'literate-agda'), ('*.lagda',), ('text/x-literate-agda',)),
    'LiterateHaskellLexer': ('pygments.lexers.functional', 'Literate Haskell', ('lhs', 'literate-haskell', 'lhaskell'), ('*.lhs',), ('text/x-literate-haskell',)),
    'LiveScriptLexer': ('pygments.lexers.web', 'LiveScript', ('live-script', 'livescript'), ('*.ls',), ('text/livescript',)),
    'LlvmLexer': ('pygments.lexers.asm', 'LLVM', ('llvm',), ('*.ll',), ('text/x-llvm',)),
    'LogosLexer': ('pygments.lexers.compiled', 'Logos', ('logos',), ('*.x', '*.xi', '*.xm', '*.xmi'), ('text/x-logos',)),
    'LogtalkLexer': ('pygments.lexers.other', 'Logtalk', ('logtalk',), ('*.lgt',), ('text/x-logtalk',)),
    'LuaLexer': ('pygments.lexers.agile', 'Lua', ('lua',), ('*.lua', '*.wlua'), ('text/x-lua', 'application/x-lua')),
    'MOOCodeLexer': ('pygments.lexers.other', 'MOOCode', ('moocode', 'moo'), ('*.moo',), ('text/x-moocode',)),
    'MakefileLexer': ('pygments.lexers.text', 'Makefile', ('make', 'makefile', 'mf', 'bsdmake'), ('*.mak', 'Makefile', 'makefile', 'Makefile.*', 'GNUmakefile'), ('text/x-makefile',)),
    'MakoCssLexer': ('pygments.lexers.templates', 'CSS+Mako', ('css+mako',), (), ('text/css+mako',)),
    'MakoHtmlLexer': ('pygments.lexers.templates', 'HTML+Mako', ('html+mako',), (), ('text/html+mako',)),
    'MakoJavascriptLexer': ('pygments.lexers.templates', 'JavaScript+Mako', ('js+mako', 'javascript+mako'), (), ('application/x-javascript+mako', 'text/x-javascript+mako', 'text/javascript+mako')),
    'MakoLexer': ('pygments.lexers.templates', 'Mako', ('mako',), ('*.mao',), ('application/x-mako',)),
    'MakoXmlLexer': ('pygments.lexers.templates', 'XML+Mako', ('xml+mako',), (), ('application/xml+mako',)),
    'MaqlLexer': ('pygments.lexers.other', 'MAQL', ('maql',), ('*.maql',), ('text/x-gooddata-maql', 'application/x-gooddata-maql')),
    'MasonLexer': ('pygments.lexers.templates', 'Mason', ('mason',), ('*.m', '*.mhtml', '*.mc', '*.mi', 'autohandler', 'dhandler'), ('application/x-mason',)),
    'MatlabLexer': ('pygments.lexers.math', 'Matlab', ('matlab',), ('*.m',), ('text/matlab',)),
    'MatlabSessionLexer': ('pygments.lexers.math', 'Matlab session', ('matlabsession',), (), ()),
    'MiniDLexer': ('pygments.lexers.agile', 'MiniD', ('minid',), ('*.md',), ('text/x-minidsrc',)),
    'ModelicaLexer': ('pygments.lexers.other', 'Modelica', ('modelica',), ('*.mo',), ('text/x-modelica',)),
    'Modula2Lexer': ('pygments.lexers.compiled', 'Modula-2', ('modula2', 'm2'), ('*.def', '*.mod'), ('text/x-modula2',)),
    'MoinWikiLexer': ('pygments.lexers.text', 'MoinMoin/Trac Wiki markup', ('trac-wiki', 'moin'), (), ('text/x-trac-wiki',)),
    'MonkeyLexer': ('pygments.lexers.compiled', 'Monkey', ('monkey',), ('*.monkey',), ('text/x-monkey',)),
    'MoonScriptLexer': ('pygments.lexers.agile', 'MoonScript', ('moon', 'moonscript'), ('*.moon',), ('text/x-moonscript', 'application/x-moonscript')),
    'MscgenLexer': ('pygments.lexers.other', 'Mscgen', ('mscgen', 'msc'), ('*.msc',), ()),
    'MuPADLexer': ('pygments.lexers.math', 'MuPAD', ('mupad',), ('*.mu',), ()),
    'MxmlLexer': ('pygments.lexers.web', 'MXML', ('mxml',), ('*.mxml',), ()),
    'MySqlLexer': ('pygments.lexers.sql', 'MySQL', ('mysql',), (), ('text/x-mysql',)),
    'MyghtyCssLexer': ('pygments.lexers.templates', 'CSS+Myghty', ('css+myghty',), (), ('text/css+myghty',)),
    'MyghtyHtmlLexer': ('pygments.lexers.templates', 'HTML+Myghty', ('html+myghty',), (), ('text/html+myghty',)),
    'MyghtyJavascriptLexer': ('pygments.lexers.templates', 'JavaScript+Myghty', ('js+myghty', 'javascript+myghty'), (), ('application/x-javascript+myghty', 'text/x-javascript+myghty', 'text/javascript+mygthy')),
    'MyghtyLexer': ('pygments.lexers.templates', 'Myghty', ('myghty',), ('*.myt', 'autodelegate'), ('application/x-myghty',)),
    'MyghtyXmlLexer': ('pygments.lexers.templates', 'XML+Myghty', ('xml+myghty',), (), ('application/xml+myghty',)),
    'NSISLexer': ('pygments.lexers.other', 'NSIS', ('nsis', 'nsi', 'nsh'), ('*.nsi', '*.nsh'), ('text/x-nsis',)),
    'NasmLexer': ('pygments.lexers.asm', 'NASM', ('nasm',), ('*.asm', '*.ASM'), ('text/x-nasm',)),
    'NemerleLexer': ('pygments.lexers.dotnet', 'Nemerle', ('nemerle',), ('*.n',), ('text/x-nemerle',)),
    'NesCLexer': ('pygments.lexers.compiled', 'nesC', ('nesc',), ('*.nc',), ('text/x-nescsrc',)),
    'NewLispLexer': ('pygments.lexers.functional', 'NewLisp', ('newlisp',), ('*.lsp', '*.nl'), ('text/x-newlisp', 'application/x-newlisp')),
    'NewspeakLexer': ('pygments.lexers.other', 'Newspeak', ('newspeak',), ('*.ns2',), ('text/x-newspeak',)),
    'NginxConfLexer': ('pygments.lexers.text', 'Nginx configuration file', ('nginx',), (), ('text/x-nginx-conf',)),
    'NimrodLexer': ('pygments.lexers.compiled', 'Nimrod', ('nimrod', 'nim'), ('*.nim', '*.nimrod'), ('text/x-nimrod',)),
    'NumPyLexer': ('pygments.lexers.math', 'NumPy', ('numpy',), (), ()),
    'ObjdumpLexer': ('pygments.lexers.asm', 'objdump', ('objdump',), ('*.objdump',), ('text/x-objdump',)),
    'ObjectiveCLexer': ('pygments.lexers.compiled', 'Objective-C', ('objective-c', 'objectivec', 'obj-c', 'objc'), ('*.m', '*.h'), ('text/x-objective-c',)),
    'ObjectiveCppLexer': ('pygments.lexers.compiled', 'Objective-C++', ('objective-c++', 'objectivec++', 'obj-c++', 'objc++'), ('*.mm', '*.hh'), ('text/x-objective-c++',)),
    'ObjectiveJLexer': ('pygments.lexers.web', 'Objective-J', ('objective-j', 'objectivej', 'obj-j', 'objj'), ('*.j',), ('text/x-objective-j',)),
    'OcamlLexer': ('pygments.lexers.functional', 'OCaml', ('ocaml',), ('*.ml', '*.mli', '*.mll', '*.mly'), ('text/x-ocaml',)),
    'OctaveLexer': ('pygments.lexers.math', 'Octave', ('octave',), ('*.m',), ('text/octave',)),
    'OocLexer': ('pygments.lexers.compiled', 'Ooc', ('ooc',), ('*.ooc',), ('text/x-ooc',)),
    'OpaLexer': ('pygments.lexers.functional', 'Opa', ('opa',), ('*.opa',), ('text/x-opa',)),
    'OpenEdgeLexer': ('pygments.lexers.other', 'OpenEdge ABL', ('openedge', 'abl', 'progress'), ('*.p', '*.cls'), ('text/x-openedge', 'application/x-openedge')),
    'Perl6Lexer': ('pygments.lexers.agile', 'Perl6', ('perl6', 'pl6'), ('*.pl', '*.pm', '*.nqp', '*.p6', '*.6pl', '*.p6l', '*.pl6', '*.6pm', '*.p6m', '*.pm6'), ('text/x-perl6', 'application/x-perl6')),
    'PerlLexer': ('pygments.lexers.agile', 'Perl', ('perl', 'pl'), ('*.pl', '*.pm'), ('text/x-perl', 'application/x-perl')),
    'PhpLexer': ('pygments.lexers.web', 'PHP', ('php', 'php3', 'php4', 'php5'), ('*.php', '*.php[345]', '*.inc'), ('text/x-php',)),
    'PlPgsqlLexer': ('pygments.lexers.sql', 'PL/pgSQL', ('plpgsql',), (), ('text/x-plpgsql',)),
    'PostScriptLexer': ('pygments.lexers.other', 'PostScript', ('postscript', 'postscr'), ('*.ps', '*.eps'), ('application/postscript',)),
    'PostgresConsoleLexer': ('pygments.lexers.sql', 'PostgreSQL console (psql)', ('psql', 'postgresql-console', 'postgres-console'), (), ('text/x-postgresql-psql',)),
    'PostgresLexer': ('pygments.lexers.sql', 'PostgreSQL SQL dialect', ('postgresql', 'postgres'), (), ('text/x-postgresql',)),
    'PovrayLexer': ('pygments.lexers.other', 'POVRay', ('pov',), ('*.pov', '*.inc'), ('text/x-povray',)),
    'PowerShellLexer': ('pygments.lexers.shell', 'PowerShell', ('powershell', 'posh', 'ps1', 'psm1'), ('*.ps1', '*.psm1'), ('text/x-powershell',)),
    'PrologLexer': ('pygments.lexers.compiled', 'Prolog', ('prolog',), ('*.prolog', '*.pro', '*.pl'), ('text/x-prolog',)),
    'PropertiesLexer': ('pygments.lexers.text', 'Properties', ('properties', 'jproperties'), ('*.properties',), ('text/x-java-properties',)),
    'ProtoBufLexer': ('pygments.lexers.other', 'Protocol Buffer', ('protobuf', 'proto'), ('*.proto',), ()),
    'PuppetLexer': ('pygments.lexers.github', 'Puppet', ('puppet',), ('*.pp',), ()),
    'PuppetLexer': ('pygments.lexers.other', 'Puppet', ('puppet',), ('*.pp',), ()),
    'PyPyLogLexer': ('pygments.lexers.text', 'PyPy Log', ('pypylog', 'pypy'), ('*.pypylog',), ('application/x-pypylog',)),
    'Python3Lexer': ('pygments.lexers.agile', 'Python 3', ('python3', 'py3'), (), ('text/x-python3', 'application/x-python3')),
    'Python3TracebackLexer': ('pygments.lexers.agile', 'Python 3.0 Traceback', ('py3tb',), ('*.py3tb',), ('text/x-python3-traceback',)),
    'PythonConsoleLexer': ('pygments.lexers.agile', 'Python console session', ('pycon',), (), ('text/x-python-doctest',)),
    'PythonLexer': ('pygments.lexers.agile', 'Python', ('python', 'py', 'sage'), ('*.py', '*.pyw', '*.sc', 'SConstruct', 'SConscript', '*.tac', '*.sage'), ('text/x-python', 'application/x-python')),
    'PythonTracebackLexer': ('pygments.lexers.agile', 'Python Traceback', ('pytb',), ('*.pytb',), ('text/x-python-traceback',)),
    'QmlLexer': ('pygments.lexers.web', 'QML', ('qml', 'Qt Meta Language', 'Qt modeling Language'), ('*.qml',), ('application/x-qml',)),
    'RConsoleLexer': ('pygments.lexers.math', 'RConsole', ('rconsole', 'rout'), ('*.Rout',), ()),
    'RPMSpecLexer': ('pygments.lexers.other', 'RPMSpec', ('spec',), ('*.spec',), ('text/x-rpm-spec',)),
    'RacketLexer': ('pygments.lexers.functional', 'Racket', ('racket', 'rkt'), ('*.rkt', '*.rktl'), ('text/x-racket', 'application/x-racket')),
    'RagelCLexer': ('pygments.lexers.parsers', 'Ragel in C Host', ('ragel-c',), ('*.rl',), ()),
    'RagelCppLexer': ('pygments.lexers.parsers', 'Ragel in CPP Host', ('ragel-cpp',), ('*.rl',), ()),
    'RagelDLexer': ('pygments.lexers.parsers', 'Ragel in D Host', ('ragel-d',), ('*.rl',), ()),
    'RagelEmbeddedLexer': ('pygments.lexers.parsers', 'Embedded Ragel', ('ragel-em',), ('*.rl',), ()),
    'RagelJavaLexer': ('pygments.lexers.parsers', 'Ragel in Java Host', ('ragel-java',), ('*.rl',), ()),
    'RagelLexer': ('pygments.lexers.parsers', 'Ragel', ('ragel',), (), ()),
    'RagelObjectiveCLexer': ('pygments.lexers.parsers', 'Ragel in Objective C Host', ('ragel-objc',), ('*.rl',), ()),
    'RagelRubyLexer': ('pygments.lexers.parsers', 'Ragel in Ruby Host', ('ragel-ruby', 'ragel-rb'), ('*.rl',), ()),
    'RawTokenLexer': ('pygments.lexers.special', 'Raw token data', ('raw',), (), ('application/x-pygments-tokens',)),
    'RdLexer': ('pygments.lexers.math', 'Rd', ('rd',), ('*.Rd',), ('text/x-r-doc',)),
    'RebolLexer': ('pygments.lexers.other', 'REBOL', ('rebol',), ('*.r', '*.r3'), ('text/x-rebol',)),
    'RedcodeLexer': ('pygments.lexers.other', 'Redcode', ('redcode',), ('*.cw',), ()),
    'RegeditLexer': ('pygments.lexers.text', 'reg', ('registry',), ('*.reg',), ('text/x-windows-registry',)),
    'RexxLexer': ('pygments.lexers.other', 'Rexx', ('rexx', 'ARexx', 'arexx'), ('*.rexx', '*.rex', '*.rx', '*.arexx'), ('text/x-rexx',)),
    'RhtmlLexer': ('pygments.lexers.templates', 'RHTML', ('rhtml', 'html+erb', 'html+ruby'), ('*.rhtml',), ('text/html+ruby',)),
    'RobotFrameworkLexer': ('pygments.lexers.other', 'RobotFramework', ('RobotFramework', 'robotframework'), ('*.txt', '*.robot'), ('text/x-robotframework',)),
    'RstLexer': ('pygments.lexers.text', 'reStructuredText', ('rst', 'rest', 'restructuredtext'), ('*.rst', '*.rest'), ('text/x-rst', 'text/prs.fallenstein.rst')),
    'RubyConsoleLexer': ('pygments.lexers.agile', 'Ruby irb session', ('rbcon', 'irb'), (), ('text/x-ruby-shellsession',)),
    'RubyLexer': ('pygments.lexers.agile', 'Ruby', ('rb', 'ruby', 'duby'), ('*.rb', '*.rbw', 'Rakefile', '*.rake', '*.gemspec', '*.rbx', '*.duby'), ('text/x-ruby', 'application/x-ruby')),
    'RustLexer': ('pygments.lexers.compiled', 'Rust', ('rust',), ('*.rs', '*.rc'), ('text/x-rustsrc',)),
    'SLexer': ('pygments.lexers.math', 'S', ('splus', 's', 'r'), ('*.S', '*.R', '.Rhistory', '.Rprofile'), ('text/S-plus', 'text/S', 'text/x-r-source', 'text/x-r', 'text/x-R', 'text/x-r-history', 'text/x-r-profile')),
    'SMLLexer': ('pygments.lexers.functional', 'Standard ML', ('sml',), ('*.sml', '*.sig', '*.fun'), ('text/x-standardml', 'application/x-standardml')),
    'SassLexer': ('pygments.lexers.web', 'Sass', ('sass', 'SASS'), ('*.sass',), ('text/x-sass',)),
    'ScalaLexer': ('pygments.lexers.jvm', 'Scala', ('scala',), ('*.scala',), ('text/x-scala',)),
    'ScamlLexer': ('pygments.lexers.web', 'Scaml', ('scaml', 'SCAML'), ('*.scaml',), ('text/x-scaml',)),
    'SchemeLexer': ('pygments.lexers.functional', 'Scheme', ('scheme', 'scm'), ('*.scm', '*.ss'), ('text/x-scheme', 'application/x-scheme')),
    'ScilabLexer': ('pygments.lexers.math', 'Scilab', ('scilab',), ('*.sci', '*.sce', '*.tst'), ('text/scilab',)),
    'ScssLexer': ('pygments.lexers.web', 'SCSS', ('scss',), ('*.scss',), ('text/x-scss',)),
    'ShellSessionLexer': ('pygments.lexers.shell', 'Shell Session', ('shell-session',), ('*.shell-session',), ('application/x-sh-session',)),
    'SlashLexer': ('pygments.lexers.github', 'Slash', ('slash',), ('*.sl',), ()),
    'SmaliLexer': ('pygments.lexers.dalvik', 'Smali', ('smali',), ('*.smali',), ('text/smali',)),
    'SmalltalkLexer': ('pygments.lexers.other', 'Smalltalk', ('smalltalk', 'squeak', 'st'), ('*.st',), ('text/x-smalltalk',)),
    'SmartyLexer': ('pygments.lexers.templates', 'Smarty', ('smarty',), ('*.tpl',), ('application/x-smarty',)),
    'SnobolLexer': ('pygments.lexers.other', 'Snobol', ('snobol',), ('*.snobol',), ('text/x-snobol',)),
    'SourcePawnLexer': ('pygments.lexers.other', 'SourcePawn', ('sp',), ('*.sp',), ('text/x-sourcepawn',)),
    'SourcesListLexer': ('pygments.lexers.text', 'Debian Sourcelist', ('sourceslist', 'sources.list', 'debsources'), ('sources.list',), ()),
    'SqlLexer': ('pygments.lexers.sql', 'SQL', ('sql',), ('*.sql',), ('text/x-sql',)),
    'SqliteConsoleLexer': ('pygments.lexers.sql', 'sqlite3con', ('sqlite3',), ('*.sqlite3-console',), ('text/x-sqlite3-console',)),
    'SquidConfLexer': ('pygments.lexers.text', 'SquidConf', ('squidconf', 'squid.conf', 'squid'), ('squid.conf',), ('text/x-squidconf',)),
    'SspLexer': ('pygments.lexers.templates', 'Scalate Server Page', ('ssp',), ('*.ssp',), ('application/x-ssp',)),
    'StanLexer': ('pygments.lexers.math', 'Stan', ('stan',), ('*.stan',), ()),
    'SwigLexer': ('pygments.lexers.compiled', 'SWIG', ('Swig', 'swig'), ('*.swg', '*.i'), ('text/swig',)),
    'SystemVerilogLexer': ('pygments.lexers.hdl', 'systemverilog', ('systemverilog', 'sv'), ('*.sv', '*.svh'), ('text/x-systemverilog',)),
    'TOMLLexer': ('pygments.lexers.github', 'TOML', ('toml',), ('*.toml',), ()),
    'TclLexer': ('pygments.lexers.agile', 'Tcl', ('tcl',), ('*.tcl',), ('text/x-tcl', 'text/x-script.tcl', 'application/x-tcl')),
    'TcshLexer': ('pygments.lexers.shell', 'Tcsh', ('tcsh', 'csh'), ('*.tcsh', '*.csh'), ('application/x-csh',)),
    'TeaTemplateLexer': ('pygments.lexers.templates', 'Tea', ('tea',), ('*.tea',), ('text/x-tea',)),
    'TexLexer': ('pygments.lexers.text', 'TeX', ('tex', 'latex'), ('*.tex', '*.aux', '*.toc'), ('text/x-tex', 'text/x-latex')),
    'TextLexer': ('pygments.lexers.special', 'Text only', ('text',), ('*.txt',), ('text/plain',)),
    'TpLexer': ('pygments.lexers.onerobotics', 'TP', ('tp', 'tpp', 'tpe'), ('*.ls',), ()),
    'TreetopLexer': ('pygments.lexers.parsers', 'Treetop', ('treetop',), ('*.treetop', '*.tt'), ()),
    'TypeScriptLexer': ('pygments.lexers.web', 'TypeScript', ('ts',), ('*.ts',), ('text/x-typescript',)),
    'UrbiscriptLexer': ('pygments.lexers.other', 'UrbiScript', ('urbiscript',), ('*.u',), ('application/x-urbiscript',)),
    'VGLLexer': ('pygments.lexers.other', 'VGL', ('vgl',), ('*.rpf',), ()),
    'ValaLexer': ('pygments.lexers.compiled', 'Vala', ('vala', 'vapi'), ('*.vala', '*.vapi'), ('text/x-vala',)),
    'VbNetAspxLexer': ('pygments.lexers.dotnet', 'aspx-vb', ('aspx-vb',), ('*.aspx', '*.asax', '*.ascx', '*.ashx', '*.asmx', '*.axd'), ()),
    'VbNetLexer': ('pygments.lexers.dotnet', 'VB.net', ('vb.net', 'vbnet'), ('*.vb', '*.bas'), ('text/x-vbnet', 'text/x-vba')),
    'VelocityHtmlLexer': ('pygments.lexers.templates', 'HTML+Velocity', ('html+velocity',), (), ('text/html+velocity',)),
    'VelocityLexer': ('pygments.lexers.templates', 'Velocity', ('velocity',), ('*.vm', '*.fhtml'), ()),
    'VelocityXmlLexer': ('pygments.lexers.templates', 'XML+Velocity', ('xml+velocity',), (), ('application/xml+velocity',)),
    'VerilogLexer': ('pygments.lexers.hdl', 'verilog', ('verilog', 'v'), ('*.v',), ('text/x-verilog',)),
    'VhdlLexer': ('pygments.lexers.hdl', 'vhdl', ('vhdl',), ('*.vhdl', '*.vhd'), ('text/x-vhdl',)),
    'VimLexer': ('pygments.lexers.text', 'VimL', ('vim',), ('*.vim', '.vimrc', '.exrc', '.gvimrc', '_vimrc', '_exrc', '_gvimrc', 'vimrc', 'gvimrc'), ('text/x-vim',)),
    'XQueryLexer': ('pygments.lexers.web', 'XQuery', ('xquery', 'xqy', 'xq', 'xql', 'xqm'), ('*.xqy', '*.xquery', '*.xq', '*.xql', '*.xqm'), ('text/xquery', 'application/xquery')),
    'XmlDjangoLexer': ('pygments.lexers.templates', 'XML+Django/Jinja', ('xml+django', 'xml+jinja'), (), ('application/xml+django', 'application/xml+jinja')),
    'XmlErbLexer': ('pygments.lexers.templates', 'XML+Ruby', ('xml+erb', 'xml+ruby'), (), ('application/xml+ruby',)),
    'XmlLexer': ('pygments.lexers.web', 'XML', ('xml',), ('*.xml', '*.xsl', '*.rss', '*.xslt', '*.xsd', '*.wsdl', '*.wsf'), ('text/xml', 'application/xml', 'image/svg+xml', 'application/rss+xml', 'application/atom+xml')),
    'XmlPhpLexer': ('pygments.lexers.templates', 'XML+PHP', ('xml+php',), (), ('application/xml+php',)),
    'XmlSmartyLexer': ('pygments.lexers.templates', 'XML+Smarty', ('xml+smarty',), (), ('application/xml+smarty',)),
    'XsltLexer': ('pygments.lexers.web', 'XSLT', ('xslt',), ('*.xsl', '*.xslt', '*.xpl'), ('application/xsl+xml', 'application/xslt+xml')),
    'XtendLexer': ('pygments.lexers.jvm', 'Xtend', ('xtend',), ('*.xtend',), ('text/x-xtend',)),
    'YamlLexer': ('pygments.lexers.text', 'YAML', ('yaml',), ('*.yaml', '*.yml'), ('text/x-yaml',)),
}

if __name__ == '__main__':
    import sys
    import os

    # lookup lexers
    found_lexers = []
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
    for filename in os.listdir('.'):
        if filename.endswith('.py') and not filename.startswith('_'):
            module_name = 'pygments.lexers.%s' % filename[:-3]
            print module_name
            module = __import__(module_name, None, None, [''])
            for lexer_name in module.__all__:
                lexer = getattr(module, lexer_name)
                found_lexers.append(
                    '%r: %r' % (lexer_name,
                                (module_name,
                                 lexer.name,
                                 tuple(lexer.aliases),
                                 tuple(lexer.filenames),
                                 tuple(lexer.mimetypes))))
    # sort them, that should make the diff files for svn smaller
    found_lexers.sort()

    # extract useful sourcecode from this file
    f = open(__file__)
    try:
        content = f.read()
    finally:
        f.close()
    header = content[:content.find('LEXERS = {')]
    footer = content[content.find("if __name__ == '__main__':"):]

    # write new file
    f = open(__file__, 'wb')
    f.write(header)
    f.write('LEXERS = {\n    %s,\n}\n\n' % ',\n    '.join(found_lexers))
    f.write(footer)
    f.close()
