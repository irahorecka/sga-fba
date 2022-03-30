"""
Defines upper bounds of in silico SD media used by Szappanos et al., 2011
"""

from fba.src.media.constants import media_components
from fba.src.media.sd.base import sd

szappanos = {
    media_components["oxygen"]: 6.3,
    media_components["sulphate"]: 100.0,
    media_components["phosphate"]: 0.89,
    # Carbon
    media_components["D-glucose"]: 22.6,
    # AA
    media_components["L-alanine"]: 0.36,
    media_components["L-asparagine"]: 0.36,
    media_components["L-aspartate"]: 0.36,
    media_components["L-cysteine"]: 0.36,
    media_components["L-glutamate"]: 3.6,
    media_components["L-glutamine"]: 0.36,
    media_components["L-glycine"]: 0.36,
    media_components["L-isoleucine"]: 0.36,
    media_components["L-leucine"]: 1.8,
    media_components["L-methionine"]: 0.36,
    media_components["L-phenylalanine"]: 0.36,
    media_components["L-proline"]: 0.36,
    media_components["L-serine"]: 0.36,
    media_components["L-threonine"]: 0.36,
    media_components["L-tryptophan"]: 0.36,
    media_components["L-tyrosine"]: 0.36,
    media_components["L-valine"]: 0.36,
    media_components["potassium"]: 4.44,
    media_components["sodium"]: 0.75,
    media_components["biotin"]: 0.00000142,
    media_components["choline"]: 0.00437,
    media_components["riboflavin"]: 0.00092,
    media_components["thiamine(1+)"]: 0.0032,
    media_components["myo-inositol"]: 0.11,
    media_components["nicotinate"]: 0.000002,
    media_components["4-aminobenzoate"]: 0.000002,
    media_components["(R)-pantothenate"]: 0.0002,
    # NT
    media_components["uracil"]: 3.63,
    media_components["adenine"]: 3.01,
}

sdszappanos = {**sd, **szappanos}
