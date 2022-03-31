"""
Defines upper bounds of SC-Lys media for FBA
"""

from fba.src.media.constants import media_reagents
from fba.src.media.sc.base import sc

lys = {
    media_reagents["L-lysine"]: 0.0,
}

sclys = {**sc, **lys}
