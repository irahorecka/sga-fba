"""
Defines upper bounds of YPRaff media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.yp.base import yp

raff = {
    reagents["raffinose"]: 6.85,
}

ypraff = {**yp, **raff}
