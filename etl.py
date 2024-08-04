from pyspark.sql import SparkSession

def etl():
    spark = SparkSession.builder.appName("LogAnalysis").getOrCreate()

    # Load log data
    log_df = spark.read.text("/usr/local/airflow/logs/logs.txt")

    # Process log data
    processed_df = log_df.withColumn("level", log_df.value.substr(20, 5)) \
                         .withColumn("message", log_df.value.substr(26, 100))

    # Filter and save processed data
    error_logs = processed_df.filter(processed_df.level == "ERROR")
    error_logs.write.mode("overwrite").csv("/usr/local/airflow/logs/error_logs.csv")

if __name__ == "__main__":
    etl()
