import pymysql.cursors

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'test',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = 'INSERT INTO  sign_guest (name, phone, email, sign, event_id, creat_time) VALUES ' \
              '("alen", 1881111222, "alen@lifesense.com", 0, 1, NOW());'
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = 'SELECT *  FROM sign_guest WHERE phone=%s'
        cursor.execute(sql, ('1881111222',))
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()
