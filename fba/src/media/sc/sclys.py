"""
Defines upper bounds of SC-Lys media for FBA
"""

from fba.src.media.constants import media_components
from fba.src.media.sc.base import sc

lys = {
    media_components["L-lysine"]: 0.0,
}

sclys = {**sc, **lys}
