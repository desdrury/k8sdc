#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from k8sdc import __version__, __author__, __email__
import os
from collections import namedtuple


def add_data_files(directory, data_files):
  DataFiles = namedtuple('DataFiles', ['directory', 'files'])
  for root, dirnames, filenames in os.walk(directory):
    if len(filenames) > 0:
      files = DataFiles('k8sdc/' + root, [])
      for filename in filenames:
        files[1].append(os.path.join(root, filename))
      data_files.append(files)


data_files = []
data_files.append(('k8sdc', ['site.yaml', 'LICENSE']))
add_data_files('providers', data_files)
add_data_files('roles', data_files)
add_data_files('group_vars', data_files)
add_data_files('keys', data_files)
add_data_files('utilities', data_files)

with open('README.rst') as readme_file:
    long_description = readme_file.read()


setup(name             = 'k8sdc',
      version          = __version__,
      description      = 'k8sdc',
      long_description = long_description,
      keywords         = ['k8sdc'],
      author           = __author__,
      author_email     = __email__,
      url              = 'https://github.com/desdrury/k8sdc',
      license          = 'Apache License version 2.0',
      classifiers      = ['Development Status :: 2 - Pre-Alpha',
                          'Environment :: Console',
                          'Intended Audience :: System Administrators',
                          'Intended Audience :: Developers',
                          'License :: OSI Approved :: Apache Software License',
                          'Natural Language :: English',
                          'Programming Language :: Python :: 2.7'],
      packages         = find_packages(),
      data_files       = data_files,
      scripts          = ['bin/k8sdc'],
      install_requires = ['ansible>=2.1.1.0',
                          'docopt>=0.6.2'])