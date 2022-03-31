"""
Defines upper bounds of SC-Met media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.sc.base import sc

met = {
    reagents["L-methionine"]: 0.0,
}

scmet = {**sc, **met}
