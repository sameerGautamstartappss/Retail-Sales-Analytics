from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Retail Sales Analytics") \
    .getOrCreate()

# Load CSV with headers and infer schema
df = spark.read.csv("data/sales.csv", header=True, inferSchema=True)

# Show top 5 rows
df.show(5)
