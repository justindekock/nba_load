import database.db
import data.get
import data.clean
from datetime import datetime, timedelta

yesterday = (datetime.today() - timedelta(1)).strftime('%m/%d/%Y')

# ideally, class definitions will go in a file in the data directory
# keep in main for now while developing
class TeamData:
    def __init__(self, lg, game_date):
        self.raw_tm = data.get.game_logs(game_date=game_date, player_team='T', lg=lg)
        if not self.raw_tm.empty:
            self.cln_tm = data.clean.raw_df(self.raw_tm)
            self.season_df = data.clean.season_df(self.cln_tm)
            self.game_df = data.clean.game(self.cln_tm)
            self.tgame_df = data.clean.tgame(self.cln_tm)
            self.tbox_df = data.clean.tbox(self.cln_tm)
            self.tshtg_df = data.clean.tshtg(self.cln_tm)
            
            # COMMENT THIS LINE TO STOP PRINTING ALL THE DFS
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

nba_tm = TeamData('NBA', yesterday)
# print(nba_tm.game_df)
# print(nba_tm.season_df)

# def get_clean_data(lg):
#     raw_tm_logs = data.get.game_logs(game_date=yesterday, player_team='T', lg=lg)
#     cln_tm_logs = data.clean.raw_df(raw_tm_logs)

#     szn_df = data.clean.season_df(cln_tm_logs)

#     game_df = data.clean.game(cln_tm_logs)
#     tlogs_df = data.clean.tgame(cln_tm_logs)
#     tbox_df = data.clean.tbox(cln_tm_logs)
#     tshtg_df = data.clean.tshtg(cln_tm_logs)
#     print(szn_df)
#     print(game_df)
#     # print(tlogs_df)
#     # print(tbox_df)
#     # print(tshtg_df)



# TODO - GET AND CLEAN WNBA LOGS

# TODO - GET AND CLEAN G LEAGUE LOGS


# raw_plr_logs = data.get.game_logs(game_date='05/11/2025')
