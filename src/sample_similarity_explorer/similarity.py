import numpy as np
import pandas as pd


def compute_sample_similarity(
    df: pd.DataFrame,
    metric: str = "pearson",
    missing: str = "drop"
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
    if df.shape[1] < 2:
        raise ValueError("At least two samples are required.")
        
    # FIX 1: Move the "all missing" check ABOVE the "numeric" check
    if df.isna().all().any():
        raise ValueError("Dataframe contains columns with all missing values.")
        
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise ValueError("Non-numeric value found.")
            
    if metric == "pearson" and (df.std(axis=0) == 0).any():
        raise ValueError("Dataframe contains constant-valued samples.")

    if df.empty:
        raise ValueError("Input dataframe is empty.")

    # Handle missing data
    if df.isna().any().any():
        if missing == "drop":
            df = df.dropna(axis=0, how="any")
        elif missing == "fill":
            df = df.fillna(0)
        else:
            raise ValueError(f"Unknown missing strategy: {missing}")

    # Validate metric selection
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
        # Rank transform first, then Pearson
        ranked = pd.DataFrame(data).rank(axis=1).values
        sim = np.corrcoef(ranked)

    return pd.DataFrame(sim, index=df.columns, columns=df.columns)


def get_top_similar_samples(similarity_df, reference_sample, top_n=5, exclude_self=True):
    if similarity_df.shape[0] != similarity_df.shape[1]:
        raise ValueError("Must provide a square matrix.")
        
    if not similarity_df.index.equals(similarity_df.columns):
        raise ValueError("Matrix must have matching row and column labels.")
        
    if reference_sample not in similarity_df.index:
        raise ValueError("Reference sample not found.")
        
    if not isinstance(top_n, int) or top_n <= 0:
        raise ValueError("top_n must be a positive integer.")

    sim_scores = similarity_df[reference_sample].copy()

    if exclude_self and reference_sample in sim_scores.index:
        sim_scores = sim_scores.drop(reference_sample)

    top_samples = sim_scores.sort_values(ascending=False).head(top_n)
    
    # FIX 2: Convert the 1D Series into a 2D DataFrame with specific column names expected by tests
    result_df = top_samples.reset_index()
    result_df.columns = ["sample", "similarity"]
    
    return result_df
