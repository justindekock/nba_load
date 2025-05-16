import srcdatabase.config_db
import data.get
import data.clean
import data.vali
from datetime import datetime, timedelta

class PlayerData:
    def __init__(self, lg, game_date, tm_df, print_on = None):
        # players from api
        self.active_players = data.get.active_players()
        
        self.raw_pl = data.get.game_logs(game_date=game_date, player_team='P', lg=lg)
        if not self.raw_pl.empty:
            self.tm_df = tm_df
            self.cln_pl = data.clean.raw_df(self.raw_pl)
            self.pgame_df = data.clean.pgame(self.cln_pl, tm_df)
            self.pbox_df = data.clean.pbox(self.cln_pl)
            self.pshtg_df = data.clean.pshtg(self.cln_pl)
            
            # PASS ANYTHING TO print_on TO PRINT DFS
            if print_on:
                self.print_dfs()
                
        else:
            # log no games 
            print(f'No {lg} League games found for {game_date}')
            
    def print_dfs(self):
        print(self.pgame_df)
        print(self.pbox_df)
        print(self.pshtg_df)
        
    # compare the fetched players to what is in the database, 
    # return df of players that need to be updated
    def compare_db():
        pass
        
    # update the players that are different in the database 
    def players_update(self):
        pass
        # function should be defined in database.update