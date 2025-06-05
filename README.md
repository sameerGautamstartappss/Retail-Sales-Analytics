# Retail-Sales-Analytics


## ✅ Problem 1: Retail Sales Analytics using PySpark

### 📘 Scenario:

You are working as a data engineer for a large retail chain. You’ve been provided with a daily sales dataset containing transactions from 100 different stores.

You are required to perform a series of data transformations and aggregations using **PySpark** to analyze store performance.

---

### 📂 Dataset: `sales.csv`

**Columns:**

```
transaction_id | store_id | product_id | sale_date | quantity | price
```

Each row represents a sale of one product at a specific store on a specific date.

---

### 🔍 Task Instructions:

1. **Load the data** from `sales.csv` using `spark.read.csv()` with headers and schema inference enabled.

2. **Create a new column** called `total_amount`, calculated as:

   ```
   total_amount = quantity * price
   ```

3. **Group the data** by `store_id` and compute:

   * Total revenue (sum of `total_amount`)
   * Total number of transactions (count of `transaction_id`)

4. **Register the DataFrame** as a **temporary view** called `sales` and write a SQL query to return:

   ```sql
   SELECT store_id, SUM(total_amount) AS revenue
   FROM sales
   GROUP BY store_id
   ORDER BY revenue DESC;
   ```

5. **Write the final aggregated result** as a **Parquet file** to disk using `df.write.parquet()`.

---

### 💡 Skills Tested:

* PySpark DataFrame operations
* Column creation with `withColumn`
* Grouping and aggregation with `groupBy` and `agg`
* Using Spark SQL with temp views
* Writing output in Parquet format

---


