"""
Defines upper bounds of YPD media for FBA
"""

from fba.src.growth.media.constants import media_components
from fba.src.growth.media.yp import yp

d = {
    media_components["D-glucose"]: 22.6,
}

ypd = {**yp, **d}
