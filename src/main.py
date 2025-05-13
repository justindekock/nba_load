import database.db
import data.get
import data.clean
from datetime import datetime, timedelta

yesterday = (datetime.today() - timedelta(1)).strftime('%m/%d/%Y')

# ideally, class definitions will go in a file in the data directory
# keep in main for now while developing
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
            print(f'No {lg} League games found for {yesterday}')
            
    def print_dfs(self):
        print(self.season_df)
        print(self.game_df)
        print(self.tgame_df)
        print(self.tbox_df)
        print(self.tshtg_df)
        
class PlayerData:
    def __init__(self, lg, game_date, tm_df, print_on = None):
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
            print(f'No {lg} League games found for {yesterday}')
            
    def print_dfs(self):
        print(self.pgame_df)
        print(self.pbox_df)
        print(self.pshtg_df)


nba_tm = TeamData('NBA', yesterday)#, 'print')
# wnba_tm = TeamData('WNBA', yesterday)#, 'print')
# g_tm = TeamData('G', yesterday, 'print')

nba_pl = PlayerData('NBA', yesterday, nba_tm.tgame_df)#, 'print')

