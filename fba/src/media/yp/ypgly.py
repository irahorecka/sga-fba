"""
Defines upper bounds of YPGly media for FBA
"""

from fba.src.media.constants import media_reagents
from fba.src.media.yp.base import yp

gly = {
    media_reagents["glycerol"]: 84.0,
}

ypgly = {**yp, **gly}
