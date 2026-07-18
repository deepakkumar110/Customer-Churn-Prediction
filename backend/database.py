import os
import mysql.connector

try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "Malviya@123"),
        database=os.getenv("DB_NAME", "churn_db")
    )

    cursor = conn.cursor()

    print("✅ MySQL Connected")

except Exception as e:
    conn = None
    cursor = None

    print("❌ MySQL Not Connected")
    print(e)


def create_tables():
    if conn is None:
        return

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        gender VARCHAR(10),
        senior_citizen INT,
        partner VARCHAR(10),
        dependents VARCHAR(10),
        tenure INT,
        monthly_charges FLOAT,
        total_charges FLOAT,
        contract_type VARCHAR(30),
        prediction VARCHAR(20),
        confidence FLOAT
    )
    """)

    conn.commit()
    print("✅ Table Checked")