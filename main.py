import pandas as pd
import numpy as np

# read csv
advanced_df = pd.read_csv('csv/advanced.csv')
all_star_selections_df = pd.read_csv('csv/All-Star Selections.csv')
end_of_season_teams_voting_df = pd.read_csv('csv/End of Season Teams (Voting).csv')
end_of_season_teams_df = pd.read_csv('csv/End of Season Teams.csv')
opponent_stats_per_100_poss_df = pd.read_csv('csv/Opponent Stats Per 100 Poss.csv')
opponent_stats_per_game_df = pd.read_csv('csv/Opponent Stats Per Game.csv')
opponent_totals_df = pd.read_csv('csv/Opponent Totals.csv')
per_36_minutes_df = pd.read_csv('csv/Per 36 Minutes.csv')
per_100_poss_df = pd.read_csv('csv/Per 100 Poss.csv')
player_award_shares_df = pd.read_csv('csv/Player Award Shares.csv')
player_career_info_df = pd.read_csv('csv/Player Career Info.csv')
player_per_game_df = pd.read_csv('csv/Player Per Game.csv')
player_play_by_play_df = pd.read_csv('csv/Player Play By Play.csv')
player_season_info_df = pd.read_csv('csv/Player Season Info.csv')
player_shooting_df = pd.read_csv('csv/Player Shooting.csv')
player_totals_df = pd.read_csv('csv/Player Totals.csv')
team_abbrev_df = pd.read_csv('csv/Team Abbrev.csv')
team_stats_per_100_poss_df = pd.read_csv('csv/Team Stats Per 100 Poss.csv')
team_stats_per_game_df = pd.read_csv('csv/Team Stats Per Game.csv')
team_summaries_df = pd.read_csv('csv/Team Summaries.csv')
team_totals_df = pd.read_csv('csv/Team Totals.csv')

