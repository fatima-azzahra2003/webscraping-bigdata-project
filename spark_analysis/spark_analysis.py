from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

spark = SparkSession.builder.appName("BooksAnalysis").getOrCreate()
df = spark.read.json("../books_scraper/books.json")

df = df.withColumn("price", df["price"].cast("float"))
df.select(avg("price")).show()
df.groupBy("rating").agg(count("*").alias("count")).show()
print("Books in stock:", df.filter(df["availability"] == "In").count())