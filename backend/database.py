import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Deepak@123",
    database="churn_db"
)

cursor = conn.cursor()