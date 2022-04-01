"""
Defines upper bounds of SC base media for FBA
"""

from yeast.core.media.constants import reagents

sc = {
    reagents["oxygen"]: 6.3,
    reagents["ammonium"]: 100.0,
    reagents["sulphite"]: 100.0,
    reagents["phosphate"]: 0.89,
    # Carbon
    reagents["D-glucose"]: 22.6,
    reagents["glycerol"]: 0.0,
    reagents["(S)-lactate"]: 0.0,
    reagents["D-galactose"]: 0.0,
    reagents["raffinose"]: 0.0,
    reagents["ethanol"]: 0.0,
    reagents["acetate"]: 0.0,
    # Steroids
    reagents["ergosterol"]: 0.0,
    reagents["zymosterol"]: 0.0,
    reagents["palmitoleate"]: 0.0,
    reagents["stearate"]: 0.0,
    reagents["oleate"]: 0.0,
    # AA
    reagents["L-alanine"]: 0.457,
    reagents["L-arginine"]: 0.234,
    reagents["L-asparagine"]: 0.308,
    reagents["L-aspartate"]: 0.306,
    reagents["L-cysteine"]: 0.306,
    reagents["L-glutamate"]: 0.277,
    reagents["L-glutamine"]: 0.278,
    reagents["L-glycine"]: 0.543,
    reagents["L-histidine"]: 2.63,
    reagents["L-isoleucine"]: 0.311,
    reagents["L-leucine"]: 6.21,
    reagents["L-lysine"]: 0.279,
    reagents["L-methionine"]: 0.273,
    reagents["L-phenylalanine"]: 0.247,
    reagents["L-proline"]: 0.354,
    reagents["L-serine"]: 0.388,
    reagents["L-threonine"]: 0.342,
    reagents["L-tryptophan"]: 0.199,
    reagents["L-tyrosine"]: 0.0279,
    reagents["L-valine"]: 0.348,
    reagents["potassium"]: 4.44,
    reagents["sodium"]: 0.75,
    reagents["biotin"]: 0.00000142,
    reagents["choline"]: 0.0,
    reagents["riboflavin"]: 0.0,
    reagents["thiamine(1+)"]: 0.0,
    reagents["myo-inositol"]: 0.11,
    reagents["thymidine"]: 0.0,
    reagents["nicotinate"]: 0.0,
    reagents["4-aminobenzoate"]: 0.0,
    reagents["(R)-pantothenate"]: 0.0,
    reagents["pyridoxine"]: 0.0,
    # NT
    reagents["uracil"]: 3.63,
    reagents["adenine"]: 3.01,
}
