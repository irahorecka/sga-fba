"""
Defines upper bounds of YPEtOH media for FBA
"""

from fba.src.growth.media.constants import media_components
from fba.src.growth.media.yp import yp

etoh = {
    media_components["ethanol"]: 44.2,
}

ypetoh = {**yp, **etoh}
