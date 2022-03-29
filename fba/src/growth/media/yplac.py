"""
Defines upper bounds of YPLac media for FBA
"""

from constants import media_components
from yp import yp

lac = {
    media_components["(S)-lactate"]: 22.6,
}

yplac = {**yp, **lac}
