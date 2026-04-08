import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Walmart_Sales.csv")

conn = sqlite3.connect("walmart.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Table created successfully")

print(df.columns)

# 1. Total Sales by Store
query = """
SELECT Store, ROUND(SUM(Weekly_Sales), 2) AS total_sales
FROM sales
GROUP BY Store
ORDER BY total_sales DESC;
"""

result = pd.read_sql(query, conn)
print(result)

top10 = result.head(10)

top10.plot(kind="barh", x="Store", y="total_sales")
plt.title("Top 10 Stores by Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Store")
plt.tight_layout()
plt.show()

# 2. Average Sales by Department
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
conn = sqlite3.connect("walmart.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

query = """
SELECT strftime('%Y-%m', Date) AS month,
       ROUND(SUM(Weekly_Sales), 2) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month;
"""

monthly_sales = pd.read_sql(query, conn)
print(monthly_sales)

import matplotlib.pyplot as plt

monthly_sales.plot(x="month", y="monthly_sales", kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# 3. Holiday vs Non-Holiday Sales
query = """
SELECT Holiday_Flag,
       ROUND(AVG(Weekly_Sales), 2) AS avg_sales
FROM sales
GROUP BY Holiday_Flag;
"""

holiday_sales = pd.read_sql(query, conn)
print(holiday_sales)

holiday_sales.plot(kind="bar", x="Holiday_Flag", y="avg_sales")
plt.title("Average Weekly Sales: Holiday vs Non-Holiday")
plt.xlabel("Holiday Flag (1 = Holiday, 0 = Non-Holiday)")
plt.ylabel("Average Weekly Sales")
plt.tight_layout()
plt.show()

# 4. Temperature Impact
query = """
SELECT ROUND(AVG(Temperature), 2) AS avg_temp,
       ROUND(AVG(Weekly_Sales), 2) AS avg_sales
FROM sales;
"""

temp_sales = pd.read_sql(query, conn)
print(temp_sales)

# 5. Unemployment Impact
query = """
SELECT ROUND(AVG(Unemployment), 2) AS avg_unemployment,
       ROUND(AVG(Weekly_Sales), 2) AS avg_sales
FROM sales;
"""

unemp_sales = pd.read_sql(query, conn)
print(unemp_sales)