# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# Copyright © 2014 Roland Sieker <ospalh@gmail.com>
#
# License: GNU AGPL, version 3 or later;
# http://www.gnu.org/licenses/agpl.html

from .template import Template
from .view import View


def render(template, context=None, **kwargs):
    context = context and context.copy() or {}
    context.update(kwargs)
    return Template(template, context).render()
