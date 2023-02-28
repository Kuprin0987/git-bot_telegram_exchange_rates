import requests
from bs4 import BeautifulSoup as bs
import json

urls = ['https://myfin.by/crypto-rates', 'https://myfin.by/crypto-rates?page=2', 'https://myfin.by/crypto-rates?page=3']

dict_exchanges = {}

for url in urls:
    r = requests.get(url)
    soup = bs(r.text, 'lxml')

    table = soup.find('tbody', class_="table-body")

    rates = table.find_all('tr')

    for tr in rates:
        dict_exchange = {}
        tds = tr.find_all('td')
        
        dict_exchange['name']           = tds[0].a.text.rstrip()         #название валюты
        dict_exchange['name_crypto']    = tds[0].find('div', class_='crypto_iname hidden-xs').text

        dict_exchange['price']          = tds[1].text.split(' ')[0]      #исправь      #цена
        dict_exchange['capitalization'] = tds[2].text                    #капитализация
        dict_exchange['volume']         = tds[3].text                    #обьём за 24 часа
        dict_exchange['change']         = tds[4].text                    #изменение за 24 часа

        dict_exchanges[dict_exchange['name']] = dict_exchange


with open(f'dict_exchanges.json', 'w') as file:
    json.dump(dict_exchanges, file)
