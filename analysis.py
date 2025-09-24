import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

# Total sales
print("Total Sales:", (df["Quantity"] * df["Price"]).sum())

# Top product
print("Top Product:", df.groupby("Product")["Quantity"].sum().idxmax())

# Sales by product
sales_by_product = df.groupby("Product")["Price"].sum()
print("\nSales by Product:\n", sales_by_product)

# Visualization
sales_by_product.plot(kind="bar", title="Sales by Product")
plt.show()
