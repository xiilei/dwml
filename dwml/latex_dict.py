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
	'\u0300' : r'\grave',
	'\u0301' : r'\acute',
	'\u0302' : r'\hat',
	'\u0303' : r'\tilde',  
	'\u0304' : r'\bar',
	'\u0305' : r'\overbar',
	'\u0306' : r'\breve',
	'\u0307' : r'\dot',	  
	'\u0308' : r'\ddot',
	'\u0309' : r'\ovhook',
	'\u030A' : r'\ocirc',
	'\u030C' : r'\check',
	'\u0310' : r'\candra',
	'\u0312' : r'\oturnedcomma',
	'\u0315' : r'\ocommatopright',
	'\u031A' : r'\droang',
	'\u0338' : r'\not',
	'\u20D0' : r'\leftharpoonaccent',
	'\u20D1' : r'\rightharpoonaccent',
	'\u20D2' : r'\vertoverlay',
	'\u20D6' : r'\overleftarrow',
	'\u20D7' : r'\vec',
	'\u20DB' : r'\dddot',
	'\u20DC' : r'\ddddot',
	'\u20E1' : r'\overleftrightarrow',
	'\u20E7' : r'\annuity',
	'\u20E9' : r'\widebridgeabove',
	'\u20F0' : r'\asteraccent',
	 #Bottom accents
	'\u0330' : r'\wideutilde',
	'\u0331' : r'\underbar',
	'\u20E8' : r'\threeunderdot',
	'\u20EC' : r'\underrightharpoondown',
	'\u20ED' : r'\underleftharpoondown',
	'\u20EE' : r'\underledtarrow',
	'\u20EF' : r'\underrightarrow',
}

CHR_DEFAULT = {
	'ACC_VAL':r'\hat',
}

POS = {
	'top' : r'\overline', # not sure
	'bot' : r'\underline',
}

POS_DEFAULT = {
	'BAR_VAL': r'\overline',
}

SUB = '_'

SUP = '^'