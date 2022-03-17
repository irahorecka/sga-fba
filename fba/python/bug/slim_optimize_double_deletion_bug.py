import cobra
import lxml


def load_model(sbml_path, solver="glpk"):
    """Loads model from SBML XML file."""
    model = cobra.io.read_sbml_model(sbml_path)
    model.solver = solver
    model.tolerance = 1e-6
    return model


if __name__ == "__main__":
    model = load_model("yeast-GEM.xml", solver="cplex")
    print("Optimizing now...")
    model.slim_optimize()
