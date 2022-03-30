"""
Defines upper bounds of YPTE with no oxygen media for FBA
"""

from fba.src.media.constants import media_components
from fba.src.media.yp.base import yp

te_no_o2 = {
    media_components["D-glucose"]: 22.6,
    media_components["oxygen"]: 0.0,
    media_components["ergosterol"]: 0.0026,
    media_components["zymosterol"]: 0.0026,
    media_components["palmitoleate"]: 0.005,
    media_components["stearate"]: 0.0016,
    media_components["oleate"]: 0.0078,
}

ypte_no_o2 = {**yp, **te_no_o2}
