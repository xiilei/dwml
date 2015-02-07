#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from base import PROJECT_ROOT

from dwml import omml

class TestTurnML(unittest.TestCase):

	def test_acc_latex(self):
		"""
		simple.ml acc element to latex 
		"""
		tree = omml.ET.parse(PROJECT_ROOT+'/tests/simple.ml')
		for omath in tree.findall(omml.OMML_NS+'oMath'):
			for elm in omath:
				if elm.tag == (omml.OMML_NS+'acc'):
					chr_elm = elm.find('./{0}accPr/{0}chr'.format(omml.OMML_NS))
					val = chr_elm.get('{0}val'.format(omml.OMML_NS))
					if not val:
						val = '\u0302' # as default
					latex_s = omml.CHR.get(val)
					if not latex_s:
						raise ValueError('miss latex symbols')
					t_elm = elm.find('./{0}e/{0}r/{0}t'.format(omml.OMML_NS))
					latex =  r'\{0}{{{1}}}'.format(latex_s,t_elm.text)
					self.assertEqual(latex,r'\tilde{a}')
			

if __name__ == '__main__':
	unittest.main()