"""
OOP representation of yeast-GEM media
"""

# SC-based media
from yeast.core.media.sc import sc, sc_no_ade, sc_no_arg, sc_no_ino, sc_no_lys, sc_no_met

# SD-based media
from yeast.core.media.sd import sd, sdszappanos

# YP-based media
from yeast.core.media.yp import (
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


def get_every_media():
    """Returns every registered medium as a key-value pair."""
    return {
        "SC": sc,
        "SC-Ade": sc_no_ade,
        "SC-Arg": sc_no_arg,
        "SC-Ino": sc_no_ino,
        "SC-Lys": sc_no_lys,
        "SC-Met": sc_no_met,
        "SD": sd,
        "SD:Szappanos": sdszappanos,
        "YP": yp,
        "YPAc": ypac,
        "YPD": ypd,
        "YPEtOH": ypetoh,
        "YPGal": ypgal,
        "YPGly": ypgly,
        "YPLac": yplac,
        "YPRaff": ypraff,
        "YPTE-GLC": ypte_no_glc,
        "YPTE-O2": ypte_no_o2,
    }
