# Diligent Assessment

This project contains:
- Synthetic e‑commerce CSV datasets
- SQLite ingestion script
- SQL analysis query
- Fully ready to push to GitHub

## How to Run

### 1. Install Python 3.x  
Ensure Python works:  
```
python --version
```

### 2. Run the ingestion script  
```
python ingest.py
```
This will generate `ecommerce.db`.

### 3. Run the SQL query  
Open `analysis.sql` using any SQLite tool.

### 4. Push to GitHub  
```
git init
git add .
git commit -m "Initial commit"
git remote add origin <your_repo_url>
git push -u origin main
```
