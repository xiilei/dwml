# -*- coding: utf-8 -*-

"""
Thinks for
http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html
http://en.wikibooks.org/wiki/LaTeX/Mathematics
http://www.ctan.org/tex-archive/macros/latex/contrib/unicode-math
https://github.com/wspr/unicode-math/blob/master/unicode-math-table.tex
"""

CHR = {
	#Unicode : Latex Math Symbols
	#Top accents
	'\u0300' : r'\grave{{{0}}}',
	'\u0301' : r'\acute{{{0}}}',
	'\u0302' : r'\hat{{{0}}}',
	'\u0303' : r'\tilde{{{0}}}',  
	'\u0304' : r'\bar{{{0}}}',
	'\u0305' : r'\overbar{{{0}}}',
	'\u0306' : r'\breve{{{0}}}',
	'\u0307' : r'\dot{{{0}}}',	  
	'\u0308' : r'\ddot{{{0}}}',
	'\u0309' : r'\ovhook{{{0}}}',
	'\u030A' : r'\ocirc{{{0}}}}',
	'\u030C' : r'\check{{{0}}}}',
	'\u0310' : r'\candra{{{0}}}',
	'\u0312' : r'\oturnedcomma{{{0}}}',
	'\u0315' : r'\ocommatopright{{{0}}}',
	'\u031A' : r'\droang{{{0}}}',
	'\u0338' : r'\not{{{0}}}',
	'\u20D0' : r'\leftharpoonaccent{{{0}}}',
	'\u20D1' : r'\rightharpoonaccent{{{0}}}',
	'\u20D2' : r'\vertoverlay{{{0}}}',
	'\u20D6' : r'\overleftarrow{{{0}}}',
	'\u20D7' : r'\vec{{{0}}}',
	'\u20DB' : r'\dddot{{{0}}}',
	'\u20DC' : r'\ddddot{{{0}}}',
	'\u20E1' : r'\overleftrightarrow{{{0}}}',
	'\u20E7' : r'\annuity{{{0}}}',
	'\u20E9' : r'\widebridgeabove{{{0}}}',
	'\u20F0' : r'\asteraccent{{{0}}}',
	 #Bottom accents
	'\u0330' : r'\wideutilde{{{0}}}',
	'\u0331' : r'\underbar{{{0}}}',
	'\u20E8' : r'\threeunderdot{{{0}}}',
	'\u20EC' : r'\underrightharpoondown{{{0}}}',
	'\u20ED' : r'\underleftharpoondown{{{0}}}',
	'\u20EE' : r'\underledtarrow{{{0}}}',
	'\u20EF' : r'\underrightarrow{{{0}}}',
}

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

F  = r'\frac{{{num}}}{{{den}}}'