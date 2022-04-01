from yeast.core.gene import assess_gene_knockout_viability
from yeast.core.gene.exceptions import IsNonEssentialGene
from yeast.util.model import optimize


@optimize
def attenuate_flux(model, gene_name, flux_ratio=0.50, flux_margin=0.0000001):
    """Attenuates an essential gene to `flux_ratio` fraction of its WT flux.
    The model state is persisted thereafter and returned to caller."""
    if assess_gene_knockout_viability(model, gene_name) is True:
        raise IsNonEssentialGene(f"Gene {gene_name} is not an essential gene.")
    wt_flux = model.optimize().objective_value
    target_lower_flux = (wt_flux * flux_ratio) - flux_margin
    target_upper_flux = (wt_flux * flux_ratio) + flux_margin
    gene = model.genes.query(gene_name)[0]

    def recurse_attenuation(model, upper_flux, upper_bound, lower_flux, lower_bound):
        """Recursively find the gene's reaction upper bound that leads to `flux_ratio`
        attenuation of the WT flux. This algorithm implements the binary search."""
        new_bound = (upper_bound + lower_bound) / 2
        list(gene.reactions)[0].upper_bound = new_bound
        flux = model.optimize().objective_value
        if flux < target_lower_flux:
            return recurse_attenuation(model, upper_flux, upper_bound, flux, new_bound)
        if flux > target_upper_flux:
            return recurse_attenuation(model, flux, new_bound, lower_flux, lower_bound)
        return new_bound

    with model:
        upper_bound = list(gene.reactions)[0].upper_bound
        lower_bound = list(gene.reactions)[0].lower_bound
        attenuated_bound = recurse_attenuation(
            model, target_upper_flux, upper_bound, target_lower_flux, lower_bound
        )

    list(gene.reactions)[0].upper_bound = attenuated_bound
    return model
