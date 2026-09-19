# Unit 5 · Data Science and Storage

> Choosing the right storage model, and putting data science to work on a real dataset.

## SQL vs NoSQL
- **SQL** — structured, strict schema, ACID; ideal for transactions (banking, finance, inventory). Examples: MySQL, PostgreSQL, SQL Server. Excels at data integrity, consistency, and relationships.
- **NoSQL** — flexible / schema-less; horizontal scaling for unstructured, high-volume, real-time data (social media, IoT, big-data analytics). Examples: MongoDB, Cassandra, Redis.

Choosing between them depends on the business need: strict consistency and structured relationships → SQL; scalability and real-time performance → NoSQL. A bank tracks transactions with high accuracy in SQL, while platforms like Facebook and Twitter manage billions of real-time interactions efficiently in NoSQL.

## Netflix: data science + storage in a recommendation system
Data science lets Netflix collect behaviour data (browsing history, watch time), then machine-learning models study those patterns to produce personalised recommendations. Storage technology (databases, cloud) lets Netflix save and manage that large-scale data with fast, stable access.

**Why NoSQL fits Netflix better than SQL:** user-behaviour logs such as browsing history have variable formats and need flexible schemas, so NoSQL (e.g. Cassandra) stores them cleanly and scales horizontally across servers — something rigid SQL tables struggle with.

## Privacy & ethical concerns
Netflix faces real risks from behaviour analytics: protecting massive sensitive data from leaks, meeting GDPR (with heavy fines for violation), and avoiding surveillance worries. Biased recommendation algorithms can also trap users in narrow content "bubbles".

## Data-analysis reflection: NASA temperature data
The NASA GISTEMP series stores data in a clean, fixed-schema table — `int64` years and `float64` temperature anomalies. That structure maps naturally onto SQL: strict types, `ACID`, and aggregate functions such as `AVG` / `CORR` / `GROUP BY` directly mirror the Pandas steps. NoSQL would only win if the data grew semi-structured or needed massive horizontal scaling.

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
