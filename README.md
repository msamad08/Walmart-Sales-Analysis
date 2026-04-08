# Walmart Sales & Economic Analysis (SQL + Python)

## Overview

This project analyzes Walmart sales data using SQL and Python to identify store performance trends, seasonal patterns, and the impact of external factors such as holidays and economic conditions on retail sales.

## Problem Statement

Retail organizations must understand sales trends and external influences to optimize inventory, staffing, and marketing strategies. This project aims to analyze Walmart’s weekly sales data to uncover key drivers of performance and support data-driven decision-making.

## Dataset

Walmart Weekly Sales Dataset
Features include:

* Store
* Date
* Weekly Sales
* Holiday Flag
* Temperature
* Fuel Price
* CPI (Consumer Price Index)
* Unemployment

## Technologies Used

* Python (Pandas, Matplotlib)
* SQL (SQLite)
* Data Analysis & Visualization

## Project Workflow

1. Data loading and preprocessing
2. SQL database creation using SQLite
3. Exploratory data analysis (EDA)
4. Business-focused SQL queries
5. Time-series analysis
6. Visualization of trends and insights

---

## Business Questions

* Which stores generate the highest total sales?
* How do holidays impact sales performance?
* What are the monthly sales trends?
* How do economic factors influence retail sales?

---

## Key Insights

### 1. Store Performance

Store-level analysis revealed significant variation in performance across locations.

* Store 20 generated the highest total sales (~$301M)
* Store 33 generated the lowest (~$37M)

This indicates strong differences in regional demand and store-level performance.

---

### 2. Holiday Impact

Holiday periods significantly increase sales:

* Non-holiday average: ~$1.04M
* Holiday average: ~$1.12M

This represents a ~7.8% increase, highlighting the importance of seasonal demand.

---

### 3. Seasonal Trends

Time-series analysis shows clear seasonal patterns:

* Peak sales occur in **December (~$288M)**
* Mid-year months (June–July) also show strong performance
* January consistently shows the lowest sales

This reflects predictable consumer behavior and retail cycles.

---

## Visualizations

### Monthly Sales Trend

![Monthly Sales Trend](images/monthly_sales_trend.png)

(Add additional charts such as store performance and holiday comparison here)

---

## Model / Analysis Output

* SQL queries used for aggregation and trend analysis
* Python used for visualization and time-series interpretation

---

## Project Structure

walmart-sales-analysis/
│── data/
│   └── Walmart_Sales.csv
│── sql/
│   └── queries.sql
│── notebooks/
│── images/
│── README.md
│── requirements.txt

---

## How to Run

1. Add dataset to:
   data/Walmart_Sales.csv

2. Run Python script:

```bash
python walmart-sales-analysis.py
```

3. Execute SQL queries using SQLite connection

---

## Future Improvements

* Add Power BI dashboard for interactive visualization
* Perform predictive modeling (sales forecasting)
* Analyze impact of economic indicators (CPI, unemployment) in depth
* Deploy as a data dashboard application

---

## Author

Mohammad Samad
Aspiring Data Scientist | MS Computer Science & Quantitative Methods
