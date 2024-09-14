from langchain.sql_database import SQLDatabase

user = "root"
password = ""
host = "localhost"
port = 3306
database = "retail_sales"

uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
db = SQLDatabase.from_uri(uri)
