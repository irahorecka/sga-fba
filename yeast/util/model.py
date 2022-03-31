def optimize(model_func):
    """Decorator that optimizes model prior to returning
    to caller."""

    def wrapper(*args, **kwargs):
        model = model_func(*args, **kwargs)
        model.optimize()
        return model

    return wrapper
