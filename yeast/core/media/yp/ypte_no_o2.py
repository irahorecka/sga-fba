"""
Defines upper bounds of YPTE with no oxygen media for FBA
"""

from yeast.core.media.constants import reagents
from yeast.core.media.yp.base import yp

te_no_o2 = {
    reagents["D-glucose"]: 22.6,
    reagents["oxygen"]: 0.0,
    reagents["ergosterol"]: 0.0026,
    reagents["zymosterol"]: 0.0026,
    reagents["palmitoleate"]: 0.005,
    reagents["stearate"]: 0.0016,
    reagents["oleate"]: 0.0078,
}

ypte_no_o2 = {**yp, **te_no_o2}
