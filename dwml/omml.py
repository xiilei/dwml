# -*- coding: utf-8 -*-

"""
Office Math Markup Language (OMML)
"""

try:
	import lxml.etree as ET # It's faster than 'xml.etree.ElementTree' in CPython
except ImportError:
	import xml.etree.ElementTree as ET

from dwml.utils import PY3

from dwml.latex_dict import (CHARS,CHR,CHR_BO,CHR_DEFAULT,POS,POS_DEFAULT
	,SUB,SUP,F,F_DEFAULT,T,FUNC,D,D_DEFAULT,RAD,RAD_DEFAULT,ARR
	,LIM_FUNC,LIM_TO,LIM_UPP,M,BRK)

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

def get_val(key,default=None,store=CHR):
	if key:
		return key if not store else store.get(key,key)
	else:
		return default

class NotSupport(Exception):
	pass


class Tag2Method(object):

	def call_method(self,elm,stag=None):
		getmethod = self.tag2meth.get
		if stag is None:
			stag = elm.tag.replace(OMML_NS,'')
		method = getmethod(stag)
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
			stag = _e.tag.replace(OMML_NS,'')			
			if include and (stag not in include):
				continue
			t = self.call_method(_e,stag=stag)
			if t is None:
				t = self.process_unknow(_e,stag)
				if t is None:
					continue
			yield (stag,t,_e)

	def process_children_dict(self,elm,include=None):
		"""
		process children of the elm,return dict
		"""
		latex_chars = dict()
		for stag,t,e in self.process_children_list(elm,include):
			latex_chars[stag] = t
		return latex_chars

	def process_children(self,elm,include=None):
		"""
		process children of the elm,return string
		"""
		return ''.join(( str(t) for stag,t,e in self.process_children_list(elm,include)))

	def process_unknow(self,elm,stag):
		return None


class Pr(Tag2Method):

	brk = None

	chr = None

	pos = None

	begChr = None

	endChr = None

	type = None

	__val_tags = ('chr','pos','begChr','endChr','type')

	""" common properties of element"""
	def __init__(self, elm):
		self.process_children(elm)

	def __str__(self):
		return '' if self.brk is None else str(self.brk)

	def do_common(self,elm):
		stag = elm.tag.replace(OMML_NS,'')
		if stag in self.__val_tags:
			self.__dict__[stag] = elm.get('{0}val'.format(OMML_NS))
			
	tag2meth = {
		'brk':do_common,
		'chr':do_common,
		'pos':do_common,
		'begChr':do_common,
		'endChr':do_common,
		'type':do_common,
	}


class oMath2Latex(Tag2Method):
	"""
	Convert oMath element of omml to latex
	"""
	_t_dict = T

	__direct_tags = ('box','sSub','sSup','sSubSup','num','den','deg','e')

	def __init__(self,element):
		self._latex = self.process_children(element)		

	def __str__(self):
		return str(self.latex)	

	def process_unknow(self,elm,stag):
		if 	stag[-2:] == 'Pr':
			return Pr(elm)
		elif stag in self.__direct_tags:
			return self.process_children(elm)
		else:
			return None

	@property
	def latex(self):
		return self._latex if PY3 else self._latex.encode('utf-8')

	def do_acc(self,elm):
		"""
		the accent function
		"""
		c_dict = self.process_children_dict(elm)
		latex_s = get_val(c_dict['accPr'].chr,default=CHR_DEFAULT.get('ACC_VAL'),store=CHR)
		return latex_s.format(c_dict['e'])		

	def do_bar(self,elm):
		"""
		the bar function
		"""
		c_dict = self.process_children_dict(elm)
		latex_s = get_val(c_dict['barPr'].pos,default=POS_DEFAULT.get('BAR_VAL'),store=POS)
		return latex_s.format(c_dict['e'])

	def do_d(self,elm):
		"""
		the delimiter object
		"""
		c_dict = self.process_children_dict(elm)
		s_val = get_val(c_dict['dPr'].begChr,default=D_DEFAULT.get('left'),store=None)
		e_val = get_val(c_dict['dPr'].endChr,default=D_DEFAULT.get('right'),store=None)
		null = D_DEFAULT.get('null')
		return D.format(left= null if not s_val else escape_latex(s_val),
					text=c_dict['e'],
					right= null if not e_val else  escape_latex(e_val))


	def do_spre(self,elm):
		"""
		the Pre-Sub-Superscript object -- Not support yet
		"""
		pass

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
		latex_s = get_val(c_dict['fPr'].type,default=F_DEFAULT,store=F)
		return latex_s.format(num=c_dict.get('num'),den=c_dict.get('den'))

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
		for stag,t,e in self.process_children_list(elm):
			if stag == 'r':
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
		c_dict = self.process_children_dict(elm)
		latex_s = get_val(c_dict['groupChrPr'].chr)
		return latex_s.format(c_dict['e'])

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
			
	def do_eqarr(self,elm):
		"""
		the Array object
		"""
		return ARR.format(text=BRK.join(
			[t for stag,t,e in self.process_children_list(elm,include=('e',))]))


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
		t_dict = self.process_children_dict(elm,include=('e','lim'))
		return LIM_UPP.format(lim=t_dict.get('lim'),text=t_dict.get('e'))

	def do_lim(self,elm):
		"""
		the lower limit of the limLow object and the upper limit of the limUpp function
		"""
		return self.process_children(elm).replace(LIM_TO[0],LIM_TO[1])
	
	def do_m(self,elm):
		"""
		the Matrix object
		"""
		rows = []
		for stag,t,e in self.process_children_list(elm):
			if stag is 'mPr':
				pass
			elif stag == 'mr':
				rows.append(t)
		return M.format(text=BRK.join(rows))

	def do_mr(self,elm):
		"""
		a single row of the matrix m
		"""
		return '&'.join(
			[t for stag,t,e in self.process_children_list(elm,include=('e',))])

	def do_nary(self,elm):
		"""
		the n-ary object
		"""
		res = []
		bo = ''
		for stag,t,e in self.process_children_list(elm):
			if stag == 'naryPr':
				bo = get_val(t.chr,store=CHR_BO)
			else :
				res.append(t)
		return bo+''.join(res)

	def do_r(self,elm):
		"""
		Get text from 'r' element,And try convert them to latex symbols
		@todo text style support , (sty)
		@todo \text (latex pure text support)
		"""
		_str = []
		for s in elm.findtext('./{0}t'.format(OMML_NS)):
			_str.append(self._t_dict.get(s,s))
		return escape_latex(''.join(_str))

	tag2meth={
		'acc' : do_acc,
		'r' : do_r,
		'bar' : do_bar,
		'sub' : do_sub,
		'sup' : do_sup,
		'f'   : do_f,
		'func': do_func,
		'fName' : do_fname,
		'groupChr' : do_groupchr,
		'd' : do_d,
		'rad' : do_rad,
		'eqArr' : do_eqarr,
		'limLow' : do_limlow,
		'limUpp' : do_limupp,
		'lim' : do_lim,
		'm' : do_m,
		'mr' : do_mr,
		'nary' : do_nary,
 	}
