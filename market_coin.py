import requests
from bs4 import BeautifulSoup


def get_page_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    page = requests.get(url, headers=headers)
    return BeautifulSoup(page.text, 'html.parser')


def get_currency(soup):
    data = soup.select(".sc-4984dd93-0.kKpPOn")
    return [x.get_text() for x in data]


def get_price(soup):
    price = soup.select(".sc-bc83b59-0.iVdfNf")
    return [x.get_text() for x in price]


result = {}
url = "https://coinmarketcap.com/"
soup = get_page_soup(url)

lst_currency = get_currency(soup)
lst_price = get_price(soup)

for i in range(len(lst_price)):
    result[lst_currency[i]] = lst_price[i]
print(result)



