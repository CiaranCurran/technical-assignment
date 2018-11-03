from flask import render_template
from app import app
from app.forms import WordCountForm
from app.scrape import Scraper


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = WordCountForm()
    if form.validate_on_submit():
        scraped = Scraper(form.word.data, form.url.data, form.case.data)
        return render_template('form.html', title='Word Count App', form=form, complete=True, scraped=scraped)
    return render_template('form.html', title='Word Count App', form=form, complete=False)

