#influenced by https://github.com/mcmclean/cfb-score-scraper/blob/master/scraper.py

#TODO check this out: https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/experimental-python-code

import pandas as pd
import re
import csv
import os
from numpy.linalg import inv
import numpy as np
import time

#fbs_url="https://www.cbssports.com/college-football/scoreboard/FBS/"
#b1g_url="https://www.cbssports.com/college-football/scoreboard/BIG10/"
#top25_url="https://www.cbssports.com/college-football/scoreboard/top25/"

#for a specific week:
#"http://www.cbssports.com/college-football/scoreboard/FBS/" + str(year) + "/regular/" + str(week)

current_url = "https://www.cbssports.com/nfl/scoreboard/"

games_list = []

def update():
    global games_list
    frame = pd.read_html( current_url )

    #print( frame )
    for x in frame:
        print( x )
    exit( 0 )

    game_frame = pd.DataFrame({'Date' : [], 'Away Team' : [], 'Home Team' : [], 
    'Away Final' : [], 'Home Final' : [], 'Away Record After' : [], 'Home Record After' : [], 
    'Away Rank Prior' : [], 'Home Rank Prior' : []})

    games1 = map(lambda x : x, filter(lambda y : len(y) > 1, frame))
    games_list = list( games1 )
'''
    try:
        games = map(lambda x : x, filter(lambda y : len(y.columns) >= 6, games1))
    except:
        games = games1
'''

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def collect_info(game, num):
    x = game.loc( 0 )[ num ]
    header = x[ 0 ]
    header_tokens = header.split()

    '''
    Header is [rank][team name][record]
    rank can be absent
    team name can have spaces
    '''

    team_name = "";
    if not is_number( header_tokens[ 0 ] ):
        team_name = header_tokens[ 0 ] + " "

    for ind in range ( 1, len( header_tokens ) - 1 ):
        team_name += header_tokens[ ind ] + " "

    #remove final space
    team_name = team_name[:-1]

    score = x[ len(x)-1 ]

    return team_name, score


def display( game ):
    away_team, away_score = collect_info( game, 0 )
    home_team, home_score = collect_info( game, 1 )
    print( away_team, away_score )
    print( home_team, home_score )

def game_contains_team( game, team_name ):
    away_team, away_score = collect_info( game, 0 )
    home_team, home_score = collect_info( game, 1 )
    return team_name == away_team or team_name == home_team


update()
for game in games_list:
    #display( game )
    print( game )
    time.sleep(5)
    print( "" )