# creating copies of csvs into xlsx
advanced_df.to_excel('advanced.xlsx', index=False)
all_star_selections_df.to_excel('All-Star Selections.xlsx', index=False)
end_of_season_teams_voting_df.to_excel('End of Season Teams (Voting).xlsx', index=False)
end_of_season_teams_df.to_excel('End of Season Teams.xlsx', index=False)
opponent_stats_per_100_poss_df.to_excel('Opponent Stats Per 100 Poss.xlsx', index=False)
opponent_stats_per_game_df.to_excel('Opponent Stats Per Game.xlsx', index=False)
opponent_totals_df.to_excel('Opponent Totals.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
player_award_shares_df.to_excel('Player Award Shares.xlsx', index=False)
player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_100_poss_df.to_excel('Team Stats Per 100 Poss.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)


#print(player_award_shares_df)
#print(player_per_game_df)

# convert season values to str
advanced_df['season'] = advanced_df['season'].astype(str)
all_star_selections_df['season'] = all_star_selections_df['season'].astype(str)
end_of_season_teams_voting_df['season'] = end_of_season_teams_voting_df['season'].astype(str)
end_of_season_teams_df['season'] = end_of_season_teams_df['season'].astype(str)
opponent_stats_per_100_poss_df['season'] = opponent_stats_per_100_poss_df['season'].astype(str)
opponent_stats_per_game_df['season'] = opponent_stats_per_game_df['season'].astype(str)
opponent_totals_df['season'] = opponent_totals_df['season'].astype(str)
per_36_minutes_df['season'] = per_36_minutes_df['season'].astype(str)
per_100_poss_df['season'] = per_100_poss_df['season'].astype(str)
player_award_shares_df['season'] = player_award_shares_df['season'].astype(str)
player_career_info_df['first_seas'] = player_career_info_df['first_seas'].astype(str) # first_seas
player_career_info_df['last_seas'] = player_career_info_df['last_seas'].astype(str) # last_seas
player_per_game_df['season'] = player_per_game_df['season'].astype(str)
player_play_by_play_df['season'] = player_play_by_play_df['season'].astype(str)
player_season_info_df['season'] = player_season_info_df['season'].astype(str)
player_shooting_df['season'] = player_shooting_df['season'].astype(str)
player_totals_df['season'] = player_totals_df['season'].astype(str)
team_abbrev_df['season'] = team_abbrev_df['season'].astype(str)
team_stats_per_100_poss_df['season'] = team_stats_per_100_poss_df['season'].astype(str)
team_stats_per_game_df['season'] = team_stats_per_game_df['season'].astype(str)
team_summaries_df['season'] = team_summaries_df['season'].astype(str)
team_totals_df['season'] = team_totals_df['season'].astype(str)

# saving updated season value conversions to all files
advanced_df.to_excel('advanced.xlsx', index=False)
all_star_selections_df.to_excel('All-Star Selections.xlsx', index=False)
end_of_season_teams_voting_df.to_excel('End of Season Teams (Voting).xlsx', index=False)
end_of_season_teams_df.to_excel('End of Season Teams.xlsx', index=False)
opponent_stats_per_100_poss_df.to_excel('Opponent Stats Per 100 Poss.xlsx', index=False)
opponent_stats_per_game_df.to_excel('Opponent Stats Per Game.xlsx', index=False)
opponent_totals_df.to_excel('Opponent Totals.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
player_award_shares_df.to_excel('Player Award Shares.xlsx', index=False)
player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_100_poss_df.to_excel('Team Stats Per 100 Poss.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)

# changing name of season column to year
def year(df):
    try:
        return df.rename(columns={'season': 'year'})
    except:
        print('cannot change name of column')

advanced_df = year(advanced_df)
all_star_selections_df = year(all_star_selections_df)
end_of_season_teams_voting_df = year(end_of_season_teams_voting_df)
end_of_season_teams_df = year(end_of_season_teams_df)
opponent_stats_per_100_poss_df = year(opponent_stats_per_100_poss_df)
opponent_stats_per_game_df = year(opponent_stats_per_game_df)
opponent_totals_df = year(opponent_totals_df)
per_36_minutes_df = year(per_36_minutes_df)
per_100_poss_df = year(per_100_poss_df)
player_award_shares_df = year(player_award_shares_df)
player_per_game_df = year(player_per_game_df)
player_play_by_play_df = year(player_play_by_play_df)
player_season_info_df = year(player_season_info_df)
player_shooting_df = year(player_shooting_df)
player_totals_df = year(player_totals_df)
team_abbrev_df = year(team_abbrev_df)
team_stats_per_100_poss_df = year(team_stats_per_100_poss_df)
team_stats_per_game_df = year(team_stats_per_game_df)
team_summaries_df = year(team_summaries_df)
team_totals_df = year(team_totals_df)

# saving changes to all files
advanced_df.to_excel('advanced.xlsx', index=False)
all_star_selections_df.to_excel('All-Star Selections.xlsx', index=False)
end_of_season_teams_voting_df.to_excel('End of Season Teams (Voting).xlsx', index=False)
end_of_season_teams_df.to_excel('End of Season Teams.xlsx', index=False)
opponent_stats_per_100_poss_df.to_excel('Opponent Stats Per 100 Poss.xlsx', index=False)
opponent_stats_per_game_df.to_excel('Opponent Stats Per Game.xlsx', index=False)
opponent_totals_df.to_excel('Opponent Totals.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
player_award_shares_df.to_excel('Player Award Shares.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_100_poss_df.to_excel('Team Stats Per 100 Poss.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)

# adding season column to all dataframes, will be the last column
advanced_df['season'] = advanced_df['year']
all_star_selections_df['season'] = all_star_selections_df['year']
end_of_season_teams_voting_df['season'] = end_of_season_teams_voting_df['year']
end_of_season_teams_df['season'] = end_of_season_teams_df['year']
opponent_stats_per_100_poss_df['season'] = opponent_stats_per_100_poss_df['year']
opponent_stats_per_game_df['season'] = opponent_stats_per_game_df['year']
opponent_totals_df['season'] = opponent_totals_df['year']
per_36_minutes_df['season'] = per_36_minutes_df['year']
per_100_poss_df['season'] = per_100_poss_df['year']
player_award_shares_df['season'] = player_award_shares_df['year']
player_per_game_df['season'] = player_per_game_df['year']
player_play_by_play_df['season'] = player_play_by_play_df['year']
player_season_info_df['season'] = player_season_info_df['year']
player_shooting_df['season'] = player_shooting_df['year']
player_totals_df['season'] = player_totals_df['year']
team_abbrev_df['season'] = team_abbrev_df['year']
team_stats_per_100_poss_df['season'] = team_stats_per_100_poss_df['year']
team_stats_per_game_df['season'] = team_stats_per_game_df['year']
team_summaries_df['season'] = team_summaries_df['year']
team_totals_df['season'] = team_totals_df['year']


# saving changes to all files
advanced_df.to_excel('advanced.xlsx', index=False)
all_star_selections_df.to_excel('All-Star Selections.xlsx', index=False)
end_of_season_teams_voting_df.to_excel('End of Season Teams (Voting).xlsx', index=False)
end_of_season_teams_df.to_excel('End of Season Teams.xlsx', index=False)
opponent_stats_per_100_poss_df.to_excel('Opponent Stats Per 100 Poss.xlsx', index=False)
opponent_stats_per_game_df.to_excel('Opponent Stats Per Game.xlsx', index=False)
opponent_totals_df.to_excel('Opponent Totals.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
player_award_shares_df.to_excel('Player Award Shares.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_100_poss_df.to_excel('Team Stats Per 100 Poss.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)


# define function that corrects season value 
#   ex: 1956 -> 1955-56
def season_values(df):
    try:
        return df.replace(to_replace={'season': {'1947': '1946-47', 
                                                '1948': '1947-48',
                                                '1949': '1948-49',
                                                '1950': '1949-50',
                                                '1951': '1950-51',
                                                '1952': '1951-52',
                                                '1953': '1952-53',
                                                '1954': '1953-54',
                                                '1955': '1954-55',
                                                '1956': '1955-56',
                                                '1957': '1956-57',
                                                '1958': '1957-58',
                                                '1959': '1958-59',
                                                '1960': '1959-60',
                                                '1961': '1960-61',
                                                '1962': '1960-62',
                                                '1963': '1962-63',
                                                '1964': '1963-64',
                                                '1965': '1964-65',
                                                '1966': '1965-66',
                                                '1967': '1966-67',
                                                '1968': '1967-68',
                                                '1969': '1968-69',
                                                '1970': '1969-70',
                                                '1971': '1970-71',
                                                '1972': '1971-72',
                                                '1973': '1972-73',
                                                '1974': '1973-74',
                                                '1975': '1974-75',
                                                '1976': '1975-76',
                                                '1977': '1976-77',
                                                '1978': '1977-78',
                                                '1979': '1978-79',
                                                '1980': '1979-80',
                                                '1981': '1980-81',
                                                '1982': '1981-82',
                                                '1983': '1982-83',
                                                '1984': '1983-84',
                                                '1985': '1984-85',
                                                '1986': '1985-86',
                                                '1987': '1986-87',
                                                '1988': '1987-88',
                                                '1989': '1988-89',
                                                '1990': '1989-90',
                                                '1991': '1990-91',
                                                '1992': '1991-92',
                                                '1993': '1992-93',
                                                '1994': '1993-94',
                                                '1995': '1994-95',
                                                '1996': '1995-06',
                                                '1997': '1996-97',
                                                '1998': '1997-98',
                                                '1999': '1998-99',
                                                '2000': '1999-00',
                                                '2001': '2000-01',
                                                '2002': '2001-02',
                                                '2003': '2002-03',
                                                '2004': '2003-04',
                                                '2005': '2004-05',
                                                '2006': '2005-06',
                                                '2007': '2006-07',
                                                '2008': '2007-08',
                                                '2009': '2008-09',
                                                '2010': '2009-10',
                                                '2011': '2010-11',
                                                '2012': '2011-12',
                                                '2013': '2012-13',
                                                '2014': '2013-14',
                                                '2015': '2014-15',
                                                '2016': '2015-16',
                                                '2017': '2016-17',
                                                '2018': '2017-18',
                                                '2019': '2018-19',
                                                '2020': '2019-20',
                                                '2021': '2020-21',
                                                '2022': '2021-22',
                                                '2023': '2022-23',
                                                '2024': '2023-24',
                                                '2025': '2024-25'
                                                }}) 
    except Exception as e:
        print(f'caught {type(e)}: e \n'
            f'cannot update values')

advanced_df = season_values(advanced_df)
all_star_selections_df = season_values(all_star_selections_df)
end_of_season_teams_voting_df = season_values(end_of_season_teams_voting_df)
end_of_season_teams_df = season_values(end_of_season_teams_df)
opponent_stats_per_100_poss_df = season_values(opponent_stats_per_100_poss_df)
opponent_stats_per_game_df = season_values(opponent_stats_per_game_df)
opponent_totals_df = season_values(opponent_totals_df)
per_36_minutes_df = season_values(per_36_minutes_df)
per_100_poss_df = season_values(per_100_poss_df)
player_award_shares_df = season_values(player_award_shares_df)
player_per_game_df = season_values(player_per_game_df)
player_play_by_play_df = season_values(player_play_by_play_df)
player_season_info_df = season_values(player_season_info_df)
player_shooting_df = season_values(player_shooting_df)
player_totals_df = season_values(player_totals_df)
team_abbrev_df = season_values(team_abbrev_df)
team_stats_per_100_poss_df = season_values(team_stats_per_100_poss_df)
team_stats_per_game_df = season_values(team_stats_per_game_df)
team_summaries_df = season_values(team_summaries_df)
team_totals_df = season_values(team_totals_df)

# saving changes to all files
advanced_df.to_excel('advanced.xlsx', index=False)
all_star_selections_df.to_excel('All-Star Selections.xlsx', index=False)
end_of_season_teams_voting_df.to_excel('End of Season Teams (Voting).xlsx', index=False)
end_of_season_teams_df.to_excel('End of Season Teams.xlsx', index=False)
opponent_stats_per_100_poss_df.to_excel('Opponent Stats Per 100 Poss.xlsx', index=False)
opponent_stats_per_game_df.to_excel('Opponent Stats Per Game.xlsx', index=False)
opponent_totals_df.to_excel('Opponent Totals.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
player_award_shares_df.to_excel('Player Award Shares.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_100_poss_df.to_excel('Team Stats Per 100 Poss.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)

# first_seas column in player_career_info_df
def first_season_values(df):
    try:
        return df.replace(to_replace={'first_seas': {'1947': '1946-47', 
                                                '1948': '1947-48',
                                                '1949': '1948-49',
                                                '1950': '1949-50',
                                                '1951': '1950-51',
                                                '1952': '1951-52',
                                                '1953': '1952-53',
                                                '1954': '1953-54',
                                                '1955': '1954-55',
                                                '1956': '1955-56',
                                                '1957': '1956-57',
                                                '1958': '1957-58',
                                                '1959': '1958-59',
                                                '1960': '1959-60',
                                                '1961': '1960-61',
                                                '1962': '1960-62',
                                                '1963': '1962-63',
                                                '1964': '1963-64',
                                                '1965': '1964-65',
                                                '1966': '1965-66',
                                                '1967': '1966-67',
                                                '1968': '1967-68',
                                                '1969': '1968-69',
                                                '1970': '1969-70',
                                                '1971': '1970-71',
                                                '1972': '1971-72',
                                                '1973': '1972-73',
                                                '1974': '1973-74',
                                                '1975': '1974-75',
                                                '1976': '1975-76',
                                                '1977': '1976-77',
                                                '1978': '1977-78',
                                                '1979': '1978-79',
                                                '1980': '1979-80',
                                                '1981': '1980-81',
                                                '1982': '1981-82',
                                                '1983': '1982-83',
                                                '1984': '1983-84',
                                                '1985': '1984-85',
                                                '1986': '1985-86',
                                                '1987': '1986-87',
                                                '1988': '1987-88',
                                                '1989': '1988-89',
                                                '1990': '1989-90',
                                                '1991': '1990-91',
                                                '1992': '1991-92',
                                                '1993': '1992-93',
                                                '1994': '1993-94',
                                                '1995': '1994-95',
                                                '1996': '1995-06',
                                                '1997': '1996-97',
                                                '1998': '1997-98',
                                                '1999': '1998-99',
                                                '2000': '1999-00',
                                                '2001': '2000-01',
                                                '2002': '2001-02',
                                                '2003': '2002-03',
                                                '2004': '2003-04',
                                                '2005': '2004-05',
                                                '2006': '2005-06',
                                                '2007': '2006-07',
                                                '2008': '2007-08',
                                                '2009': '2008-09',
                                                '2010': '2009-10',
                                                '2011': '2010-11',
                                                '2012': '2011-12',
                                                '2013': '2012-13',
                                                '2014': '2013-14',
                                                '2015': '2014-15',
                                                '2016': '2015-16',
                                                '2017': '2016-17',
                                                '2018': '2017-18',
                                                '2019': '2018-19',
                                                '2020': '2019-20',
                                                '2021': '2020-21',
                                                '2022': '2021-22',
                                                '2023': '2022-23',
                                                '2024': '2023-24',
                                                '2025': '2024-25'
                                                }}) 
    except Exception as e:
        print(f'caught {type(e)}: e \n'
            f'cannot update values')

player_career_info_df = first_season_values(player_career_info_df)

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)

# last seas column in player_career_info_df
def last_season_values(df):
    try:
        return df.replace(to_replace={'last_seas': {'1947': '1946-47', 
                                                '1948': '1947-48',
                                                '1949': '1948-49',
                                                '1950': '1949-50',
                                                '1951': '1950-51',
                                                '1952': '1951-52',
                                                '1953': '1952-53',
                                                '1954': '1953-54',
                                                '1955': '1954-55',
                                                '1956': '1955-56',
                                                '1957': '1956-57',
                                                '1958': '1957-58',
                                                '1959': '1958-59',
                                                '1960': '1959-60',
                                                '1961': '1960-61',
                                                '1962': '1960-62',
                                                '1963': '1962-63',
                                                '1964': '1963-64',
                                                '1965': '1964-65',
                                                '1966': '1965-66',
                                                '1967': '1966-67',
                                                '1968': '1967-68',
                                                '1969': '1968-69',
                                                '1970': '1969-70',
                                                '1971': '1970-71',
                                                '1972': '1971-72',
                                                '1973': '1972-73',
                                                '1974': '1973-74',
                                                '1975': '1974-75',
                                                '1976': '1975-76',
                                                '1977': '1976-77',
                                                '1978': '1977-78',
                                                '1979': '1978-79',
                                                '1980': '1979-80',
                                                '1981': '1980-81',
                                                '1982': '1981-82',
                                                '1983': '1982-83',
                                                '1984': '1983-84',
                                                '1985': '1984-85',
                                                '1986': '1985-86',
                                                '1987': '1986-87',
                                                '1988': '1987-88',
                                                '1989': '1988-89',
                                                '1990': '1989-90',
                                                '1991': '1990-91',
                                                '1992': '1991-92',
                                                '1993': '1992-93',
                                                '1994': '1993-94',
                                                '1995': '1994-95',
                                                '1996': '1995-06',
                                                '1997': '1996-97',
                                                '1998': '1997-98',
                                                '1999': '1998-99',
                                                '2000': '1999-00',
                                                '2001': '2000-01',
                                                '2002': '2001-02',
                                                '2003': '2002-03',
                                                '2004': '2003-04',
                                                '2005': '2004-05',
                                                '2006': '2005-06',
                                                '2007': '2006-07',
                                                '2008': '2007-08',
                                                '2009': '2008-09',
                                                '2010': '2009-10',
                                                '2011': '2010-11',
                                                '2012': '2011-12',
                                                '2013': '2012-13',
                                                '2014': '2013-14',
                                                '2015': '2014-15',
                                                '2016': '2015-16',
                                                '2017': '2016-17',
                                                '2018': '2017-18',
                                                '2019': '2018-19',
                                                '2020': '2019-20',
                                                '2021': '2020-21',
                                                '2022': '2021-22',
                                                '2023': '2022-23',
                                                '2024': '2023-24',
                                                '2025': '2024-25'
                                                }}) 
    except Exception as e:
        print(f'caught {type(e)}: e \n'
            f'cannot update values')

player_career_info_df = last_season_values(player_career_info_df)

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)


# changing names of first_seas and second_seas columns in player_career_info_df respectively
def season_column_names(df):
    try:
        return df.rename(columns={'first_seas': 'first_season',
                                  'last_seas': 'last_season'})
    except:
        print('cannot change name of column')

player_career_info_df = season_column_names(player_career_info_df)

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)


# Patrick Ewing born 1984 should be Patrick Ewing Jr.
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 3967, 'player'] = 'Patrick Ewing Jr.'

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)


# CREATING DOUBLE-DOUBLE AND TRIPLE-DOUBLE COLUMNS (VALUES = YES/NO) in player_per_game_df
player_per_game_df['double_double_avg'] = [''] * len(player_per_game_df)

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
# checking to see what positions trb_per_game, ast_per_game, stl_per_game, blk_per_game, and pts_per_game are located at
# result -> [28 29 30 31 34]  (ADD 1 TO EACH ELEMENT INDEX) -> [29 30 31 32 35]
print(player_per_game_df.columns.get_indexer(['trb_per_game', 'ast_per_game', 'stl_per_game', 'blk_per_game', 'pts_per_game']))
# determine if a player have averged a double-double in a season via list comprehension, placing 'Yes' or 'No' values in double_double_avg column
player_per_game_df['double_double_avg'] = ['Yes' 
                                           if x[29] >= 10.0 and x[30] >= 10.0 or 
                                           x[29] >= 10.0 and x[31] >= 10.0 or
                                           x[29] >= 10.0 and x[32] >= 10.0 or
                                           x[29] >= 10.0 and x[35] >= 10.0 or
                                           x[30] >= 10.0 and x[29] >= 10.0 or
                                           x[30] >= 10.0 and x[31] >= 10.0 or
                                           x[30] >= 10.0 and x[32] >= 10.0 or
                                           x[30] >= 10.0 and x[35] >= 10.0 or
                                           x[31] >= 10.0 and x[29] >= 10.0 or
                                           x[31] >= 10.0 and x[30] >= 10.0 or
                                           x[31] >= 10.0 and x[32] >= 10.0 or
                                           x[31] >= 10.0 and x[35] >= 10.0 or
                                           x[32] >= 10.0 and x[29] >= 10.0 or
                                           x[32] >= 10.0 and x[30] >= 10.0 or
                                           x[32] >= 10.0 and x[31] >= 10.0 or
                                           x[32] >= 10.0 and x[35] >= 10.0 or
                                           x[35] >= 10.0 and x[29] >= 10.0 or
                                           x[35] >= 10.0 and x[30] >= 10.0 or
                                           x[35] >= 10.0 and x[31] >= 10.0 or
                                           x[35] >= 10.0 and x[32] >= 10.0                                                                                                                                                                                                                                                                
                                           else "No" 
                                           for x in player_per_game_df.itertuples()] 

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

player_per_game_df['triple_double_avg'] = [''] * len(player_per_game_df)
# determine if a player have averged a triple-double in a season via list comprehension, placing 'Yes' or 'No' values in triple_double_avg column
player_per_game_df['triple_double_avg'] = ['Yes' 
                                           if x[29] >= 10.0 and x[30] >= 10.0 and x[31] >= 10.0 or 
                                           x[29] >= 10.0 and x[30] >= 10.0 and x[32] >= 10.0 or 
                                           x[29] >= 10.0 and x[30] >= 10.0 and x[35] >= 10.0 or
                                           x[29] >= 10.0 and x[31] >= 10.0 and x[32] >= 10.0 or
                                           x[29] >= 10.0 and x[31] >= 10.0 and x[35] >= 10.0 or
                                           x[29] >= 10.0 and x[32] >= 10.0 and x[35] >= 10.0 or
                                           x[30] >= 10.0 and x[31] >= 10.0 and x[32] >= 10.0 or
                                           x[30] >= 10.0 and x[31] >= 10.0 and x[35] >= 10.0 or
                                           x[30] >= 10.0 and x[32] >= 10.0 and x[35] >= 10.0 or 
                                           x[31] >= 10.0 and x[32] >= 10.0 and x[35] >= 10.0
                                           else "No" 
                                           for x in player_per_game_df.itertuples()] 

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)


# populating the stl_per_game and blk_per_game columns with the following ->
#   N/A - Stat tracked as of the 1973-74 NBA Season;
#   N/A - Stat tracked as of the 1973-74 ABA Season
player_per_game_df.loc[(player_per_game_df['year'].astype(int) < 1974) & \
    ((player_per_game_df['lg'] == 'NBA') | (player_per_game_df['lg'] == 'BAA')), 'stl_per_game'] = \
    'N/A - Stat tracked as of the 1973-74 NBA Season'

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

player_per_game_df.loc[(player_per_game_df['year'].astype(int) < 1974) & \
    ((player_per_game_df['lg'] == 'NBA') | (player_per_game_df['lg'] == 'BAA')), 'blk_per_game'] = \
    'N/A - Stat tracked as of the 1973-74 NBA Season'

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

player_per_game_df.loc[(player_per_game_df['year'].astype(int) < 1974) & (player_per_game_df['lg'] == 'ABA'), 
                       'blk_per_game'] = 'N/A - Stat tracked as of the 1973-74 ABA Season'

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

player_per_game_df.loc[(player_per_game_df['year'].astype(int) < 1974) & (player_per_game_df['lg'] == 'ABA'), 
                       'stl_per_game'] = 'N/A - Stat tracked as of the 1973-74 ABA Season'

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)


