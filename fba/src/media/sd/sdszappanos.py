"""
Defines upper bounds of in silico SD media used by Szappanos et al., 2011
"""

from fba.src.media.constants import media_reagents
from fba.src.media.sd.base import sd

szappanos = {
    media_reagents["oxygen"]: 6.3,
    media_reagents["sulphate"]: 100.0,
    media_reagents["phosphate"]: 0.89,
    # Carbon
    media_reagents["D-glucose"]: 22.6,
    # AA
    media_reagents["L-alanine"]: 0.36,
    media_reagents["L-asparagine"]: 0.36,
    media_reagents["L-aspartate"]: 0.36,
    media_reagents["L-cysteine"]: 0.36,
    media_reagents["L-glutamate"]: 3.6,
    media_reagents["L-glutamine"]: 0.36,
    media_reagents["L-glycine"]: 0.36,
    media_reagents["L-isoleucine"]: 0.36,
    media_reagents["L-leucine"]: 1.8,
    media_reagents["L-methionine"]: 0.36,
    media_reagents["L-phenylalanine"]: 0.36,
    media_reagents["L-proline"]: 0.36,
    media_reagents["L-serine"]: 0.36,
    media_reagents["L-threonine"]: 0.36,
    media_reagents["L-tryptophan"]: 0.36,
    media_reagents["L-tyrosine"]: 0.36,
    media_reagents["L-valine"]: 0.36,
    media_reagents["potassium"]: 4.44,
    media_reagents["sodium"]: 0.75,
    media_reagents["biotin"]: 0.00000142,
    media_reagents["choline"]: 0.00437,
    media_reagents["riboflavin"]: 0.00092,
    media_reagents["thiamine(1+)"]: 0.0032,
    media_reagents["myo-inositol"]: 0.11,
    media_reagents["nicotinate"]: 0.000002,
    media_reagents["4-aminobenzoate"]: 0.000002,
    media_reagents["(R)-pantothenate"]: 0.0002,
    # NT
    media_reagents["uracil"]: 3.63,
    media_reagents["adenine"]: 3.01,
}

sdszappanos = {**sd, **szappanos}
