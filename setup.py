import gettext
import glob
import os
import subprocess
import sys

from setuptools import setup, find_packages, findall

setup(name='api_mask',
      version='0.0.1',
      license='',
      description='Override API END Point Table',
      author='Michael Kuty',
      author_email='',
      url='',
      packages=find_packages(exclude=['bin', 'smoketests', 'tests']),
      package_data = {'api_mask':
                        [s[len('api_mask/'):] for s in
                         findall('api_mask/templates')]},
      py_modules=[],
      test_suite='tests'
)

