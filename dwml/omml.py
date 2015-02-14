# -*- coding: utf-8 -*-

"""
Office Math Markup Language (OMML)
"""

try:
	import lxml.etree as ET # It's faster than 'xml.etree.ElementTree' in CPython
except ImportError:
	import xml.etree.ElementTree as ET

from dwml.utils import PY3

from dwml.latex_dict import (CHARS,CHR,CHR_DEFAULT,POS,POS_DEFAULT
	,SUB,SUP,F,F_DEFAULT,T,FUNC,D,D_DEFAULT,RAD,RAD_DEFAULT,ARR
	,LIM_FUNC,LIM_TO)

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
		return str(self.get_latex())


	def call_method(self,elm,s_tag=None):
		getmethod = self.tag2meth.get
		if s_tag is None:
			s_tag = elm.tag.replace(OMML_NS,'')
		method = getmethod(s_tag)
		if method:
			return method(self,elm)
		else:
			return None

	def process_children_list(self,elm,include=None):
		"""
		process children of the elm,return iterable
		"""
		for _e in list(elm):
			if (OMML_NS not in _e.tag):
				continue
			s_tag = _e.tag.replace(OMML_NS,'')
			if include and (s_tag not in include):
				continue
			t = self.call_method(_e,s_tag=s_tag)
			if t is None:
				continue
			yield (s_tag,t)
			
	def process_children_dict(self,elm,include=None):
		"""
		process children of the elm,return dict
		"""
		latex_chars = dict()
		for s_tag,t in self.process_children_list(elm,include):
			latex_chars[s_tag] = t
		return latex_chars

	def process_children(self,elm,include=None):
		"""
		process children of the elm,return string
		"""
		return ''.join(( t for s_tag,t in self.process_children_list(elm,include)))

	def process_chrval(self,elm,chr_match,default=None,with_e=True,store=CHR):
		"""
		the accent function,
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
			text = self.call_method(elm.find('./{0}e'.format(OMML_NS)))
			return (latex_s,text)
		else:
			return latex_s


	def get_latex(self):
		return self._latex if PY3 else self._latex.encode('utf-8')

	def do_acc(self,elm):
		"""
		the accent function
		"""
		latex_s,text = self.process_chrval(elm,chr_match='./{0}accPr/{0}chr'
			,default = CHR_DEFAULT.get('ACC_VAL'))
		return latex_s.format(text)
		

	def do_bar(self,elm):
		"""
		the bar function
		"""
		latex_s,text = self.process_chrval(elm,chr_match='./{0}barPr/{0}pos'
			,default = POS_DEFAULT.get('BAR_VAL'),store=POS)
		return latex_s.format(text)		

	def do_box(self,elm):
		"""
		the box object
		"""
		return self.process_children(elm)

	def do_d(self,elm):
		"""
		the delimiter object
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
		the Pre-Sub-Superscript object -- Not support yet
		"""
		pass

	def do_ssub(self,elm):
		"""
		the subscript object
		"""
		return self.process_children(elm)

	def do_ssup(self,elm):
		"""
		the supscript object
		"""
		return self.process_children(elm)

	def do_ssubsup(self,elm):
		"""
		the sub-superscript object
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
		the fraction object
		"""
		c_dict = self.process_children_dict(elm)
		latex_s = c_dict.get('fPr',F_DEFAULT)
		return latex_s.format(num=c_dict.get('num'),den=c_dict.get('den'))

	def do_fpr(self,elm):
		type_elm = elm.find('./{0}type'.format(OMML_NS))
		if type_elm is not None:
			val = type_elm.get('{0}val'.format(OMML_NS))
			if val is not None:
				return F.get(val,F_DEFAULT)
		return F_DEFAULT

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
		the Function-Apply object (Examples:sin cos)
		"""
		c_dict = self.process_children_dict(elm)
		func_name = c_dict.get('fName')
		return func_name.replace('{fe}',c_dict.get('e'))

	def do_fname(self,elm):
		"""
		the func name
		"""
		latex_chars = []
		for s_tag,t in self.process_children_list(elm):
			if s_tag == 'r':
				if FUNC.get(t):
					latex_chars.append(FUNC[t])
				else :
					raise NotSupport("Not support func %s" % t)
			else:
				latex_chars.append(t)
		latex_chars.append('{fe}') #do_func will replace this
		return ''.join(latex_chars)

	def do_groupchr(self,elm):
		"""
		the Group-Character object
		"""
		latex_s,text = self.process_chrval(elm,chr_match='./{0}groupChrPr/{0}chr')
		return latex_s.format(text)

	def do_rad(self,elm):
		"""
		the radical object
		"""
		c_dict = self.process_children_dict(elm)
		text = c_dict.get('e')
		deg_text = c_dict.get('deg')
		if deg_text:
			return RAD.format(deg=deg_text,text=text)
		else:
			return RAD_DEFAULT.format(text=text)
			

	def do_deg(self,elm):
		"""
		the degree in the mathematical radical
		"""
		return self.process_children(elm)		

	def do_eqarr(self,elm):
		"""
		the Array object
		"""
		return ARR.format(text='\\\\'.join(
			[t for s_tag,t in self.process_children_list(elm,include=('e',))]))


	def do_limlow(self,elm):
		"""
		the Lower-Limit object
		"""
		t_dict = self.process_children_dict(elm,include=('e','lim'))
		latex_s = LIM_FUNC.get(t_dict['e'])
		if not latex_s :
			raise NotSupport("Not support lim %s" % t_dict['e'])
		else:
			return latex_s.format(lim=t_dict.get('lim'))

	def do_limupp(self,elm):
		"""
		the Upper-Limit object
		"""
		pass

	def do_lim(self,elm):
		"""
		the lower limit of the limLow object and the upper limit of the limUpp function
		"""
		return self.process_children(elm).replace(LIM_TO[0],LIM_TO[1])

	def do_nary(self,elm):
		"""
		the n-ary object
		"""
		pass

	def do_e(self,elm):
		"""
		the "element object" has more unknown elements,so process all children of it
		"""
		return self.process_children(elm)

	def do_r(self,elm):
		"""
		Get text from 'r' element,And try convert them to latex symbols
		@todo text style support , (sty)
		"""
		_str = []
		for s in elm.findtext('./{0}t'.format(OMML_NS)):
			_str.append(self._t_dict.get(s,s))
		return escape_latex(''.join(_str))

	#@todo restructure
	tag2meth={
		'acc' : do_acc,
		'e' : do_e,
		'r' : do_r,
		'bar' : do_bar,
		'box' : do_box,
		'sub' : do_sub,
		'sup' : do_sup,
		'sSub' : do_ssub,
		'sSup' : do_ssup,
		'sSubSup' : do_ssubsup,
		'f'   : do_f,
		'num' : do_num,
		'den' : do_den,
		'func': do_func,
		'fPr' : do_fpr,
		'fName' : do_fname,
		'groupChr' : do_groupchr,
		'd' : do_d,
		'rad' : do_rad,
		'deg' : do_deg,
		'eqArr' : do_eqarr,
		'limLow' : do_limlow,
		'lim' : do_lim,
 	}
