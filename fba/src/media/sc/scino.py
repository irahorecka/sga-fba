"""
Defines upper bounds of SC-Ino media for FBA
"""

from fba.src.media.constants import media_components
from fba.src.media.sc.base import sc

ino = {
    media_components["myo-inositol"]: 0.0,
}

scino = {**sc, **ino}
