# Week 6 assignment

## Create DB (only execute first time)
```bash
mysql -u root -p < schema.sql


```
## How to start
```bash
cd backend
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

