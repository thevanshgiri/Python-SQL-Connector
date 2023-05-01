import mysql.connector as sql

def create_db(dbname):

    db = sql.connect(host="localhost", user="root", password="root")
    
    cursor = db.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS %s" %dbname)
    
    db.commit()
    db.close()

def create_table(dbname, table_name, structure):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()
    
    cursor.execute("USE %s" %dbname)
    cursor.execute("CREATE TABLE IF NOT EXISTS %s (%s);" %(table_name, structure))
    
    db.commit()
    db.close()

def drop_column(dbname, table_name, column_name):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()
    
    cursor.execute("USE %s" %dbname)
    cursor.execute("ALTER TABLE %s DROP COLUMN %s;" %(table_name, column_name))
    
    db.commit()
    db.close()

def create_column(dbname, table_name, column_name, column_type):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()
    
    cursor.execute("USE %s" %dbname)
    cursor.execute("ALTER TABLE %s ADD %s %s;" %(table_name, column_name, column_type))
    
    db.commit()
    db.close()

def insert_data(dbname, table_name, values):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()
    
    cursor.execute("USE %s" %dbname)
    cursor.execute("INSERT INTO %s VALUES (%s);" %(table_name, values))
    
    db.commit()
    db.close()
    
def update_data(dbname, table_name, value, where):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()
    
    cursor.execute("USE %s" %dbname)

    if where == -1:
    
        cursor.execute("UPDATE %s SET %s;" %(table_name, value))
    else:
    
        cursor.execute("UPDATE %s SET %s WHERE %s;" %(table_name, value, where))
    
    db.commit()
    db.close()

def show_databases():

    db = sql.connect(host="localhost", user="root", password="root")
    
    cursor = db.cursor()
    
    cursor.execute("SHOW DATABASES")
    result = cursor.fetchall()

    db.close()
    return result

def show_table(dbname):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()
    
    cursor.execute("USE %s" %dbname)
    cursor.execute("SHOW TABLES")
    
    result = cursor.fetchall()

    db.close()
    return result

def describe(dbname, table_name):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()
    
    cursor.execute("USE %s" %dbname)
    cursor.execute("DESCRIBE %s" %table_name)
    result = cursor.fetchall()

    db.close()
    return result

def delete_data(dbname, table_name, where):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()
    
    cursor.execute("USE %s" %dbname)
    cursor.execute("DELETE FROM %s WHERE %s;" %(table_name, where))
    
    db.commit()
    db.close()

def add_primary_key(dbname, table_name, column_name):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()

    cursor.execute("USE %s" %dbname)
    cursor.execute("ALTER TABLE %s ADD PRIMARY KEY (%s);" %table_name, column_name)

    db.commit()
    db.close()
    
def delete_primary_key(dbname, table_name):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)

    cursor = db.cursor()

    cursor.execute("USE %s" %dbname)
    cursor.execute("ALTER TABLE %s DROP PRIMARY KEY;" %table_name)

    db.commit()
    db.close()

def aggregate(dbname, table_name, column_name, function):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()

    cursor.execute("USE %s" %dbname)
    cursor.execute("SELECT %s(%s) FROM %s;" %(function, column_name, table_name))
    result = cursor.fetchall()
    db.close()

    return result
    
def drop_db(dbname):

    db = sql.connect(host="localhost", user="root", password="root")
    
    cursor = db.cursor()

    cursor.execute("DROP DATABASE IF EXISTS %s" %dbname)
    
    db.commit()
    db.close()

def drop_table(dbname, table_name):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()

    cursor.execute("USE %s" %dbname)
    cursor.execute("DROP TABLE IF EXISTS %s" %table_name)
    
    db.commit()
    db.close()
    
def drop_column(dbname, table_name, column_name):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()

    cursor.execute("USE %s" %dbname)
    cursor.execute("ALTER TABLE %s DROP COLUMN %s" %(table_name, column_name))
    
    db.commit()
    db.close()

def select(dbname, table_name, column_name, where):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)
    
    cursor = db.cursor()
    
    cursor.execute("USE %s" %dbname)

    if where == "":
        cursor.execute("SELECT %s FROM %s;" %(column_name, table_name))
    else:
        cursor.execute("SELECT %s FROM %s WHERE %s;" %(column_name, table_name, where))

    result = cursor.fetchall()    
    db.close()
    return result


def truncate_table(dbname, table_name):

    db = sql.connect(host="localhost", user="root", password="root", database=dbname)

    cursor = db.cursor()

    cursor.execute("USE %s" %dbname)
    cursor.execute("TRUNCATE TABLE %s" %table_name)
    
    db.commit()
    db.close()

