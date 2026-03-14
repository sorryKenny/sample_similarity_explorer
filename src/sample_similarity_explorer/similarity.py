import numpy as np
import pandas as pd


def compute_sample_similarity(df: pd.DataFrame, metric: str = "pearson") -> pd.DataFrame:
    """
    Compute pairwise sample-to-sample similarity from a feature-by-sample matrix.

    Parameters
    ----------
    df : pd.DataFrame
        Feature-by-sample matrix (rows = features, columns = samples).
    metric : str
        Similarity metric to use. Currently supported: "pearson", "cosine".

    Returns
    -------
    pd.DataFrame
        Sample-by-sample similarity matrix.
    """

    # Added: basic input type validation
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")

    if df.empty:
        raise ValueError("Input dataframe is empty.")

    # Added: require at least two samples
    if df.shape[1] < 2:
        raise ValueError("At least two samples are required to compute similarity.")

    # Added: detect all-missing sample columns before dropping rows
    all_missing_samples = df.columns[df.isna().all(axis=0)].tolist()
    if all_missing_samples:
        raise ValueError(
            f"Samples with all missing values are not allowed: {all_missing_samples}"
        )

    # Added: numeric validation
    numeric_df = df.apply(pd.to_numeric, errors="coerce")
    original_missing = df.isna()
    invalid_values = numeric_df.isna() & ~original_missing
    if invalid_values.any().any():
        bad_rows, bad_cols = invalid_values.to_numpy().nonzero()
        first_bad_row = df.index[bad_rows[0]]
        first_bad_col = df.columns[bad_cols[0]]
        bad_value = df.loc[first_bad_row, first_bad_col]
        raise ValueError(
            f"Non-numeric value found in dataframe at feature '{first_bad_row}', "
            f"sample '{first_bad_col}': {bad_value!r}"
        )
        
    df = df.dropna(axis=0, how="any")

    # Added: check whether any usable rows remain
    if df.empty:
        raise ValueError("No valid features remain after removing rows with missing values.")

    if metric not in {"pearson", "cosine"}:
        raise ValueError(f"Unsupported metric: {metric}")

    data = df.values.T  # samples x features

    # Added: define clear behavior for constant-valued samples in Pearson
    if metric == "pearson":
        constant_samples = [col for col in df.columns if df[col].nunique() <= 1]
        if constant_samples:
            raise ValueError(f"Pearson correlation cannot be computed for constant-valued samples: {constant_samples}")

    if metric == "pearson":
        sim = np.corrcoef(data)
    elif metric == "cosine":
        norms = np.linalg.norm(data, axis=1, keepdims=True)
        normalized = data / (norms + 1e-8)
        sim = normalized @ normalized.T

    return pd.DataFrame(sim, index=df.columns, columns=df.columns)

