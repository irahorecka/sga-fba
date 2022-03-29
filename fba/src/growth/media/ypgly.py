"""
Defines upper bounds of YPGly media for FBA
"""

from constants import media_components
from yp import yp

gly = {
    media_components["glycerol"]: 84.0,
}

ypgly = {**yp, **gly}
