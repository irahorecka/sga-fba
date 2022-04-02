import os
import sys
from datetime import datetime
from pathlib import Path
from pprint import pprint

ROOT_DIR = Path().resolve().parent
sys.path.append(str(ROOT_DIR))

from cobra.flux_analysis import double_gene_deletion, single_gene_deletion

from scripts.utils import export_deletion_flux_as_tsv, write_json
from yeast.core.gene import assess_gene_knockout_viability, knockout_genes
from yeast.core.gene.essential import attenuate_flux
from yeast.core.media import apply_media, get_every_media
from yeast.core.model import get_objective_value, load_model


def main(model_description=""):
    # Apply media as constructed in in silico model from Szappanos et al., 2011 paper
    for medium_name, medium in get_every_media().items():
        # Load model and apply medium
        print("loading model...")
        model = load_model()
        print(f"applying media {medium_name}...")
        model = apply_media(model, medium)

        # URA3 ('YEL021W') and LEU2 ('YCL018W')
        # KO of YPR021 derived from Heavner and Price - 2015 - update: doesn't help the model
        ko_genes = ["YEL063C", "YNL268W", "YLR303W", "YEL021W", "YCL018W"]
        non_lethal_ko_genes = [
            gene for gene in ko_genes if assess_gene_knockout_viability(model, gene) is True
        ]
        lethal_genes = list(set(ko_genes).symmetric_difference(set(non_lethal_ko_genes)))

        # Gene knockout
        print("non-essential genes to delete:", non_lethal_ko_genes)
        summary = {"medium": medium_name, "non-lethal-gene-ko": non_lethal_ko_genes}
        model = knockout_genes(model, non_lethal_ko_genes)
        print("essential genes to attenuate to 80% fitness each:", lethal_genes)
        summary["lethal-gene-attenuate"] = lethal_genes

        # The order in which genes are attenuated MATTERS
        model = attenuate_flux(model, "YCL018W", flux_ratio=0.8)
        model = attenuate_flux(model, "YEL021W", flux_ratio=0.85)

        # for gene in lethal_genes:
        #     model = attenuate_flux(model, gene, flux_ratio=0.8)

        # Find WT growth
        wt_fitness = get_objective_value(model)
        print("WT fitness is:", wt_fitness)
        summary["wt-fitness"] = wt_fitness

        # =======================================================
        # Perform every single gene knockout
        print("performing total single gene knockout...")
        single_gene_deletions_szappanos = single_gene_deletion(model)
        # Perform every double gene knockout
        # print("performing total double gene knockout...")
        # double_gene_deletions_szappanos = double_gene_deletion(model)

        # Generate appropriate filename
        date = datetime.now().strftime("%Y%m%d")
        dirname = f"{model_description}_{medium_name}_{date}"
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        json_filename = f"{dirname}.json"
        tsv_filename = f"{dirname}.tsv"

        single_gene_ko_tsv_filename = f"single_gene_ko_{tsv_filename}"
        # double_gene_ko_tsv_filename = f"double_gene_ko_{tsv_filename}"
        summary["single-gene-ko-tsv-filename"] = single_gene_ko_tsv_filename
        # summary["double-gene-ko-tsv-filename"] = double_gene_ko_tsv_filename

        # Export
        print("exporting as tsv...")
        export_deletion_flux_as_tsv(
            single_gene_deletions_szappanos, os.path.join(dirname, single_gene_ko_tsv_filename)
        )
        # export_deletion_flux_as_tsv(
        #     double_gene_deletions_szappanos, os.path.join(dirname, double_gene_ko_tsv_filename)
        # )
        write_json(summary, os.path.join(dirname, json_filename))
        pprint(summary)


if __name__ == "__main__":
    main(model_description="szappanos")
