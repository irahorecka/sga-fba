"""
Defines upper bounds of YPTE with no glucose media for FBA
"""

from constants import media_components
from yp import yp

te_no_glc = {
    media_components["ergosterol"]: 0.0026,
    media_components["zymosterol"]: 0.0026,
    media_components["palmitoleate"]: 0.005,
    media_components["stearate"]: 0.0016,
    media_components["oleate"]: 0.0078,
}

ypte_no_glc = {**yp, **te_no_glc}
