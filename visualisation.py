import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example DataFrame definition (replace with your actual data loading code)
df = pd.read_csv('Cleaned_SampleSuperstore.csv')

# Sales by category
plt.figure(figsize=(6,4))
sns.barplot(data=df, x='category', y='sales')
plt.title("Sales by Category")
plt.show()

# Profit vs Discount
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='discount', y='profit')
plt.title("Profit vs Discount")
plt.show()

# Quantity by Region
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x='region', y='quantity')
plt.title("Quantity Distribution by Region")
plt.show()
