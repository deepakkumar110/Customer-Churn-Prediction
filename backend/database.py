import mysql.connector

try:

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Deepak@123",
        database="churn_db"
    )

    cursor = conn.cursor()

    print("MySQL Connected")

except:

    conn = None
    cursor = None

    print("MySQL Not Connected")