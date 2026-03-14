import pandas as pd
import pytest
from sample_similarity_explorer.similarity import compute_sample_similarity


def test_pearson_similarity():
    df = pd.DataFrame({
        "S1": [1, 2, 3],
        "S2": [1, 2, 3],
        "S3": [3, 2, 1]
    })
    sim = compute_sample_similarity(df, metric="pearson")
    assert sim.shape == (3, 3)
    assert sim.loc["S1", "S2"] == pytest.approx(1.0)


def test_cosine_similarity():
    df = pd.DataFrame({
        "S1": [1, 0],
        "S2": [0, 1]
    })
    sim = compute_sample_similarity(df, metric="cosine")
    assert sim.shape == (2, 2)


def test_invalid_metric():
    df = pd.DataFrame({
        "S1": [1, 2],
        "S2": [3, 4]
    })
    with pytest.raises(ValueError):
        compute_sample_similarity(df, metric="invalid")


def test_edge_case_single_feature():
    df = pd.DataFrame({
        "S1": [1],
        "S2": [1]
    })
    sim = compute_sample_similarity(df)
    assert sim.shape == (2, 2)


def test_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        compute_sample_similarity(df)


# Added tests

# Added tests for new validation behavior

def test_single_sample_column():
    df = pd.DataFrame({
        "S1": [1, 2, 3]
    })
    with pytest.raises(ValueError, match="At least two samples are required"):
        compute_sample_similarity(df)


def test_all_missing_sample_column():
    df = pd.DataFrame({
        "S1": [1, 2, 3],
        "S2": [None, None, None]
    })
    with pytest.raises(ValueError, match="all missing values"):
        compute_sample_similarity(df)


def test_non_numeric_matrix_values():
    df = pd.DataFrame({
        "S1": [1, 2, "abc"],
        "S2": [3, 4, 5]
    })
    with pytest.raises(ValueError, match="Non-numeric value found"):
        compute_sample_similarity(df)


def test_constant_valued_samples_for_pearson():
    df = pd.DataFrame({
        "S1": [1, 1, 1],
        "S2": [2, 3, 4]
    })
    with pytest.raises(ValueError, match="constant-valued samples"):
        compute_sample_similarity(df, metric="pearson")
