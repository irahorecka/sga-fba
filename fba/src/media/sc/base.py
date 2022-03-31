"""
Defines upper bounds of SC base media for FBA
"""

from fba.src.media.constants import media_reagents

sc = {
    media_reagents["oxygen"]: 6.3,
    media_reagents["ammonium"]: 100.0,
    media_reagents["sulphate"]: 100.0,
    media_reagents["phosphate"]: 0.89,
    # Carbon
    media_reagents["D-glucose"]: 22.6,
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
    media_reagents["L-alanine"]: 0.457,
    media_reagents["L-arginine"]: 0.234,
    media_reagents["L-asparagine"]: 0.308,
    media_reagents["L-aspartate"]: 0.306,
    media_reagents["L-cysteine"]: 0.306,
    media_reagents["L-glutamate"]: 0.277,
    media_reagents["L-glutamine"]: 0.278,
    media_reagents["L-glycine"]: 0.543,
    media_reagents["L-histidine"]: 2.63,
    media_reagents["L-isoleucine"]: 0.311,
    media_reagents["L-leucine"]: 6.21,
    media_reagents["L-lysine"]: 0.279,
    media_reagents["L-methionine"]: 0.273,
    media_reagents["L-phenylalanine"]: 0.247,
    media_reagents["L-proline"]: 0.354,
    media_reagents["L-serine"]: 0.388,
    media_reagents["L-threonine"]: 0.342,
    media_reagents["L-tryptophan"]: 0.199,
    media_reagents["L-tyrosine"]: 0.0279,
    media_reagents["L-valine"]: 0.348,
    media_reagents["potassium"]: 4.44,
    media_reagents["sodium"]: 0.75,
    media_reagents["biotin"]: 0.00000142,
    media_reagents["choline"]: 0.0,
    media_reagents["riboflavin"]: 0.0,
    media_reagents["thiamine(1+)"]: 0.0,
    media_reagents["myo-inositol"]: 0.11,
    media_reagents["thymidine"]: 0.0,
    media_reagents["nicotinate"]: 0.0,
    media_reagents["4-aminobenzoate"]: 0.0,
    media_reagents["(R)-pantothenate"]: 0.0,
    media_reagents["pyridoxine"]: 0.0,
    # NT
    media_reagents["uracil"]: 3.63,
    media_reagents["adenine"]: 3.01,
}
