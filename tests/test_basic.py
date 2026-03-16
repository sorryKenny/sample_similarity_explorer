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



# Added tests for get_top_similar_samples

def test_get_top_similar_samples_basic():
    similarity_df = pd.DataFrame(
        [
            [1.0, 0.9, 0.2],
            [0.9, 1.0, 0.3],
            [0.2, 0.3, 1.0]
        ],
        index=["S1", "S2", "S3"],
        columns=["S1", "S2", "S3"]
    )

    result = get_top_similar_samples(similarity_df, reference_sample="S1", top_n=2)

    assert result.shape == (2, 2)
    assert list(result.columns) == ["sample", "similarity"]
    assert result.iloc[0]["sample"] == "S2"
    assert result.iloc[0]["similarity"] == pytest.approx(0.9)
    assert result.iloc[1]["sample"] == "S3"


def test_get_top_similar_samples_include_self():
    similarity_df = pd.DataFrame(
        [
            [1.0, 0.9, 0.2],
            [0.9, 1.0, 0.3],
            [0.2, 0.3, 1.0]
        ],
        index=["S1", "S2", "S3"],
        columns=["S1", "S2", "S3"]
    )

    result = get_top_similar_samples(
        similarity_df,
        reference_sample="S1",
        top_n=2,
        exclude_self=False
    )

    assert result.iloc[0]["sample"] == "S1"
    assert result.iloc[0]["similarity"] == pytest.approx(1.0)
    assert result.iloc[1]["sample"] == "S2"


def test_get_top_similar_samples_reference_not_found():
    similarity_df = pd.DataFrame(
        [
            [1.0, 0.5],
            [0.5, 1.0]
        ],
        index=["S1", "S2"],
        columns=["S1", "S2"]
    )

    with pytest.raises(ValueError, match="Reference sample not found"):
        get_top_similar_samples(similarity_df, reference_sample="S3")


def test_get_top_similar_samples_invalid_top_n():
    similarity_df = pd.DataFrame(
        [
            [1.0, 0.5],
            [0.5, 1.0]
        ],
        index=["S1", "S2"],
        columns=["S1", "S2"]
    )

    with pytest.raises(ValueError, match="top_n must be a positive integer"):
        get_top_similar_samples(similarity_df, reference_sample="S1", top_n=0)


def test_get_top_similar_samples_non_square_matrix():
    similarity_df = pd.DataFrame(
        [
            [1.0, 0.5, 0.2],
            [0.5, 1.0, 0.3]
        ],
        index=["S1", "S2"],
        columns=["S1", "S2", "S3"]
    )

    with pytest.raises(ValueError, match="square matrix"):
        get_top_similar_samples(similarity_df, reference_sample="S1")


def test_get_top_similar_samples_mismatched_labels():
    similarity_df = pd.DataFrame(
        [
            [1.0, 0.5],
            [0.5, 1.0]
        ],
        index=["S1", "S2"],
        columns=["S1", "S3"]
    )

    with pytest.raises(ValueError, match="matching row and column labels"):
        get_top_similar_samples(similarity_df, reference_sample="S1")
