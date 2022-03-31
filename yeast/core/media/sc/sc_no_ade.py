"""
Defines upper bounds of SC-Ade media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.sc.base import sc

ade = {
    reagents["adenine"]: 0.0,
}

sc_no_ade = {**sc, **ade}
