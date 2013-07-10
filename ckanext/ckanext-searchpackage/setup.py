from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-searchpackage',
	version=version,
	description="Change search order of package",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Arne Jensen',
	author_email='arfj@aarhus.dk',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.searchpackage'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[],
	entry_points=\
	"""
		[ckan.plugins]		 
			searchpackage=ckanext.searchpackage.plugin:SearchPlugin
	""",
)
