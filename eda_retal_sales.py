import pandas as pd
df = pd.read_csv("Cleaned_SampleSuperstore.csv")
df.head()
#Basic eda questions 
# top 10 cities by total sales
top_cities = df.groupby('city')['sales'].sum().sort_values(ascending=False).head(10)
print("Top 10 cities by total sales:", top_cities)
#region wise profit
region_profit = df.groupby('region')['profit'].sum()
print("\nRegion wise profit:", region_profit)
#most profitable product category
Most_profitable_category = df.groupby('category')['profit'].sum()
print("\nMost profitable product category:", Most_profitable_category)
#profit per quantity sold 
profit_per_quantity = df['profit']/df['quantity']
print("\n profit per quantity:", profit_per_quantity)