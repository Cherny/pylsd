#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Link    : https://github.com/primetang/pylsd
# @Version : 0.0.1
import numpy.ctypeslib as npct
from .bindings.lsd_ctypes import *


class Point:
    def __init__(self, data):
        self.x, self.y = data


class Line:
    def __init__(self, data):
        self.pt0 = Point(data[0: 2])
        self.pt1 = Point(data[2: 4])
        self.width = data[4]


class TupleListInfo(ctypes.Structure):
    _fields_ = [
            ("size", ctypes.c_uint),
            ("max_size", ctypes.c_uint),
            ("dim", ctypes.c_uint),
            ("values", ctypes.POINTER(ctypes.c_double))
        ]


def lsd(src):
    rows, cols = src.shape
    src = src.reshape(1, rows * cols).tolist()[0]

    lens = len(src)
    src = (ctypes.c_double * lens)(*src)

    lsdlib.lsdGet.restype = ctypes.POINTER(TupleListInfo)
    tuple_list_info = lsdlib.lsdGet(src, ctypes.c_int(rows), ctypes.c_int(cols))
    lsdlib.lsdClean()

    size, dim = tuple_list_info.contents.size, tuple_list_info.contents.dim
    values = npct.as_array(tuple_list_info.contents.values, (size * dim,))
    values = values.reshape(size, dim)

    line_list = [Line(x) for x in values]
    return line_list
