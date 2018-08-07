import requests
import bs4

def scrapUS_CN():
    '''
    extract currency exchange data between US dollars and Chinese Yuan and date from
    https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CNY
    '''
    res = requests.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CNY')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    currency_exchange = soup.find('span',attrs = {'class':'uccResultAmount'}).text
    date = soup.find('span',attrs = {'class':'resultTime'}).text
    return date + ',' + currency_exchange+'\n'

result = scrapUS_CN()
f = open('myData.csv','a')
f.write(result)
f.close()