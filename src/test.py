
# import data.get
# import data.vali
# from data.team import TeamData
# from data.player import PlayerData

# from datetime import datetime, timedelta

import database.db 
database.db.select('player_team', 'fetchall')

# yesterday = (datetime.today() - timedelta(1)).strftime('%m/%d/%Y')

# # this needs to be after data is fetched i believe
# players_db = database.db.players()
# seasons_db = database.db.seasons()

# new_szns = data.vali.seasons()



# nba_tm = TeamData('NBA', yesterday, 'print')
# wnba_tm = TeamData('WNBA', yesterday, 'print')
# g_tm = TeamData('G', yesterday, 'print')

# nba_pl = PlayerData('NBA', yesterday, nba_tm.tgame_df, 'print')



