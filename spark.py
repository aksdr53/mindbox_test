from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_product_category_pairs(spark: SparkSession):
    # предполагаем, что датафреймы уже определены
    products_df = spark.table("products")
    categories_df = spark.table("categories")
    product_categories_df = spark.table("product_categories")

    # Выполняем left outer join между продуктами и связями продуктов с категориями
    products_with_categories_df = products_df.alias("p").join(
        product_categories_df.alias("pc"),
        col("p.product_id") == col("pc.product_id"),
        "left_outer"
    )

    # Теперь выполняем left outer join с категориями
    result_df = products_with_categories_df.join(
        categories_df.alias("c"),
        col("pc.category_id") == col("c.category_id"),
        "left_outer"
    ).select(
        col("p.product_name").alias("Имя продукта"),
        col("c.category_name").alias("Имя категории")
    )

    # Возвращаем итоговый датафрейм
    return result_df

# Инициализируйте SparkSession и вызовите метод
spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()
result_df = get_product_category_pairs(spark)
result_df.show()