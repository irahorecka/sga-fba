"""
Defines upper bounds of YPGly media for FBA
"""

from fba.src.growth.media.constants import media_components
from fba.src.growth.media.yp import yp

gly = {
    media_components["glycerol"]: 84.0,
}

ypgly = {**yp, **gly}
