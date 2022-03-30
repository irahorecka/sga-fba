"""
Defines upper bounds of YPRaff media for FBA
"""

from fba.src.media.constants import media_components
from fba.src.media.yp.base import yp

raff = {
    media_components["raffinose"]: 6.85,
}

ypraff = {**yp, **raff}
