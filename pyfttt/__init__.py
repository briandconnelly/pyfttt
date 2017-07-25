# -*- coding: utf-8 -*-

VERSION = (0, 3, 2)
__version__ = ".".join(map(str, VERSION[0:3])) + "".join(VERSION[3:])
__license__ = "BSD"

from pyfttt.sending import *