# groupby
player_award_shares_df.groupby(['award', 'player'])
print(player_award_shares_df.head())


# ============= #
# merging certain dataframes 
# ============= #

# merging player award shares and player per game dataframes
player_award_shares_and_player_per_game_merged_df = pd.merge(player_award_shares_df,
                                                          player_per_game_df, 
                                                          on=['player_id'])
#print(player_award_shares_and_player_per_game_merged_df)
player_award_shares_and_player_per_game_merged_df.\
    to_excel('player_award_shares_and_player_per_game_merged.xlsx', index=False)
# merging player shooting and player totals dataframes
player_shooting_and_player_totals_merged_df = pd.merge(player_shooting_df, 
                                                       player_totals_df,
                                                       on=['player_id'])
#print(player_shooting_and_player_totals_merged_df)
player_shooting_and_player_totals_merged_df.\
    to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)


# defining a player class that corresponds to the 
#   player_award_shares_and_player_per_game_merged dataframe
class Player:
    def __init__(self, name, year, award, pts_per_game):
        self.name = name
        self.year = year
        self.award = award
        self.pts_per_game = pts_per_game

    def info(self):
        try:
            return f"{self.name} won the {self.year} {self.award} while averaging {self.pts_per_game} points per game."
        except Exception as e:
            print(f'caught {type(e)}: e \n'
                f'cannot list results')
    
