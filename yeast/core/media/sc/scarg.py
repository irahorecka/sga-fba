"""
Defines upper bounds of SC-Arg media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.sc.base import sc

arg = {
    reagents["L-arginine"]: 0.0,
}

scarg = {**sc, **arg}
