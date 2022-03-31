import os
import sys
from datetime import datetime
from pathlib import Path
from pprint import pprint

ROOT_DIR = Path().resolve().parent
sys.path.append(str(ROOT_DIR))

from cobra.flux_analysis import single_gene_deletion

from fba.src.media import (
    apply_media,
    scade,
    scarg,
    scino,
    sclys,
    scmet,
    sd,
    sdszappanos,
    yp,
    ypac,
    ypd,
    ypetoh,
    ypgal,
    ypgly,
    yplac,
    ypraff,
    ypte_no_glc,
    ypte_no_o2,
)

from scripts.utils import (
    assess_gene_knockout_lethality,
    export_deletion_flux_as_tsv,
    knockout_gene,
    load_model,
    write_json,
)

FBA_MODEL_DIR = ROOT_DIR / "fba" / "model"


def main(model_filepath, model_description=""):
    # Apply media as constructed in in silico model from Szappanos et al., 2011 paper
    media = (
        ("scade", scade),
        ("scarg", scarg),
        ("scino", scino),
        ("sclys", sclys),
        ("scmet", scmet),
        ("sd", sd),
        ("sdszappanos", sdszappanos),
        ("yp", yp),
        ("ypac", ypac),
        ("ypd", ypd),
        ("ypetoh", ypetoh),
        ("ypgal", ypgal),
        ("ypgly", ypgly),
        ("yplac", yplac),
        ("ypraff", ypraff),
        ("ypte_no_glc", ypte_no_glc),
        ("ypte_no_o2", ypte_no_o2),
    )
    for medium_name, medium in media:
        print("loading model...")
        model = load_model(str(model_filepath))

        print(f"applying media {medium_name}...")
        summary = {"medium": medium_name}
        model = apply_media(model, medium)

        # URA3 ('YEL021W') and LEU2 ('YCL018W')
        ko_genes = ["YEL063C", "YNL268W", "YLR303W", "YEL021W", "YCL018W"]
        non_lethal_ko_genes = [
            gene for gene in ko_genes if assess_gene_knockout_lethality(model, gene) is False
        ]
        print("non-lethal genes to delete:", non_lethal_ko_genes)
        summary["non-lethal-gene-ko"] = non_lethal_ko_genes
        model = knockout_gene(model, non_lethal_ko_genes)

        # Find WT growth
        wt_fitness = model.optimize().objective_value
        print("WT fitness is:", wt_fitness)
        summary["wt-fitness"] = wt_fitness

        # =======================================================
        # Perform every single gene knockout
        print("performing total single gene knockout...")
        single_gene_deletions_szappanos = single_gene_deletion(model)

        # Generate appropriate filename
        date = datetime.now().strftime("%Y%m%d")
        dirname = f"{model_description}_{medium_name}_{date}"
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        json_filename = f"{dirname}.json"
        tsv_filename = f"{dirname}.tsv"
        summary["tsv-filename"] = tsv_filename

        # Export
        print("exporting as tsv...")
        export_deletion_flux_as_tsv(
            single_gene_deletions_szappanos, os.path.join(dirname, tsv_filename)
        )
        write_json(summary, os.path.join(dirname, json_filename))
        pprint(summary)


if __name__ == "__main__":
    main(
        FBA_MODEL_DIR / "yeast-GEM.xml",
        model_description="szappanos",
    )
