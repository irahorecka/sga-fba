import cobra
import optlang
import lxml
from cobra.flux_analysis import double_gene_deletion


def load_model(sbml_path, solver="glpk"):
    """Loads model from SBML XML file."""
    model = cobra.io.read_sbml_model(sbml_path)
    model.solver = solver
    return model


def generate_deletion_flux(deletion_func, model, **kwargs):
    """Generates deletion flux pandas DataFrame by applying
    `deletion_func` to a model."""
    return deletion_func(model, **kwargs)


if __name__ == "__main__":
    optlang.cplex_interface.Configuration.verbosity = 3
    model = load_model("yeast-GEM.xml", solver="cplex")
    generate_deletion_flux(
        double_gene_deletion,
        model,
        gene_list1=(model.genes[1],),
        gene_list2=(model.genes[2],),
        processes=1,
    )
