import pandas as pd

# Try semicolon first
df = pd.read_csv("books_cleaned.csv", sep=';', on_bad_lines='skip', encoding='utf-8-sig')

# If that doesn't work, try tab
# df = pd.read_csv("books_cleaned.csv", sep='\t')

# Clean up the columns immediately
df.columns = df.columns.str.strip().str.replace('"', '')
print("Columns detected:", df.columns.tolist())