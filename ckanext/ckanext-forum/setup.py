from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-forum',
	version=version,
	description="Adds support for Drupal forum link",
	long_description='',
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Jesper Kristensen',
	author_email='jeskr@aarhus.dk',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.forum'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[],
	entry_points=\
	"""
        [ckan.plugins]
		forum=ckanext.forum.plugin:ForumPlugin
	""",
)

