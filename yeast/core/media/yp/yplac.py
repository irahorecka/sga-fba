"""
Defines upper bounds of YPLac media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.yp.base import yp

lac = {
    reagents["(S)-lactate"]: 22.6,
}

yplac = {**yp, **lac}
