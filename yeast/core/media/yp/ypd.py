"""
Defines upper bounds of YPD media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.yp.base import yp

d = {
    reagents["D-glucose"]: 22.6,
}

ypd = {**yp, **d}
