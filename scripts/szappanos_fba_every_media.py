import os
import sys
from datetime import datetime
from pathlib import Path
from pprint import pprint

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import yaml
from cobra.flux_analysis import double_gene_deletion, single_gene_deletion

from scripts.utils import export_df_as_tsv, write_json
from yeast.core.gene import knockout_genes
from yeast.core.gene.essential import attenuate_flux
from yeast.core.media import apply_media, get_every_media
from yeast.core.model import get_objective_value, load_model

with open(Path(__file__).resolve().parent / "config.yaml", "r", encoding="utf-8") as config:
    YEAST_FBA = yaml.safe_load(config)["yeast-fba"]


def main(model_description=""):
    # Apply media as constructed in in silico model from Szappanos et al., 2011 paper
    media = get_every_media()
    if YEAST_FBA["media"]:
        media = {medium_name: media[medium_name] for medium_name in YEAST_FBA["media"]}
    for medium_name, medium in media.items():
        # Load model and apply medium
        model = load_model()
        model = apply_media(model, medium)

        # Perform gene knockout(s)
        knockout = {
            gene: flux for gene, flux in YEAST_FBA["gene"]["deletions"].items() if flux == 0
        }
        summary = {
            "medium": medium_name,
            "gene-knockout": knockout,
            "gene-knockout-order": list(knockout.keys()),
        }
        model = knockout_genes(model, list(knockout.keys()))

        # Perform gene attenuation(s)
        attenuate = {
            gene: flux for gene, flux in YEAST_FBA["gene"]["deletions"].items() if flux > 0
        }
        for gene, flux in attenuate.items():
            model = attenuate_flux(model, gene, flux_ratio=flux)
        summary = {
            **summary,
            **{"gene-attenuate": attenuate, "gene-attenuate-order": list(attenuate.keys())},
        }

        # Find WT growth
        wt_fitness = get_objective_value(model)
        summary["wt-fitness"] = wt_fitness

        # Perform total single and double gene knockout
        single_gene_deletions_szappanos = single_gene_deletion(model)
        # double_gene_deletions_szappanos = double_gene_deletion(model)

        # Generate appropriate filename
        dirname = f"{model_description}_{medium_name}_{datetime.now().strftime('%Y%m%d')}"
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        json_filename = f"{dirname}.json"
        tsv_filename = f"{dirname}.tsv"
        single_gene_ko_tsv_filename = f"single_gene_ko_{tsv_filename}"
        # double_gene_ko_tsv_filename = f"double_gene_ko_{tsv_filename}"
        summary["single-gene-ko-tsv-filename"] = single_gene_ko_tsv_filename
        # summary["double-gene-ko-tsv-filename"] = double_gene_ko_tsv_filename

        # Export TSV and JSON files
        export_df_as_tsv(
            single_gene_deletions_szappanos, os.path.join(dirname, single_gene_ko_tsv_filename)
        )
        # export_df_as_tsv(
        #     double_gene_deletions_szappanos, os.path.join(dirname, double_gene_ko_tsv_filename)
        # )
        write_json(summary, os.path.join(dirname, json_filename))
        pprint(summary)


if __name__ == "__main__":
    main(model_description=YEAST_FBA["model-description"])
