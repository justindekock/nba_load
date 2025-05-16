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
def connect() -> None:
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

def select(query, fetch_type='fetchone'):    
    queries = {
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
    
    print(res)

def db_players(query):
    #  WILL NEED TO UPDATE TABLE NAME FOR NEW DB
    query = query
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)    
    pls = []
    for (id, name, team, lg, active) in cur:
        pl = (id, name, team, lg, active)
        pls.append(pl)
        
        
    q = '''select * from player inner join team on team.team_id = player.team_id;'''
        
    print(pls)
    conn.close()    
    return pls

def seasons():
    
    query = 'select * from season;'
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)    
    szns = []
    
    # need to add wseason and wseason_desc for new db
    for (id, season, desc) in cur:
        szn = (id, season, desc)
        szns.append(szn)
        
    print(szns)
    conn.close()    
    return szns

def update_player_team():
    # update existing player row with new team_id
    pass

def insert_player():
    # insert a new player record when a new player is found
    pass

def deactivate_player():
    # remove a player from the player table if they aren't found as an active player
    pass

def insert_season():
    # insert a new season when it comes up
    pass
    

# tables = show_tables()



# mariadb.connect()