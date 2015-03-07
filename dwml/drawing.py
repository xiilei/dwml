# -*- coding: utf-8 -*-
"""
An EMU is defined as follows:
	1\ emu=\frac{1}{914400}US\ inch=\frac{1}{360000}cm
"""


from dwml import ET

#execl drawing namespace
XLSX_NS = '{http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}' 

class XlsxDrawing(object):
	"""
	the drawing object of Spreadsheet	
	"""

	def __init__(self):
		pass

class DocxDrawing(object):
	"""
	the drawing object of Wordprocessing
	"""
	pass

