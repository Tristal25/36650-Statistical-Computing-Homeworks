import psycopg2

def create_employee():
    conn = psycopg2.connect(database="postgres", user='postgres', password='Lylbigland25jly&', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    cursor.execute('''CREATE TABLE EMPLOYEE(id serial, fname varchar(10), lname varchar(10))''')
    conn.commit()
    conn.close()