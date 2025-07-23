# Super_store-analysis-using-Python



Project Overview : 
This project analyzes Superstore sales data to uncover patterns in customer behavior, sales trends, and product performance. Tools like Pandas, Numpy, Matplotlib, and Seaborn were used for data cleaning, visualization, and exploratory analysis.
---
Objective :
The primary goals of this analysis include:

Segmenting customers to identify key user groups.

Examining sales trends over time.

Analyzing the performance of products and categories.

Providing actionable recommendations to improve sales and customer retention.
---
#Dataset
The dataset includes the following key features:

Order ID: Unique identifier for each transaction.

Customer Name/ID: Customer information.

Segment: Customer segment (e.g., Consumer, Corporate).

Category: Product categories (Furniture, Technology, etc.).

Sales: Revenue generated.

Order Date: Date of purchase.
Ship Mode: Delivery type.
---
Workflow and Key Steps

# Data Cleaning

#Handling Missing Values:

Replaced missing Postal Code values with 0 and converted it to integer.
---
#Data Deduplication:

Removed duplicate records.
---
2. Exploratory Data Analysis (EDA)
Customer Analysis

#Customer Segmentation:

Segmented customers by types: Consumer, Corporate, Home Office.

Visualized distribution using pie charts.
---
#Sales Analysis

3.Sales per Customer Type:

Calculated total sales per segment.

Created bar charts and pie charts to visualize the distribution.
---
4.Customer Loyalty:
Identified repeat customers and their total orders.

Highlighted top customers in terms of order frequency and sales contribution.
---
5.Shipping Analysis:
Evaluated the popularity of different shipping modes.

Analyzed states and cities contributing the highest sales.
---
6.Product Performance:
Categorized sales across product categories.

Visualized the best and worst-performing subcategories.
---
#Trend Analysis:
7.Yearly Sales Trends:

Analyzed yearly growth in sales using bar charts.
---
8.Quarterly Sales:

Examined seasonal trends within a year using line charts.
----
9.Monthly Trends:

Tracked month-by-month sales for detailed performance analysis.
---
#Key Findings and Insights

10.Sales Segmentation:

Consumers account for the majority of sales, followed by Corporate and Home Office segments.

#Shipping Modes:

Standard Class is the most used shipping mode, indicating a preference for economical delivery options.
---
#Top Performing Regions:

California and New York lead in sales contribution by state.

Major cities like Los Angeles and New York City also drive significant revenue.
---

#Product Trends:

Technology category dominates in terms of sales, followed by Furniture and Office Supplies.

Subcategories like Phones and Chairs perform exceptionally well.
----
#Seasonal Trends:

Sales spike during the fourth quarter, likely due to holiday shopping.
----
#Recommendations
Enhance Customer Retention:

Focus on high-value repeat customers by offering loyalty programs.
---
#Optimize Shipping Strategies:

Promote faster shipping methods to attract premium customers.
---
#Region-Specific Promotions:

Target high-performing states and cities with exclusive offers.
----
#Product Strategy:

Increase inventory and marketing for top-performing subcategories like Phones and Chairs.
---
#Seasonal Campaigns:

Plan aggressive marketing campaigns in the fourth quarter to leverage the holiday season.

##How to Run This Project

 1. Clone the repository:
   ```bash
   git clone git clone https://github.com/stevejobs27/Superstore_Sales_Analysis.git
   ```
2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Run the **Jupyter notebook** or **Python script**:
   ```bash
   python Superstore_Sales_Analysis.py
   ```
---
#Future Work
Develop predictive models to forecast future sales and demand trends.

Perform sentiment analysis on customer reviews to identify pain points.

Create an interactive dashboard using tools like Power BI or Tableau.



