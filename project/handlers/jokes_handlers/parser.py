from bs4 import BeautifulSoup
import requests

url = 'https://www.anekdot.ru/last/anekdot/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
jokes = soup.find_all('div', class_='text')

jokes = [joke.text for joke in jokes]

