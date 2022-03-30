"""
Defines upper bounds of YPGal media for FBA
"""

from fba.src.media.constants import media_components
from fba.src.media.yp.base import yp

gal = {
    media_components["D-galactose"]: 22.6,
}

ypgal = {**yp, **gal}
