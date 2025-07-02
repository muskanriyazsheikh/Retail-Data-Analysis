import pandas as pd
import numpy as np
# Load the dataset
df = pd.read_csv("SampleSuperstore.csv")
df.head()
# Check for Shape of the dataset
print("Rows and Columns:",df.shape)
#check Column Names
print("Columns Before cleanup:",df.columns)
#strip spaces and standardized names
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
print("Cleaned Columns:", df.columns)
print(df.dtypes)
print("Column Names:", df.columns)

#check for null values
print(df.isnull().sum())
df = df.dropna()
#check for duplicates
print("Duplicate rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)
df.to_csv("Cleaned_SampleSuperstore.csv", index=False)
print("✅ Cleaned data saved successfully.")
