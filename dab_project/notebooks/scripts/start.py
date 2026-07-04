# from databricks.connect import DatabricksSession
# spark = DatabricksSession.builder.getOrCreate()

# spark.sql("SELECT 1").show()
# print('1')

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()