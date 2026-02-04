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

## Activity 2: Support Multiple Similarity Metrics

### Goal
Extend the tool to support multiple similarity or distance metrics beyond the default option.

### Task 1: Define Supported Metrics

**Description:**  
Decide on a small set of supported metrics (e.g., Pearson correlation, cosine similarity, Euclidean distance).

**Deliverable:**  
A documented list of supported metrics in the code or README.

**Completion Criteria:**  
At least two different metrics are clearly defined and documented.

---

### Task 2: Implement Metric Selection

**Description:**  
Modify the similarity computation function to allow the user to choose which metric to use.

**Deliverable:**  
An updated similarity computation function with a metric parameter.

**Completion Criteria:**  
The function correctly computes similarity using different metrics based on user input.

---

### Task 3: Validate Metric Outputs

**Description:**  
Test the implemented metrics on a small dataset and compare outputs to expected behavior.

**Deliverable:**  
Basic test cases or example outputs for different metrics.

**Completion Criteria:**  
Different metrics produce different, reasonable similarity values on the same dataset.

---

## Activity 3: Command-Line Interface (CLI) for Running the Tool

### Goal
Provide a simple command-line interface so users can run the tool without modifying code.

### Task 1: Design CLI Arguments

**Description:**  
Decide on required and optional command-line arguments (input file, output file, metric type).

**Deliverable:**  
A documented list of CLI arguments.

**Completion Criteria:**  
The CLI arguments are clearly specified and consistent with the tool functionality.

---

### Task 2: Implement CLI Wrapper

**Description:**  
Implement a main script that parses command-line arguments and runs the core pipeline.

**Deliverable:**  
A runnable CLI script.

**Completion Criteria:**  
The tool can be executed from the command line with user-specified inputs and outputs.

---

### Task 3: Basic CLI Testing

**Description:**  
Run the CLI on a small dataset and verify that outputs are generated correctly.

**Deliverable:**  
A short example command and corresponding output files.

**Completion Criteria:**  
The CLI runs without errors and produces expected output files.

---

## Activity 4: Result Exploration and Basic Visualization

### Goal
Provide simple ways to explore or summarize similarity results.

### Task 1: Implement Ranked Similar Sample Output

**Description:**  
Add functionality to output, for a given reference sample, a ranked list of most similar samples.

**Deliverable:**  
A function that outputs a ranked list of similar samples with similarity scores.

**Completion Criteria:**  
The ranked list correctly orders samples by similarity.

---

### Task 2: Optional Basic Visualization

**Description:**  
Optionally generate a simple heatmap or summary table of the similarity matrix.

**Deliverable:**  
A basic visualization script or output file.

**Completion Criteria:**  
The visualization or summary output is generated without errors for a small dataset.

---

### Task 3: Document Result Interpretation

**Description:**  
Add brief documentation describing how to interpret similarity outputs.

**Deliverable:**  
Short documentation in README or docs folder.

**Completion Criteria:**  
Users can understand what the similarity scores represent and how to interpret them.
