############ Final oddsportal scraper

# ATP, baseball, basket, darts, eSports, football, nfl, nhl, rugby
''' Create 4 main functions : scrape_historical, scrape_specific_season, scrape current_season, scrape_next_games
NB : You need to be in the right repository to import functions...'''
import os

#os.chdir("C:\\Users\\Sébastien CARARO\\Desktop\\ATP& &Others\\WebScraping")
from functions import *

print('Data will be saved in the following directory:', os.getcwd())

# -- Key for sports! --
# soccer | basketball | esports | darts
# tennis | baseball | rugby-union | rugby-league
# american-football | hockey | volleyball | handball

# -- Warning --
# All requests need to be made in lowercase "usa", "nfl", etc
# For NFL seasons must input season as 2021-2022, maybe the same for other leagues/sports
# check oddsportal.com to be sure!

# scrape_oddsportal_historical(sport = 'soccer', country = 'france', league = 'ligue-1', start_season = '2010-2011', nseasons = 5, current_season = 'yes', max_page = 25)
# scrape_oddsportal_current_season(sport = 'soccer', country = 'finland', league = 'veikkausliiga', season = '2020', max_page = 25)
# scrape_oddsportal_specific_season(sport = 'american-football', country = 'usa', league = 'nfl', season = '2021-2022', max_page = 2)
# scrape_oddsportal_next_games(sport = 'tennis', country = 'germany', league = 'exhibition-bett1-aces-berlin-women', season = '2020')
# scrape_nfl(season="2021-2022")




