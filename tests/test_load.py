#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from base import PROJECT_ROOT

from dwml import omml

class TestLoad(unittest.TestCase):

	def test_load_ml(self):
		for omath in omml.load(PROJECT_ROOT+'/tests/simple.xml'):
			print(omath)

	def test_load_group(self):
		for omath in omml.load(PROJECT_ROOT+'/tests/group.xml'):
			print(omath)




if __name__ == '__main__':
	unittest.main()
