"""
Defines upper bounds of YPD media for FBA
"""

from constants import media_components
from yp import yp

d = {
    media_components["D-glucose"]: 22.6,
}

ypd = {**yp, **d}
