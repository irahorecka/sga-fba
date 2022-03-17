import time

import cobra
import lxml
from cobra.flux_analysis import single_gene_deletion


def load_model(sbml_path, solver="glpk"):
    """Loads model from SBML XML file."""
    model = cobra.io.read_sbml_model(sbml_path)
    model.solver = solver
    # model.tolerance = 1e-6
    return model


def generate_deletion_flux(deletion_func, model, **kwargs):
    """Generates deletion flux pandas DataFrame by applying
    `deletion_func` to a model."""
    return deletion_func(model, **kwargs)


if __name__ == "__main__":
    # CPLEX works fine without lowering model tolerance.
    model = load_model("yeast-GEM.xml", solver="cplex")
    # Test multiprocessing gridlock in increments of 50 genes.
    for gene_num in range(10, 500, 50):
        t0 = time.time()
        try:
            single_deletion_flux = generate_deletion_flux(
                single_gene_deletion, model, gene_list=model.genes[:gene_num]
            )
        except KeyboardInterrupt as e:
            print(
                f"Process exited by user.\ntime elapsed processing {gene_num} genes: {round(time.time() - t0, 1)} sec"
            )
            raise KeyboardInterrupt from e
        print(f"time elapsed processing {gene_num} genes: {round(time.time() - t0, 1)} sec")
