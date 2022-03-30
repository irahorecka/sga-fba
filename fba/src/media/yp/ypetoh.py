"""
Defines upper bounds of YPEtOH media for FBA
"""

from fba.src.media.constants import media_components
from fba.src.media.yp.base import yp

etoh = {
    media_components["ethanol"]: 44.2,
}

ypetoh = {**yp, **etoh}
