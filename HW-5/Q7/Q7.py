import psycopg2

def insert_employee():
    conn = psycopg2.connect(database="postgres", user='postgres', password='Lylbigland25jly&', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    cursor.execute('''insert into employee (fname,lname)
    (select substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ',((random()*(26-1)+1)::integer),10), 
    substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ',((random()*(26-1)+1)::integer),10) 
    from generate_series(1,500));''')
    conn.commit()
    conn.close()
