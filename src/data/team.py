import database.config_db
import data.get
import data.clean
import data.vali
from datetime import datetime, timedelta

class TeamData:
    def __init__(self, lg, game_date, print_on = None):
        self.raw_tm = data.get.game_logs(game_date=game_date, player_team='T', lg=lg)
        if not self.raw_tm.empty:
            self.cln_tm = data.clean.raw_df(self.raw_tm)
            self.season_df = data.clean.season_df(self.cln_tm)
            self.game_df = data.clean.game(self.cln_tm)
            self.tgame_df = data.clean.tgame(self.cln_tm)
            self.tbox_df = data.clean.tbox(self.cln_tm)
            self.tshtg_df = data.clean.tshtg(self.cln_tm)
            
            # PASS ANYTHING TO print_on TO PRINT DFS
            if print_on:
                self.print_dfs()
                
                
        else:
            # log no games 
            print(f'No {lg} League games found for {game_date}')
            
    def print_dfs(self):
        print(self.season_df)
        print(self.game_df)
        print(self.tgame_df)
        print(self.tbox_df)
        print(self.tshtg_df)