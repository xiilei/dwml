# -*- coding: utf-8 -*-

"""
Thinks for
http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html
http://en.wikibooks.org/wiki/LaTeX/Mathematics
http://www.ctan.org/tex-archive/macros/latex/contrib/unicode-math
https://github.com/wspr/unicode-math/blob/master/unicode-math-table.tex
"""

CHARS = ('{','}', '_', '^', '#', '&', '$', '%', '~')

BLANK = ''
BACKSLASH = '\\'
ALN = '&'

CHR = {
	#Unicode : Latex Math Symbols
	#Top accents
	u'\u0300' : r'\grave{{{0}}}',
	u'\u0301' : r'\acute{{{0}}}',
	u'\u0302' : r'\hat{{{0}}}',
	u'\u0303' : r'\tilde{{{0}}}',  
	u'\u0304' : r'\bar{{{0}}}',
	u'\u0305' : r'\overbar{{{0}}}',
	u'\u0306' : r'\breve{{{0}}}',
	u'\u0307' : r'\dot{{{0}}}',	  
	u'\u0308' : r'\ddot{{{0}}}',
	u'\u0309' : r'\ovhook{{{0}}}',
	u'\u030a' : r'\ocirc{{{0}}}}',
	u'\u030c' : r'\check{{{0}}}}',
	u'\u0310' : r'\candra{{{0}}}',
	u'\u0312' : r'\oturnedcomma{{{0}}}',
	u'\u0315' : r'\ocommatopright{{{0}}}',
	u'\u031a' : r'\droang{{{0}}}',
	u'\u0338' : r'\not{{{0}}}',
	u'\u20d0' : r'\leftharpoonaccent{{{0}}}',
	u'\u20d1' : r'\rightharpoonaccent{{{0}}}',
	u'\u20d2' : r'\vertoverlay{{{0}}}',
	u'\u20d6' : r'\overleftarrow{{{0}}}',
	u'\u20d7' : r'\vec{{{0}}}',
	u'\u20db' : r'\dddot{{{0}}}',
	u'\u20dc' : r'\ddddot{{{0}}}',
	u'\u20e1' : r'\overleftrightarrow{{{0}}}',
	u'\u20e7' : r'\annuity{{{0}}}',
	u'\u20e9' : r'\widebridgeabove{{{0}}}',
	u'\u20f0' : r'\asteraccent{{{0}}}',
	 #Bottom accents
	u'\u0330' : r'\wideutilde{{{0}}}',
	u'\u0331' : r'\underbar{{{0}}}',
	u'\u20e8' : r'\threeunderdot{{{0}}}',
	u'\u20ec' : r'\underrightharpoondown{{{0}}}',
	u'\u20ed' : r'\underleftharpoondown{{{0}}}',
	u'\u20ee' : r'\underledtarrow{{{0}}}',
	u'\u20ef' : r'\underrightarrow{{{0}}}',
	#Over | group
	u'\u23b4' : r'\overbracket{{{0}}}',
	u'\u23dc' : r'\overparen{{{0}}}',
	u'\u23de' : r'\overbrace{{{0}}}',
	#Under| group
	u'\u23b5' : r'\underbracket{{{0}}}',
	u'\u23dd' : r'\underparen{{{0}}}',
	u'\u23df' : r'\underbrace{{{0}}}',
}

CHR_BO = {
	#Big operators,
	u'\u2140' : r'\Bbbsum',
	u'\u220f' : r'\prod',
	u'\u2210' : r'\coprod',
	u'\u2211' : r'\sum',
	u'\u222b' : r'\int',
	u'\u22c0' : r'\bigwedge',
	u'\u22c1' : r'\bigvee',
	u'\u22c2' : r'\bigcap',
	u'\u22c3' : r'\bigcup',
	u'\u2a00' : r'\bigodot',
	u'\u2a01' : r'\bigoplus',
	u'\u2a02' : r'\bigotimes',
}

