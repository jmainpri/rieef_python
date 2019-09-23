cmake_minimum_required(VERSION 2.8.12)
project(rieef_python)

set(PYBIND11_PYTHON_VERSION 2.7 CACHE STRING "")
add_subdirectory(pybind11)
pybind11_add_module(rieef rieef/main.cpp)

# The library must not have any prefix and should be located in
# a subfolder that includes the package name. The setup will be
# more complicated otherwise.
set_target_properties( rieef
PROPERTIES
  PREFIX ""
  LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/rieef"
)

# Place the initialization file in the output directory for the Python
# bindings. This will simplify the installation.
configure_file( rieef/__init__.py
${CMAKE_CURRENT_BINARY_DIR}/rieef/__init__.py
)

# Ditto for the setup file.
configure_file( rieef/setup.py
${CMAKE_CURRENT_BINARY_DIR}/rieef/setup.py
)