import json
from pathlib import Path

import cobra
import lxml

FBA_DIR = Path(__file__).parent.resolve().parent.parent


def load_model(sbml_path: str, solver: str = "cplex") -> cobra.core.model.Model:
    """Loads model from SBML XML file."""
    model = cobra.io.read_sbml_model(str(sbml_path))
    model.solver = solver
    return model


def write_json(data, filepath):
    """Writes `data` <dict> to filepath as .json file."""
    with open(filepath, "w") as f:
        json.dump(data, f)
