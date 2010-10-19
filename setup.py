from setuptools import setup, find_packages
import os

version = open(os.path.join("iqbio", "pasurvey", "version.txt")).read().strip()

setup(name='iqbio.pasurvey',
      version=version,
      description="Pre-admission survey form and type",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Kurt Bendl',
      author_email='kurt@tool.net',
      url='http://tool.net/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['iqbio'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'collective.autopermission',
          'plone.formwidget.namedfile',
          'plone.namedfile[blobs]',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
