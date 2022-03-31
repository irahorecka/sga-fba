"""
Defines upper bounds of YPRaff media for FBA
"""

from fba.src.media.constants import media_reagents
from fba.src.media.yp.base import yp

raff = {
    media_reagents["raffinose"]: 6.85,
}

ypraff = {**yp, **raff}
