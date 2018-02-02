"""Properly init the package.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""
from __future__ import print_function, absolute_import
import os

from pyaer import log

FILE_PATH = os.path.realpath(__file__)
CURR_PATH = os.path.dirname(os.path.realpath(__file__))
PKG_PATH = os.path.dirname(CURR_PATH)

# System logging level
LOG_LEVEL = log.DEBUG


try:
    from pyaer import libcaer_wrap as libcaer
except ImportError:
    raise ImportError("libcaer is not in the LD_LIBRARY_PATH")
