import pandas as pd
from sample_similarity_explorer.similarity import compute_sample_similarity


def test_similarity_shape():
    df = pd.DataFrame(
        {
            "S1": [1, 2, 3],
            "S2": [1, 2, 3],
            "S3": [3, 2, 1],
        },
        index=["G1", "G2", "G3"],
    )

    sim = compute_sample_similarity(df, metric="pearson")
    assert sim.shape == (3, 3)