value = player_award_shares_and_player_per_game_merged_df.iloc[5]

player_instance = Player(name=value['player_x'], 
                         year=value['year_x'], 
                         award=value['award'],
                         pts_per_game=value['pts_per_game'])

print(player_instance.info())


# converting values to string format
player_award_shares_and_player_per_game_merged_df['winner'] = \
    player_award_shares_and_player_per_game_merged_df['winner'].astype(str)

# changing 'nan' values to 'True' in Bobby Jones' case - 1983 sixth man of the year
player_award_shares_and_player_per_game_merged_df['winner'] = \
    player_award_shares_and_player_per_game_merged_df['winner'].replace('nan', 'True')


# ================== #
# adding fgs and fts made combined/fgs and fts attempted combined/tsp - true shooting percentage 
#   columns
# ================== #

# attempts made in all 3 categories
player_shooting_and_player_totals_merged_df['x2p + x3p + ft'] = \
    player_shooting_and_player_totals_merged_df.apply(lambda row: row['x2p'] + row['x3p'] + row['ft'],axis=1)

player_shooting_and_player_totals_merged_df.\
    to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# converting all values to floats
player_shooting_and_player_totals_merged_df['x2p + x3p + ft'] = \
    player_shooting_and_player_totals_merged_df['x2p + x3p + ft'].astype(float)

