from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parent / "data" / "Ecommerce_purchases.txt"

df = pd.read_csv(DATA_PATH)

# Check the columns and types first
print(df.columns.tolist())
df.info()

price = df["Purchase Price"]

# 1. Rows and columns
rows, columns = df.shape
print(f"1. {rows} rows and {columns} columns")

# 2. Average purchase price
print("2. Average purchase price:", price.mean())

# 3. Highest and lowest purchase prices
print("3. Highest:", price.max(), "| Lowest:", price.min())

# 4. People who chose English ('en')
print("4. Language 'en':", (df["Language"] == "en").sum())

# 5. People with the job title "Lawyer"
print("5. Lawyers:", (df["Job"] == "Lawyer").sum())

# 6. Purchases made in the AM and in the PM
print("6. AM / PM:")
print(df["AM or PM"].value_counts())

# 7. The 5 most common job titles
print("7. Top 5 job titles:")
print(df["Job"].value_counts().head(5))

# 8. Purchase price for Lot "90 WT"
print('8. Price for Lot "90 WT":')
print(df.loc[df["Lot"] == "90 WT", "Purchase Price"])

# 9. Email of the person with this credit card number
print("9. Email for card 4926535242672853:")
print(df.loc[df["Credit Card"] == 4926535242672853, "Email"])

# 10. American Express users with a purchase above $95
amex_over_95 = (df["CC Provider"] == "American Express") & (price > 95)
print("10. American Express and price > 95:", amex_over_95.sum())

# 11. Credit cards that expire in 2025 (dates look like MM/YY)
print("11. Cards expiring in 2025:", (df["CC Exp Date"].str[-2:] == "25").sum())

# 12. Top 5 email hosts
print("12. Top 5 email hosts:")
print(df["Email"].str.split("@").str[1].value_counts().head(5))