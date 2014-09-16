# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# Copyright © 2014 Roland Sieker <ospalh@gmail.com>
#
# License: GNU AGPL, version 3 or later;
# http://www.gnu.org/licenses/agpl.html

from ..lang import _
from .anki2 import Anki2Importer
from .apkg import AnkiPackageImporter
from .csvfile import TextImporter
from .mnemo import MnemosyneImporter
from .pauker import PaukerImporter
from .supermemo_xml import SupermemoXmlImporter

Importers = (
    (_("Text separated by tabs or semicolons (*)"), TextImporter),
    (_("Packaged Anki Deck (*.apkg *.zip)"), AnkiPackageImporter),
    (_("Mnemosyne 2.0 Deck (*.db)"), MnemosyneImporter),
    (_("Supermemo XML export (*.xml)"), SupermemoXmlImporter),
    (_("Pauker 1.8 Lesson (*.pau.gz)"), PaukerImporter))
