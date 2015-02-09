# -*- coding: utf-8 -*-

"""
Office Math Markup Language (OMML)
"""

import xml.etree.ElementTree as ET

from dwml.latex_dict import CHR,CHR_DEFAULT,POS,POS_DEFAULT

OMML_NS = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"

def load(stream):
	tree = ET.parse(stream)
	for omath in tree.findall(OMML_NS+'oMath'):
		yield oMath2Latex(omath)


class oMath2Latex(object):

	def __init__(self,element):
		self._latex = ''
		self.process(element)

	def __str__(self):
		return self._latex
	
	def process(self,elm):
		latex_chars = list()
		getmetod = self.tag2meth.get
		for elm in list(elm):
			s_tag = elm.tag.replace(OMML_NS,'')
			meth = getmetod(s_tag)
			if meth :
				latex_chars.append(meth(self,elm))
		self._latex = ''.join(latex_chars)

	def get_latex(self):
		return self._latex

	def do_acc(self,elm):
		"""
		process the accent function
		"""
		chr_elm = elm.find('./{0}accPr/{0}chr'.format(OMML_NS))
		latex_func = None
		default_val  = CHR_DEFAULT.get('ACC_VAL')
		if chr_elm is None:
			latex_func = default_val
		else:
			char_val = chr_elm.get('{0}val'.format(OMML_NS))			
			latex_func = self.get_latex(char_val,store=CHR,default=default_val)
		text = self.do_e(elm.find('./{0}e'.format(OMML_NS)))
		return '%s{%s}'  % (latex_func,text)

	def do_bar(self,elm):
		"""
		process the bar function
		"""
		pos_elm = elm.find('./{0}barPr/{0}pos'.format(OMML_NS))
		latex_func = None
		default_val  = POS_DEFAULT.get('POS_VAL')
		if pos_elm is None:
			latex_func = default_val
		else:
			char_val = pos_elm.get('{0}val'.format(OMML_NS))			
			latex_func = self.get_latex(char_val,store=POS,default=default_val)
		text = self.do_e(elm.find('./{0}e'.format(OMML_NS)))
		return '%s{%s}'  % (latex_func,text)

	def do_box(self,elm):
		"""
		process the box object
		"""
		pass

	def do_d(self,elm):
		"""
		process the delimiter object
		"""
		pass

	def do_e(self,elm):
		run_elm = elm.find('./{0}r'.format(OMML_NS))
		return self.do_r(run_elm)

	def do_r(self,elm):
		return elm.findtext('./{0}t'.format(OMML_NS))

	def get_latex(self,key,store=CHR,default=None):
		latex = store.get(key)
		return default if not latex else latex


	tag2meth={
		'acc' : do_acc,
		'e' : do_e,
		'r' : do_r,
		'bar':do_bar,
	}





	




