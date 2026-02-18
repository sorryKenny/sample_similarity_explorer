import numpy as np
import pandas as pd

# remove rows with any NaN
X = X[~np.isnan(X).any(axis=1)]

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

    if df.empty:
        raise ValueError("Input dataframe is empty.")
        
    df = df.dropna(axis=0, how="any")

    if metric not in {"pearson", "cosine"}:
        raise ValueError(f"Unsupported metric: {metric}")

    data = df.values.T  # samples x features
    
    if metric not in {"pearson", "cosine"}:
        raise ValueError(f"Unsupported metric: {metric}")

    data = df.values.T  # samples x features

    if metric == "pearson":
        sim = np.corrcoef(data)
    elif metric == "cosine":
        norms = np.linalg.norm(data, axis=1, keepdims=True)
        normalized = data / (norms + 1e-8)
        sim = normalized @ normalized.T

    return pd.DataFrame(sim, index=df.columns, columns=df.columns)

