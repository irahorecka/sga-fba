from functools import reduce

import cobra

from yeast.util.model import optimize


def assess_gene_knockout_viability(model, gene_name):
    """Assesses viability of model when `gene_name` is knocked out.
    Returns True if viable, False if lethal."""
    with model:
        model.genes.query(gene_name).pop().knock_out()
        if model.optimize().objective_value == 0:
            return False
        return True


def get_gene(model, gene_name):
    return model.genes.query(gene_name)[0]


def get_gene_summary(gene):
    """Gets gene summary from a model's gene."""
    return {
        gene.id: {
            "name": gene.name,
            "is_functional": gene.functional,
            "reactions": [{rxn.id: rxn.name} for rxn in gene.reactions],
            "annotation": gene.annotation,
            "notes": gene.notes,
        }
    }


def get_total_gene_summary(model):
    """Gets every gene's summary from a model."""
    return reduce(lambda x, y: {**x, **y}, (get_gene_summary(gene) for gene in model.genes))


@optimize
def knockout_gene(model, gene):
    """Knocks out a gene from model. The model state
    is persisted thereafter and returned to caller."""
    # Removes gene entirely from model
    model.genes.query(gene).pop().knock_out()
    return model


@optimize
def knockout_genes(model, genes):
    """Knocks out an array of genes from model. The model state
    is persisted thereafter and returned to caller."""
    # Removes genes entirely from model
    cobra.manipulation.remove_genes(model, genes)
    return model
