# CUSTOMER SALES ANALYSIS REPORT

## 1. Project Overview

### Objective

The objective of this project is to analyze customer purchasing behavior, sales performance, and customer churn using Python and Pandas. The analysis helps identify top customers, sales trends, regional performance, and customer retention opportunities to support business decision-making.

---

## 2. Dataset Description

### Sales Dataset

The sales dataset contains transaction records including sales date, product information, quantity sold, customer ID, region, and total sales amount.

### Customer Churn Dataset

The customer churn dataset contains customer information including tenure, monthly charges, total charges, contract type, payment method, and churn status.

---

## 3. Data Cleaning and Preparation

The following preprocessing steps were performed:

* Loaded datasets using Pandas.
* Checked for missing values.
* Converted Date column into datetime format.
* Extracted Year, Month, and Day from transaction dates.
* Standardized text fields where necessary.
* Created calculated columns for analysis.
* Validated data types and corrected inconsistencies.

---

## 4. Customer Analysis

### Top Customers

Customers were ranked based on their total spending.

#### Findings

* Identified the top 10 customers contributing the highest revenue.
* A small percentage of customers generated a significant portion of total sales.
* High-value customers can be targeted for loyalty programs and personalized offers.

### Customer Lifetime Value

Customer lifetime value was estimated using total spending.

#### Findings

* Long-term customers generated higher revenue.
* Customers with higher tenure generally showed increased profitability.

---

## 5. Sales Performance Analysis

### Monthly Sales Trends

Sales were grouped by month to identify seasonal patterns and business growth trends.

#### Findings

* Certain months showed significantly higher sales volumes.
* Seasonal fluctuations indicate opportunities for promotional campaigns during low-performing periods.

### Product Performance

Products were analyzed based on sales quantity and revenue contribution.

#### Findings

* Top-selling products contributed the majority of total revenue.
* Some products generated high revenue despite lower sales volume due to higher pricing.

---

## 6. Regional Sales Analysis

Sales were analyzed across different geographic regions.

#### Findings

* Certain regions consistently outperformed others.
* High-performing regions present opportunities for expansion.
* Low-performing regions may require targeted marketing efforts.

---

## 7. Customer Churn Analysis

Customer churn was analyzed using contract types and customer behavior.

### Findings

* Customers with long-term contracts showed lower churn rates.
* Month-to-month customers had a higher probability of leaving.
* Customers with higher tenure demonstrated stronger retention.

### Churn Rate

Overall churn rate was calculated using customer records and used as a key retention metric.

---

## 8. Advanced Analysis

### Data Filtering

Multiple conditions were used to identify specific customer segments and sales patterns.

### Data Merging

Sales data and customer data were merged to create a unified customer view.

### Pivot Table Analysis

Pivot tables were used to summarize revenue by region and product category.

#### Benefits

* Quick comparison of product performance.
* Better understanding of regional demand.
* Easier identification of business opportunities.

---

## 9. Dashboard Visualizations

The dashboard includes:

1. Monthly Sales Trend (Line Chart)
2. Product Performance Analysis (Bar Chart)
3. Regional Sales Distribution (Pie Chart)
4. Customer Churn Distribution (Bar Chart)
5. Contract-wise Churn Analysis (Bar Chart)

These visualizations provide an intuitive understanding of business performance.

---

## 10. Key Business Metrics

### Total Revenue

Calculated as the sum of all sales transactions.

### Total Customers

Unique customers identified in the sales dataset.

### Average Order Value

Average revenue generated per transaction.

### Customer Churn Rate

Percentage of customers who discontinued services.

---

## 11. Business Insights

### Insight 1

A small group of customers contributes a large percentage of total revenue.

### Insight 2

Some products consistently outperform others and should receive priority in inventory planning.

### Insight 3

Sales performance varies significantly across regions.

### Insight 4

Customer churn is strongly related to contract type and customer tenure.

### Insight 5

Seasonal sales patterns can be leveraged for targeted marketing campaigns.

---

## 12. Recommendations

### Customer Retention

* Introduce loyalty and rewards programs.
* Offer personalized discounts to high-value customers.
* Improve customer support and engagement.

### Sales Growth

* Increase inventory for high-demand products.
* Launch promotional campaigns during low-sales periods.
* Expand operations in high-performing regions.

### Churn Reduction

* Encourage customers to move to long-term contracts.
* Provide incentives for customer renewal.
* Identify at-risk customers early using predictive analytics.

---

## 13. Conclusion

The Customer Sales Analysis project successfully identified customer purchasing patterns, sales trends, product performance, regional strengths, and churn behavior. The findings provide actionable business insights that can improve customer retention, increase revenue, and support strategic decision-making.
