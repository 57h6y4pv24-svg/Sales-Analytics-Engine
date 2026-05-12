# How to Run the Code on Google Colab

## Option 1: Quick copy and paste

### Step 1: Open Google Colab
https://colab.research.google.com/

### Step 2: Create a new notebook
Create a blank notebook

### Step 3: Paste this code in a cell

```python
# Install dependencies
!pip install pandas matplotlib openpyxl -q

# Paste the full contents of sellsdata_colab.py here
```

### Step 4: Run
- Press `Shift + Enter`
- Upload your CSV file when prompted
- The files will download automatically

---

## Option 2: Professional (GitHub)

### Step 1: Upload code to GitHub
1. Create a repository on GitHub
2. Upload `sellsdata_colab.py`
3. Copy the raw file link

### Step 2: In Colab, use:

```python
!wget https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/sellsdata_colab.py
!pip install pandas matplotlib openpyxl -q
exec(open('sellsdata_colab.py').read())
```

---

## Option 3: Built-in notebook

### Step 1: Create a Colab notebook

```python
!pip install pandas matplotlib openpyxl -q

from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt

print("Upload a CSV or Excel file:")
uploaded = files.upload()
archivo = list(uploaded.keys())[0]

if archivo.endswith('.csv'):
    df = pd.read_csv(archivo)
else:
    df = pd.read_excel(archivo)

# Remaining code here...
```

---

## Files used in Colab

- You can upload a CSV directly
- Or use the provided sample data

---

## Automatic downloads

The Colab code downloads:

- `sales_report.xlsx`
- `executive_summary.txt`
- `01_products.png`
- `02_customers.png`
- `03_categories.png`

---

## Recommendation

Use Option 1 for the fastest setup.
