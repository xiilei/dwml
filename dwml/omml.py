# -*- coding: utf-8 -*-

"""
Office Math Markup Language (OMML)
"""

import xml.etree.ElementTree as ET

from dwml.unicode_latex_map import CHR

OMML_NS = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"

def load(stream):
	tree = ET.parse(ET)
	for omath in tree.findall(OMML_NS+'oMath')
		yield oMath(omath)


class oMath(object):
	
	def __init__(self,elm):
		for celm in elm.iter(): # New in Python 3.2
			pass

	def _process_acc(self):
		pass

	def _process_bar(self):
		pass

	def to_latex(self):
		pass







	