player_shooting_and_player_totals_merged_df.\
    to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# total attempts in all 3 categories
player_shooting_and_player_totals_merged_df['x2pa + x3pa + fta'] = \
    player_shooting_and_player_totals_merged_df.apply(lambda row: row['x2pa'] + row['x3pa'] + row['fta'], axis=1)

player_shooting_and_player_totals_merged_df.\
    to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# converting all values to floats
player_shooting_and_player_totals_merged_df['x2pa + x3pa + fta'] = \
    player_shooting_and_player_totals_merged_df['x2pa + x3pa + fta'].astype(float)

player_shooting_and_player_totals_merged_df.\
    to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# fill missing values under x3p_percent column with 0
player_award_shares_and_player_per_game_merged_df['x3p_percent'] = \
    player_award_shares_and_player_per_game_merged_df['x3p_percent'].fillna(0)

player_shooting_and_player_totals_merged_df.to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# created true_shooting_percentage column containing a quotient of makes/attempts
player_shooting_and_player_totals_merged_df['true_shooting_percentage'] = \
    player_shooting_and_player_totals_merged_df['x2p + x3p + ft'].astype(float)/\
        player_shooting_and_player_totals_merged_df['x2pa + x3pa + fta'].astype(float)

player_shooting_and_player_totals_merged_df.to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# only 3 digits past the decimal should remain in the values under true_shooting_percentage column
player_shooting_and_player_totals_merged_df['true_shooting_percentage'] = \
    player_shooting_and_player_totals_merged_df['true_shooting_percentage'].apply(lambda row: round(row, 3))

player_shooting_and_player_totals_merged_df.to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)


# ================== #
# filtering #
# ================== #

