# Unit 5 · Data Science and Storage

> Choosing the right storage model, and putting data science to work on a real dataset.

## Task / Assignment
Compare storage models and show how data science powers a recommendation system.

### SQL vs NoSQL
- **SQL** — structured, strict schema, ACID; ideal for transactions (banking, inventory). Examples: MySQL,
  PostgreSQL, SQL Server.
- **NoSQL** — flexible / schema-less; horizontal scaling for unstructured, high-volume, real-time data
  (social media, IoT, big-data analytics). Examples: MongoDB, Cassandra, Redis.
- **Netflix case** — behavioural logs have variable formats, so NoSQL (e.g. Cassandra) fits far better than
  rigid SQL tables; ML on that data drives personalised recommendations.
- **Risks** — privacy/GDPR exposure, surveillance worries, biased recommendation "bubbles".

### Data-analysis reflection (NASA temperature data)
The NASA GISTEMP series is a clean, fixed-schema time series → **SQL is the natural fit** (strict typing,
joins, `AVG`/`CORR`/`GROUP BY` mirror the Pandas steps). NoSQL would only win if the data grew
semi-structured or needed massive horizontal scaling.

## Code — NASA temperature analysis (`Unit5 data_analysis_reflection.py`)
```python
import pandas as pd
import matplotlib.pyplot as plt

url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
db = pd.read_csv(url, skiprows=1, na_values="***")
db = db[db["Year"] <= 2025].copy()

db = db.fillna(db.mean(numeric_only=True))
db_xy = db[["Year", "J-D"]]
print("Overall mean anomaly:", round(db["J-D"].mean(), 3))
print("Correlation year~temp:", round(db["Year"].corr(db["J-D"]), 3))

plt.figure(figsize=(10, 10))
plt.plot(db["Year"], db["J-D"], color="#ff7f0e", linewidth=1.2)
plt.title("Correlation between year and temperature")
plt.xlabel("Year"); plt.ylabel("Temperature anomalies")
plt.grid(alpha=1); plt.show()
```

## Associated source files
| File | Type | Notes |
|------|------|-------|
| `Unit5 case study.docx` | Word | SQL vs NoSQL comparison + Netflix recommendation case |
| `Unit5 data_analysis_reflection.md` | Markdown | Reflection on why SQL fits the NASA fixed-schema series |
| `Unit5 data_analysis_reflection.py` | Python | Pandas + Matplotlib analysis of year ↔ temperature anomaly |
