import requests
from bs4 import BeautifulSoup
import pandas as pd

country = input('Enter a country:')

city = input(f'Enter a city from {country}:')

page = requests.get(f'https://www.timeanddate.com/weather/{country}/{city}/ext')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id ='wt-ext')

column = table.find_all('tr')[2:-1]

days = [i.find('th').get_text()[:3] for i in column]
date = [i.find('th').get_text()[3:] for i in column]
descp = [i.find(class_ ='small').get_text().strip('.') for i in column]
temp = [i.find(class_ = 'wt-ic').findNext('td').get_text().replace('\xa0','') for i in column]


weather = pd.DataFrame({
	'Day': days,
	'Date': date,
	'Description':descp,
	'Temparature(Fareinheit)':temp,
})

print(weather)

weather.to_csv('weather.csv')
