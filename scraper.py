from re import S
import requests
from bs4 import BeautifulSoup


# url = 'https://en.wikipedia.org/wiki/Ice'
# url = 'https://en.wikipedia.org/wiki/Football'
# url = 'https://en.wikipedia.org/wiki/Formula_One'
# url = 'https://en.wikipedia.org/wiki/Barcelona'
url = 'https://en.wikipedia.org/wiki/Ferrari'


def get_citations_needed_count(url):
    '''Here we are create a function to gets all the missing citations, 
    and show the number of citations missing'''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    count = soup.find_all(title="Wikipedia:Citation needed")
    number = len(count)
    print(f'Number of ciations is --> {number}')
    print()
    return number


def get_citations_needed_report(url):
    '''Here we are create a function to gets a paragraphs that missing a citations'''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    paragraph = soup.find_all(title="Wikipedia:Citation needed")
    for i in paragraph:
        print(i.parent.parent.parent.text)
        print()




get_citations_needed_count(url)
get_citations_needed_report(url)