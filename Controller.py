import os

#os.chdir("C:\\Users\\Sébastien CARARO\\Desktop\\ATP& &Others\\WebScraping")
from MyScraperFunctions import *

print('Data will be saved in the following directory:', os.getcwd())

# -- Key for sports! --
# soccer | basketball | esports | darts
# tennis | baseball | rugby-union | rugby-league
# american-football | hockey | volleyball | handball

# -- Warning --
# All requests need to be made in lowercase "usa", "nfl", etc
# For NFL seasons must input season as 2021-2022, maybe the same for other leagues/sports
# check oddsportal.com to be sure!

# scrape_nfl(season="2008-2009")
# scrape_nfl(season="2009-2010")
# scrape_nfl(season="2010-2011")
# scrape_nfl(season="2011-2012")
# scrape_nfl(season="2012-2013")
# scrape_nfl(season="2013-2014")
# scrape_nfl(season="2014-2015")
# scrape_nfl(season="2015-2016")
# scrape_nfl(season="2016-2017")
# scrape_nfl(season="2017-2018")
# scrape_nfl(season="2018-2019")
# scrape_nfl(season="2019-2020")
# scrape_nfl(season="2020-2021")
# scrape_nfl(season="2021-2022")
scrape_nfl(season="2022-2023")