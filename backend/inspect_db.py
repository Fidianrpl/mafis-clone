
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', database='activos', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
with conn.cursor() as cursor:
    cursor.execute("DESCRIBE usuarios")
    print(cursor.fetchall())
conn.close()
