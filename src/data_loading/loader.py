import pandas as pd
from typing import Optional


def load_csv(path: str, dtype: Optional[dict] = None) -> pd.DataFrame:
    """Load CSV file into a pandas DataFrame.

    Parameters
    ----------
    path: str
        Path to the CSV file.
    dtype: Optional[dict]
        Optional dtype mapping for columns.
    """
    return pd.read_csv(path, dtype=dtype)


