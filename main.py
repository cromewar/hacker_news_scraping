import requests
from bs4 import BeautifulSoup
import pprint

#Takes an HTML page from the given URL
response = requests.get('https://news.ycombinator.com/news')

#Parses String info to a HTML format
soup = BeautifulSoup(response.text, 'html.parser')

# Takes every item on the html with an CSS selector using it's class name for Links and Subtext
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    '''
    sorts the list given as input by an specific key and a reverse acomodation
    '''
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_hn(links, subtext):
    '''
    Creates a new List of items,
    for each element on links List splits the title, the Href (link to page) and the count of votes
    if the vote has item on in take just the points parsed in to integer and if it is greater than 90
    appends it to the new list of items named hn
    returns hn.
    '''
    hn = []
    for idx, item in enumerate(links):
        title =  item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 90:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_hn(links, subtext))