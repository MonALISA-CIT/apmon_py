"""
Distutils script for MonaLisa Python ApMon.

To Install:
    python setup.py build --compiler=mingw32 install
"""
from distutils.core import setup

setup(
    name="apmon",
    version="2.17.02",
    long_description=
    "This module provides a lightweight python-based "
    "interface to send monitoring information to "
    "MonaLisa services, using the ApMon API.",
    author="ML Team",
    author_email="MonALISA-CIT@cern.ch",
    url="http://monalisa.caltech.edu",
    download_url = "https://github.com/MonALISA-CIT/apmon_py/tarball/2.17.02",
    keywords = ['ApMon', 'Monalisa', 'system', 'monitor'],
    install_requires = ['psutil', 'future'],
    py_modules=["apmon", "Logger", "ProcInfo"],
    scripts=["examples/mlmetric"],
)
