# Data Audit Tool
A Python tool for profiling datasets and checking data quality.

## Overview
This project helps you quickly understand your data by:

```Checking for missing values, duplicates, and data types

Summarizing unique values and common values per column

Detecting outliers using the Interquartile Range (IQR) method

Flagging potential data quality issues

Exporting a detailed report in Markdown
```

## What is IQR?
The Interquartile Range (IQR) is a way to find outliers in your numeric data. It measures the range of the middle 50% of values — between the 25th percentile (Q1) and 75th percentile (Q3). Values far outside this range are flagged as outliers.

Outliers are values smaller than Q1 - 1.5 * IQR or larger than Q3 + 1.5 * IQR.

This helps you spot unusual or suspicious data points.

You can find the full explanation and results related to IQR-based outlier detection in the generated Markdown report (reports/sample_report.md).

## How to use
1. Install required packages:
``` pip install -r requirements.txt ```
2. Put your dataset CSV file into the datasets folder
3. Run the tool:
   python main.py datasets/your_dataset.csv
4. Find the report in the reports/ folder
