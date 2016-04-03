#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/HappenApps/Quiver/wiki/Quiver-Data-Format
import json
import os
import os.path
from os.path import join
from pathlib import Path
from pprint import pprint as pp

import sys

# fletchmod = sys.modules[__name__]
#
#
# def load_from_path(path, ext, obj):
#     ret = {}
#     lib_dir = Path(path)
#     data = [x for x in lib_dir.iterdir() if x.is_dir() and x.suffix == ext]
#     for d in data:
#         try:
#             ret[d.stem] = getattr(fletchmod, obj)(d)
#         except Exception as e:
#             print(e.args)
#     return ret
#
#
# def load_json(self, filename):
#     with open(filename.as_posix()) as f:
#         meta_data = json.loads(f.read())
#     return meta_data
#
#
# class Library(object):
#     def __init__(self, path):
#         self.path = path
#         self.ext = ".qvnotebook"
#         self.library = load_from_path(self.path, self.ext, "NoteBook")
#
#
# class NoteBook(object):
#     def __init__(self, path):
#         self.ext = ".qvnote"
#         self.path = path
#         self.notes = load_from_path(self.path, self.ext, "Note")
#
#
# class Note(object):
#     def __init__(self, path):
#         self.path = path
#
#
# n = x.library
# for k, v in n.items():
#     print(k)
#     print(v)
# for k, v in x.library.items():
#     print(k)
#     print(v.notes)


class Fletching(object):
    EXCLUDED = ["Trash.qvnotebook"]
    def __init__(self, path):
        self.path = path
        self.library = self.load_library_from_path(self.path)


    def load_library_from_path(self, path):
        ret = {"path": path}
        notebooks = []
        for dir in os.listdir(path):
            if not os.path.isdir(join(path, dir)):
                continue
            if dir in Fletching.EXCLUDED:
                continue
            cur_notebook = {}

            cur_notebook["path"] = join(path, dir)
            cur_notebook["notes"] = self.load_notes_from_path(join(cur_notebook["path"]))
            if os.path.exists(join(cur_notebook["path"], "meta.json")):
                with open(join(cur_notebook["path"], "meta.json")) as f:
                    cur_notebook.update(json.loads(f.read()))
            notebooks.append(cur_notebook)
        ret["notebooks"] = notebooks
        return ret

    def load_notes_from_path(self, path):
        notes = []
        # print(path)
        for f in os.listdir(path):
            note = {}
            if not f.endswith(".qvnote"):
                continue
            # print("path", f)
            content_file = join(path, f, "content.json")
            meta_file = join(path, f, "meta.json")
            with open(content_file) as c:
                note.update(json.loads(c.read()))
            with open(meta_file) as m:
                note.update(json.loads(m.read()))
            notes.append(note)
        # print(notes)
        return notes




x = Fletching("/Users/jwelch/Quiver.qvlibrary")
pp(x.library)



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
