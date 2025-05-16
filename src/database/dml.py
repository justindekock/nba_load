import mariadb
import pandas as pd
import database.config_db as db

def test_insert(table, fields, values):
    valid_table = db.table_validation(table)    
    valid_fields = db.field_validation(valid_table, fields)
    
    # if not bad_fields:  
    if type(valid_fields) == str:
        # get placeholders (?, ?,...) based on number of values
        if len(values[0]) == len(fields):
            val_ph = '?'
            for i in range(1, len(values[0])):
                val_ph = val_ph + ', ' + '?'

            q = f'insert ignore into {valid_table} ({valid_fields}) values ({val_ph})'
            # print(q) # UNCOMMENT TO SEE THE CONSTRUCTED QUERY
            try:
                conn = db.connect()
                cur = conn.cursor()
                
                print(f'Rows before insert: {db.select_count(cur, valid_table)}')
                
                cur.executemany(q, values)
                conn.commit()   
                
                print(f'Rows after insert: {db.select_count(cur, valid_table)}')
                
            except mariadb.Error as e:
                print(e)
                
        else:
            raise Exception(f'Number of values to insert does not match number of fields')
    else: 
        return f'Invalid field(s) for table "{valid_table}: {valid_fields}"' # really they're bad fields
            
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
    