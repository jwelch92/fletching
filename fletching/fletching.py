#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/HappenApps/Quiver/wiki/Quiver-Data-Format
import json
import os
import os.path
from os.path import join

from pprint import pprint as pp


class Fletching(object):
    EXCLUDED = ["Trash.qvnotebook"]

    def __init__(self, path):
        self.path = path
        self.library = self._load_library_from_path(self.path)

    def _load_library_from_path(self, path):
        ret = {"path": path}
        notebooks = []
        notebook_paths = [n for n in os.listdir(path) if self.is_qvnotebook(path, n)]
        for ndir in notebook_paths:
            if ndir in Fletching.EXCLUDED:
                continue
            cur_notebook = {"path": join(path, ndir)}
            cur_notebook["notes"] = self._load_notes_from_path(join(cur_notebook["path"]))
            if os.path.exists(join(cur_notebook["path"], "meta.json")):
                with open(join(cur_notebook["path"], "meta.json")) as f:
                    cur_notebook.update(json.load(f))
            notebooks.append(cur_notebook)
        ret["notebooks"] = notebooks
        return ret

    def is_qvnotebook(self, path, dirname):
        if not os.path.isdir(join(path, dirname)):
            return False
        if not dirname.split(".")[-1] == "qvnotebook":
            return False
        return True

    def is_qvnote(self, path, dirname):
        if not os.path.isdir(join(path, dirname)):
            return False
        if not dirname.split(".")[-1] == "qvnote":
            return False
        return True

    def _load_notes_from_path(self, path):
        notes = []
        note_paths = [n for n in os.listdir(path) if self.is_qvnote(path, n)]
        for f in note_paths:
            note = {}
            content_file = join(path, f, "content.json")
            meta_file = join(path, f, "meta.json")
            with open(content_file) as c:
                note.update(json.loads(c.read()))
            with open(meta_file) as m:
                note.update(json.loads(m.read()))
            notes.append(note)
        return notes

    @property
    def notebooks(self):
        return self.library["notebooks"]

    @property
    def notes(self):
        ret = []
        for n in self.library["notebooks"]:
            ret.extend(n["notes"])
        return ret

    def get_notebook_by_title(self, title):
        for n in self.notebooks:
            if n["title"] == title:
                return n
        return None

    def get_notebook_by_uuid(self, uuid):
        for n in self.notebooks:
            if n["uuid"] == uuid:
                return n
        return None

    def get_note_by_title(self, title):
        for n in self.notes:
            if n["title"] == title:
                return n
        return None

    def get_note_by_uuid(self, uuid):
        for n in self.notes:
            if n["uuid"] == uuid:
                return n
        return None

    def get_cells_for_note_by_title(self, title):
        note = self.get_note_by_title(title)
        return note["cells"]

    def get_cells_for_note_by_uuid(self, uuid):
        note = self.get_note_by_uuid(uuid)
        return note["cells"]

    def get_notes_by_tag(self, tags: list) -> list:
        pass

    def get_tags(self) -> list:
        pass

    def create_empty_notebook(self, title):
        pass

    def create_notebook(self, title, notes):
        pass

    def create_empty_note(self, title, tags=None):
        pass

    def create_note(self, title, cells, tags=None, resources=None):
        pass

    def update_note_by_uuid(self, uuid, content):
        pass

    def update_note_by_title(self, title, content):
        pass

    def make_cell(self, data, datatype, language=None, diagram_type=None):
        pass




x = Fletching("/Users/jwelch/Quiver.qvlibrary")
pp(x.library)
# print(x.notebooks)
# pp(x.notes)



# print(x.get_notebook_by_uuid("3939F9BF-EC32-438C-A771-DE183F8374F5"))

l = {
    "path": "path",
    "notebooks": [
        {
            "display_name": "Tutorial",
            "uuid": "uuid",
            "path": "path",
            "notes": [
                {
                    "created_at": 1417080157,
                    "tags": [
                        "quiver"
                    ],
                    "title": "02 - Cells",
                    "updated_at": 1417080595,
                    "uuid": "9686AA1A-A5E9-41FF-9260-C3E0D0E9D4CB",
                    "path": "../9686AA1A-A5E9-41FF-9260-C3E0D0E9D4CB.qvnote",
                    "resources": None,
                    "cells": [
                        {
                            "type": "text",
                            "data": "For example, this is a <b>text cell</b> with <i>some <u>formatting</u> applied</i>."
                        },
                        {
                            "type": "code",
                            "language": "javascript",
                            "data": "void hello()\n{\n    console.log(\"Hello World!\");\n}"
                        },
                        {
                            "type": "markdown",
                            "data": "## Markdown Cell\n\nThis is a markdown cell. You can use common markdown syntax here.\n\nBasic formatting of *italic* and **bold** is supported.\n\nSo is `inline code`.\n\nAnd lists.\n\n### Ordered list\n\n1. Item 1\n2. A second item\n3. Number 3\n4. Ⅳ\n\n### Unordered list\n\n* An item\n* Another item\n* Yet another item\n* And there's more...\n\n### Quote\n\n> Here is a quote.\n\nCustom CSS options can be set in the *Preferences* panel.\n"
                        }
                    ]
                }
            ]
        },
    ]
}
