
# import data.get
# import data.vali
# from data.team import TeamData
# from data.player import PlayerData

# from datetime import datetime, timedelta

import database.config_db as db
import database.dml as dml
# print(db.select('player', 'fetchall'))
# db.select('tables', 'fetchall')
# print(db.show_cols('player'))

dml.test_insert(table='team', 
                fields=['team_id', 'team', 'team_name', 'lg'], 
                values=[(1111111111, 'TST', 'Test', 'nba'), 
                        (1111111112, 'TTT', 'Test1', 'nba'),
                        (1111111113, 'TET', 'Test2', 'nba'),
                        (1111111114, 'TGT', 'Test3', 'nba'), 
                        (1111111115, 'THT', 'Test4', 'nba'),
                        (1111111117, 'TPT', 'Test6', 'nba')])


print(db.select('team', 'fetchall'))

dml.test_insert(table='player', 
                fields=['player_id', 'player', 'team_id', 'lg', 'active'], 
                values=[(111111, 'Test', 1111111111, 'nba', 1), 
                        (111112, 'Test1', 1111111112, 'nba', 1),
                        (111113, 'Test2', 1111111113, 'nba', 1),
                        (111115, 'Test3', 1111111114, 'nba', 1),
                        (111115, 'Test4', 1111111115, 'nba', 1),
                        (111117, 'Test6', 1111111117, 'nba', 1),])

print(db.select('player', 'fetchall'))

# yesterday = (datetime.today() - timedelta(1)).strftime('%m/%d/%Y')

# # this needs to be after data is fetched i believe
# players_db = database.db.players()
# seasons_db = database.db.seasons()

# new_szns = data.vali.seasons()



# nba_tm = TeamData('NBA', yesterday, 'print')
# wnba_tm = TeamData('WNBA', yesterday, 'print')
# g_tm = TeamData('G', yesterday, 'print')

# nba_pl = PlayerData('NBA', yesterday, nba_tm.tgame_df, 'print')



