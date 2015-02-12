# -*- coding: utf-8 -*-

"""
Office Math Markup Language (OMML)
"""
try:
	import lxml.etree as ET # It's faster than 'xml.etree.ElementTree' in CPython
except ImportError:
	import xml.etree.ElementTree as ET


from dwml.latex_dict import CHARS,CHR,CHR_DEFAULT,POS,POS_DEFAULT,SUB,SUP,F,T,FUNC,D,D_DEFAULT

OMML_NS = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"


def load(stream):
	tree = ET.parse(stream)
	for omath in tree.findall(OMML_NS+'oMath'):
		yield oMath2Latex(omath)

def escape_latex(strs):
	last = None
	new_chr = []
	for c in strs :
		if (c in CHARS) and (last != '\\'):
			new_chr.append("\\"+c)
		else:
			new_chr.append(c)
		last = c
	return ''.join(new_chr)


class NotSupport(Exception):
	pass


class oMath2Latex(object):
	"""

	"""
	_t_dict = T

	def __init__(self,element):
		self._latex = self.process_children(element)
		

	def __str__(self):
		return self.get_latex()


	def call_methon(self,elm):
		getmethod = self.tag2meth.get
		s_tag = elm.tag.replace(OMML_NS,'')
		method = getmethod(s_tag)
		if method:
			return method(self,elm)
		else:
			return None

	def process_children(self,elm,return_dict=False,t_dict=None):
		latex_chars = list() if not return_dict else dict()
		t_dict_back = self._t_dict	
		if t_dict:
			self._t_dict = t_dict
		
		for _e in list(elm):
			#Ignore elements which not 'm' namespace prefix
			if OMML_NS not in _e.tag:
				continue
			if not return_dict:			
				latex_chars.append(self.call_methon(_e))
			else:
				latex_chars[_e.tag] = self.call_methon(_e)

		self._t_dict = t_dict_back
		if not return_dict:
			return ''.join(latex_chars)
		else:
			return latex_chars

	def process_chrval(self,elm,chr_match,default=None,with_e=True,store=CHR):
		"""
		process the accent function,
		"""
		val_elm = elm.find(chr_match.format(OMML_NS))
		latex_s = ''
		if val_elm is None:
			latex_s = default
		else:
			char_val= val_elm.get('{0}val'.format(OMML_NS))
			if char_val is not None:
				latex_s = store.get(char_val,char_val)
			else:
				latex_s = default
		if with_e:	
			text = self.do_e(elm.find('./{0}e'.format(OMML_NS)))
			return (latex_s,text)
		else:
			return latex_s


	def get_latex(self):
		return self._latex

	def do_acc(self,elm):
		"""
		process the accent function
		"""
		latex_s,text = self.process_chrval(elm,chr_match='./{0}accPr/{0}chr'
			,default = CHR_DEFAULT.get('ACC_VAL'))
		return latex_s.format(text)
		

	def do_bar(self,elm):
		"""
		process the bar function
		"""
		latex_s,text = self.process_chrval(elm,chr_match='./{0}barPr/{0}pos'
			,default = POS_DEFAULT.get('BAR_VAL'),store=POS)
		return latex_s.format(text)		

	def do_box(self,elm):
		"""
		process the box object
		"""
		pass

	def do_d(self,elm):
		"""
		process the delimiter object
		"""
		s_val = self.process_chrval(elm,chr_match='./{0}dPr/{0}begChr',
				default=D_DEFAULT.get('left'),with_e=False)
		e_val,text = self.process_chrval(elm,chr_match='./{0}dPr/{0}endChr',
				default=D_DEFAULT.get('right'))
		null = D_DEFAULT.get('null')
		return D.format(left= null if not s_val else escape_latex(s_val),
					text=text,
					right= null if not e_val else  escape_latex(e_val))


	def do_spre(self,elm):
		"""
		process the Pre-Sub-Superscript object -- Not support yet
		"""
		pass

	def do_ssub(self,elm):
		"""
		process the subscript object
		"""
		return self.process_children(elm)

	def do_ssup(self,elm):
		"""
		process the supscript object
		"""
		return self.process_children(elm)

	def do_ssubsup(self,elm):
		"""
		process the sub-superscript object
		"""
		return self.process_children(elm)

	def do_sub(self,elm):
		text = self.process_children(elm)
		return SUB.format(text)

	def do_sup(self,elm):
		text = self.process_children(elm)
		return SUP.format(text)

	def do_f(self,elm):
		"""
		process the fraction object
		"""
		c_dict = self.process_children(elm,return_dict=True)
		return F.format(num=c_dict.get(OMML_NS+'num'),den=c_dict.get(OMML_NS+'den'))

	def do_num(self,elm):
		"""
		the numerator
		"""
		return self.process_children(elm)

	def do_den(self,elm):
		"""
		the denominator
		"""
		return self.process_children(elm)


	def do_func(self,elm):
		"""
		process the Function-Apply object (Examples:sin cos)
		"""
		c_dict = self.process_children(elm,return_dict=True)
		func_name = c_dict.get(OMML_NS+'fName')
		return func_name.format(c_dict.get(OMML_NS+'e'))

	def do_f_name(self,elm):
		"""
		the func name
		"""
		nr_elm = elm.find('./{0}r'.format(OMML_NS))
		name = self.do_r(nr_elm)
		if FUNC.get(name):
			return FUNC[name]
		else :
			raise NotSupport("Not support func %s" % name)

	def do_group_chr(self,elm):
		"""
		process the Group-Character object
		"""
		latex_s,text = self.process_chrval(elm,chr_match='./{0}groupChrPr/{0}chr')
		return latex_s.format(text)


	def do_e(self,elm):
		"""
		the "element object" has more unknown elements,so process all children of it
		"""
		return self.process_children(elm)

	def do_r(self,elm):
		"""
		Get text from 'r' element,And try convert them to latex symbols
		"""
		_str = []
		for s in elm.findtext('./{0}t'.format(OMML_NS)):
			_str.append(self._t_dict.get(s,s))
		return ''.join(_str)

	#@todo restructure
	tag2meth={
		'acc' : do_acc,
		'e' : do_e,
		'r' : do_r,
		'bar' : do_bar,
		'sub' : do_sub,
		'sup' : do_sup,
		'sSub' : do_ssub,
		'sSup' : do_ssup,
		'sSubSup' : do_ssubsup,
		'f'   : do_f,
		'num' : do_num,
		'den' : do_den,
		'func': do_func,
		'fName' : do_f_name,
		'groupChr' : do_group_chr,
		'd' : do_d,
 	}





	




