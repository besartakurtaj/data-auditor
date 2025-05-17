# Data Audit Report: sample.csv

## Column Summary

|    | column   | dtype   |   null_pct |   unique | top    |   top_freq |   min |   max |     mean |   outliers_count |
|----|----------|---------|------------|----------|--------|------------|-------|-------|----------|------------------|
|  0 | name     | object  |       0    |        6 | Alice  |          1 |   nan |   nan |   nan    |              nan |
|  1 | age      | int64   |       0    |        4 | nan    |        nan |    28 |    99 |    43.67 |                1 |
|  2 | gender   | object  |       0    |        2 | Female |          3 |   nan |   nan |   nan    |              nan |
|  3 | income   | float64 |      33.33 |        2 | nan    |        nan | 70000 | 80000 | 72500    |                1 |
|  4 | status   | object  |       0    |        2 | Active |          5 |   nan |   nan |   nan    |              nan |

## Warnings

- !!!!Column `age` has 1 outlier(s) detected by IQR method.
- !!!!Column `income` has 1 outlier(s) detected by IQR method.
