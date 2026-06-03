import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

tables = [
    "fund_master",
    "nav_history",
    "scheme_performance",
    "investor_transactions"
]

for table in tables:

    db_rows = pd.read_sql(
        f"SELECT COUNT(*) AS cnt FROM {table}",
        conn
    )["cnt"][0]

    print(table, db_rows)

conn.close()