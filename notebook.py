
CLEANING CODE
import pandas as pd
df = pd.read_csv("olist_sales_project.csv")

#1
df['product_id'] = df['product_id'].fillna('unknown_product')
df['product_category_name'] = df['product_category_name'].fillna('unknown_category')

#2
df['price'] = df['price'].fillna(0)
df['freight_value'] = df['freight_value'].fillna(0)
df['payment_value'] = df['payment_value'].fillna(0)

#3
df['payment_type'] = df['payment_type'].fillna('unknown')

#4
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'], errors='coerce')

#5
df.to_csv("olist_sales_cleaned.csv", index=False)
print("Cleaning selesai! File tersimpan sebagai olist_sales_cleaned.csv")


REASONING
1. Handle missing product information
Any missing values in `product_id` and `product_category_name` are replaced with placeholders (`unknown_product`, `unknown_category`) to keep all transactions in the dataset for aggregation and analysis.

2. Handle missing numeric values
Missing values in `price`, `freight_value`, and `payment_value` are set to `0` to ensure that total calculations like revenue are not affected by nulls.

3. Handle missing payment types  
Rows with missing `payment_type` are labeled as `unknown` to allow consistent grouping when analyzing payment method trends.

4. Convert timestamp to datetime  
`order_purchase_timestamp` is converted into datetime format so that it can be used for time-based analysis and visualizations in Tableau.

5. Fill missing order_item_id  
Missing `order_item_id` values are set to `1`, following the dataset's typical item-sequence pattern.

6. Export cleaned dataset
The final, processed dataset is saved for use in dashboards..

