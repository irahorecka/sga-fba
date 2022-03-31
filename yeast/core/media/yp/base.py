"""
Defines upper bounds of YP base media for FBA
"""

from yeast.core.media.constants import reagents

yp = {
    reagents["oxygen"]: 6.3,
    reagents["ammonium"]: 100.0,
    reagents["sulphate"]: 100.0,
    reagents["phosphate"]: 0.89,
    # Carbon
    reagents["D-glucose"]: 0.0,
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
    reagents["L-alanine"]: 0.519,
    reagents["L-arginine"]: 0.193,
    reagents["L-asparagine"]: 0.0,
    reagents["L-aspartate"]: 0.274,
    reagents["L-cysteine"]: 0.0192,
    reagents["L-glutamate"]: 0.479,
    reagents["L-glutamine"]: 0.0,
    reagents["L-glycine"]: 0.934,
    reagents["L-histidine"]: 0.31,
    reagents["L-isoleucine"]: 0.0952,
    reagents["L-leucine"]: 1.66,
    reagents["L-lysine"]: 0.167,
    reagents["L-methionine"]: 0.0468,
    reagents["L-phenylalanine"]: 0.0758,
    reagents["L-proline"]: 0.357,
    reagents["L-serine"]: 0.166,
    reagents["L-threonine"]: 0.112,
    reagents["L-tryptophan"]: 0.0207,
    reagents["L-tyrosine"]: 0.0279,
    reagents["L-valine"]: 0.148,
    reagents["potassium"]: 1.87,
    reagents["sodium"]: 4.43,
    reagents["biotin"]: 0.0000275,
    reagents["choline"]: 0.00437,
    reagents["riboflavin"]: 0.00063,
    reagents["thiamine(1+)"]: 0.0032,
    reagents["myo-inositol"]: 0.07,
    reagents["thymidine"]: 0.00709,
    reagents["nicotinate"]: 0.000002,
    reagents["4-aminobenzoate"]: 0.000002,
    reagents["(R)-pantothenate"]: 0.0002,
    reagents["pyridoxine"]: 0.00001,
    # NT
    reagents["uracil"]: 4.0,
    reagents["adenine"]: 0.0,
}
