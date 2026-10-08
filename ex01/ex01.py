import numpy as np
import pandas as pd

index = [1, 3, 5, 7, 9]
colors = ["Blue", "Red", "Pink", "Grey", "Black"]
lists = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
numbers = [1.1, 2.2, 3.3, 4.4, 5.5]

#using numpy array
array = np.empty((5,3), dtype=object)
array[:, 0] = colors
array[:,1] = lists
array[:, 2] = numbers

df_from_array = pd.DataFrame(array, index=index, columns=["Color", "List", "Number"])

#using pandas series
df_from_series = pd.DataFrame({
    "Color": pd.Series(colors, index=index),
    "List": pd.Series(lists, index=index),
    "Number": pd.Series(numbers, index=index)
})

for name, df in [("from NumPy array", df_from_array), ("from Series", df_from_series)]:
    print(f"--- DataFrame {name} ---")
    print(df)
    print("\nColumn dtypes:")
    print(df.dtypes)
    print("\nType of the first value of each column:")
    print(df.apply(lambda col: type(col.iloc[0])))
    print()