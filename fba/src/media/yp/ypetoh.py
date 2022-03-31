"""
Defines upper bounds of YPEtOH media for FBA
"""

from fba.src.media.constants import media_reagents
from fba.src.media.yp.base import yp

etoh = {
    media_reagents["ethanol"]: 44.2,
}

ypetoh = {**yp, **etoh}
