"""
OOP representation of yeast-GEM media
"""

# SC-based media
from fba.src.media.sc import sc, scade, scarg, scino, sclys, scmet

# SD-based media
from fba.src.media.sd import sd, sdszappanos

# YP-based media
from fba.src.media.yp import (
    yp,
    ypac,
    ypd,
    ypetoh,
    ypgal,
    ypgly,
    yplac,
    ypraff,
    ypte_no_glc,
    ypte_no_o2,
)


def apply_media(model, media):
    """Applies media <dict> to model by setting the compound /
    reaction's upper bounds."""
    for rxn_id, upper_bound in media.items():
        model.reactions.get_by_id(rxn_id).upper_bound = upper_bound
    return model
