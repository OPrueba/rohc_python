#!/usr/bin/env python

from distutils.core import setup, Extension
import sys

requires = [
    python_version >= "2.6.0"'
]

setup(name='ROHC',
      version='0.1',
      description='Python Robust Header Compression (ROHC) Module',
      author='Joseph Ishac',
      author_email='jishac@nasa.gov',
      install_requires=requires,
      ext_modules=[Extension('rohc', ['src/rohc.c'], libraries=['rohc'])],
      )

