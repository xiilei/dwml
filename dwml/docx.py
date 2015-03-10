# -*- coding: utf-8 -*-

import re
import zipfile

from dwml import ET,omml
from dwml.utils import PY2

try:
	from io import StringIO
except:
	from StringIO import StringIO


DOCXML_ROOT = ''.join(('<w:document '
			,'xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"'
			,'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" '
			,'xmlns:o="urn:schemas-microsoft-com:office:office" '
			,'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
			,'xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" '
			,'xmlns:v="urn:schemas-microsoft-com:vml" '
			,'xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" '
			,'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
			,'xmlns:w10="urn:schemas-microsoft-com:office:word" '
			,'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
			,'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" '
			,'xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" '
			,'xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" '
			,'xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" '
			,'xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 wp14">'
			,'{0}</w:document>'
		))

TEXT = '<w:r><w:t> {0} </w:t></w:r>'

omath_re = re.compile(r"<m:omath>.*?</m:omath>",re.IGNORECASE)

def to_latex(filename,repl='{0}'):
	"""
	light convert omml to latex from word file (will be changed)
	"""
	with open(filename,'rb') as f:
		peek = f.read(4)
	if peek != b"PK\x03\x04": #zip file
		raise IOError("%s not a valid file" % filename)
	zf = zipfile.ZipFile(filename,mode='a')
	doc_stream = zf.open('word/document.xml')
	all_xml = doc_stream.read()	
	t = omath_re.sub( lambda m:_latex_fn(m,repl),all_xml.decode('utf-8'))
	zf.writestr('word/document.xml',t.encode('utf-8'))
	zf.close()


def _latex_fn(mathobj,f):
	dr = DOCXML_ROOT if not PY2 else unicode(DOCXML_ROOT,'utf-8')
	xml_str = dr.format(mathobj.group(0))
	stream = StringIO(xml_str)
	for omath in omml.load(stream):
		u = TEXT.replace('{0}',f.format(omath.latex))
		stream.close()
		return u if not PY2 else unicode(u,'utf-8')
	return None