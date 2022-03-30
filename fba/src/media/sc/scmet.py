"""
Defines upper bounds of SC-Met media for FBA
"""

from fba.src.media.constants import media_components
from fba.src.media.sc.base import sc

met = {
    media_components["L-methionine"]: 0.0,
}

scmet = {**sc, **met}
