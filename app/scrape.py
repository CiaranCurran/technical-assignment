from bs4 import BeautifulSoup
import requests
from textblob import TextBlob

class Scraper:
    def __init__(self, word, url):
        self.word = word
        self.url = url

        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        self.text = soup.get_text()

    def countWord(self):
        count = self.text.count(self.word)
        return count

    #returns dictionary of sentence and polarity key/value pairs
    def getSentiments(self):
        sentences = []
        blob = TextBlob(self.text)

        #extract sentences in which the given word appears
        for sentence in blob.sentences:
            if self.word in sentence:
                sentences.append(sentence)

        sentiments = {}
        for sentence in sentences:
            sentiments[sentence] = sentence.sentiment.polarity
        return sentiments


