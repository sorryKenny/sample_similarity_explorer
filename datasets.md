# Dataset Description and Validation

## Selected Dataset Source

The primary dataset used for developing and validating the Sample Similarity Explorer will be a publicly available RNA-seq gene expression dataset obtained from the NCBI Gene Expression Omnibus (GEO). GEO provides processed expression matrices for many studies, which are suitable for direct use in exploratory analysis.

An example dataset suitable for this project is a GEO Series (GSE) containing normalized gene expression values for a cohort of biological samples (e.g., tumor vs. normal samples or different experimental conditions).

## Data Format and Structure

The dataset is provided as a tabular matrix with the following structure:

Rows: Genes (identified by gene symbols or Ensembl IDs)  
Columns: Biological samples  
Values: Normalized gene expression values (e.g., log-transformed counts or TPM)

An optional metadata file may be provided with the following structure:

Rows: Samples  
Columns: Sample annotations (e.g., condition, tissue type, batch)

Example (expression matrix):

Feature,Sample_1,Sample_2,Sample_3  
GeneA,5.2,4.8,6.1  
GeneB,2.3,2.1,2.9  
GeneC,7.4,7.9,6.8  

## Dataset Size and Basic Statistics

A typical GEO RNA-seq dataset contains:

Number of samples: 30–200  
Number of genes: 10,000–20,000  

Basic validation statistics to be computed on the selected dataset include:

- Number of samples  
- Number of features (genes)  
- Percentage of missing values  
- Summary statistics of expression values (mean, standard deviation, range)

These statistics will be used to confirm that the dataset is high-dimensional and suitable for sample-level similarity analysis.

## Subset or Simulated Data for Development

For software development and testing, a small representative subset of the full dataset will be used to ensure fast iteration and debugging. This subset will include:

- A randomly selected subset of samples (e.g., 10–20 samples)
- A subset of features (e.g., 500–1,000 genes)

Alternatively, a simulated dataset with similar dimensions and value ranges may be used for initial testing of the similarity computation functions.

The full dataset will only be used at later stages to validate that the tool scales to larger inputs and produces reasonable similarity patterns on realistic data.

## Rationale for Dataset Selection

RNA-seq gene expression data from GEO are well-suited for this project because:

- The data are high-dimensional and continuous-valued.
- The data are widely used in bioinformatics research and education.
- Processed expression matrices are readily available.
- The dataset structure matches the expected input format of the software tool.

## Example dataset for using the tool

The example dataset used in the tutorial and development of this project is the GEO DataSet **GDS6063**.

The raw dataset is stored in the repository as:

data/GDS6063_full.soft.gz

A parsed expression matrix generated from the SOFT file is provided as:

data/gds6063_expression.csv

Structure of the example dataset:

Rows: genes  
Columns: biological samples  
Values: normalized gene expression values

Basic statistics of the example dataset:

- Number of genes: ~12,000  
- Number of samples: 10  
- Data type: continuous gene expression values  

This dataset is suitable as an example because:

1. It is small enough to run quickly for demonstration purposes.
2. It contains real biological gene expression data.
3. It allows users to observe meaningful similarity patterns between samples.
4. It demonstrates the typical structure of high-dimensional biological datasets used in exploratory analysis.
