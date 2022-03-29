"""
Defines upper bounds of YPAc media for FBA
"""

from fba.src.growth.media.constants import media_components
from fba.src.growth.media.yp import yp

ac = {
    media_components["acetate"]: 41.4,
}

ypac = {**yp, **ac}
