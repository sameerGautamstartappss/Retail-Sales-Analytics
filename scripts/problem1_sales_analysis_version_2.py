from pyspark.sql import SparkSession

from pyspark.sql.functions import col, round

# Step 1: Start Spark sesssion

spark = SparkSession.builder \
    .appName("RetailSalesAnalysis") \
    .getOrCreate()

# Step 2: Read the CSV

df = spark.read.csv("data/sales.csv", header=True, inferSchema=True)

# Step 3: Add total_amount column (quantity * price)

df = df.withColumn("total_amount", round(col("quantity") * col("price"), 2))

# Step 4: Group by store_id and sum total_amoount

sales_by_store = df.groupBy("store_id").sum("total_amount") \
.withColumnRenamed("sum(total_amount)", "total_sales")

# Step 5: Show results

sales_by_store.show()

# save output

output_path = "output/total_sales_by_store.csv"

sales_by_store.coalesce(1).write.option("header", "true").mode("overwrite").csv(output_path)
# Optional : Stop Spark session

spark.stop()