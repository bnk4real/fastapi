import mysql.connector
import os
from dotenv import load_dotenv

# load config file
load_dotenv(".env.local")

# initialize from environment variables
db_config = {
    "user": os.getenv("DATABASE_USER"),
    "password": os.getenv("DATABASE_PASSWORD"),
    "host": os.getenv("DATABASE_HOST"),
    "database": os.getenv("DATABASE_NAME"),
}

# connection to MySQL
connection = mysql.connector.connect(**db_config)