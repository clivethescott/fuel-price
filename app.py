from bs4 import BeautifulSoup
import requests


prices_url = 'https://www.globalpetrolprices.com/Zimbabwe/'
content = requests.get(prices_url).content
soup = BeautifulSoup(content, "lxml")
data_rows = soup.find_all('tr')[1:]
for row in data_rows:
    fuel_type = row.find('a').string.strip()[:-1]
    rtgs_price = row.find_all('td')[1].string.strip()
    print(f'{fuel_type} is ${rtgs_price}')
