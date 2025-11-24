week 7 assignment

## Create DB (only execute 1 time)
```bash
mysql -u root -p < schemas.sql
```

## How to start
```bash
cd week7
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```