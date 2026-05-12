# Sales Data Analysis Tool 📊

Professional sales data analysis tool for automated reporting, charts, and business insights.

## 🎯 Features

✅ **Complete analysis**
- Analysis by product, customer, category, and month
- Automatic total and aggregation calculations
- Top performers identification (Top 3)

✅ **Professional visualizations**
- Bar charts, pie charts, and line charts
- Export in high resolution (300 DPI)
- Dedicated output folder for generated charts

✅ **Automated reporting**
- Excel export with multiple sheets
- Executive summary with key performance indicators
- Clear and professional documentation

✅ **Modular, reusable code**
- Well-structured functions
- Robust error handling
- Type hints for better maintainability

## 📋 Requirements

```bash
pandas>=1.3.0
matplotlib>=3.4.0
openpyxl>=3.6.0
```

### Install dependencies

```bash
pip install pandas matplotlib openpyxl
```

## 🚀 Usage

### Option 1: Use sample data

```bash
python sellsdata.py
```

### Option 2: Analyze your own file

Open `sellsdata.py` and update the last line:

```python
# For a CSV file
main('path/to/your/file.csv')

# For an Excel file
main('path/to/your/file.xlsx')
```

Required columns:
- `Date`
- `Customer`
- `Product`
- `Category`
- `Quantity`
- `Unit Price`

Date format: `YYYY-MM-DD`

## 📁 Generated Files

After running the analysis, the following files are generated:

```
├── charts/                          # Folder with generated charts
│   ├── 01_products_sold.png
│   ├── 02_customer_revenue.png
│   ├── 03_category_share.png
│   └── 04_monthly_sales.png
├── sales_report.xlsx                # Professional Excel report
└── executive_summary.txt            # Executive summary
```

## 📊 Code Structure

| Function | Description |
|---------|------------|
| `load_data()` | Loads input data from file or uses sample data |
| `calculate_totals()` | Calculates total sales for each row |
| `prepare_dates()` | Converts dates and extracts the month |
| `generate_analysis()` | Builds analysis tables by product, customer, category, and month |
| `print_analysis()` | Prints analysis results to the console |
| `create_visualizations()` | Creates professional charts |
| `export_to_excel()` | Exports analysis to Excel |
| `generate_summary()` | Generates an executive summary |
| `main()` | Runs the complete workflow |

## 💡 Usage Example

```python
from sellsdata import load_data, calculate_totals, generate_analysis

# Load data
df = load_data('my_data.csv')

# Process
df = calculate_totals(df)

df = prepare_dates(df)

# Analyze
analysis = generate_analysis(df)

# Use results
print(f"Top product: {analysis['products'].idxmax()}")
```

## 🔍 Advanced Functionality

### Error handling

The code includes robust exception handling:
- File validation
- Processing error capture
- Clear error messages

### Well-formatted output

- Emojis for readability
- Visual separators in output
- Currency formatting in reports

### Flexibility

- Supports CSV and Excel input
- Works with different data structures
- Automatically creates output folders

## 📈 Generated Metrics

**Key metrics:**
- Top selling product
- Top customer by revenue
- Category with highest revenue
- Total sales
- Average sales per transaction
- Number of transactions

## 🛠️ Customization

### Change chart styles

Edit the `create_visualizations()` function to modify:
- Colors
- Layout
- Chart size
- Resolution

### Add new metrics

```python
def calculate_custom_metric(df):
    """Calculate a custom metric."""
    result = df.groupby('Category').agg({'Total Sales': 'sum'})
    return result
```

## ⚠️ Important Notes

- Dates must be in `YYYY-MM-DD` format
- Column names must match exactly
- Quantity and Unit Price should be numeric
- The script auto-creates the output folder

## 📞 Support

If you have issues, verify:
1. Dependencies are installed
2. Input file format is correct
3. Write permissions are available

## 📝 License

This code is available for personal and commercial use.

---

**Version:** 1.0  
**Last updated:** 2026-05-11  
**Status:** ✅ Production
