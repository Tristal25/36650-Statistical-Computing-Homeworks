import psycopg2

def display_employee():
    secret = open('secret.txt', 'r')
    pw = secret.read()[:-1]
    conn = psycopg2.connect(database="postgres", user='postgres', password=pw, host='127.0.0.1', port='5432')
    cursor = conn.cursor()
    cursor.execute('''Select * from employee limit 10''')
    print(cursor.fetchall())
    conn.commit()
    conn.close()


display_employee()