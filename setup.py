from setuptools import setup, find_packages
import sys, os

version = '1'

setup(name='skynet',
      version=version,
      description="Skynet",
      long_description="""\
A self-aware program.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='skynet',
      author='Lennart Regebro',
      author_email='regebro@gmail.com',
      url='http://regebro.wordpress.com/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
