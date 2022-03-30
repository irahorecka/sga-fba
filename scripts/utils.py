import cobra
import lxml


def load_model(model_path, solver="cplex"):
    model = cobra.io.read_sbml_model(model_path)
    model.solver = solver
    return model


def export_deletion_flux_as_tsv(df, filepath):
    df.to_csv(filepath, sep="\t", index=False)


def gene_knockout(model, genes):
    for gene in genes:
        model.genes.query(gene).pop().knock_out()
    model.optimize()
    return model
