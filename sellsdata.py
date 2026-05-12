"""
Sales Data Analysis Tool
========================
Professional sales data analysis tool for automated reporting, charts, and business intelligence.

Author: Data Analyst
Version: 1.0
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import Dict


def get_sample_data() -> Dict:
    """
    Returns sample sales data for demonstration.

    Returns:
        Dict: Example sales dataset
    """
    return {
        'Date': ['2024-01-15', '2024-01-16', '2024-02-10', '2024-02-15', '2024-03-05'],
        'Customer': ['John', 'Maria', 'Pedro', 'Maria', 'John'],
        'Product': ['Shampoo', 'Sunscreen', 'Face Soap', 'Shampoo', 'Sunscreen'],
        'Category': ['Personal Care', 'Skin Care', 'Skin Care', 'Personal Care', 'Skin Care'],
        'Quantity': [2, 1, 3, 2, 1],
        'Unit Price': [45, 120, 60, 45, 120]
    }


def load_data(file_path: str = None) -> pd.DataFrame:
    """
    Load sales data from a CSV or Excel file, or use sample data.

    Args:
        file_path (str, optional): Path to CSV or Excel file. If None, sample data is used.

    Returns:
        pd.DataFrame: Sales dataset

    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file format is unsupported or cannot be parsed
    """
    try:
        if file_path and os.path.exists(file_path):
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file_path)
            else:
                raise ValueError("Unsupported file format. Please use CSV or Excel.")
            print(f"✓ Data loaded from: {file_path}")
        else:
            df = pd.DataFrame(get_sample_data())
            print("✓ Using sample data")

        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"Error loading data: {str(e)}")


def calculate_totals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total sales for each row.

    Args:
        df (pd.DataFrame): Sales dataset

    Returns:
        pd.DataFrame: Dataset with Total Sales column
    """
    df['Total Sales'] = df['Quantity'] * df['Unit Price']
    return df


