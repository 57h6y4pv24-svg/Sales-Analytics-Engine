# Copy and Paste into Colab

## Cell 1: Install libraries

```python
!pip install pandas matplotlib openpyxl -q
```

## Cell 2: Load data

```python
from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt

# SAMPLE DATA
data = {
    'Date': ['2024-01-15','2024-01-16','2024-02-10','2024-02-15','2024-03-05'],
    'Customer': ['John','Maria','Pedro','Maria','John'],
    'Product': ['Shampoo','Sunscreen','Face Soap','Shampoo','Sunscreen'],
    'Category': ['Personal Care','Skin Care','Skin Care','Personal Care','Skin Care'],
    'Quantity': [2,1,3,2,1],
    'Unit Price': [45,120,60,45,120]
}

df = pd.DataFrame(data)
df['Total Sales'] = df['Quantity'] * df['Unit Price']
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()

print("✓ Data loaded")
print(df)
```

## Cell 3: Analysis

```python
products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
customers = df.groupby('Customer')['Total Sales'].sum().sort_values(ascending=False)
categories = df.groupby('Category')['Total Sales'].sum().sort_values(ascending=False)
monthly_sales = df.groupby('Month')['Total Sales'].sum()

print("="*60)
print("🏆 TOP PRODUCTS")
print("="*60)
print(products)
print("\n" + "="*60)
print("👥 TOP CUSTOMERS")
print("="*60)
print(customers)
print("\n" + "="*60)
print("📂 CATEGORY REVENUE")
print("="*60)
print(categories)
```

## Cell 4: Charts

```python
plt.figure(figsize=(10, 6))
products.plot(kind='bar', color='steelblue')
plt.title('Top Products', fontsize=14, fontweight='bold')
plt.xlabel('Product')
plt.ylabel('Quantity')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('01_products.png', dpi=300)
plt.show()
print("✓ Chart 1 saved")

plt.figure(figsize=(10, 6))
customers.plot(kind='bar', color='coral')
plt.title('Customer Revenue', fontsize=14, fontweight='bold')
plt.xlabel('Customer')
plt.ylabel('Revenue (Q)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('02_customers.png', dpi=300)
plt.show()
print("✓ Chart 2 saved")

plt.figure(figsize=(10, 8))
categories.plot(kind='pie', autopct='%1.1f%%')
plt.title('Revenue by Category', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('03_categories.png', dpi=300)
plt.show()
print("✓ Chart 3 saved")
```

## Cell 5: Create Excel

```python
with pd.ExcelWriter('sales_report.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Data', index=False)
    products.to_excel(writer, sheet_name='Products')
    customers.to_excel(writer, sheet_name='Customers')
    categories.to_excel(writer, sheet_name='Categories')
    monthly_sales.to_excel(writer, sheet_name='Monthly Sales')

print("✓ Excel created: sales_report.xlsx")
```

## Cell 6: Create summary

```python
total_sales = df['Total Sales'].sum()
top_product = products.idxmax()
top_customer = customers.idxmax()
top_category = categories.idxmax()

summary = f"""
{'='*70}
EXECUTIVE SUMMARY
{'='*70}

KEY KPIS
{'-'*70}
Top product: {top_product}
Top customer: {top_customer}
Top category: {top_category}
Total sales: Q{total_sales:,.2f}
Number of transactions: {len(df)}

TOP 3 CUSTOMERS
{'-'*70}
{customers.head(3).to_string()}

TOP 3 PRODUCTS
{'-'*70}
{products.head(3).to_string()}

{'='*70}
"""

print(summary)

with open('executive_summary.txt', 'w', encoding='utf-8') as f:
    f.write(summary)

print("✓ Summary saved")
```

## Cell 7: Download files

```python
from google.colab import files

print("\n" + "="*60)
print("📥 DOWNLOADING FILES...")
print("="*60 + "\n")

files.download('sales_report.xlsx')
print("✓ Excel downloaded")

files.download('executive_summary.txt')
print("✓ Summary downloaded")

files.download('01_products.png')
print("✓ Chart 1 downloaded")

files.download('02_customers.png')
print("✓ Chart 2 downloaded")

files.download('03_categories.png')
print("✓ Chart 3 downloaded")

print("\n✅ DONE! All files downloaded")
```
