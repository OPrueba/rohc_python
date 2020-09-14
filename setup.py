#!/usr/bin/env python

from distutils.core import setup, Extension
import sys

setup(name='ROHC',
      version='0.1',
      description='Python Robust Header Compression (ROHC) Module',
      author='Joseph Ishac',
      author_email='jishac@nasa.gov',
      ext_modules=[Extension('rohc', ['src/rohc.c'], libraries=['rohc'])],
      )

