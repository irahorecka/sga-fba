import cobra

from yeast.util.model import optimize


@optimize
def load_model(model_path, solver="cplex"):
    model = cobra.io.read_sbml_model(model_path)
    model.solver = solver
    return model