def prepare_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the Date column to datetime and extract the month name.

    Args:
        df (pd.DataFrame): Sales dataset

    Returns:
        pd.DataFrame: Dataset with Month column
    """
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month_name()
    return df


def generate_analysis(df: pd.DataFrame) -> Dict:
    """
    Generate sales analysis tables by dimension.

    Args:
        df (pd.DataFrame): Sales dataset

    Returns:
        Dict: Analysis tables for products, customers, categories, and months
    """
    analysis = {
        'products': df.groupby('Product')['Quantity'].sum().sort_values(ascending=False),
        'customers': df.groupby('Customer')['Total Sales'].sum().sort_values(ascending=False),
        'categories': df.groupby('Category')['Total Sales'].sum().sort_values(ascending=False),
        'monthly_sales': df.groupby('Month')['Total Sales'].sum()
    }
    return analysis


def print_analysis(df: pd.DataFrame, analysis: Dict) -> None:
    """
    Print the sales analysis results.

    Args:
        df (pd.DataFrame): Sales dataset
        analysis (Dict): Analysis tables
    """
    print("\n" + "="*60)
    print("SALES DATA")
    print("="*60)
    print(df.to_string(index=False))

    print("\n" + "="*60)
    print("PRODUCT ANALYSIS")
    print("="*60)
    print(analysis['products'])

    print("\n" + "="*60)
    print("CUSTOMER ANALYSIS")
    print("="*60)
    print(analysis['customers'])

    print("\n" + "="*60)
    print("CATEGORY ANALYSIS")
    print("="*60)
    print(analysis['categories'])

    print("\n" + "="*60)
    print("SALES BY MONTH")
    print("="*60)
    print(analysis['monthly_sales'])


def create_visualizations(analysis: Dict, output_folder: str = 'charts') -> None:
    """
    Create and save sales visualizations.

    Args:
        analysis (Dict): Analysis tables
        output_folder (str): Folder to save charts
    """
    os.makedirs(output_folder, exist_ok=True)

    plt.figure(figsize=(10, 6))
    analysis['products'].plot(kind='bar', color='steelblue')
    plt.title('Top Products', fontsize=14, fontweight='bold')
    plt.xlabel('Product', fontsize=12)
    plt.ylabel('Quantity', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, '01_products_sold.png'), dpi=300)
    print(f"✓ Chart saved: {output_folder}/01_products_sold.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    analysis['customers'].plot(kind='bar', color='coral')
    plt.title('Customer Revenue', fontsize=14, fontweight='bold')
    plt.xlabel('Customer', fontsize=12)
    plt.ylabel('Revenue (Q)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, '02_customer_revenue.png'), dpi=300)
    print(f"✓ Chart saved: {output_folder}/02_customer_revenue.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    analysis['categories'].plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Revenue by Category', fontsize=14, fontweight='bold')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, '03_category_share.png'), dpi=300)
    print(f"✓ Chart saved: {output_folder}/03_category_share.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    analysis['monthly_sales'].plot(kind='line', marker='o', color='green', linewidth=2)
    plt.title('Monthly Sales', fontsize=14, fontweight='bold')
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Sales (Q)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, '04_monthly_sales.png'), dpi=300)
    print(f"✓ Chart saved: {output_folder}/04_monthly_sales.png")
    plt.close()


def export_to_excel(df: pd.DataFrame, analysis: Dict, output_file: str = 'sales_report.xlsx') -> None:
    """
    Export analysis to a multi-sheet Excel report.

    Args:
        df (pd.DataFrame): Sales dataset
        analysis (Dict): Analysis tables
        output_file (str): Output Excel filename
    """
    try:
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Original Data', index=False)
            analysis['products'].to_excel(writer, sheet_name='Products')
            analysis['customers'].to_excel(writer, sheet_name='Customers')
            analysis['categories'].to_excel(writer, sheet_name='Categories')
            analysis['monthly_sales'].to_excel(writer, sheet_name='Monthly Sales')
        print(f"✓ Excel report saved: {output_file}")
    except Exception as e:
        print(f"✗ Error saving Excel: {str(e)}")


def generate_summary(df: pd.DataFrame, analysis: Dict, output_file: str = 'executive_summary.txt') -> str:
    """
    Generate an executive summary text file.

    Args:
        df (pd.DataFrame): Sales dataset
        analysis (Dict): Analysis tables
        output_file (str): Output summary filename

    Returns:
        str: Summary text
    """
    total_sales = df['Total Sales'].sum()
    top_product = analysis['products'].idxmax()
    top_customer = analysis['customers'].idxmax()
    top_category = analysis['categories'].idxmax()

    summary = f"""
{'='*70}
EXECUTIVE SUMMARY
{'='*70}

KEY METRICS
{'-'*70}
• Top product: {top_product}
• Top customer: {top_customer}
• Top category: {top_category}
• Total sales: Q{total_sales:,.2f}
• Transactions: {len(df)}
• Average per transaction: Q{df['Total Sales'].mean():,.2f}

TOP 3 CUSTOMERS BY REVENUE
{'-'*70}
{analysis['customers'].head(3).to_string()}

TOP 3 PRODUCTS BY QUANTITY
{'-'*70}
{analysis['products'].head(3).to_string()}

{'='*70}
"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"✓ Executive summary saved: {output_file}")
    except Exception as e:
        print(f"✗ Error saving summary: {str(e)}")
    return summary


def main(data_file: str = None) -> None:
    """
    Main workflow for sales analysis.

    Args:
        data_file (str, optional): Path to the data file. If None, uses sample data.
    """
    print("\n🚀 Starting sales analysis...\n")
    try:
        df = load_data(data_file)
        df = calculate_totals(df)
        df = prepare_dates(df)
        analysis = generate_analysis(df)
        print_analysis(df, analysis)
        print("\n📈 Creating charts...")
        create_visualizations(analysis)
        print("\n📊 Exporting Excel report...")
        export_to_excel(df, analysis)
        print("\n📄 Generating executive summary...")
        summary = generate_summary(df, analysis)
        print(summary)
        print("\n✅ Analysis completed successfully!\n")
    except Exception as e:
        print(f"\n❌ Analysis error: {str(e)}\n")


if __name__ == "__main__":
    main()

    # Uncomment to use your own file:
    # main('path/to/your/file.csv')
