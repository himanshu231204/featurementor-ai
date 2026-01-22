import pandas as pd


def profile_data(df, target_column=None):
    """
    Profiles dataset columns for feature engineering.
    Target column is skipped completely.
    """

    profile = []

    for col in df.columns:
        # ✅ SKIP TARGET COLUMN
        if target_column and col == target_column:
            continue

        col_data = df[col]
        is_numeric = pd.api.types.is_numeric_dtype(col_data)

        profile.append({
            "column": col,
            "dtype": str(col_data.dtype),
            "missing_percent": round(col_data.isna().mean() * 100, 2),
            "unique_values": col_data.nunique(),
            "skewness": col_data.skew() if is_numeric else None,
            "is_numeric": is_numeric,
            "total_rows": len(df)
        })

    return profile

"""
Missing % → imputation/drop decision

Skewness → log/boxcox

Unique count → encoding decision
"""