from setuptools import setup, find_packages
import os

version = '1.0.0.dev0'

tests_require = [
    'ftw.builder',
    'ftw.testbrowser',
]

setup(name='ploneconf2015.testingdemo',
      version=version,
      url='https://github.com/jone/ploneconf2015.testingdemo',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneconf2015'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'Plone',
          'setuptools',
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
