import psycopg2

def create_employee():
    secret = open('secret.txt', 'r')
    pw = secret.read()[:-1]
    conn = psycopg2.connect(database="postgres", user='postgres', password=pw, host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    cursor.execute('''CREATE TABLE EMPLOYEE(id serial, fname varchar(10), lname varchar(10))''')
    conn.commit()
    conn.close()


create_employee()