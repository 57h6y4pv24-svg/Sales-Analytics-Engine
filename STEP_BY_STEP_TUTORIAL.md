# Step-by-step Tutorial for Google Colab

## Objective
Run the sales analysis tool in Google Colab and download the Excel report.

## Estimated time: 5 minutes

### Step 1: Open Google Colab
1. Open your browser
2. Go to https://colab.research.google.com/
3. Sign in with your Google account if needed

### Step 2: Create a new notebook
1. Click "+ NEW NOTEBOOK"
2. Wait for the blank notebook to open

### Step 3: Install dependencies
In the first cell, paste:

```python
!pip install pandas matplotlib openpyxl -q
```

Press `Shift + Enter`.

### Step 4: Paste the main code
In a new cell, paste the full code from `COLAB_COMPLETE_CODE.txt` or `sellsdata_colab.py`.

Press `Shift + Enter`.

### Step 5: Wait for execution
The notebook will run the analysis and display results.

### Step 6: Download generated files
The notebook will automatically download:
- `sales_report.xlsx`
- `executive_summary.txt`
- `01_products.png`
- `02_customers.png`
- `03_categories.png`

### Step 7: Use your own data
If you want to use your own file, replace the sample data in the code with:

```python
print("Upload your CSV or Excel file:")
uploaded = files.upload()
archivo = list(uploaded.keys())[0]

if archivo.endswith('.csv'):
    df = pd.read_csv(archivo)
else:
    df = pd.read_excel(archivo)
```

Required columns:
- Date
- Customer
- Product
- Category
- Quantity
- Unit Price

### Common issues
- File not found: check your file path
- Column error: check exact column names
- Installation error: run `pip install -r requirements.txt`
