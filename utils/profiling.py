# utils/profiling.py

import pandas as pd

def profile_dataframe(df: pd.DataFrame):
    profile = []
    warnings = []

    for col in df.columns:
        data = df[col]
        stats = {
            "column": col,
            "dtype": data.dtype.name,
            "null_pct": round(data.isnull().mean() * 100, 2),
            "unique": data.nunique(dropna=True),
        }

        # Top value and frequency for categorical
        if data.dtype == 'object':
            top_val = data.mode().iloc[0] if not data.mode().empty else None
            stats["top"] = top_val
            stats["top_freq"] = data.value_counts().get(top_val, 0)
        elif pd.api.types.is_numeric_dtype(data):
            stats["min"] = data.min()
            stats["max"] = data.max()
            stats["mean"] = round(data.mean(), 2)

            # Outlier detection using IQR
            q1 = data.quantile(0.25)
            q3 = data.quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = data[(data < lower_bound) | (data > upper_bound)]
            stats["outliers_count"] = len(outliers)

            if len(outliers) > 0:
                warnings.append(
                    f"!!!!Column `{col}` has {len(outliers)} outlier(s) detected by IQR method."
                )

        profile.append(stats)

        # Warnings
        if stats["null_pct"] > 95:
            warnings.append(f"Column `{col}` has more than 95% nulls.")

        if stats["unique"] <= 1:
            warnings.append(f"Column `{col}` has only {stats['unique']} unique value(s).")

        if pd.api.types.is_numeric_dtype(data) and stats.get("min") == stats.get("max"):
            warnings.append(f" Column `{col}` has no variance — all numeric values are the same.")

    # Count duplicate rows
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        warnings.append(f"There are {dup_count} duplicate row(s) in the dataset.")

    return pd.DataFrame(profile), warnings
