import pandas as pd


def load_feature_matrix(path: str) -> pd.DataFrame:
    """
    Load a feature-by-sample matrix from CSV or TSV.
    """
    if path.endswith(".tsv"):
        df = pd.read_csv(path, sep="\t", index_col=0)
    else:
        df = pd.read_csv(path, index_col=0)

    if df.empty:
        raise ValueError("Input matrix is empty.")

    return df

