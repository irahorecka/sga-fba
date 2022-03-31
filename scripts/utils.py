import json

import cobra
import lxml


def load_model(model_path, solver="cplex"):
    model = cobra.io.read_sbml_model(model_path)
    model.solver = solver
    return model


def export_deletion_flux_as_tsv(df, filepath):
    df.to_csv(filepath, sep="\t", index=False)


def knockout_gene(model, genes):
    for gene in genes:
        model.genes.query(gene).pop().knock_out()
    model.optimize()
    return model


def assess_gene_knockout_lethality(model, gene):
    with model:
        model.genes.query(gene).pop().knock_out()
        if model.optimize().objective_value == 0:
            return True
        return False


def read_json(filepath, **kwargs):
    """Reads and returns .json `filepath` as dictionary."""
    with open(filepath, "r") as f:
        data = json.load(f, **kwargs)
    return data


def write_json(json_data, filepath, **kwargs):
    """Exports `json_data` to `filepath`."""
    with open(filepath, "w") as f:
        json.dump(json_data, f, cls=SetEncoder, **kwargs)


class SetEncoder(json.JSONEncoder):
    """Sets set datatype to list."""

    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
