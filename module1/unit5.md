# Unit 5 · Data Science and Storage

**R****eflection comparing two storage models**
 First, SQL - or relational databases - store data in a structured, table-based format. SQL databases follow a strict schema and are best suited for transactional applications such as banking, finance, and inventory management. Examples of SQL databases include MySQL, PostgreSQL, and Microsoft SQL Server. These databases excel at ensuring data integrity, consistency, and relationships between data points.

 Conversely, NoSQL, or non-relational databases, offer more flexibility in storing unstructured or semi-structured data. NoSQL databases are designed for applications that require high scalability and real-time processing, such as social media platforms, IoT applications, and big data analytics. Examples of NoSQL databases include MongoDB, Cassandra, and Redis. These databases support horizontal scaling, meaning they can distribute data across multiple servers, making them ideal for handling large volumes of information. 
A notable example of these storage models in action is the difference between a financial institution and a social media platform. Banks use SQL databases to track customer transactions with high accuracy, while platforms like Facebook and Twitter use NoSQL databases to manage billions of real-time user interactions efficiently. 
Choosing between SQL and NoSQL depends on the specific needs of a business or application. If strict consistency and structured data relationships are required, SQL is the preferred choice. If scalability and real-time performance are more critical, NoSQL provides the flexibility needed for handling massive amounts of data.


How does Netflix use Data Science and storage technologies to enhance its recommendation system?
  Data science allows Netflix to collect information, analyze data, identify customer behavior patterns, and produce practical insights to improve decision-making. It employs big data to collect data from users’ behavior patterns, including browsing history and watch time. Using this data, machine learning models study user behavior to provide personalized recommendations. Storage technology, including databases and cloud systems, allows Netflix to save and manage large‑scale data, supporting fast and stable data access.
Why are NoSQL databases more suited for Netflix’s needs than traditional SQL-based systems?
NoSQL databases fit Netflix better than traditional SQL systems. Firstly, they flexibly store unstructured and semistructured data. Netflix collects user-behavior data like browsing logs, which have variable formats and do not require strict, fixed schemas. NoSQL is better suited for storing Netflix’s various types of data and flexible schemas. Secondly, NoSQL supports horizontal scaling across multiple servers. As Netflix has massive global users, it often needs to distribute heavy workloads. Using multiple servers can spread the load and keep the process efficient. By contrast, SQL relies on rigid tables and struggles with fast largescale expansion. Therefore, NoSQL (e.g. Cassandra) efficiently powers its recommendation engine and lowlatency global services.

What challenges might Netflix face with data privacy and ethical concerns, given its reliance on user behaviour analytics?
Netflix faces several privacy and ethical challenges when analyzing userbehavior data. First, it must protect large volumes of sensitive user activity data from data leaks or unauthorized access. It needs to follow strict regulations such as GDPR, risking heavy fines for violating the rules. Besides, overreliance on behavioral tracking may raise ethical worries about user surveillance. Biased recommendation algorithms are another risk, which could create narrow content bubbles and limit users’ diverse viewing choices

The NASA global temperature dataset use a structured table to store its data with 
fixed columns for year and months. It also uses consistant data type: 
`int64` for whole‑number year values and `float64`for temperature anomaly values.
SQL, use a structured, table-based format, is a natural match to store this type of 
dataset.SQL database such as PostgreSQL enforces strict data types and supports 
ACID transactions. It allows efficient joins—for example, linking annual temperature
records with a separate table of CO₂ emissions by year. SQL's aggregate functions 
including AVG, CORR, GROUP BY decade, directly mirror the Pandas operations used
in this analysis.
Instead,NoSQL stores unstructured or semi-structured data. It offers more flexibility 
if the dataset needs to be expanded.NoSQL allows variable schema which supports nested data, 
arrays and complex objects which do not fit neatly into flat tables.If we added unstructured data 
like images, records,documents,NoSQL would suit it better. NoSQL also scales horizontally 
more easily for high-volume, real-time climate sensor streams.

In conclusion, for this clean, fixed-schema time-series dataset, SQL is the more appropriate choice.
Only if the data grew semi-structured or required massive horizontal scaling,NoSQL would stand out as 
a better choice.

```python
import pandas as pd
import matplotlib.pyplot as plt
url="https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv" #load the data
db=pd.read_csv(url,skiprows=1,na_values="***")
db = db[db["Year"] <= 2025].copy()
print(db.head())

missing_dt=db.isnull().sum() #clean dataset
print("missing data information:",missing_dt)
db=db.fillna(db.mean(numeric_only=True))

db_xy=db[["Year","J-D"]]
print("Overall mean of annual temporature anomalies:",round(db["J-D"].mean(),3))
print("Overall median of annual temperature anomalies:",round(db["J-D"].median(),3))
corr_year_temp=db["Year"].corr(db["J-D"])
print("Correlation between year and temperature:",round(corr_year_temp,3))

plt.figure(figsize=(10,10))
plt.plot(db["Year"],db["J-D"],color="#ff7f0e", linestyle="-",linewidth=1.2)
plt.title("Correlation between year and temperature")
plt.xlabel("Year")
plt.ylabel("Temperature anomalies")
plt.grid(alpha=1)
plt.show()
```
