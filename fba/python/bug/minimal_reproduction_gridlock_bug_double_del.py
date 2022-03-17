import cobra
import lxml
from cobra.flux_analysis import double_gene_deletion


def load_model(sbml_path, solver="glpk"):
    """Loads model from SBML XML file."""
    model = cobra.io.read_sbml_model(sbml_path)
    model.solver = solver
    model.tolerance = 1e-6
    return model


def generate_deletion_flux(deletion_func, model, **kwargs):
    """Generates deletion flux pandas DataFrame by applying
    `deletion_func` to a model."""
    return deletion_func(model, **kwargs)


if __name__ == "__main__":
    model = load_model("yeast-GEM.xml", solver="cplex")
    single_deletion_flux = generate_deletion_flux(
        double_gene_deletion, model, gene_list=model.genes[:10]
    )
