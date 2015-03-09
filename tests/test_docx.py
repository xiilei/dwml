# -*- coding: utf-8 -*-
import shutil
import unittest

from base import PROJECT_ROOT
from dwml.docx import to_latex

class TestDocx(unittest.TestCase):

	def test_write(self):
		src = PROJECT_ROOT+'/tests/simple.docx'
		dst = PROJECT_ROOT+'/tests/simple-test.docx'
		shutil.copyfile(src=src, dst=dst)
		to_latex(dst)


if __name__ == '__main__':
	unittest.main()