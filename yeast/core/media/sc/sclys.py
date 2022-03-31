"""
Defines upper bounds of SC-Lys media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.sc.base import sc

lys = {
    reagents["L-lysine"]: 0.0,
}

sclys = {**sc, **lys}
