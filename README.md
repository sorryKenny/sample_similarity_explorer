
# Sample Similarity Explorer for High-Dimensional Biological Data

## Biological Question

Given high-dimensional molecular profiles (e.g., gene expression, proteomics, or other omics measurements), how similar are biological samples to each other, and which samples exhibit comparable molecular patterns?

## Project Description

This project aims to develop a general-purpose tool for quantifying and exploring sample-level similarity in high-dimensional biological datasets. The tool is designed to take a matrix of molecular measurements as input and compute pairwise similarity or distance scores between samples using standard statistical metrics.

The primary goal of the project is to support exploratory data analysis tasks such as identifying closely related samples, detecting potential clusters, and comparing molecular profiles across a cohort without restricting the analysis to a specific disease, data source, or experimental platform.

The project focuses on algorithmic clarity and flexibility, allowing different similarity metrics to be applied to the same dataset.

## Input Data

1. **Feature Matrix**
   - Format: CSV or TSV
   - Rows: Molecular features (e.g., genes, proteins, metabolites)
   - Columns: Biological samples
   - Values: Normalized quantitative measurements
   - Example:
     ```
     Feature,Sample_1,Sample_2,Sample_3
     GeneA,5.2,4.8,6.1
     GeneB,2.3,2.1,2.9
     GeneC,7.4,7.9,6.8
     ```

2. **Optional Metadata File**
   - Format: CSV or TSV
   - Content: Sample-level annotations (e.g., condition, batch, tissue type)

## Output Data

1. **Sample Similarity Matrix**
   - Format: CSV or TSV
   - Description: A square matrix where each entry represents the similarity or distance between a pair of samples.

2. **Ranked Similar Sample List**
   - Format: CSV or TSV
   - Description: For a given reference sample, a ranked list of the most similar samples along with their similarity scores.

## Core Algorithmic Workflow

1. Load and validate the input feature matrix.
2. Filter or align features across samples if necessary.
3. Optionally standardize or normalize feature values.
4. Compute pairwise sample similarity or distance using a selected metric (e.g., Pearson correlation, cosine similarity, or Euclidean distance).
5. Generate similarity matrices and ranked sample outputs.
6. Export results in standard tabular formats for downstream analysis or visualization.

### Potential Biological Applications

Beyond identifying similar samples, the tool may also be used to:

- Detect outliers or mislabeled samples
- Assess batch effects in experimental design
- Explore disease subtypes or hidden biological structure

## Scope and Limitations

This project is intended as an exploratory analysis tool and does not attempt to perform statistical inference or predictive modeling. The focus is on transparent computation and interpretability of similarity measures rather than model optimization.

### Normalization Assumptions

By default, the tool assumes that the input expression matrix has already been normalized.

Optional preprocessing strategies may include:
- Z-score standardization per feature
- Log2 transformation
- Missing value filtering

These steps are not automatically applied but can be incorporated before similarity computation.

## Use of AI Tools (Honor Code Disclosure)

Gen AI tools (e.g., ChatGPT) were used during the development of this project for:
- clarifying assignment requirements,
- discussing possible dataset choices,
- understanding software design concepts,
- debugging errors and command-line issues.

All design documents (SRS, DDS, WBS, datasets.md) and all code in this repository were written by me.  
