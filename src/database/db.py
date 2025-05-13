from dotenv import load_dotenv
import os
import mariadb

# load db config environment variables from .env file
load_dotenv()
user = os.getenv('DB_USER') 
password = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
port = int(os.getenv('DB_PORT')) # mariadb.connect() requires integer
database = os.getenv('DB')

# connect to the database 
def connect():
    try:
        return mariadb.connect(user = user, password = password, host = host, 
                               port = port, database = database)
        
    except mariadb.Error as e:
        print(e)
        return None

# prints a list of all tables in database, can be assigned to list as well
def show_tables():
    query = 'show tables;'
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)        
    
    tables = []
    for table in cur:
        tables.append(table[0])
        
    print(tables)
    conn.close()    
    return tables


# tables = show_tables()



# mariadb.connect()