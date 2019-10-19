#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import unittest
from base import PROJECT_ROOT

from dwml import omml

class TestLoad(unittest.TestCase):

	def test_load_ml(self):
		latex_results = [
		r'\sin(\sqrt[3]{x})^{x^{11}}/_{b}x_{m}^{n}',
		r'\tilde{a}\begin{array}{c}a=b+c\\d+e=f\end{array}\\\underline{cdef}']
		i = 0	
		for omath in omml.load(PROJECT_ROOT+'/tests/simple.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1

	def test_load_group(self):
		latex_results = [
			r'A\overbrace{123}\underbrace{456}=\left\{a+b\right)'
		]
		i=0
		for omath in omml.load(PROJECT_ROOT+'/tests/group.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1

	def test_load_lim(self):
		latex_results = [
			r'A=log_{x}y\max_{0\leq x\leq 1}xe^{−x^{2}}\lim_{1\to \infty }a\overset{def}{=}x'
		]
		i=0
		for omath in omml.load(PROJECT_ROOT+'/tests/lim.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1

	def test_load_m(self):
		latex_results = [
			r'A=\left(\begin{matrix}1&2&3\\4&5&6\end{matrix}\right)\sum_{1}^{20}x'
		]
		i=0
		for omath in omml.load(PROJECT_ROOT+'/tests/m.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1
	def test_load_d(self):
		latex_results = [
			r'\left\{\begin{array}{c}m+1\leq 2m-1\\m+1>5\end{array}\right.'
		]
		i=0
		for omath in omml.load(PROJECT_ROOT+'/tests/d.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1
	def test_load_d(self):
		latex_results = [
			r'\left(\begin{array}{c}m+1\leq 2m-1\\m+1>5\end{array}\right]'
		]
		i=0
		for omath in omml.load(PROJECT_ROOT+'/tests/d-np.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1
	def test_escape(self):
		self.assertEqual(omml.escape_latex(r'\\\\\\'),'\\\\\\')

	def test_nobar(self):
		latex_results = [
			r'\left(x+a\right)^{n}=\sum_{k=0}^{n}\left(\genfrac{}{}{0pt}{}{n}{k}\right)x^{k}a^{n-k}'
		]
		i=0
		for omath in omml.load(PROJECT_ROOT+'/tests/nobar.xml'):
			self.assertEqual(omath.latex,latex_results[i])
			i=i+1



if __name__ == '__main__':
	unittest.main()
