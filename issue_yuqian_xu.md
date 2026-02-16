## Biological Question Answered:

This tool is primarily designed to explore the similarity among samples in high-dimensional biological data, such as RNA-seq or other omics expression data.

The tool can help answer the followings: which biological samples exhibit similar patterns at the molecular level; is there a potential cluster or subgroup; is there any obvious structure or similarity in the data.

In practical applications, this tool can support exploratory data analysis, sample quality control or cohort exploration, downstream analysis (clustering/trajectory/subtype analysis).

## Use of tools and resources:

The project adopts the modular design emphasized in the course and the workflow is clear: data read, preprocessing, statistical similarity computation, and results export. 

The current code completes parsing SOFT file into expression matrix parsing, data cleaning and format conversion, and basic unit testing (shape validation). The project has begun to shift from design to prototype implementation.

## Goals achieved:

The goal setting is relatively reasonable, which algorithm clarity takes precedence, and exploratory tool takes precedence rather than complex modeling.

The similarity matrix computation technique has low technical risk and high feasibility.

The milestone design progresses step by step, implementing core functions first and then expanding metrics, with a logical approach.

## Progress made:

So far, the GEO SOFT file is parsed into an expression matrix, expression data clean & conversion are completed, and there’s also basic unit test for similarity function. The preliminary construction of the dataset development pipeline has been completed.

The prototype has been completed: the core part of data input and preprocessing.

For next steps suggestions, the project can consider completing the similarity computation module (core algorithm), adding metric selection, and starting to output the similarity matrix.