T = {

	u'\u2192' : r'\rightarrow ',
	#Greek letters
	u'\U0001d6fc' : r'\alpha ',
	u'\U0001d6fd' : r'\beta ',
	u'\U0001d6fe' : r'\gamma ',
	u'\U0001d6ff' : r'\theta ',
	u'\U0001d700' : r'\epsilon ',
	u'\U0001d701' : r'\zeta ',
	u'\U0001d702' : r'\eta ',
	u'\U0001d703' : r'\theta ',
	u'\U0001d704' : r'\iota ',
	u'\U0001d705' : r'\kappa ',
	u'\U0001d706' : r'\lambda ',
	u'\U0001d707' : r'\m ',
	u'\U0001d708' : r'\n ',
	u'\U0001d709' : r'\xi ',
	u'\U0001d70a' : r'\omicron ',
	u'\U0001d70b' : r'\pi ',
	u'\U0001d70c' : r'\rho ',
	u'\U0001d70d' : r'\varsigma ',
	u'\U0001d70e' : r'\sigma ',
	u'\U0001d70f' : r'\ta ',
	u'\U0001d710' : r'\upsilon ',
	u'\U0001d711' : r'\phi ',
	u'\U0001d712' : r'\chi ',
	u'\U0001d713' : r'\psi ',
	u'\U0001d714' : r'\omega ',
	u'\U0001d715' : r'\partial ',
	u'\U0001d716' : r'\varepsilon ',
	u'\U0001d717' : r'\vartheta ',
	u'\U0001d718' : r'\varkappa ',
	u'\U0001d719' : r'\varphi ',
	u'\U0001d71a' : r'\varrho ',
	u'\U0001d71b' : r'\varpi ', 
	#Relation symbols
	u'\u2190' : r'\leftarrow ',
	u'\u2191' : r'\uparrow ',
	u'\u2192' : r'\rightarrow ',
	u'\u2193' : r'\downright ',
	u'\u2194' : r'\leftrightarrow ',
	u'\u2195' : r'\updownarrow ',
	u'\u2196' : r'\nwarrow ',
	u'\u2197' : r'\nearrow ',
	u'\u2198' : r'\searrow ',
	u'\u2199' : r'\swarrow ',
	u'\u22ee' : r'\vdots ',
	u'\u22ef' : r'\cdots ',
	u'\u22f0' : r'\adots ',
	u'\u22f1' : r'\ddots ',
	u'\u2260' : r'\ne ',
	u'\u2264' : r'\leq ',
	u'\u2265' : r'\geq ',
	u'\u2266' : r'\leqq ',
	u'\u2267' : r'\geqq ',
	u'\u2268' : r'\lneqq ',
	u'\u2269' : r'\gneqq ',
	u'\u226a' : r'\ll ',
	u'\u226b' : r'\gg ',
	u'\u2208' : r'\in ',
	u'\u2209' : r'\notin ',
	u'\u220b' : r'\ni ',
	u'\u220c' : r'\nni ',

	#Ordinary symbols
	u'\u221e' : r'\infty ',
	#Binary relations
	u'\u00b1' : r'\pm ',
	u'\u2213' : r'\mp ',
	#Italic, Latin, uppercase
	u'\U0001d434' : 'A',
	u'\U0001d435' : 'B',
	u'\U0001d436' : 'C',
	u'\U0001d437' : 'D',
	u'\U0001d438' : 'E',
	u'\U0001d439' : 'F',
	u'\U0001d43a' : 'G',
	u'\U0001d43b' : 'H',
	u'\U0001d43c'  : 'I',
	u'\U0001d43d'  : 'J',
	u'\U0001d43e'  : 'K',
	u'\U0001d43f'   : 'L',
	u'\U0001d440'  : 'M',
	u'\U0001d441'  : 'N',
	u'\U0001d442'  : 'O',
	u'\U0001d443'  : 'P',
	u'\U0001d444'  : 'Q',
	u'\U0001d445'  : 'R',
	u'\U0001d446'  : 'S',
	u'\U0001d447'  : 'T',
	u'\U0001d448'  : 'U',
	u'\U0001d449'  : 'V',
	u'\U0001d44a'  : 'W',
	u'\U0001d44b'  : 'X',
	u'\U0001d44c'  : 'Y',
	u'\U0001d44d'  : 'Z',
	#Italic, Latin, lowercase
	u'\U0001d44e'  : 'a',
	u'\U0001d44f'   : 'b',
	u'\U0001d450'  : 'c',
	u'\U0001d451'  : 'd',
	u'\U0001d452'  : 'e',
	u'\U0001d453'  : 'f',
	u'\U0001d454'  : 'g',
	u'\U0001d456'  : 'i',
	u'\U0001d457'  : 'j',
	u'\U0001d458'  : 'k',
	u'\U0001d459'  : 'l',
	u'\U0001d45a'  : 'm',
	u'\U0001d45b'  : 'n',
	u'\U0001d45c'   : 'o',
	u'\U0001d45d'  : 'p',
	u'\U0001d45e'  : 'q',
	u'\U0001d45f'   : 'r',
	u'\U0001d460'  : 's',
	u'\U0001d461'  : 't',
	u'\U0001d462'  : 'u',
	u'\U0001d463'  : 'v',
	u'\U0001d464'  : 'w',
	u'\U0001d465'  : 'x',
	u'\U0001d466'  : 'y',
	u'\U0001d467'  : 'z',
}

FUNC ={
	'sin' : r'\sin({fe})',
	'cos' : r'\cos({fe})',
	'tan' : r'\tan({fe})',
	'arcsin' : r'\arcsin({fe})',
	'arccos' : r'\arccos({fe})',
	'arctan' : r'\arctan({fe})',
	'arccot' : r'\arccot({fe})',
	'sinh' : r'\sinh({fe})',
	'cosh' : r'\cosh({fe})',
	'tanh' : r'\tanh({fe})',
	'coth' : r'\coth({fe})',
	'sec'  : r'\sec({fe})',
	'csc'  : r'\csc({fe})',
}

FUNC_PLACE = '{fe}'

BRK = '\\\\'

CHR_DEFAULT = {
	'ACC_VAL':r'\hat{{{0}}}',
}

POS = {
	'top' : r'\overline{{{0}}}', # not sure
	'bot' : r'\underline{{{0}}}',
}

POS_DEFAULT = {
	'BAR_VAL': r'\overline{{{0}}}',
}

SUB = '_{{{0}}}'

SUP = '^{{{0}}}'

F = {
	'bar': r'\frac{{{num}}}{{{den}}}',
	'skw': r'^{{{num}}}/_{{{den}}}',
	#noBar -- not support
	#lin -- not support
}
F_DEFAULT = r'\frac{{{num}}}{{{den}}}'

D  = r'\left{left}{text}\right{right}'

D_DEFAULT = {
	'left':'(',
	'right':')',
	'null':'.',
}

RAD = r'\sqrt[{deg}]{{{text}}}'

RAD_DEFAULT = r'\sqrt{{{text}}}'

ARR = r'\begin{{array}}{{c}}{text}\end{{array}}'

LIM_FUNC = {
	'lim':r'\lim_{{{lim}}}',
	'max':r'\max_{{{lim}}}',
	'min':r'\min_{{{lim}}}',
}

LIM_TO  = (r'\rightarrow',r'\to')

LIM_UPP = r'\overset{{{lim}}}{{{text}}}'

M = r'\begin{{matrix}}{text}\end{{matrix}}'