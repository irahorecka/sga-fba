"""
Defines upper bounds of YPAc media for FBA
"""

from fba.src.media.constants import media_reagents
from fba.src.media.yp.base import yp

ac = {
    media_reagents["acetate"]: 41.4,
}

ypac = {**yp, **ac}
