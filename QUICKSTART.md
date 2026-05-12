# Quickstart - Sales Data Analysis Tool

## 3 steps to start

### Step 1: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run with sample data
```bash
python sellsdata.py
```

### Step 3: Review results
- 📊 Charts in: `charts/`
- 📈 Excel report: `sales_report.xlsx`
- 📄 Summary: `executive_summary.txt`

---

## Using your own file

### Option A: Command line
Edit the last line of `sellsdata.py`:

```python
main('path/to/your/file.csv')
```

Then run:
```bash
python sellsdata.py
```

### Option B: Python import

```python
from sellsdata import load_data, calculate_totals, generate_analysis

df = load_data('your_file.csv')
df = calculate_totals(df)
analysis = generate_analysis(df)
```

---

## Required file format

Your CSV/Excel file must include these columns:

| Column | Type | Example |
|--------|------|---------|
| Date | Text (YYYY-MM-DD) | 2024-01-15 |
| Customer | Text | John |
| Product | Text | Shampoo |
| Category | Text | Personal Care |
| Quantity | Number | 2 |
| Unit Price | Number | 45 |

### Example CSV:
```csv
Date,Customer,Product,Category,Quantity,Unit Price
2024-01-15,John,Shampoo,Personal Care,2,45
2024-01-16,Maria,Sunscreen,Skin Care,1,120
```

---

## What you will get

✅ Analysis by: Product | Customer | Category | Month  
✅ 4 professional PNG charts  
✅ Multi-sheet Excel report  
✅ Executive summary with KPIs  
✅ Fully automated workflow

---

## Advanced examples

```bash
python examples.py
```

---

## Common issues

**Issue: File not found**  
Solution: Check the path and file name.

**Issue: Column error**  
Solution: Verify the exact column names.

**Issue: Import error**  
Solution: Run `pip install -r requirements.txt`

---

## Support
See `README.md` for more details.
