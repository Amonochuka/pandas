from pathlib import Path

import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).parent / "data" / "iris.csv"

# False: follow the exercise literally.
# True : also treat impossible values (negative or 10 and above) as missing.
CLEAN_IMPOSSIBLE = False

df = pd.read_csv(DATA_PATH)

# Bonus: find the special row (this must happen before dropping "flower")
valid_flowers = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
special_row = df[~df["flower"].isin(valid_flowers)]
print("Special row:")
print(special_row)

# Preliminary: drop the flower column
df = df.drop(columns="flower")

# Some columns were loaded as text because of junk entries. Convert them to
# numbers: anything that is not a number becomes NaN (missing).
df = df.apply(pd.to_numeric, errors="coerce")

if CLEAN_IMPOSSIBLE:
    df = df.mask((df < 0) | (df >= 10), np.nan)

print("\nMissing values per column:")
print(df.isna().sum())

# 1. A different strategy for each column
fill_values = {
    "sepal_length": df["sepal_length"].mean(),
    "sepal_width": df["sepal_width"].median(),
    "petal_length": 0,
    "petal_width": 0,
}
print("\nFill values:", fill_values)
filled_by_strategy = df.fillna(fill_values)
print(filled_by_strategy.isna().sum().sum(), "missing values left")
print(filled_by_strategy.head(12))

# 2. Fill every column with its own median
filled_by_median = df.fillna(df.median())
print(filled_by_median.isna().sum().sum(), "missing values left")
print(filled_by_median.head(12))