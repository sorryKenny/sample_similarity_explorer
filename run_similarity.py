from sample_similarity_explorer.io import load_feature_matrix
from sample_similarity_explorer.similarity import compute_sample_similarity

df = load_feature_matrix("data/gds6063_expression.csv")
sim = compute_sample_similarity(df)

sim.to_csv("data/similarity_matrix.csv")
print("Similarity matrix saved.")
