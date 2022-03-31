"""
Defines upper bounds of YPEtOH media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.yp.base import yp

etoh = {
    reagents["ethanol"]: 44.2,
}

ypetoh = {**yp, **etoh}
