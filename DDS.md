# Design Document Specification (DDS)

## Project Goals

The goal of this project is to build a simple and general-purpose tool for computing and exploring similarity between biological samples based on high-dimensional molecular profiles (e.g., gene expression data). The tool is intended for exploratory data analysis and aims to provide transparent and interpretable similarity computations rather than predictive modeling.

The initial milestone is to support loading a feature matrix, computing a sample-by-sample similarity matrix using a selected metric, and exporting the results in a standard tabular format. Later milestones will focus on supporting multiple similarity metrics, basic visualization, and simple command-line usage.

---

## Modules and Scope

### 1. Data I/O Module

**Scope:**  
This module is responsible for loading input datasets and writing output results.

**Content:**  
- Functions to read CSV/TSV feature matrices  
- Basic input validation (format, missing values, numeric values)  
- Functions to write similarity matrices to CSV/TSV files  

**Dependencies:**  
- Used by all downstream modules

---

### 2. Preprocessing Module

**Scope:**  
This module handles optional preprocessing of the input feature matrix before similarity computation.

**Content:**  
- Feature-wise normalization or standardization (e.g., z-score)  
- Optional filtering of features with missing or invalid values  

**Dependencies:**  
- Depends on Data I/O Module  
- Used by Similarity Computation Module

---

### 3. Similarity Computation Module

**Scope:**  
This module implements the core algorithms for computing similarity or distance between samples.

**Content:**  
- Implementation of similarity metrics (e.g., Pearson correlation, cosine similarity)  
- Construction of sample-by-sample similarity matrices  
- Utility functions for extracting most similar samples for a given reference sample  

**Dependencies:**  
- Depends on Preprocessing Module  

---

### 4. Interface Module

**Scope:**  
This module provides a simple interface for users to run the tool.

**Content:**  
- Command-line interface or main script  
- Argument parsing (input file, output file, similarity metric)  
- Orchestration of data loading, preprocessing, and similarity computation  

**Dependencies:**  
- Depends on Data I/O, Preprocessing, and Similarity Computation Modules  

---

## Module Dependencies (High-Level)

Data I/O  
→ Preprocessing  
→ Similarity Computation  
→ Interface

This modular structure is designed to keep the core computation logic independent from data loading and user interface code, making the tool easier to extend and maintain.

---

## Milestones

**Milestone 1:**  
Load input feature matrix and compute a sample-by-sample similarity matrix using a default metric.

**Milestone 2:**  
Support multiple similarity metrics and basic preprocessing options.

**Milestone 3:**  
Add simple visualization or reporting of most similar samples for a selected reference sample.

Future improvements suggested during peer review include:

- Adding non-linear similarity metrics such as Spearman rank correlation
- Improving handling of missing values before similarity computation
