from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import WordCountForm
from app.scrape import Scraper

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Word Count App')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = WordCountForm()
    if form.validate_on_submit():
        scraped = Scraper(form.word.data, form.url.data)
        message = ""
        message += 'The word "{}" appears in {} {} times'.format(
            scraped.word, scraped.url, scraped.countWord())

        for sentence, polarity in scraped.getSentiments().items():
            message += '/n {} : {}'.format(sentence, polarity)

        return render_template('form.html', title='Word Count App', form=form, message=message)
    return render_template('form.html', title='Word Count App', form=form)