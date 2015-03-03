#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import unittest
from base import PROJECT_ROOT

from dwml import omml

class TestLoad(unittest.TestCase):

	def test_load_ml(self):
		latex_results = [
		r'\sin(\sqrt[3]{x})\sqrt[3]{x}^{x^{11}}/_{b}x_{m}^{n}',
		r'\tilde{a}\begin{array}{c}a=b+c\\d+e=f\end{array}\underline{cdef}']
		i = 0	
		for omath in omml.load(PROJECT_ROOT+'/tests/simple.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1

	def test_load_group(self):
		latex_results = [
			r'𝐴\overbrace{123}\underbrace{456}=\left\{a+b\right)'
		]
		i=0
		for omath in omml.load(PROJECT_ROOT+'/tests/group.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1

	def test_load_lim(self):
		latex_results = [
			r'𝐴=log_{𝑥}𝑦\max_{0≤𝑥≤1}𝑥𝑒^{−𝑥^{2}}\lim_{1\to\infty}𝑎\overset{def}{=}x'
		]
		i=0
		for omath in omml.load(PROJECT_ROOT+'/tests/lim.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1

	def test_load_m(self):
		latex_results = [
			r'𝐴=\left(\begin{matrix}1&2&3\\4&5&6\end{matrix}\right)\sum_{1}^{20}x'
		]
		i=0
		for omath in omml.load(PROJECT_ROOT+'/tests/m.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1



if __name__ == '__main__':
	unittest.main()
