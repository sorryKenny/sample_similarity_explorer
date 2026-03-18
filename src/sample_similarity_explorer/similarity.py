import numpy as np
import pandas as pd


def compute_sample_similarity(
    df: pd.DataFrame,
    metric: str = "pearson",
    missing: str = "drop"  # NEW
) -> pd.DataFrame:
    """
    Compute pairwise sample-to-sample similarity.

    Parameters
    ----------
    df : pd.DataFrame
        Feature-by-sample matrix (rows = features, columns = samples)
    metric : str
        "pearson", "cosine", or "spearman"
    missing : str
        How to handle missing values:
        - "drop": remove rows with NaN
        - "fill": replace NaN with 0

    Returns
    -------
    pd.DataFrame
        Sample-by-sample similarity matrix
    """

    if df.empty:
        raise ValueError("Input dataframe is empty.")

    # ===== NEW: Missing data handling =====
    if df.isna().any().any():
        if missing == "drop":
            df = df.dropna(axis=0, how="any")
        elif missing == "fill":
            df = df.fillna(0)
        else:
            raise ValueError(f"Unknown missing strategy: {missing}")

    # ===== NEW: support spearman =====
    if metric not in {"pearson", "cosine", "spearman"}:
        raise ValueError(f"Unsupported metric: {metric}")

    data = df.values.T  # samples x features

    if metric == "pearson":
        sim = np.corrcoef(data)

    elif metric == "cosine":
        norms = np.linalg.norm(data, axis=1, keepdims=True)
        normalized = data / (norms + 1e-8)
        sim = normalized @ normalized.T

    elif metric == "spearman":
        # rank transform first, then Pearson
        ranked = pd.DataFrame(data).rank(axis=1).values
        sim = np.corrcoef(ranked)

    return pd.DataFrame(sim, index=df.columns, columns=df.columns)