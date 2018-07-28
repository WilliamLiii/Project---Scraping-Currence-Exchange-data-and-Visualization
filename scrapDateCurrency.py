import requests
import bs4
import re

def scrapUS_CN():
    '''
    extract currency exchange data between US dollars and Chinese Yuan and date from
    https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CNY
    '''
    res = requests.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CNY')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    raw_exchange = soup.select('#ucc-container > span.uccAmountWrap > span.uccResultAmount')
    raw_date = soup.select('#ucc-container > span.uccResultTitle.clearfix')
    # use re to extract specific exchange rate and date
    currencyRegex = re.compile(r'\d\.\d+')
    dateRegex = re.compile(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d [A-Z]{3}')
    exchange = currencyRegex.search(str(raw_exchange)).group()
    date = dateRegex.search(str(raw_date)).group()

    return exchange + '/' + date

test = scrapUS_CN()
print(test)
