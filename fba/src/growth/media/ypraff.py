"""
Defines upper bounds of YPRaff media for FBA
"""

from constants import media_components
from yp import yp

raff = {
    media_components["raffinose"]: 6.85,
}

ypraff = {**yp, **raff}
