#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of nautilus-compare
#
# Copyright (c) 2020 Lorenzo Carbonell Cerezo <a.k.a. atareao>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import gi
try:
    gi.require_version('Nautilus', '3.0')
    gi.require_version('GObject', '2.0')
except ValueError as e:
    print(e)
    exit(1)
from gi.repository import Nautilus as FileManager
from gi.repository import GObject
import os
import sys
import locale
import gettext
from plumbum import local

APP = 'nautilus-compare'
LANGDIR = os.path.join('usr', 'share', 'locale-langpack')

try:
    current_locale, encoding = locale.getdefaultlocale()
    language = gettext.translation(APP, LANGDIR, [current_locale])
    language.install()
    _ = language.gettext
except:
    _ = str

COMPARE_NONE = 0
COMPARE_DIRECTORIES = 1
COMPARE_FILES = 2


class CompareMenuProvider(GObject.GObject, FileManager.MenuProvider):
    """Implements the 'Compare' extension to the File Manager
    right-click menu"""

    def __init__(self):
        """File Manager crashes if a plugin doesn't implement the __init__
        method"""
        GObject.Object.__init__(self)

    def get_file_items(self, window, sel_items):
        if len(sel_items) == 2 or len(sel_items) == 3:
            compare = COMPARE_NONE
            for afile in sel_items:
                if compare == COMPARE_NONE:
                    if afile.is_directory():
                        compare = COMPARE_DIRECTORIES
                    else:
                        compare = COMPARE_FILES
                elif compare == COMPARE_DIRECTORIES:
                    if not afile.is_directory():
                        return
                elif compare == COMPARE_FILES:
                    if afile.is_directory():
                        return
        else:
            return
        if len(sel_items) == 2:
            label = _('Compare {} with {}').format(
                    sel_items[0].get_name(),
                    sel_items[1].get_name())
        else:
            label = _('Compare {} with {} and {}').format(
                    sel_items[0].get_name(),
                    sel_items[1].get_name(),
                    sel_items[2].get_name())
        menuitem = FileManager.MenuItem(
            name='FileManagerCompare::compare_items',
            label=label,
            tip=_('Compare content'),
            icon='org.gnome.meld')
        menuitem.connect('activate', self.on_menuitem_activated, sel_items)
        return menuitem,

    def on_menuitem_activated(self, widget, sel_items):
        files = [file_in.get_location().get_path() for file_in in sel_items]
        meld = local['meld']
        meld[files]()
        return
