import pandas as pd


def load_feature_matrix(path: str) -> pd.DataFrame:
    """
    Load a feature-by-sample matrix from CSV or TSV.
    """

    # Added: basic path validation
    if not isinstance(path, str) or not path.strip():
        raise ValueError("Input path must be a non-empty string.")

    # Added: file existence validation
    file_path = Path(path)
    if not file_path.exists():
        raise ValueError(f"Input file does not exist: {path}")

    # Added: supported file type validation
    if not (path.endswith(".tsv") or path.endswith(".csv")):
        raise ValueError(
            "Unsupported file type. Please provide a .csv or .tsv file."
        )

    
    if path.endswith(".tsv"):
        df = pd.read_csv(path, sep="\t", index_col=0)
    else:
        df = pd.read_csv(path, index_col=0)

    if df.empty:
        raise ValueError("Input matrix is empty.")

    # Added: at least two sample columns
    if df.shape[1] < 2:
        raise ValueError("Input matrix must contain at least two sample columns.")

    # Added: feature identifier / row index validation
    if df.index.isnull().any():
        raise ValueError("Feature identifiers / row index contain missing values.")

    if df.index.astype(str).str.strip().eq("").any():
        raise ValueError("Feature identifiers / row index contain empty values.")

    if df.index.duplicated().any():
        duplicated_features = df.index[df.index.duplicated()].tolist()
        raise ValueError(
            f"Feature identifiers must be unique. Duplicates found: {duplicated_features[:5]}"
        )

    
    # Added: sample name validation
    if df.columns.isnull().any():
        raise ValueError("Sample names contain missing values.")

    if pd.Index(df.columns).astype(str).str.strip().eq("").any():
        raise ValueError("Sample names contain empty values.")

    if df.columns.duplicated().any():
        duplicated_samples = df.columns[df.columns.duplicated()].tolist()
        raise ValueError(
            f"Sample names must be unique. Duplicates found: {duplicated_samples[:5]}"
        )

    # Added: numeric value validation
    numeric_df = df.apply(pd.to_numeric, errors="coerce")

    original_missing = df.isna()
    invalid_values = numeric_df.isna() & ~original_missing

    if invalid_values.any().any():
        bad_rows, bad_cols = invalid_values.to_numpy().nonzero()
        first_bad_row = df.index[bad_rows[0]]
        first_bad_col = df.columns[bad_cols[0]]
        bad_value = df.loc[first_bad_row, first_bad_col]
        raise ValueError(
            f"Non-numeric value found in matrix at feature '{first_bad_row}', "
            f"sample '{first_bad_col}': {bad_value!r}"
        )

    return numeric_df

