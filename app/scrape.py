from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
from textblob import TextBlob

class Scraper:
    def __init__(self, word, url):
        self.word = word
        self.url = url

        source = requests.get(url).text
        self.text = text_from_html(source)

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


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)
