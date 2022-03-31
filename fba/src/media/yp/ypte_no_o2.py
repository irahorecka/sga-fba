"""
Defines upper bounds of YPTE with no oxygen media for FBA
"""

from fba.src.media.constants import media_reagents
from fba.src.media.yp.base import yp

te_no_o2 = {
    media_reagents["D-glucose"]: 22.6,
    media_reagents["oxygen"]: 0.0,
    media_reagents["ergosterol"]: 0.0026,
    media_reagents["zymosterol"]: 0.0026,
    media_reagents["palmitoleate"]: 0.005,
    media_reagents["stearate"]: 0.0016,
    media_reagents["oleate"]: 0.0078,
}

ypte_no_o2 = {**yp, **te_no_o2}
