from dotenv import load_dotenv
import os
import mariadb
import pandas as pd

# how can i update table? 
QUERIES = {
        'columns': 1,
        'tables': 'show tables',
        'player': 'select * from player',
        'team': 'select * from team',
        'player_team': '''
            select 
                a.player, b.team_name, b.lg, a.active 
            from player a 
                inner join team b 
                on b.team_id = a.team_id
            '''
    }

# load db config environment variables from .env file
load_dotenv()
user = os.getenv('DB_USER') 
password = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
port = int(os.getenv('DB_PORT')) # mariadb.connect() requires integer
database = os.getenv('DB')

# connect to the database 
def connect() -> None:
    try:
        return mariadb.connect(user = user, password = password, host = host, 
                               port = port, database = database)
        
    except mariadb.Error as e:
        print(e)
        return None

# get the a list of the fields in the cursor
def curcols(cur):
    return cur.metadata['field']

# validate table passedd as input in show_cols
def table_validation(input_table):
    db_tables = show_tables()
    for db_table in db_tables:
        if db_table == input_table:
            return db_table
            
    return f"Invalid input: '{input_table}' does not exist in database"
             
def field_validation(table, fields):
    db_fields = show_cols(table)['Field'].unique().tolist()
    bad_fields = []
    for i, field in enumerate(fields): 
        if field not in db_fields:
            bad_fields.append(field)
            del fields[i]
            
    if not bad_fields:
        return fields_str(db_fields)
    else:
        return bad_fields


def fields_str(db_fields):
    # first field starts the string, then add a comma and the next field
    valid_fields = db_fields[0] 
    for i in range(1, len(db_fields)):
        valid_fields = valid_fields + ', ' + db_fields[i]
    return valid_fields
             
# called in input_vali
def show_tables():
    cur = connect().cursor()
    cur.execute('show tables')
    res = cur.fetchall()
    
    tables = []
    for table in res:
        tables.append(table[0])
    return tables
    
# validate table exists, then return columns as df
def show_cols(table='team'):
    valid_table = table_validation(table)
    if valid_table == table:
        q = f'show columns from {valid_table}'
        conn = connect()
        cur = conn.cursor()
        cur.execute(q)
        res = cur.fetchall()
        return pd.DataFrame(res, columns=curcols(cur))
        
    else:
         raise Exception(valid_table)
    
# select season, players, teams, players/teams together    
def select(query, fetch_type='fetchone', table='team') -> pd.DataFrame:    
    queries = {
        'season': 'select * from season',
        'player': 'select * from player',
        'team': 'select * from team',
        'player_team': '''
            select 
                a.player, b.team_name, b.lg, a.active 
            from player a 
                inner join team b 
                on b.team_id = a.team_id
            '''
    }
    
    q = queries[query]
    
    conn = connect()
    cur = conn.cursor()
    cur.execute(q)
    
    if fetch_type == 'fetchone':
        res = cur.fetchone()
    elif fetch_type == 'fetchall':
        res = cur.fetchall()
    else: 
        raise Exception('fetch_type should be fetchone or fetchall')
    
    # return query output as df
    return pd.DataFrame(res, columns=curcols(cur))

# return the count of a table
def select_count(cur, table) -> int:
    valid_table = table_validation(table)
    if valid_table == table:
        cur.execute(f'select count(*) from {valid_table}')
        return cur.fetchone()[0]