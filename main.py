# main.py

import pandas as pd
from tabulate import tabulate
from utils.profiling import profile_dataframe
import sys

filename = sys.argv[1]  # Pass CSV filename as argument
df = pd.read_csv(filename)

summary_df, warnings = profile_dataframe(df)

print(tabulate(summary_df, headers='keys', tablefmt='github'))

with open("reports/sample_report.md", "w", encoding="utf-8") as f:
    f.write("# Data Audit Report: sample.csv\n\n")
    f.write("## Column Summary\n\n")
    f.write(tabulate(summary_df, headers='keys', tablefmt='github'))
    f.write("\n\n## Warnings\n\n")
    if warnings:
        for w in warnings:
            f.write(f"- {w}\n")
    else:
        f.write("No major issues detected.\n")

with open("reports/sample_report.md", "r", encoding="utf-8") as md_file:
    md_content = md_file.read()

