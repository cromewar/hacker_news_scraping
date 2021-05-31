import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.select('.storylink')
votes = soup.select('.score')

def create_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        hn.append({'title': title, 'link': href})
    return hn

print(create_hn(links, votes))