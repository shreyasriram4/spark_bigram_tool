# Text Analysis Tools: Word Count and Bigram Distribution

This repository contains two powerful text analysis tools: a Word Count script and a Bigram Distribution Computational Tool using Apache Spark. The Word Count script analyzes text files to count the frequency of each word, while the Bigram Distribution tool computes the probability of the occurrence of a second word given the first word in a pair, offering deep insights into the structure and patterns of language in large datasets.

## Getting Started

These instructions will guide you on how to use both tools, including setup, execution, and result interpretation.

### Prerequisites

- Python
- Apache Spark: Both tools require Apache Spark, as they utilize PySpark for processing large datasets.

### Installation

#### PySpark Installation

If you haven't installed PySpark, run:

```bash
pip install pyspark
```

### Contents:
1. wordcount.py
2. bigram.py


## Word Count Tool

1. Download wordcount.py from Google Drive link
2. Place your text file (in this case wiki.txt) in same directory.
3. Open a terminal, navigate to the directory containing wordcount.py, and run:

```bash
spark-submit ./wordcount.py ./wiki.txt ./output
```
Replace wiki.txt with your relevant text file if needed.

### Word Count Tool Output
Output to word count tool using wiki.txt: [link]

## Bigram Count & Distribution Tool

1. Download bigramcount.py from Google Drive link specified above.
2. Ensure your input text file (in this case: wiki.txt) is placed in same directory.
3. In a terminal, navigate to the directory containing bigramcount.py.
4. Execute the script using Spark-submit, replacing paths as necessary

```bash
spark-submit bigramcount.py /path/to/input/wiki.txt /path/to/output/directory
```
Replace wiki.txt with your relevant file if needed.

## Interpreting the Results
Word Count Tool: The output is in wordcounts.txt. Interpretation is straightforward, listing each word encountered in the text alongside its frequency of occurrence.

Bigram Distribution Tool: The results are formatted as follows:
1. bigram_counts.txt: (('first word', 'second word'), 'count')
2. bigram_dist.txt: (('first word', 'second word'), 'probability of second word given first word appearing right before it')


