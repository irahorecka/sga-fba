import pathlib
from typing import Callable, Union

import cobra
import pandas as pd
from cobra.flux_analysis import single_gene_deletion, double_gene_deletion

from cobra_utils import load_model, FBA_DIR


def generate_deletion_flux(
    gene_deletion_func: Callable, model: cobra.core.model.Model, **kwargs
) -> pd.core.frame.DataFrame:
    return gene_deletion_func(model, **kwargs)


def export_deletion_flux_as_tsv(
    df: pd.core.frame.DataFrame, filepath: Union[str, pathlib.Path]
) -> None:
    df.to_csv(filepath, sep="\t", index=False)


if __name__ == "__main__":
    model = load_model(str(FBA_DIR / "model" / "yeast-GEM.xml"))
    # Generate single deletion
    single_deletion_flux = generate_deletion_flux(
        single_gene_deletion, model, gene_list=model.genes[:], solver="cplex"
    )
    export_deletion_flux_as_tsv(
        single_deletion_flux, FBA_DIR / "data" / "single_gene_deletion_output.tsv"
    )
    # Generate double deletion
    # double_deletion_flux = generate_deletion_flux(
    #     double_gene_deletion, model, gene_list=model.genes[:], , solver="cplex"
    # )
    # export_deletion_flux_as_tsv(double_deletion_flux, FBA_DIR / "data" / "double_gene_deletion_output.tsv")
