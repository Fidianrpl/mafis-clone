import os
import pymysql

try:
    conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

    with conn.cursor() as cursor:
        cursor.execute("DESCRIBE usuarios")
        resultado = cursor.fetchall()

        for fila in resultado:
            print(fila)

except pymysql.MySQLError as e:
    print("Error de base de datos:", e)

finally:
    try:
        conn.close()
    except:
        pass