import sqlalchemy
import psycopg2

# Use the EXACT same connection string as in your main etl_pipeline.py script
db_uri = "postgresql://postgres:your_password@localhost:5432/netflix"

print("Attempting to connect to the database...")

try:
    engine = sqlalchemy.create_engine(db_uri)
    connection = engine.connect()
    print("✅ Connection successful!")
    connection.close()
except Exception as e:
    print("❌ Connection failed. Here is the error:")
    print(e)