# finding unique values under 'award' column
# result -> ['clutch_poy' 'dpoy' 'mip' 'nba mvp' 'nba roy' 'smoy' 'aba mvp' 'aba roy']
#print(player_award_shares_and_player_per_game_merged_df['award'].unique())
# award winners
# clutch poy
def clutch_poy_winners(df):
    try:
        return df[(df['award'] == 'clutch_poy') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y']) ]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

clutch_poy_winners_df = clutch_poy_winners(player_award_shares_and_player_per_game_merged_df)

clutch_poy_winners_df.to_excel('clutch_poy_winners.xlsx', index=False)
# dpoy
def dpoy_winners(df):
    try:
        return df[(df['award'] == 'dpoy') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

dpoy_winners_df = dpoy_winners(player_award_shares_and_player_per_game_merged_df)

dpoy_winners_df.to_excel('dpoy_winners.xlsx', index=False)
# mip (most improved player)
def mip_winners(df):
    try:
        return df[(df['award'] == 'mip') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

mip_winners_df = mip_winners(player_award_shares_and_player_per_game_merged_df)

mip_winners_df.to_excel('mip_winners.xlsx', index=False)
# nba mvp
def nba_mvp_winners(df):
    try:
        return df[(df['award'] == 'nba mvp') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

nba_mvp_winners_df = nba_mvp_winners(player_award_shares_and_player_per_game_merged_df)

nba_mvp_winners_df.to_excel('nba_mvp_winners.xlsx', index=False)
# nba roy (rookie of the year)
def nba_roy_winners(df):
    try:
        return df[(df['award'] == 'nba roy') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

nba_roy_winners_df = nba_roy_winners(player_award_shares_and_player_per_game_merged_df)

nba_roy_winners_df.to_excel('nba_roy_winners.xlsx', index=False)
# smoy (6th man of the year)
def smoy_winners(df):
    try:
        return df[(df['award'] == 'smoy') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

smoy_winners_df = smoy_winners(player_award_shares_and_player_per_game_merged_df)

smoy_winners_df.to_excel('smoy_winners.xlsx', index=False)
# aba mvp
def aba_mvp_winners(df):
    try:
        return df[(df['award'] == 'aba mvp') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

aba_mvp_winners_df = aba_mvp_winners(player_award_shares_and_player_per_game_merged_df)

aba_mvp_winners_df.to_excel('aba_mvp_winners.xlsx', index=False)
# aba roy (rookie of the year)
def aba_roy_winners(df):
    try:
        return df[(df['award'] == 'aba roy') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

aba_roy_winners_df = aba_roy_winners(player_award_shares_and_player_per_game_merged_df)

aba_roy_winners_df.to_excel('aba_roy_winners.xlsx', index=False)


# =========== #
# pivot tables - individual awards
# =========== #

# clutch poy
clutch_poy_pivot_table_df = \
    pd.pivot_table(clutch_poy_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

clutch_poy_pivot_table_df.to_excel('clutch_poy_pivot_table.xlsx')

clutch_poy_pivot_table_df = \
    pd.read_excel('clutch_poy_pivot_table.xlsx')

clutch_poy_pivot_table_df.to_excel('clutch_poy_pivot_table.xlsx', index=False)

print(clutch_poy_pivot_table_df)
# dpoy
dpoy_pivot_table_df = \
    pd.pivot_table(dpoy_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

dpoy_pivot_table_df.to_excel('dpoy_pivot_table.xlsx')

#print(dpoy_pivot_table_df.sort_values(by=['award'], ascending=False))

dpoy_pivot_table_df = \
    pd.read_excel('dpoy_pivot_table.xlsx')

dpoy_pivot_table_df.to_excel('dpoy_pivot_table.xlsx', index=False)
# updating Dikembe Mutombo's dpoy award count from 6 to 4
dpoy_pivot_table_df['award'] = \
    dpoy_pivot_table_df['award'].where(
        ~dpoy_pivot_table_df['player_x'].\
            isin(['Dikembe Mutombo']), \
                4
    )

print(dpoy_pivot_table_df.sort_values(by=['award'], ascending=False))

dpoy_pivot_table_df.to_excel('dpoy_pivot_table.xlsx', index=False)
# mip
mip_pivot_table_df = \
    pd.pivot_table(mip_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

mip_pivot_table_df.to_excel('mip_pivot_table.xlsx')

mip_pivot_table_df = \
    pd.read_excel('mip_pivot_table.xlsx')

mip_pivot_table_df.to_excel('mip_pivot_table.xlsx', index=False)
# nba mvp
nba_mvp_pivot_table_df = \
    pd.pivot_table(nba_mvp_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

nba_mvp_pivot_table_df.to_excel('nba_mvp_pivot_table.xlsx')

nba_mvp_pivot_table_df = \
    pd.read_excel('nba_mvp_pivot_table.xlsx')

nba_mvp_pivot_table_df.to_excel('nba_mvp_pivot_table.xlsx', index=False)
# nba roy
nba_roy_pivot_table_df = \
    pd.pivot_table(nba_roy_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

nba_roy_pivot_table_df.to_excel('nba_roy_pivot_table.xlsx')

nba_roy_pivot_table_df = \
    pd.read_excel('nba_roy_pivot_table.xlsx')

nba_roy_pivot_table_df.to_excel('nba_roy_pivot_table.xlsx', index=False)
# smoy
smoy_pivot_table_df = \
    pd.pivot_table(smoy_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

smoy_pivot_table_df.to_excel('smoy_pivot_table.xlsx')

smoy_pivot_table_df = \
    pd.read_excel('smoy_pivot_table.xlsx')

smoy_pivot_table_df.to_excel('smoy_pivot_table.xlsx', index=False)
# aba mvp
aba_mvp_pivot_table_df = \
    pd.pivot_table(aba_mvp_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

aba_mvp_pivot_table_df.to_excel('aba_mvp_pivot_table.xlsx')

aba_mvp_pivot_table_df = \
    pd.read_excel('aba_mvp_pivot_table.xlsx')

aba_mvp_pivot_table_df.to_excel('aba_mvp_pivot_table.xlsx', index=False)
# aba roy
aba_roy_pivot_table_df = \
    pd.pivot_table(aba_roy_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

aba_roy_pivot_table_df.to_excel('aba_roy_pivot_table.xlsx')

aba_roy_pivot_table_df = \
    pd.read_excel('aba_roy_pivot_table.xlsx')

aba_roy_pivot_table_df.to_excel('aba_roy_pivot_table.xlsx', index=False)

# updating Swen Nater's aba_roy award count from 3 to 1 since he was traded midseason
aba_roy_pivot_table_df['award'] = \
    aba_roy_pivot_table_df['award'].where(
        ~aba_roy_pivot_table_df['player_x'].\
            isin(['Swen Nater']), \
                1
    )

print(aba_roy_pivot_table_df.sort_values(by=['award'], ascending=False))

aba_roy_pivot_table_df.to_excel('aba_roy_pivot_table.xlsx', index=False)


# nba mvp and top 10 highest scoring averages
def nba_mvp_ppg(df):
    try:
        return df[(df['award'] == 'nba mvp') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

top_5_nba_mvp_ppg_df = nba_mvp_ppg(player_award_shares_and_player_per_game_merged_df)
top_10_nba_mvp_ppg_df = nba_mvp_ppg(player_award_shares_and_player_per_game_merged_df)

top_5_nba_mvp_ppg_df.to_excel('top_5_nba_mvp_ppg_df.xlsx', index=False)
top_10_nba_mvp_ppg_df.to_excel('top_10_nba_mvp_ppg_df.xlsx', index=False)

# sort values by pts_per_game
top_5_nba_mvp_ppg_df = top_5_nba_mvp_ppg_df.sort_values(['pts_per_game'], ascending=False).head(5)
top_10_nba_mvp_ppg_df = top_10_nba_mvp_ppg_df.sort_values(['pts_per_game'], ascending=False).head(10)

top_5_nba_mvp_ppg_df.to_excel('top_5_nba_mvp_ppg_df.xlsx', index=False)
top_10_nba_mvp_ppg_df.to_excel('top_10_nba_mvp_ppg_df.xlsx', index=False)
# drop unnecessary columns from top_5_nba_mvp_ppg_df
top_5_nba_mvp_ppg_df = \
    top_5_nba_mvp_ppg_df.drop(top_5_nba_mvp_ppg_df.iloc[:,6:45], axis=1)
# drop unnecessary columns from top_10_nba_mvp_ppg_df
top_10_nba_mvp_ppg_df = \
    top_10_nba_mvp_ppg_df.drop(top_10_nba_mvp_ppg_df.iloc[:,6:45], axis=1)
# drop unnecessary columns from top_5_nba_mvp_ppg_df
top_5_nba_mvp_ppg_df = \
    top_5_nba_mvp_ppg_df.drop(['first'], axis=1)
# drop unnecessary columns from top_10_nba_mvp_ppg_df
top_10_nba_mvp_ppg_df = \
    top_10_nba_mvp_ppg_df.drop(['first'], axis=1)

#print(top_10_nba_mvp_ppg_df)
# rename certain columns in top_5_nba_mvp_ppg_df
top_5_nba_mvp_ppg_df = top_5_nba_mvp_ppg_df.rename(columns={'year_x': 'year',
                                                            'player_x': 'player',
                                                            'age_x': 'age',
                                                            'tm_x':'team'})

top_5_nba_mvp_ppg_df.to_excel('top_5_nba_mvp_ppg_df.xlsx', index=False)

# rename certain columns in top_10_nba_mvp_ppg_df
top_10_nba_mvp_ppg_df = top_10_nba_mvp_ppg_df.rename(columns={'year_x': 'year',
                                                            'player_x': 'player',
                                                            'age_x': 'age',
                                                            'tm_x':'team'})

#print(top_10_nba_mvp_ppg_df)
top_10_nba_mvp_ppg_df.to_excel('top_10_nba_mvp_ppg_df.xlsx', index=False)


# rename a column in clutch_poy_pivot_table_df
clutch_poy_pivot_table_df = clutch_poy_pivot_table_df.\
    rename(columns={'player_x': 'player'})

clutch_poy_pivot_table_df.to_excel('clutch_poy_pivot_table.xlsx', index=False)

# rename a column in dpoy_pivot_table_df
dpoy_pivot_table_df = dpoy_pivot_table_df.\
    rename(columns={'player_x': 'player'})

dpoy_pivot_table_df.to_excel('dpoy_pivot_table.xlsx', index=False)

# rename a column in mip_pivot_table_df
mip_pivot_table_df = mip_pivot_table_df.\
    rename(columns={'player_x': 'player'})

mip_pivot_table_df.to_excel('mip_pivot_table.xlsx', index=False)

# rename a column in nba_mvp_pivot_table_df
nba_mvp_pivot_table_df = nba_mvp_pivot_table_df.\
    rename(columns={'player_x': 'player'})

nba_mvp_pivot_table_df.to_excel('nba_mvp_pivot_table.xlsx', index=False)

# rename a column in nba_roy_pivot_table_df
nba_roy_pivot_table_df = nba_roy_pivot_table_df.\
    rename(columns={'player_x': 'player'})

nba_roy_pivot_table_df.to_excel('nba_roy_pivot_table.xlsx', index=False)

# rename a column in smoy_pivot_table_df
smoy_pivot_table_df = smoy_pivot_table_df.\
    rename(columns={'player_x': 'player'})

smoy_pivot_table_df.to_excel('smoy_pivot_table.xlsx', index=False)

# rename a column in aba_mvp_pivot_table_df
aba_mvp_pivot_table_df = aba_mvp_pivot_table_df.\
    rename(columns={'player_x': 'player'})

aba_mvp_pivot_table_df.to_excel('aba_mvp_pivot_table.xlsx', index=False)

# rename a column in aba_roy_pivot_table_df
aba_roy_pivot_table_df = aba_roy_pivot_table_df.\
    rename(columns={'player_x': 'player'})

aba_roy_pivot_table_df.to_excel('aba_roy_pivot_table.xlsx', index=False)


# ================= #
# creating more dfs 
# ================= #

# bill russell dataframe - per game averages
def bill_russell(df):
    try:
        return df[df['player'] == 'Bill Russell']
    except:
        print('cannot filter dataframe')

bill_russell_per_game_avgs_df = bill_russell(player_per_game_df)

bill_russell_per_game_avgs_df.to_excel('bill_russell_per_game_averages.xlsx', index=False)

# wilt chamberlain dataframe - per game averages
def wilt_chamberlain(df):
    try:
        return df[df['player'] == 'Wilt Chamberlain']
    except:
        print('cannot filter dataframe')

wilt_chamberlain_per_game_avgs_df = wilt_chamberlain(player_per_game_df)

wilt_chamberlain_per_game_avgs_df.to_excel(
    'wilt_chamberlain_per_game_averages.xlsx', index=False)

# merging bill russell and wilt chamberlain per game avgs dataframes 
#   (when they played in the same years only)
bill_russell_and_wilt_chamberlain_per_game_avgs_merged_df = pd.merge(bill_russell_per_game_avgs_df, 
                                                       wilt_chamberlain_per_game_avgs_df,
                                                       on=['year'])

bill_russell_and_wilt_chamberlain_per_game_avgs_merged_df.to_excel(
    'bill_russell_and_wilt_chamberlain_per_game_avgs_merged.xlsx',
    index=False)

# get column names with corresponding index
col = list(bill_russell_and_wilt_chamberlain_per_game_avgs_merged_df.columns)
index = 0
print('bill_russell_and_wilt_chamberlain_per_game_avgs_merged_df:')

for x in col:
    print(index, x)
    index += 1

# michael jordan dataframe - per game averages
def michael_jordan(df):
    try:
        return df[df['player'] == 'Michael Jordan']
    except:
        print('cannot filter dataframe')

michael_jordan_per_game_avgs_df = michael_jordan(player_per_game_df)

michael_jordan_per_game_avgs_df.to_excel('michael_jordan_per_game_averages.xlsx', index=False)

# lebron james dataframe - per game averages
def lebron_james(df):
    try:
        return df[df['player'] == 'LeBron James']
    except:
        print('cannot filter dataframe')

lebron_james_per_game_avgs_df = lebron_james(player_per_game_df)

lebron_james_per_game_avgs_df.to_excel('lebron_james_per_game_averages.xlsx', index=False)
# michael jordan and lebron james - per game averages
def michael_jordan_and_lebron_james(df):
    try:
        return df[(df['player'] == 'LeBron James') | (df['player'] == 'Michael Jordan')]
    except:
        print('cannot filter dataframe')

michael_jordan_and_lebron_james_per_game_avgs_df = michael_jordan_and_lebron_james(player_per_game_df)

michael_jordan_and_lebron_james_per_game_avgs_df.to_excel('michael_jordan_and_lebron_james_per_game_averages.xlsx', index=False)
# michael jordan and lebron james - pivot table
michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df = pd.pivot_table(
    michael_jordan_and_lebron_james_per_game_avgs_df,index=['player'],
    values=['pts_per_game',
    'trb_per_game',
    'ast_per_game',
    'stl_per_game',
    'blk_per_game'], 
    aggfunc='mean')

print(michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df)

michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df.\
    to_excel('michael_jordan_and_lebron_james_per_game_avgs_pivot_table.xlsx')

michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df = \
    pd.read_excel('michael_jordan_and_lebron_james_per_game_avgs_pivot_table.xlsx')

michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df.\
    to_excel('michael_jordan_and_lebron_james_per_game_avgs_pivot_table.xlsx', index=False)

cols = ['pts_per_game','trb_per_game','ast_per_game','stl_per_game','blk_per_game']

michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df[cols] = \
    michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df[cols].round(2)

michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df.\
    to_excel('michael_jordan_and_lebron_james_per_game_avgs_pivot_table.xlsx', index=False)


# ================== #
# creating graphs via matplotlib
# ================== #
import matplotlib.pyplot as plt
# top 5 nba mvp ppg
x = top_5_nba_mvp_ppg_df['player'].astype(str) + '\n' +\
      top_5_nba_mvp_ppg_df['year'].astype(str) + ' Season \n' +\
      top_5_nba_mvp_ppg_df['pts_per_game'].astype(str) + ' Points Per Game' +\
      '\n'
y = top_5_nba_mvp_ppg_df['pts_per_game']
color = 'blue'
plt.bar(x, y, color=color)
plt.title('NBA MVP Winners Points Per Game Average - Top 5')
plt.xlabel('PLAYERS')
plt.ylabel('POINTS PER GAME')
plt.show()
# top 10 nba mvp ppg
x = top_10_nba_mvp_ppg_df['player'].astype(str) + '\n' +\
      top_10_nba_mvp_ppg_df['year'].astype(str) + ' Season \n' +\
      top_10_nba_mvp_ppg_df['pts_per_game'].astype(str) + ' PPG' +\
      '\n'
y = top_10_nba_mvp_ppg_df['pts_per_game']
plt.bar(x, y, color=color)
plt.title('NBA MVP Winners Points Per Game Average - Top 10')
plt.xlabel('PLAYERS')
plt.ylabel('POINTS PER GAME')
plt.show()
# clutch poy
x = clutch_poy_pivot_table_df['player'].astype(str) + '\n'
y = clutch_poy_pivot_table_df['award']
plt.bar(x, y, color=color)
plt.title('# of Clutch POY Awards Per Player')
plt.xlabel('PLAYERS')
plt.ylabel('# of Times Won')
plt.show()
# dpoy 
x = dpoy_pivot_table_df['player'].astype(str)
y = dpoy_pivot_table_df['award']
plt.barh(x, y, color=color)
plt.title('# of DPOY Awards Per Player')
plt.xlabel('PLAYERS')
plt.ylabel('# of Times Won')
plt.show()
# mip 
x = mip_pivot_table_df['player'].astype(str)
y = mip_pivot_table_df['award']
plt.barh(x, y, color=color)
plt.title('# of MIP Awards Per Player')
plt.xlabel('PLAYERS')
plt.ylabel('# of Times Won')
plt.show()
# nba mvp
x = nba_mvp_pivot_table_df['player'].astype(str)
y = nba_mvp_pivot_table_df['award']
plt.barh(x, y, color=color)
plt.title('# of NBA MVP Awards Per Player')
plt.xlabel('PLAYERS')
plt.ylabel('# of Times Won')
plt.show()
# *NO ROY (NBA) CHART DUE TO QUANTITY ISSUE* #
# aba mvp
x = aba_mvp_pivot_table_df['player'].astype(str)
y = aba_mvp_pivot_table_df['award']
plt.bar(x, y, color=color)
plt.title('# of ABA MVP Awards Per Player')
plt.xlabel('PLAYERS')
plt.ylabel('# of Times Won')
plt.show()
# *NOT NECESSARY TO CREATE ABA_ROY CHART* #
# bill russell chart - rebounds per game
x = bill_russell_per_game_avgs_df['player'].astype(str) + '\n' + \
    bill_russell_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    bill_russell_per_game_avgs_df['trb_per_game'].astype(str) + ' RPG'
y = bill_russell_per_game_avgs_df['trb_per_game']
plt.bar(x, y, color=color)
plt.title('Bill Russell RPG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('RPG')
plt.show()
# bill russell chart - ast per game
x = bill_russell_per_game_avgs_df['player'].astype(str) + '\n' + \
    bill_russell_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    bill_russell_per_game_avgs_df['ast_per_game'].astype(str) + ' APG'
y = bill_russell_per_game_avgs_df['ast_per_game']
plt.bar(x, y, color=color)
plt.title('Bill Russell APG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('APG')
plt.show()
# bill russell chart - pts per game
x = bill_russell_per_game_avgs_df['player'].astype(str) + '\n' + \
    bill_russell_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    bill_russell_per_game_avgs_df['pts_per_game'].astype(str) + ' PPG'
y = bill_russell_per_game_avgs_df['pts_per_game']
plt.bar(x, y, color=color)
plt.title('Bill Russell PPG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('PPG')
plt.show()
# wilt chamberlain chart - rebounds per game
x = wilt_chamberlain_per_game_avgs_df['player'].astype(str) + '\n' + \
    wilt_chamberlain_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    wilt_chamberlain_per_game_avgs_df['trb_per_game'].astype(str) + ' RPG'
y = wilt_chamberlain_per_game_avgs_df['trb_per_game']
plt.bar(x, y, color=color)
plt.title('Wilt Chamberlain RPG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('RPG')
plt.show()
# wilt chamberlain chart - ast per game
x = wilt_chamberlain_per_game_avgs_df['player'].astype(str) + '\n' + \
    wilt_chamberlain_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    wilt_chamberlain_per_game_avgs_df['ast_per_game'].astype(str) + ' AST'
y = wilt_chamberlain_per_game_avgs_df['ast_per_game']
plt.bar(x, y, color=color)
plt.title('Wilt Chamberlain APG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('APG')
plt.show()
# wilt chamberlain chart - points per game
x = wilt_chamberlain_per_game_avgs_df['player'].astype(str) + '\n' + \
    wilt_chamberlain_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    wilt_chamberlain_per_game_avgs_df['pts_per_game'].astype(str) + ' PPG'
y = wilt_chamberlain_per_game_avgs_df['pts_per_game']
plt.bar(x, y, color=color)
plt.title('Wilt Chamberlain PPG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('PPG')
plt.show()

# michael jordan and lebron james
x = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['player'].astype(str)
y = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['pts_per_game']
plt.bar(x, y, color=color)
plt.title('Michael Jordan and Lebron James - PPG Career Avg')
plt.xlabel('PLAYERS')
plt.ylabel('Career PPG Averages')
plt.show()

x = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['player'].astype(str)
y = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['trb_per_game']
plt.bar(x, y, color=color)
plt.title('Michael Jordan and Lebron James - RPG Career Avg')
plt.xlabel('PLAYERS')
plt.ylabel('Career RPG Averages')
plt.show()

x = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['player'].astype(str)
y = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['ast_per_game']
plt.bar(x, y, color=color)
plt.title('Michael Jordan and Lebron James - AST Career Avg')
plt.xlabel('PLAYERS')
plt.ylabel('Career AST Averages')
plt.show()

x = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['player'].astype(str)
y = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['stl_per_game']
plt.bar(x, y, color=color)
plt.title('Michael Jordan and Lebron James - SPG Career Avg')
plt.xlabel('PLAYERS')
plt.ylabel('Career SPG Averages')
plt.show()

x = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['player'].astype(str)
y = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['blk_per_game']
plt.bar(x, y, color=color)
plt.title('Michael Jordan and Lebron James - BPG Career Avg')
plt.xlabel('PLAYERS')
plt.ylabel('Career BPG Averages')
plt.show()


# =============== #
# conditional formatting 
# =============== #
def award_winners_highlighted(x):
    try:
        if x == 'True':
            return 'background-color: green'     
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

player_award_shares_and_player_per_game_merged_styled_df = (
    player_award_shares_and_player_per_game_merged_df.
    style.
    applymap(award_winners_highlighted, subset=['winner'])
)

player_award_shares_and_player_per_game_merged_styled_df.to_excel('player_award_shares_and_player_per_game_merged.xlsx', index=False)

# highlight max values in certain columns in the merged dataframe
bill_russell_and_wilt_chamberlain_per_game_avgs_merged_styled_df = \
    bill_russell_and_wilt_chamberlain_per_game_avgs_merged_df.style.\
        highlight_max(subset=[
            'trb_per_game_x', 
            'ast_per_game_x', 
            'pts_per_game_x',
            'trb_per_game_y', 
            'ast_per_game_y', 
            'pts_per_game_y'], 
            color='yellow', 
            axis=0)

bill_russell_and_wilt_chamberlain_per_game_avgs_merged_styled_df.\
    to_excel('bill_russell_and_wilt_chamberlain_per_game_avgs_merged.xlsx', index=False)

def player_per_game_highlighted(x):
    try:
        if x == 'N/A - Stat tracked as of the 1973-74 NBA Season' or x == 'N/A - Stat tracked as of the 1973-74 ABA Season':
            return 'background-color: red'
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')
        
player_per_game_df = player_per_game_df.style.applymap(player_per_game_highlighted, 
                                                       subset=['stl_per_game', 'blk_per_game'])

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

# ============ #