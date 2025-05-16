from data.team import TeamData
from data.player import PlayerData
from datetime import datetime, timedelta

def main():
    yesterday = (datetime.today() - timedelta(1)).strftime('%m/%d/%Y')
        
    nba_tm = TeamData('NBA', yesterday, 'print')
    wnba_tm = TeamData('WNBA', yesterday, 'print')
    g_tm = TeamData('G', yesterday, 'print')

    nba_pl = PlayerData('NBA', yesterday, nba_tm.tgame_df, 'print')
    
    
    
if __name__ == '__main__':
    main()