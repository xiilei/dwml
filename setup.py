# -*- coding: utf-8 -*-

from setuptools import setup

from dwml import __VERSION__


setup(
	name='dwml',
	version=__VERSION__,
	license='http://www.apache.org/licenses/LICENSE-2.0',
	description='read drawing of Ms-office (2007 and above,omml,picture),And Convert them to latex',
	author='xilei',
	author_email='xilei125@163.com',
	packages=['dwml'],
	keywords=['word','execl','omml','latex'],
	classifiers=[
		'Development Status :: 3 - Alpha Development Status',
		'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Office/Education',
	]

)