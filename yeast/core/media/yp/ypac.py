"""
Defines upper bounds of YPAc media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.yp.base import yp

ac = {
    reagents["acetate"]: 41.4,
}

ypac = {**yp, **ac}
