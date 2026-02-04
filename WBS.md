# Work Breakdown Structure (WBS)

## Activity 1: Compute Sample-to-Sample Similarity Matrix

### Goal
Implement the first basic functionality of the project: computing a sample-by-sample similarity matrix from a high-dimensional feature matrix and exporting the result as a table.

---

### Task 1: Prepare Development Dataset

**Description:**  
Select a GEO gene expression dataset and create a small representative subset for development and testing.

**Deliverable:**  
A local CSV/TSV file containing a feature-by-sample matrix (e.g., 10–20 samples, 500–1,000 genes).

**Completion Criteria:**  
The dataset can be loaded successfully and matches the expected input format.

---

### Task 2: Load and Validate Input Data

**Description:**  
Implement a function to load the input matrix and check that rows are features, columns are samples, and values are numeric.

**Deliverable:**  
A data loading and validation function.

**Completion Criteria:**  
Input data can be read without errors and basic format checks pass.

---

### Task 3: Compute Pairwise Sample Similarity

**Description:**  
Implement a function to compute pairwise similarity between samples using a default metric (e.g., Pearson correlation).

**Deliverable:**  
A function that returns a square similarity matrix with sample IDs as row and column labels.

**Completion Criteria:**  
A similarity matrix with valid numeric values is produced.

---

### Task 4: Export Similarity Results

**Description:**  
Write the similarity matrix to a CSV/TSV file for downstream analysis or visualization.

**Deliverable:**  
An output file containing the similarity matrix.

**Completion Criteria:**  
The output file is created and can be opened and interpreted correctly.
