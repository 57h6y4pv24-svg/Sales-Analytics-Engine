# Colab Instructions

## Step 1: Open Google Colab
Go to: https://colab.research.google.com/

## Step 2: Create a New Notebook
Click "+ NEW NOTEBOOK"

## Step 3: Run the library installation
Paste this code into the first cell:

```python
!pip install pandas matplotlib openpyxl -q
```

Press `Shift + Enter`.

## Step 4: Paste the analysis code

Paste the complete code from `COLAB_COMPLETE_CODE.txt` or `sellsdata_colab.py` into the next cell.

## Step 5: Run the notebook
Press `Shift + Enter`.

## Step 6: Download the files
The notebook will generate and download:
- `sales_report.xlsx`
- `executive_summary.txt`
- `01_products.png`
- `02_customers.png`
- `03_categories.png`

## Using your own file
Replace the sample data section with:

```python
print("Upload your CSV or Excel file:")
uploaded = files.upload()
archivo = list(uploaded.keys())[0]

if archivo.endswith('.csv'):
    df = pd.read_csv(archivo)
else:
    df = pd.read_excel(archivo)
```

Required column names:
- Date
- Customer
- Product
- Category
- Quantity
- Unit Price
