"""
Defines upper bounds of SC base media for FBA
"""

from fba.src.media.constants import media_components

sc = {
    media_components["oxygen"]: 6.3,
    media_components["ammonium"]: 100.0,
    media_components["sulphate"]: 100.0,
    media_components["phosphate"]: 0.89,
    # Carbon
    media_components["D-glucose"]: 22.6,
    media_components["glycerol"]: 0.0,
    media_components["(S)-lactate"]: 0.0,
    media_components["D-galactose"]: 0.0,
    media_components["raffinose"]: 0.0,
    media_components["ethanol"]: 0.0,
    media_components["acetate"]: 0.0,
    # Steroids
    media_components["ergosterol"]: 0.0,
    media_components["zymosterol"]: 0.0,
    media_components["palmitoleate"]: 0.0,
    media_components["stearate"]: 0.0,
    media_components["oleate"]: 0.0,
    # AA
    media_components["L-alanine"]: 0.457,
    media_components["L-arginine"]: 0.234,
    media_components["L-asparagine"]: 0.308,
    media_components["L-aspartate"]: 0.306,
    media_components["L-cysteine"]: 0.306,
    media_components["L-glutamate"]: 0.277,
    media_components["L-glutamine"]: 0.278,
    media_components["L-glycine"]: 0.543,
    media_components["L-histidine"]: 2.63,
    media_components["L-isoleucine"]: 0.311,
    media_components["L-leucine"]: 6.21,
    media_components["L-lysine"]: 0.279,
    media_components["L-methionine"]: 0.273,
    media_components["L-phenylalanine"]: 0.247,
    media_components["L-proline"]: 0.354,
    media_components["L-serine"]: 0.388,
    media_components["L-threonine"]: 0.342,
    media_components["L-tryptophan"]: 0.199,
    media_components["L-tyrosine"]: 0.0279,
    media_components["L-valine"]: 0.348,
    media_components["potassium"]: 4.44,
    media_components["sodium"]: 0.75,
    media_components["biotin"]: 0.00000142,
    media_components["choline"]: 0.0,
    media_components["riboflavin"]: 0.0,
    media_components["thiamine(1+)"]: 0.0,
    media_components["myo-inositol"]: 0.11,
    media_components["thymidine"]: 0.0,
    media_components["nicotinate"]: 0.0,
    media_components["4-aminobenzoate"]: 0.0,
    media_components["(R)-pantothenate"]: 0.0,
    media_components["pyridoxine"]: 0.0,
    # NT
    media_components["uracil"]: 3.63,
    media_components["adenine"]: 3.01,
}
