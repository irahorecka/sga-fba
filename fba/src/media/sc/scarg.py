"""
Defines upper bounds of SC-Arg media for FBA
"""

from fba.src.media.constants import media_reagents
from fba.src.media.sc.base import sc

arg = {
    media_reagents["L-arginine"]: 0.0,
}

scarg = {**sc, **arg}
