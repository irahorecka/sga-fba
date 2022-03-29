"""
Defines upper bounds of YPAc media for FBA
"""

from constants import media_components
from yp import yp

ac = {
    media_components["acetate"]: 41.4,
}

ypac = {**yp, **ac}
