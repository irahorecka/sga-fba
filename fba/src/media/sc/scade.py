"""
Defines upper bounds of SC-Ade media for FBA
"""

from fba.src.media.constants import media_components
from fba.src.media.sc.base import sc

ade = {
    media_components["adenine"]: 0.0,
}

scade = {**sc, **ade}
