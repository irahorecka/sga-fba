"""
Defines upper bounds of YPAc media for FBA
"""

from fba.src.media.constants import media_components
from fba.src.media.yp.base import yp

ac = {
    media_components["acetate"]: 41.4,
}

ypac = {**yp, **ac}
