import mysql.connector
from faker import Faker
import random

#MYSQL연결 설정

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8715",
    database="testdatabase"
)
#MYSQL 연결
cursor = db_connection.cursor()
faker = Faker()

# #user테이블에 데이더 삽입
for _ in range(100):
    username = faker.user_name()
    email = faker.email()
    sql = "INSERT INTO users(username, email) VALUE(%s, %s)"
    values = (username, email)
    cursor.execute(sql, values)


#user_id 불러오기
cursor.execute('SELECT user_id FROM users')
valid_user_id = [row[0] for row in cursor.fetchall()]
# 100개의 주문 더미 데이터
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1, 10)

    try:
        sql = "INSERT INTO orders(user_id, product_name, quantity) VALUES(%s, %s, %s)"
        values = (user_id, product_name, quantity)

        cursor.execute(sql, values)
    except:
        print('오류발생')
        pass


db_connection.commit()
cursor.close()
db_connection.close()