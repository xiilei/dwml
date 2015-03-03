# -*- coding: utf-8 -*-

"""
Thinks for
http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html
http://en.wikibooks.org/wiki/LaTeX/Mathematics
http://www.ctan.org/tex-archive/macros/latex/contrib/unicode-math
https://github.com/wspr/unicode-math/blob/master/unicode-math-table.tex
"""

CHARS = ('{','}', '_', '^', '#', '&', '$', '%', '~')

#@todo Compatible python2.x with unicode
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
	u'\u030A' : r'\ocirc{{{0}}}}',
	u'\u030C' : r'\check{{{0}}}}',
	u'\u0310' : r'\candra{{{0}}}',
	u'\u0312' : r'\oturnedcomma{{{0}}}',
	u'\u0315' : r'\ocommatopright{{{0}}}',
	u'\u031A' : r'\droang{{{0}}}',
	u'\u0338' : r'\not{{{0}}}',
	u'\u20D0' : r'\leftharpoonaccent{{{0}}}',
	u'\u20D1' : r'\rightharpoonaccent{{{0}}}',
	u'\u20D2' : r'\vertoverlay{{{0}}}',
	u'\u20D6' : r'\overleftarrow{{{0}}}',
	u'\u20D7' : r'\vec{{{0}}}',
	u'\u20DB' : r'\dddot{{{0}}}',
	u'\u20DC' : r'\ddddot{{{0}}}',
	u'\u20E1' : r'\overleftrightarrow{{{0}}}',
	u'\u20E7' : r'\annuity{{{0}}}',
	u'\u20E9' : r'\widebridgeabove{{{0}}}',
	u'\u20F0' : r'\asteraccent{{{0}}}',
	 #Bottom accents
	u'\u0330' : r'\wideutilde{{{0}}}',
	u'\u0331' : r'\underbar{{{0}}}',
	u'\u20E8' : r'\threeunderdot{{{0}}}',
	u'\u20EC' : r'\underrightharpoondown{{{0}}}',
	u'\u20ED' : r'\underleftharpoondown{{{0}}}',
	u'\u20EE' : r'\underledtarrow{{{0}}}',
	u'\u20EF' : r'\underrightarrow{{{0}}}',
	#Over | group
	u'\u23B4' : r'\overbracket{{{0}}}',
	u'\u23DC' : r'\overparen{{{0}}}',
	u'\u23DE' : r'\overbrace{{{0}}}',
	#Under| group
	u'\u23B5' : r'\underbracket{{{0}}}',
	u'\u23DD' : r'\underparen{{{0}}}',
	u'\u23DF' : r'\underbrace{{{0}}}',

}

CHR_BO = {
	#Big operators,
	u'\u2140' : r'\Bbbsum',
	u'\u220F' : r'\prod',
	u'\u2210' : r'\coprod',
	u'\u2211' : r'\sum',
	u'\u222B' : r'\int',
	u'\u22C0' : r'\bigwedge',
	u'\u22C1' : r'\bigvee',
	u'\u22C2' : r'\bigcap',
	u'\u22C3' : r'\bigcup',
	u'\u2A00' : r'\bigodot',
	u'\u2A01' : r'\bigoplus',
	u'\u2A02' : r'\bigotimes',
}

T = {

	u'\u2192' : r'\rightarrow',
	#Greek letters
	u'\U0001D6FC' : r'\alpha',
	u'\U0001D6FD' : r'\beta',
	u'\U0001D6FE' : r'\gamma',
	u'\U0001D6FF' : r'\theta',
	u'\U0001D700' : r'\epsilon',
	u'\U0001D701' : r'\zeta',
	u'\U0001D702' : r'\eta',
	u'\U0001D703' : r'\theta',
	u'\U0001D704' : r'\iota',
	u'\U0001D705' : r'\kappa',
	u'\U0001D706' : r'\lambda',
	u'\U0001D707' : r'\mu',
	u'\U0001D708' : r'\nu',
	u'\U0001D709' : r'\xi',
	u'\U0001D70A' : r'\omicron',
	u'\U0001D70B' : r'\pi',
	u'\U0001D70C' : r'\rho',
	u'\U0001D70D' : r'\varsigma',
	u'\U0001D70E' : r'\sigma',
	u'\U0001D70F' : r'\tau',
	u'\U0001D710' : r'\upsilon',
	u'\U0001D711' : r'\phi',
	u'\U0001D712' : r'\chi',
	u'\U0001D713' : r'\psi',
	u'\U0001D714' : r'\omega',
	u'\U0001D715' : r'\partial',
	u'\U0001D716' : r'\varepsilon',
	u'\U0001D717' : r'\vartheta',
	u'\U0001D718' : r'\varkappa',
	u'\U0001D719' : r'\varphi',
	u'\U0001D71A' : r'\varrho',
	u'\U0001D71B' : r'\varpi', 
	#Relation symbols
	u'\u2190' : r'\leftarrow',
	u'\u2191' : r'\uparrow',
	u'\u2192' : r'\rightarrow',
	u'\u2193' : r'\downright',
	u'\u2194' : r'\leftrightarrow',
	u'\u2195' : r'\updownarrow',
	u'\u2196' : r'\nwarrow',
	u'\u2197' : r'\nearrow',
	u'\u2198' : r'\searrow',
	u'\u2199' : r'\swarrow',
	u'\u22EE' : r'\vdots',
	u'\u22EF' : r'\cdots',
	u'\u22F0' : r'\adots',
	u'\u22F1' : r'\ddots',
	#Ordinary symbols
	u'\u221E' : r'\infty',
}

FUNC ={
	u'sin' : r'\sin({fe})',
	u'cos' : r'\cos({fe})',
	u'tan' : r'\tan({fe})',
	u'arcsin' : r'\arcsin({fe})',
	u'arccos' : r'\arccos({fe})',
	u'arctan' : r'\arctan({fe})',
	u'arccot' : r'\arccot({fe})',
	u'sinh' : r'\sinh({fe})',
	u'cosh' : r'\cosh({fe})',
	u'tanh' : r'\tanh({fe})',
	u'coth' : r'\coth({fe})',
	u'sec'  : r'\sec({fe})',
	u'csc'  : r'\csc({fe})',
}

BRK = '\\\\'

CHR_DEFAULT = {
	u'ACC_VAL':r'\hat{{{0}}}',
}

POS = {
	u'top' : r'\overline{{{0}}}', # not sure
	u'bot' : r'\underline{{{0}}}',
}

POS_DEFAULT = {
	u'BAR_VAL': r'\overline{{{0}}}',
}

SUB = '_{{{0}}}'

SUP = '^{{{0}}}'

F = {
	u'bar': r'\frac{{{num}}}{{{den}}}',
	u'skw': r'^{{{num}}}/_{{{den}}}',
	#noBar -- not support
	#lin -- not support
}
F_DEFAULT = r'\frac{{{num}}}{{{den}}}'

D  = r'\left{left}{text}\right{right}'

D_DEFAULT = {
	u'left':'(',
	u'right':')',
	u'null':'.',
}

RAD = r'\sqrt[{deg}]{{{text}}}'

RAD_DEFAULT = r'\sqrt{{{text}}}'

ARR = r'\begin{{array}}{{c}}{text}\end{{array}}'

LIM_FUNC = {
	u'lim':r'\lim_{{{lim}}}',
	u'max':r'\max_{{{lim}}}',
	u'min':r'\min_{{{lim}}}',
}

LIM_TO  = (r'\rightarrow',r'\to')

LIM_UPP = r'\overset{{{lim}}}{{{text}}}'

M = r'\begin{{matrix}}{text}\end{{matrix}}'