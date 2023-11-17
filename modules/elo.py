# elo.py

# Imports
import numpy as np

# Constants


# Functions
def calculate_expected_score(rating1, rating2):
    """
    Calculate the expected score of player 1 
    for player 1 with elo = rating1 
    against player 2 with elo = rating2
    """
    return 1 / (1 + 10**((rating2 - rating1) / 500))


def mean_expected_score(player_a, player_c, player_d):
    """Calculate the mean expected score for player a vs [c , d]"""
    playera_against_playerc = calculate_expected_score(player_a, player_c)
    playera_against_playerd = calculate_expected_score(player_a, player_d)
    
    return (playera_against_playerc + playera_against_playerd) / 2


def calculate_point_factor(score_difference):
    """Calculate the point factor based on the score difference"""
    return 2 + (np.log(score_difference + 1) / np.log(10)) ** 3


def specific_player_games(player, num_rows, game_log):
    """Extracts rows for games played by a specific player.

    Filters the game log dataframe to only include rows where 
    the specified player played, up to the provided number of rows.

    Args:
        player (str): Player name to filter on
        num_rows (int): Number of rows to return 
        game_log (DataFrame): DataFrame of game log data

    Returns:
       DataFrame: Rows where provided player played, up to num_rows
    """    
    df2 = game_log.iloc[:num_rows+1].copy()
    condition = ((df2['Player1'] == player) | 
                 (df2['Player2'] == player) | 
                 (df2['Player3'] == player) | 
                 (df2['Player4'] == player))

    return df2[condition]