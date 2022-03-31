"""
Defines upper bounds of SC-Ade media for FBA
"""

from fba.src.media.constants import media_reagents
from fba.src.media.sc.base import sc

ade = {
    media_reagents["adenine"]: 0.0,
}

scade = {**sc, **ade}
