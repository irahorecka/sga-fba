import sys
from pathlib import Path

ROOT_DIR = Path().resolve().parent
sys.path.append(str(ROOT_DIR))

from cobra.flux_analysis import single_gene_deletion, double_gene_deletion

from fba.src.media import apply_media, sdszappanos
from scripts.utils import export_deletion_flux_as_tsv, gene_knockout, load_model

FBA_MODEL_DIR = ROOT_DIR / "fba" / "model"


def main(model, single_del_export_tsv_filename, double_del_export_tsv_filename):
    # Apply media as constructed in in silico model from Szappanos et al., 2011 paper
    print("applying minimal media...")
    model = apply_media(model, sdszappanos)

    # Exclude URA3 ('YEL021W') and LEU2 ('YCL018W')
    print("performing background gene knockouts...")
    ko_genes = ["YEL063C", "YNL268W", "YLR303W"]
    model = gene_knockout(model, ko_genes)

    # Find WT growth
    print("WT fitness is:", model.optimize().objective_value)

    # =======================================================
    # Perform every single gene knockout
    print("performing total single gene knockout...")
    single_gene_deletions_szappanos = single_gene_deletion(model)
    # Export
    print("exporting as tsv...")
    export_deletion_flux_as_tsv(single_gene_deletions_szappanos, single_del_export_tsv_filename)

    # =======================================================
    # Perform every double gene knockout
    print("performing total double gene knockout...")
    double_gene_deletions_szappanos = double_gene_deletion(model)
    # Export
    print("exporting as tsv...")
    export_deletion_flux_as_tsv(double_gene_deletions_szappanos, double_del_export_tsv_filename)


if __name__ == "__main__":
    print("loading model...")
    model = load_model(str(FBA_MODEL_DIR / "yeast-GEM.xml"))
    main(
        model,
        single_del_export_tsv_filename="single_gene_deletions_szappanos_20220329.tsv",
        double_del_export_tsv_filename="double_gene_deletions_szappanos_20220329.tsv",
    )
