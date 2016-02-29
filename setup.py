from setuptools import setup, find_packages
import sys, os

version = '1.1'


setup(name='skynet',
      version=version,
      description="import skynet, if you dare",
      long_description=open('README.rst', 'rt').read() + '\n\n' + open('CHANGES.txt', 'rt').read(),
      classifiers=[
          'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='skynet',
      author='Lennart Regebro',
      author_email='regebro@gmail.com',
      url='http://xkcd.com/521/',
      license='CC0 1.0 Universal',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      entry_points={
               'console_scripts': [
                   'skynet = skynet:Skynet',
               ],
      },
      zip_safe=False,
      )
