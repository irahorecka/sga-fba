"""
Defines upper bounds of YPEtOH media for FBA
"""

from constants import media_components
from yp import yp

etoh = {
    media_components["ethanol"]: 44.2,
}

ypetoh = {**yp, **etoh}
