from bs4 import BeautifulSoup
import requests


def countWord(word, url):
    #make request for URl
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    #count occurences of given word in text of webpage
    count = soup.get_text().count(word)

    return count

