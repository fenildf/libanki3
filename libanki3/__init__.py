# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# Copyright © 2013–2014 Roland Sieker <ospalh@gmail.com>
#
# License: GNU AGPL, version 3 or later;
# http://www.gnu.org/licenses/agpl.html

import os
import platform
import sys

# Removed check for Python version. Crash and burn when people try to
# run this with Pythons < 3.

import simplejson as json

__version__ = "0.0.1"

from .storage import Collection
__all__ = ["Collection"]
