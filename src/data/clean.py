import pandas as pd

# any fetched game logs needs to be passed through here
def raw_df(df):
    df.columns = [col.lower() for col in df.columns]
    df = df.rename(columns={'team_abbreviation': 'team', 'min': 'mins', 'plus_minus': 'pm'})
    df = df.fillna(0)
    return df

# pass team logs, assign the season based on the first character

def season_df(df):
    season_id = df['season_id'].unique()
    season = []
    season_desc = []
    wseason = []
    wseason_desc = []
    
    # for loop in case multiple seasons in df
    for id in season_id:
        # characters 1 through 5 in season_id are the year
        year1 = id[1:5]
        year2 = int(year1) + 1
        
        # first character in id is the season type
        stype = int(id[0])
        stypes = {
            1: ['PRE', 'Pre Season'], 
            2: ['RS', 'Regular Season'], 
            3: ['AS', 'All Star Week'],
            4: ['PO', 'Playoffs'], 
            5: ['PI', 'Play-In Tournament'], 
            6: ['NC', 'NBA Cup']
        }      
        
        season.append(f'{year1}-{year2}-{stypes[stype][0]}')
        season_desc.append(f'{year1}-{year2} {stypes[stype][1]}')
        wseason.append(f'{year1}-{stypes[stype][0]}')
        wseason_desc.append(f'{year1} WNBA {stypes[stype][1]}')
        
    # return a dataframe with the lists as columns
    return pd.DataFrame({
        'season_id': season_id,
        'season': season,
        'season_desc': season_desc, 
        'wseason': wseason,
        'wseason_desc': wseason_desc
    })

def get_ot(mins):
    return 0 if mins < 260 else (2 if mins > 280 else 1)

def get_loc(matchup):
    return 'A' if matchup[4] == '@' else 'H'

def game(df):
    # returns a formatted string scores eg 'DAL 110 - 105 BOS
    def get_final_scores(df): # adds a formatted final score column
        # final_scores = df.pivot(index='game_id', columns='team', values='pts')
        final_scores = df.pivot(index='game_id', columns='team', values='pts')
    
    # returns string formatted score - pass with .apply to each row
        def format_score(row): # pass to each row with apply function
            teams = list(row.dropna().index)
            scores = list(row.dropna().values)
            
            # ensure both teams have data, otherwise return nothing        
            if len(teams) == 2: 
                if scores[0] > scores[1]: # winning team first
                    return f"{teams[0]} {int(scores[0])} - {int(scores[1])} {teams[1]}"
                return f"{teams[1]} {int(scores[1])} - {int(scores[0])} {teams[0]}"
            return None

        # get final scores
        final_scores['final_score'] = final_scores.apply(format_score, axis=1)
        final_scores = final_scores[['final_score']].reset_index()
        
        # return final scores df merged with df passed in
        return (df.merge(final_scores, on='game_id', how='left')
                .drop(['team', 'pts'], axis=1).drop_duplicates())
    
    # CALLS START HERE - get copy df for function
    game_df = df[['game_id', 'season_id', 'lg', 'team_id', 'team', 'game_date', 'matchup', 'pts', 'mins']].copy()

    # call final scores function to get final string
    game_df = get_final_scores(game_df)
    
    # ot indicator, if mins > 240, game went to ot. if > 280, game went to double ot
    game_df['ot'] = game_df['mins'].apply(get_ot)
    
    # game_df['lg'] = lg if lg in ['NBA', 'WNBA', 'G'] else None
    
    # drop the rows with @, drop unecessary columns
    game_df = game_df[game_df['matchup'].str[4] == 'v'].reset_index() 
    game_df = game_df.drop(columns=['index', 'mins', 'team_id'])
    return game_df

# TEAM GAMES
def tgame(df):
    # have to make a copy to not affect original df
    tgame_df = df[['game_id', 'season_id', 'team_id', 'game_date', 'matchup',
                   'pts', 'pm', 'wl', 'mins']].copy() 

    # add loc field (home/away indicator)
    #tgame_df['loc'] = tgame_df['matchup'].apply(lambda x: 'A' if x[4] == '@' else 'H')
    tgame_df['loc'] = tgame_df['matchup'].apply(get_loc)
    # add ot indicator (based on minutes) -- 0 if < 260, 2 if > 280, 1 if between 260 & 280
    tgame_df['ot'] = tgame_df['mins'].apply(get_ot)
    tgame_df['pm'] = tgame_df['pm'].astype(int)
    tgame_df = tgame_df.rename(columns={'pm': 'diff'})
    tgame_df = tgame_df.drop(['mins'], axis=1)
    
    return tgame_df

def tbox(df):
    return df[['game_id', 'season_id', 'team_id', 'mins', 'pts', 'ast', 
           'reb', 'stl', 'blk', 'oreb', 'dreb', 'pm', 'tov', 'pf']].copy() 
    
def tshtg(df):
    return df[['game_id', 'season_id', 'team_id', 'fgm', 'fga', 'fg3m', 
           'fg3a', 'ftm', 'fta', 'fg_pct', 'fg3_pct', 'ft_pct']].copy() 
    
# pass the clean team game logs to this to get the ot/wl/loc data
def pgame(df, tm_df):
    pl_df = df[['game_id', 'season_id', 'team_id', 'player_id', 'mins', 'pts']].copy()
    
    joined = pl_df.merge(tm_df, on=['game_id', 'season_id', 'team_id'])
    
    joined = joined.rename(columns={'pts_x': 'pts'})
    # joined = joined.drop(columns=['pts_y'])
    
    
    cols = ['game_id', 'season_id', 'team_id', 'player_id', 'game_date', 
            'matchup', 'mins', 'pts', 'diff', 'wl', 'loc', 'ot']
    
    pgame_df = joined[cols]
    print(pgame_df)

def pbox(df):
    return df[['game_id', 'season_id', 'team_id', 'player_id', 'mins', 'pts', 'ast', 
           'reb', 'stl', 'blk', 'oreb', 'dreb', 'pm', 'tov', 'pf']].copy() 
    

def pshtg(df):
    return df[['game_id', 'season_id', 'team_id', 'player_id', 'fgm', 'fga', 'fg3m', 
           'fg3a', 'ftm', 'fta', 'fg_pct', 'fg3_pct', 'ft_pct']].copy() 
