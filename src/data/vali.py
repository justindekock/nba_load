
from database.config_db import seasons, players

# this file will interact directly with the database file

# functions in this file compare existing database data to newly fetched data
# TODO - RETURN THE PLAYERS THAT NEED TO BE UPDATED IN A WAY THAT CAN BE PASSED TO UPDATE
def check_szn(szn_df):
    szn_db = seasons()

# TODO - RETURN THE PLAYERS THAT NEED TO BE UPDATED IN A WAY THAT CAN BE PASSED TO UPDATE
def check_players():
    pls_db = players()
    
class DatabaseVali:
    def __init__(self):
        self.db_players = self.select_players()
        self.db_seasons = self.select_seasons()
        
        
    def select_players():
        # select active players in database
        pass
    
    def select_seasons():
        pass
    
