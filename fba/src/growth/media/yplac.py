"""
Defines upper bounds of YPLac media for FBA
"""

from fba.src.growth.media.constants import media_components
from fba.src.growth.media.yp import yp

lac = {
    media_components["(S)-lactate"]: 22.6,
}

yplac = {**yp, **lac}
