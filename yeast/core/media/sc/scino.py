"""
Defines upper bounds of SC-Ino media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.sc.base import sc

ino = {
    reagents["myo-inositol"]: 0.0,
}

scino = {**sc, **ino}
