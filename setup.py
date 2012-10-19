from setuptools import find_packages
from setuptools import setup
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('plonetheme', 'fourteamwork', 'docs', 'index.rst'))

setup(name='plonetheme.fourteamwork',
      version='1.0',
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Vilmos Somogyi',
      author_email='vilmos@alasdoo.com',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'hexagonit.portletstyle',
          'hexagonit.testing',
          'manuel',
          'plone.app.testing',
          'plone.app.theming',
          'plone.browserlayer',
          'setuptools',
          'unittest2',
          'zope.i18nmessageid',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
