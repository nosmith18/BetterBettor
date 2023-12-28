import time
import re

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from Seb_Scraper.create_clean_table import *

global DRIVER_LOCATION
DRIVER_LOCATION = "C:\\Users\\Utilisateur\\Desktop\\chromedriver.exe"

global TYPE_ODDS
TYPE_ODDS = 'CLOSING'  # you can change to 'OPENING' if you want to collect opening odds, any other value will make the program collect CLOSING odds

global CURRENT_SZN
CURRENT_SZN = '2022-2023'

def fi_td(a):
    try:
        return driver.find_element("xpath", a).get_attribute("innerHTML")
    except:
        return False

def fi(a):
    try:
        return driver.find_element("xpath", a).text
    except:
        return False


def ffi(a):
    if fi(a) != False:
        print("ffi")
        return driver.find_element("xpath", a).text


def fffi(a):
    if TYPE_ODDS == 'OPENING':
        try:
            # return "get_opening_odd(a)"
            return "Opening Odds"
        except:
            return ffi(a)
    else:
        return (ffi(a))


def fi2(a):
    try:
        driver.find_element("xpath", a).click()
    except:
        return False


def ffi2(a):
    if fi2(a) != False:
        fi2(a)
        return (True)
    else:
        return (None)

def get_data(link):
    driver.get(link)
    reject_ads()
    games = []
    for i in range(1, 100):
        element = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a'.format(i)
        if not fi(element):
            element = '//*[@id="tournamentTable"]/tbody/tr[{}]/*[@colspan="4"]/span'.format(i)
            if fi(element):
                date = fi(element)
                continue
        if fi(element):
            match = fi('//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a'.format(i))  # match teams
            Odd_1 = fi('//*[@id="tournamentTable"]/tbody/tr[{}]/td[4]/a'.format(i))
            Odd_2 = fi('//*[@id="tournamentTable"]/tbody/tr[{}]/td[5]/a'.format(i))
            final_score = fi_td('//*[@id="tournamentTable"]/tbody/tr[{}]/td[3]'.format(i))
            if final_score == 'canc.':
                continue
            gametime = fi_td('//*[@id="tournamentTable"]/tbody/tr[{}]/td[1]'.format(i))
            print(date, gametime, match, Odd_1, Odd_2, final_score)
            games = games + [(date, gametime, match, Odd_1, Odd_2, final_score)]
    return (games)

def scrape_webpage(sport, league, country, szn, num_page):
    global driver

    ############ Let's Scrape some Data ############
    data=[]
    for page in range(1, num_page):
        print('Scraping page #{}'.format(page))
        driver = webdriver.Chrome(executable_path=DRIVER_LOCATION)

        # Setup Page and scraper
        if szn == CURRENT_SZN:
            link = 'https://www.oddsportal.com/{}/{}/{}/results/page/1/#/page/{}' \
                .format(sport, country, league, page) # Current SZN
        else:
            link = 'https://www.oddsportal.com/{}/{}/{}-{}/results/page/1/#/page/{}'\
                .format(sport, country, league, szn, page) # Old SZNs
        content = get_data(link)
        if content != None:
            data = data + content
        print(data)
        # data = scrape_page_typeA(page, sport, country, league, szn)
        driver.close()

    data_df = pd.DataFrame(data)

    try:
        data_df.columns = ['Date', 'Time', 'Teams', 'Odds_Home', 'Odds_Away', 'Final_Score']
    except:
        print('Columns crashed')
        return 1

    # Clean Data (Split Home/Away Teams and Final Score)
    data_df['Home'] = [re.split(' - ', y)[0] for y in data_df['Teams']]
    data_df['Away'] = [re.split(' - ', y)[1] for y in data_df['Teams']]
    data_df['Home Score'] = [re.split(':', y)[0][-2:] for y in data_df['Final_Score']]
    data_df['Away Score'] = [re.split(':', y)[1][:2] for y in data_df['Final_Score']]
    data_df['Season'] = szn

    print(data_df)
    # home = data_df['Home Score'].i


    return data_df

def scrape_nfl(sport='american-football', country="usa",  league='nfl', season='2022-2023', max_page=8):
    df = scrape_webpage(sport, league, country, season, max_page)
    # df = create_clean_table_two_ways()

    if not os.path.exists('./{}'.format(sport)):
        os.makedirs('./{}'.format(sport))

    df.to_csv('./{}/{}_{}.csv'.format(sport, league, season))

def reject_ads():
    ffi2('//*[@id="onetrust-reject-all-handler"]')