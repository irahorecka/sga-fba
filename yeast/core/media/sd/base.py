"""
Defines upper bounds of SD base media for FBA
"""

from yeast.core.media.constants import reagents

sd = {
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
    reagents["L-alanine"]: 0.0,
    reagents["L-arginine"]: 0.0,
    reagents["L-asparagine"]: 0.0,
    reagents["L-aspartate"]: 0.0,
    reagents["L-cysteine"]: 0.0,
    reagents["L-glutamate"]: 0.0,
    reagents["L-glutamine"]: 0.0,
    reagents["L-glycine"]: 0.0,
    reagents["L-histidine"]: 0.082,
    reagents["L-isoleucine"]: 0.0,
    reagents["L-leucine"]: 0.4,
    reagents["L-lysine"]: 0.0,
    reagents["L-methionine"]: 0.0,
    reagents["L-phenylalanine"]: 0.0,
    reagents["L-proline"]: 0.0,
    reagents["L-serine"]: 0.0,
    reagents["L-threonine"]: 0.0,
    reagents["L-tryptophan"]: 0.0,
    reagents["L-tyrosine"]: 0.0,
    reagents["L-valine"]: 0.0,
    reagents["potassium"]: 4.44,
    reagents["sodium"]: 0.75,
    reagents["biotin"]: 0.00000142,
    reagents["choline"]: 0.000092,
    reagents["riboflavin"]: 0.0,
    reagents["thiamine(1+)"]: 0.0,
    reagents["myo-inositol"]: 0.00193,
    reagents["thymidine"]: 0.0,
    reagents["nicotinate"]: 0.0,
    reagents["4-aminobenzoate"]: 0.0,
    reagents["(R)-pantothenate"]: 0.0002,
    reagents["pyridoxine"]: 0.0,
    # NT
    reagents["uracil"]: 0.4,
    reagents["adenine"]: 0.0,
}
