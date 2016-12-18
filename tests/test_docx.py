# -*- coding: utf-8 -*-
import shutil
import unittest

from base import PROJECT_ROOT
from docx import to_latex

class TestDocx(unittest.TestCase):

	def test_write(self):
		src = PROJECT_ROOT+'/tests/tttt.docx'
		dst = PROJECT_ROOT+'/tests/tttt-test.docx'
		shutil.copyfile(src=src, dst=dst)
		to_latex(dst,repl='{0}')


if __name__ == '__main__':
	unittest.main()