# -*- coding: utf-8 -*-
import numpy as np


__doc__ = """\
BasicOperations
===============

Basic operations that can be performed in one or two images. This operations
are:
    - Add : Add two images or and image with a constant
    - Mult : Multiplicate two images or and image with a constant
    - LogicalXor : Compute xor in two bool images/matrix
"""


def AddImages(src1, src2):
    return src1 + src2


def MultImages(src1, src2):
    return src1 * src2


def LogicalXor(src1, src2):
    return np.logical_xor(src1, src2)
