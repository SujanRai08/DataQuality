# Online Retail Dataset Analysis

## Overview
This project analyzes the Online Retail Dataset to uncover patterns and insights about sales performance, customer behavior, and revenue trends. The analysis focuses on cleaning the data, summarizing key metrics, and visualizing important aspects like monthly revenue, top products, and sales distribution across countries.

## Key Features

### 1. Data Cleaning
- **Removed Missing Values:** Dropped rows with missing `CustomerID` values.
- **Handled Negative Quantities:** Separated returns/cancellations and retained only positive quantities.
- **Removed Duplicates:** Ensured data integrity by dropping duplicate records.

### 2. Key Insights
- **Monthly Revenue Trends:** Visualized total revenue by month to identify performance trends.
- **Top-Selling Products:** Highlighted the top 5 products based on quantity sold.
- **Sales Distribution by Weekday:** Analyzed sales performance across weekdays.
- **Top Countries by Revenue:** Visualized revenue contribution by top 5 countries.

### 3. Visualizations
- **Monthly Revenue Line Chart:** Displays revenue trends over time.
- **Sales by Weekday Bar Chart:** Compares sales for each weekday.
- **Top Countries Pie Chart:** Shows revenue contribution of top 5 countries.

## Example Outputs
### Sales by Weekday Bar Chart
![Sales by Weekday](image\weekend.png)

### Top Countries by Revenue Pie Chart
![Top Countries](image\top5.png)

## How to Run
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required dependencies:
   ```bash
   pip install pandas matplotlib
   ```
3. Run the Jupyter Notebook or Python script:
   ```bash
   jupyter notebook analysis.ipynb
   ```

## Data Source
The dataset used in this analysis is `online-retail-dataset.csv`, which contains retail transactions for analysis.

---