# -*- coding: utf-8 -*-

import zipfile
import xml.etree.ElementTree as ET
import os


PKGREL = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def open_workbook(filename):
	"""
	Simple read test
	"""
	with open(filename,'rb') as f:
		peek = f.read(4)
	if peek != b"PK\x03\x04": #zip file
		raise IOError("%s not a valid file" % filename)
	zf = zipfile.ZipFile(filename)
	wb_rel_stream = zf.open('xl/_rels/workbook.xml.rels')
	for rid,target,reltype in parse_relationship(wb_rel_stream):
		if reltype == 'worksheet':
			sheet_path = 'xl/'+target
			sheet_base,sheet_file = os.path.split(sheet_path) 
			sheet_rel_path = os.path.relpath('/'.join([sheet_base,'_rels',sheet_file+'.rels']))
			st_rel_stream = zf.open(sheet_rel_path)
			for rid,target,reltype in parse_relationship(st_rel_stream):
				if reltype == 'drawing':
					drawing_path = os.path.relpath(sheet_base+'/'+target)
					#drawing_base,drawing_file = os.path.split(drawing_path) 
					#drawing_rel_path = os.path.relpath('/'.join([drawing_base,'_rels',drawing_file+'.rels']))
					drawing_stream = zf.open(drawing_path)
					#
					return drawing_stream

		

def parse_relationship(stream):
	tree = ET.parse(stream)
	r_tag = PKGREL+ 'Relationship'
	for elem in tree.findall(r_tag):
		rid = elem.get('Id')
		target = elem.get('Target')
		reltype = elem.get('Type').split('/')[-1]
		yield (rid,target,reltype)


def read_picture(stream):
	pass
