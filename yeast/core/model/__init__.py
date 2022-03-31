from pathlib import Path

import cobra

from yeast.util.model import optimize

MODEL_DIR = Path(__file__).resolve().parent


def get_objective_value(model):
    return model.optimize().objective_value


@optimize
def load_model(solver="cplex"):
    model = cobra.io.read_sbml_model(str(MODEL_DIR / "yeast-GEM-8.5.0.xml"))
    model.solver = solver
    return model
