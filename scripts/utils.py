"""
Common utility functions that are apart from the
yeast FBA suite.
"""

import json


def export_df_as_tsv(df, filepath):
    """Exports pandas DataFrame as TSV."""
    df.to_csv(filepath, sep="\t", index=False)


def read_json(filepath, **kwargs):
    """Reads and returns .json `filepath` as dictionary."""
    with open(filepath, "r") as f:
        data = json.load(f, **kwargs)
    return data


def write_json(json_data, filepath, **kwargs):
    """Exports `json_data` to `filepath`."""
    with open(filepath, "w") as f:
        json.dump(json_data, f, cls=SetEncoder, **kwargs)


class SetEncoder(json.JSONEncoder):
    """Sets set datatype to list."""

    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
