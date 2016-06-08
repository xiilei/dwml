# -*- coding: utf-8 -*-

from setuptools import setup,Command

from dwml import __version__

class TestCommand(Command):
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		import sys, subprocess
		raise SystemExit(
		    subprocess.call([sys.executable,
		                     '-Wd',
		                     'tests/test_load.py']))

setup(
	name='dwml',
	version=__version__,
	license='http://www.apache.org/licenses/LICENSE-2.0',
	description='ms-office omml to latex converter',
	author='xilei',
	author_email='xilei125@163.com',
	packages=['dwml'],
	keywords=['word','excel','omml','latex'],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: Implementation :: CPython',
		'Programming Language :: Python :: Implementation :: PyPy',
	],
	cmdclass=dict(test=TestCommand)
	)