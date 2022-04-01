"""
Defines upper bounds of in silico SD media used by Szappanos et al., 2011
"""

from yeast.core.media.constants import reagents
from yeast.core.media.sd.base import sd

szappanos = {
    reagents["oxygen"]: 6.3,
    reagents["sulphite"]: 100.0,
    reagents["phosphate"]: 0.89,
    # Carbon
    reagents["D-glucose"]: 22.6,
    # AA
    reagents["L-alanine"]: 0.36,
    reagents["L-asparagine"]: 0.36,
    reagents["L-aspartate"]: 0.36,
    reagents["L-cysteine"]: 0.36,
    reagents["L-glutamate"]: 3.6,
    reagents["L-glutamine"]: 0.36,
    reagents["L-glycine"]: 0.36,
    reagents["L-isoleucine"]: 0.36,
    reagents["L-leucine"]: 1.8,
    reagents["L-methionine"]: 0.36,
    reagents["L-phenylalanine"]: 0.36,
    reagents["L-proline"]: 0.36,
    reagents["L-serine"]: 0.36,
    reagents["L-threonine"]: 0.36,
    reagents["L-tryptophan"]: 0.36,
    reagents["L-tyrosine"]: 0.36,
    reagents["L-valine"]: 0.36,
    reagents["potassium"]: 4.44,
    reagents["sodium"]: 0.75,
    reagents["biotin"]: 0.00000142,
    reagents["choline"]: 0.00437,
    reagents["riboflavin"]: 0.00092,
    reagents["thiamine(1+)"]: 0.0032,
    reagents["myo-inositol"]: 0.11,
    reagents["nicotinate"]: 0.000002,
    reagents["4-aminobenzoate"]: 0.000002,
    reagents["(R)-pantothenate"]: 0.0002,
    # NT
    reagents["uracil"]: 3.63,
    reagents["adenine"]: 3.01,
}

sdszappanos = {**sd, **szappanos}
