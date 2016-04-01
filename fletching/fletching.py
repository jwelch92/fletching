#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/HappenApps/Quiver/wiki/Quiver-Data-Format
import json
from pathlib import Path
from pprint import pprint as pp

import sys

fletchmod = sys.modules[__name__]


def load_from_path(path, ext, obj):
    ret = {}
    lib_dir = Path(path)
    data = [x for x in lib_dir.iterdir() if x.is_dir() and x.suffix == ext]
    for d in data:
        try:
            ret[d.stem] = getattr(fletchmod, obj)(d)
        except Exception as e:
            print(e.args)
    return ret


def load_json(self, filename):
    with open(filename.as_posix()) as f:
        meta_data = json.loads(f.read())
    return meta_data


class Library(object):
    def __init__(self, path):
        self.path = path
        self.ext = ".qvnotebook"
        self.library = load_from_path(self.path, self.ext, "NoteBook")


class NoteBook(object):
    def __init__(self, path):
        self.ext = ".qvnote"
        self.path = path
        self.notes = load_from_path(self.path, self.ext, "Note")


class Note(object):
    def __init__(self, path):
        self.path = path


x = Library("/Users/jwelch/Quiver.qvlibrary")
n = x.library
for k, v in n.items():
    print(k)
    print(v)
# for k, v in x.library.items():
#     print(k)
#     print(v.notes)


