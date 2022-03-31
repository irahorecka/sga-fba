"""
Defines upper bounds of YPGal media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.yp.base import yp

gal = {
    reagents["D-galactose"]: 22.6,
}

ypgal = {**yp, **gal}
