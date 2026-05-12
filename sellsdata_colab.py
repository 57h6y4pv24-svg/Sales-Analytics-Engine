"""
Sales Data Analysis Tool - Google Colab Version
================================================
Professional sales data analysis tool for Google Colab.
Generates reports, charts, and summary files.

Version: 1.0 (Colab)
"""

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files
import os
from typing import Dict


def get_sample_data() -> Dict:
    """Return sample sales data for demonstration."""
    return {
        'Date': ['2024-01-15', '2024-01-16', '2024-02-10', '2024-02-15', '2024-03-05'],
        'Customer': ['John', 'Maria', 'Pedro', 'Maria', 'John'],
        'Product': ['Shampoo', 'Sunscreen', 'Face Soap', 'Shampoo', 'Sunscreen'],
        'Category': ['Personal Care', 'Skin Care', 'Skin Care', 'Personal Care', 'Skin Care'],
        'Quantity': [2, 1, 3, 2, 1],
        'Unit Price': [45, 120, 60, 45, 120]
    }


def load_colab_file() -> pd.DataFrame:
    """Upload a CSV or Excel file in Colab or use sample data."""
    print("Do you want to upload your own file? If not, the sample dataset will be used.\n")
    try:
        print("📁 Upload a CSV or Excel file")
        print("   (Or cancel to use sample data)\n")
        uploaded = files.upload()
        if uploaded:
            filename = list(uploaded.keys())[0]
            if filename.endswith('.csv'):
                df = pd.read_csv(filename)
            elif filename.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(filename)
            else:
                raise ValueError("Unsupported format. Please upload CSV or Excel.")
            print(f"✓ File '{filename}' uploaded successfully\n")
            return df
    except Exception:
        pass
    df = pd.DataFrame(get_sample_data())
    print("✓ Using sample data\n")
    return df


def calculate_totals(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate total sales for each row."""
    df['Total Sales'] = df['Quantity'] * df['Unit Price']
    return df


def prepare_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Convert dates and extract the month name."""
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month_name()
    return df


def generate_analysis(df: pd.DataFrame) -> Dict:
    """Generate analysis tables from sales data."""
    return {
        'products': df.groupby('Product')['Quantity'].sum().sort_values(ascending=False),
        'customers': df.groupby('Customer')['Total Sales'].sum().sort_values(ascending=False),
        'categories': df.groupby('Category')['Total Sales'].sum().sort_values(ascending=False),
        'monthly_sales': df.groupby('Month')['Total Sales'].sum()
    }


def print_analysis(df: pd.DataFrame, analysis: Dict) -> None:
    """Print the sales analysis results."""
    print("\n" + "="*70)
    print("📊 SALES DATA")
    print("="*70)
    print(df.to_string(index=False))

    print("\n" + "="*70)
    print("🏆 TOP PRODUCTS")
    print("="*70)
    print(analysis['products'])

    print("\n" + "="*70)
    print("👥 TOP CUSTOMERS")
    print("="*70)
    print(analysis['customers'])

    print("\n" + "="*70)
    print("📂 CATEGORY REVENUE")
    print("="*70)
    print(analysis['categories'])


def create_charts(analysis: Dict) -> None:
    """Create and save charts in Colab."""
    print("\n📈 Generating charts...\n")

    plt.figure(figsize=(12, 6))
    analysis['products'].plot(kind='bar', color='steelblue')
    plt.title('Top Products', fontsize=14, fontweight='bold')
    plt.xlabel('Product', fontsize=12)
    plt.ylabel('Quantity', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('01_products_sold.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✓ Chart 1 saved")

    plt.figure(figsize=(12, 6))
    analysis['customers'].plot(kind='bar', color='coral')
    plt.title('Customer Revenue', fontsize=14, fontweight='bold')
    plt.xlabel('Customer', fontsize=12)
    plt.ylabel('Revenue (Q)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('02_customer_revenue.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✓ Chart 2 saved")

    plt.figure(figsize=(12, 8))
    analysis['categories'].plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Revenue by Category', fontsize=14, fontweight='bold')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('03_category_share.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✓ Chart 3 saved")

    plt.figure(figsize=(12, 6))
    analysis['monthly_sales'].plot(kind='line', marker='o', color='green', linewidth=2)
    plt.title('Monthly Sales', fontsize=14, fontweight='bold')
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Sales (Q)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('04_monthly_sales.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✓ Chart 4 saved")


def export_to_excel(df: pd.DataFrame, analysis: Dict) -> str:
    """Export all analysis data to Excel."""
    filename = 'sales_report.xlsx'
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Original Data', index=False)
        analysis['products'].to_excel(writer, sheet_name='Products')
        analysis['customers'].to_excel(writer, sheet_name='Customers')
        analysis['categories'].to_excel(writer, sheet_name='Categories')
        analysis['monthly_sales'].to_excel(writer, sheet_name='Monthly Sales')
    print(f"✓ Excel file created: {filename}")
    return filename


def generate_summary(df: pd.DataFrame, analysis: Dict) -> str:
    """Generate an executive summary file."""
    total_sales = df['Total Sales'].sum()
    summary = f"""
{'='*70}
EXECUTIVE SUMMARY
{'='*70}

Top product: {analysis['products'].idxmax()}
Top customer: {analysis['customers'].idxmax()}
Top category: {analysis['categories'].idxmax()}
Total sales: Q{total_sales:,.2f}
Number of transactions: {len(df)}

{'='*70}
"""
    with open('executive_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)
    print("✓ Executive summary saved")
    return summary


def download_files() -> None:
    """Download all generated files in Colab."""
    print("\n" + "="*60)
    print("📥 DOWNLOADING FILES")
    print("="*60)
    files.download('sales_report.xlsx')
    files.download('executive_summary.txt')
    files.download('01_products_sold.png')
    files.download('02_customer_revenue.png')
    files.download('03_category_share.png')
    files.download('04_monthly_sales.png')


print("\n" + "="*70)
print("🎯 SALES DATA ANALYSIS TOOL - GOOGLE COLAB")
print("="*70 + "\n")

sales_df = load_colab_file()
sales_df = calculate_totals(sales_df)
sales_df = prepare_dates(sales_df)
cols = generate_analysis(sales_df)
print_analysis(sales_df, cols)
create_charts(cols)
export_to_excel(sales_df, cols)
generate_summary(sales_df, cols)
download_files()
