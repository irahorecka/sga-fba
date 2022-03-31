"""
Defines upper bounds of YPTE with no glucose media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.yp.base import yp

te_no_glc = {
    reagents["ergosterol"]: 0.0026,
    reagents["zymosterol"]: 0.0026,
    reagents["palmitoleate"]: 0.005,
    reagents["stearate"]: 0.0016,
    reagents["oleate"]: 0.0078,
}

ypte_no_glc = {**yp, **te_no_glc}
