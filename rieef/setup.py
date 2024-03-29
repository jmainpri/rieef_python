from distutils.core import setup

import sys
if sys.version_info < (2,7):
  sys.exit('Sorry, Python < 2,7 is not supported')

setup(
  name        = 'cmake_cpp_pybind11',
  version     = '${PACKAGE_VERSION}', # TODO: might want to use commit ID here
  packages    = [ 'rieef' ],
  package_dir = {
    '': '${CMAKE_CURRENT_BINARY_DIR}'
  },
  package_data = {
    '': ['rieef.so']
  }
)