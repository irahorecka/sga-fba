"""
OOP representation of yeast-GEM media
"""

# fmt: off
from fba.src.growth.media import (sdszappanos,
                   ypac, ypd, ypetoh, ypgal,
                   ypgly, yplac, ypraff,
                   ypte_no_glc, ypte_no_o2)
# fmt: on


def apply_sdszappanos(model):
    return apply_media(model, sdszappanos)


def apply_ypac(model):
    return apply_media(model, ypac)


def apply_ypd(model):
    return apply_media(model, ypd)


def apply_ypetoh(model):
    return apply_media(model, ypetoh)


def apply_ypgal(model):
    return apply_media(model, ypgal)


def apply_ypgly(model):
    return apply_media(model, ypgly)


def apply_yplac(model):
    return apply_media(model, yplac)


def apply_ypraff(model):
    return apply_media(model, ypraff)


def apply_ypte_no_glc(model):
    return apply_media(model, ypte_no_glc)


def apply_ypte_no_o2(model):
    return apply_media(model, ypte_no_o2)


def apply_media(model, media):
    for rxn_id, upper_bound in media.items():
        model.reactions.get_by_id(rxn_id).upper_bound = upper_bound
    return model
