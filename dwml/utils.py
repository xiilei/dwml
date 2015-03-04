# -*- coding: utf-8 -*-

import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

def module_to_unicode(module,charset='utf-8'):
	"""
	Convert latex_dict module attrs to unicode attrs in Python2.x
	"""
	attrs = module.__dict__
	for n in dir(module):
		if n[0:2] == '__':
			continue
		if isinstance(attrs[n],str):
			attrs[n] = unicode(attrs[n],charset)			
		elif isinstance(attrs[n],dict):
			new_dict = dict()
			for k in attrs[n]:
				k = k if isinstance(k,unicode) else unicode(k,'utf-8')				
				new_dict[k]  = unicode(attrs[n][k],charset)
			attrs[n] = new_dict
		elif isinstance(attrs[n] ,list):
			new_list = list()
			for v in attrs[n]:
				new_list.append(unicode(v,charset))
			attrs[n] = new_list
