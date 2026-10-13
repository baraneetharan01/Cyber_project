from typing import List, Tuple
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def infer_feature_types(df: pd.DataFrame, target_column: str) -> Tuple[List[str], List[str]]:
    """Infer categorical and numerical feature columns from a DataFrame.

    Returns (categorical_cols, numerical_cols).
    """
    feature_cols = [c for c in df.columns if c != target_column]
    categorical_cols: List[str] = []
    numerical_cols: List[str] = []

    for col in feature_cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            numerical_cols.append(col)
        else:
            categorical_cols.append(col)
    return categorical_cols, numerical_cols


def build_preprocessor(categorical_cols: List[str], numerical_cols: List[str]) -> ColumnTransformer:
    """Build a ColumnTransformer that scales numeric features and one-hot encodes categoricals."""
    categorical_transformer = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    numerical_transformer = StandardScaler()

    preprocessor = ColumnTransformer(
        transformers=[
            ("categorical", categorical_transformer, categorical_cols),
            ("numerical", numerical_transformer, numerical_cols),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )
    return preprocessor


