"""
Configuration settings for Sales Data Analysis Tool
"""

# Folder configuration
CHARTS_FOLDER = 'charts'
OUTPUT_EXCEL = 'sales_report.xlsx'
OUTPUT_SUMMARY = 'executive_summary.txt'

# Plot configuration
GRAPH_DPI = 300
GRAPH_FIGSIZE = (10, 6)
GRAPH_COLORS = {
    'products': 'steelblue',
    'customers': 'coral',
    'categories': 'lightblue',
    'monthly_sales': 'green'
}

# Excel configuration
EXCEL_ENGINE = 'openpyxl'

# Currency symbol
CURRENCY_SYMBOL = 'Q'

# Language setting for month names
LANGUAGE = 'en'
