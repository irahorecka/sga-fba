import cobra

from pylib.std import write_json

from cobra_utils import load_model, FBA_DIR


def get_gene_rxns_from_model(model: cobra.core.model.Model) -> dict:
    """Gets every gene's reaction from an input model."""
    return {
        gene.id: {
            "name": gene.name,
            "is_functional": gene.functional,
            "reactions": [{rxn.id: rxn.name} for rxn in gene.reactions],
        }
        for gene in model.genes
    }


if __name__ == "__main__":
    model = load_model(str(FBA_DIR / "model" / "yeast-GEM.xml"))
    gene_rxns = get_gene_rxns_from_model(model)
    write_json(gene_rxns, FBA_DIR / "data" / "s_cerevisiae_gene_rxns.json")
