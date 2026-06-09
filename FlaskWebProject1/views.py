import mysql.connector
from FlaskWebProject1 import app

@app.route('/db')
def db_test():
    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root123",
        database="mysql"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return f"MySQL Connected: {result}"