"""
Defines upper bounds of YPGly media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.yp.base import yp

gly = {
    reagents["glycerol"]: 84.0,
}

ypgly = {**yp, **gly}
