from setuptools import setup, find_packages

from ckanext.dgu import __version__

setup(
    name='ckanext-dgu',
    version=__version__,
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    namespace_packages=['ckanext', 'ckanext.dgu'],
    zip_safe=False,
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    license='AGPL',
    url='http://ckan.org/',
    description='CKAN DGU extensions',
    keywords='data packaging component tool server',
    install_requires=[
        # List of dependencies is moved to pip-requirements.txt
        # to avoid conflicts with Debian packaging.
        #'swiss',
        #'ckanclient>=0.5',
        #'ckanext', when it is released
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    package_data={'ckan': ['i18n/*/LC_MESSAGES/*.mo']},
    entry_points="""
        [ckan.plugins]
       
       
       dgu= ckanext.dgu.plugin:DrupalAuthPlugin 

         
    """,
    test_suite = 'nose.collector',
)
