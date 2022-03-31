"""
Defines upper bounds of YP base media for FBA
"""

from fba.src.media.constants import media_reagents

yp = {
    media_reagents["oxygen"]: 6.3,
    media_reagents["ammonium"]: 100.0,
    media_reagents["sulphate"]: 100.0,
    media_reagents["phosphate"]: 0.89,
    # Carbon
    media_reagents["D-glucose"]: 0.0,
    media_reagents["glycerol"]: 0.0,
    media_reagents["(S)-lactate"]: 0.0,
    media_reagents["D-galactose"]: 0.0,
    media_reagents["raffinose"]: 0.0,
    media_reagents["ethanol"]: 0.0,
    media_reagents["acetate"]: 0.0,
    # Steroids
    media_reagents["ergosterol"]: 0.0,
    media_reagents["zymosterol"]: 0.0,
    media_reagents["palmitoleate"]: 0.0,
    media_reagents["stearate"]: 0.0,
    media_reagents["oleate"]: 0.0,
    # AA
    media_reagents["L-alanine"]: 0.519,
    media_reagents["L-arginine"]: 0.193,
    media_reagents["L-asparagine"]: 0.0,
    media_reagents["L-aspartate"]: 0.274,
    media_reagents["L-cysteine"]: 0.0192,
    media_reagents["L-glutamate"]: 0.479,
    media_reagents["L-glutamine"]: 0.0,
    media_reagents["L-glycine"]: 0.934,
    media_reagents["L-histidine"]: 0.31,
    media_reagents["L-isoleucine"]: 0.0952,
    media_reagents["L-leucine"]: 1.66,
    media_reagents["L-lysine"]: 0.167,
    media_reagents["L-methionine"]: 0.0468,
    media_reagents["L-phenylalanine"]: 0.0758,
    media_reagents["L-proline"]: 0.357,
    media_reagents["L-serine"]: 0.166,
    media_reagents["L-threonine"]: 0.112,
    media_reagents["L-tryptophan"]: 0.0207,
    media_reagents["L-tyrosine"]: 0.0279,
    media_reagents["L-valine"]: 0.148,
    media_reagents["potassium"]: 1.87,
    media_reagents["sodium"]: 4.43,
    media_reagents["biotin"]: 0.0000275,
    media_reagents["choline"]: 0.00437,
    media_reagents["riboflavin"]: 0.00063,
    media_reagents["thiamine(1+)"]: 0.0032,
    media_reagents["myo-inositol"]: 0.07,
    media_reagents["thymidine"]: 0.00709,
    media_reagents["nicotinate"]: 0.000002,
    media_reagents["4-aminobenzoate"]: 0.000002,
    media_reagents["(R)-pantothenate"]: 0.0002,
    media_reagents["pyridoxine"]: 0.00001,
    # NT
    media_reagents["uracil"]: 4.0,
    media_reagents["adenine"]: 0.0,
}
