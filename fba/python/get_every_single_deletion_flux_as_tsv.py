from typing import Callable

import cobra
import pandas as pd
from cobra.flux_analysis import single_gene_deletion, double_gene_deletion

from cobra_utils import load_model, FBA_DIR


def generate_deletion_flux(
    gene_deletion_func: Callable, model: cobra.core.model.Model, **kwargs
) -> pd.core.frame.DataFrame:
    return gene_deletion_func(model, **kwargs)


if __name__ == "__main__":
    model = load_model(str(FBA_DIR / "model" / "yeast-GEM.xml"))
    single_deletion_flux = generate_deletion_flux(
        single_gene_deletion, model, gene_list=model.genes[:]
    )
    single_deletion_flux.to_csv(
        FBA_DIR / "data" / "single_gene_deletion_output.tsv", sep="\t", index=False
    )
